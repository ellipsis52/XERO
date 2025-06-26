// xero-auth.js — Symbiose Xero × GPT
// =====================================================
// DÉPENDANCES
// -----------------------------------------------------
require("dotenv").config();
const express  = require("express");
const axios    = require("axios");
const qs       = require("querystring");
const sqlite3  = require("sqlite3").verbose();
const { OpenAI } = require("openai");   // ➜ npm install openai

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

// ENV VARS ---------------------------------------------------------
const {
  XERO_CLIENT_ID:     clientId,
  XERO_CLIENT_SECRET: clientSecret,
  XERO_REDIRECT_URI:  redirectUri,
  PORT               = 3001,
} = process.env;
if (!clientId || !clientSecret || !redirectUri) {
  console.error("❌  Missing XERO_* env vars. Check your .env file.");
  process.exit(1);
}

// SQLITE – stockage persistant ------------------------------------
const db = new sqlite3.Database("./xero_tokens.db");
db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS tokens (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id       TEXT,
    access_token  TEXT,
    refresh_token TEXT,
    expires_at    INTEGER,
    tenant_id     TEXT
  )`);
});
function storeTokens(userId, tokens, tenantId) {
  const expiresAt = Date.now() + tokens.expires_in * 1000;
  db.run(
    `INSERT INTO tokens (user_id, access_token, refresh_token, expires_at, tenant_id)
       VALUES (?, ?, ?, ?, ?)`,
    [userId, tokens.access_token, tokens.refresh_token, expiresAt, tenantId],
    (err) => err && console.error("DB insert error:", err.message)
  );
  console.log("💾  Tokens stored for", userId);
}
function getTokenRow(userId, cb) {
  db.get(
    `SELECT * FROM tokens WHERE user_id = ? ORDER BY expires_at DESC LIMIT 1`,
    [userId], cb
  );
}
function updateTokens(rowId, tokens) {
  const expiresAt = Date.now() + tokens.expires_in * 1000;
  db.run(
    `UPDATE tokens SET access_token = ?, refresh_token = ?, expires_at = ? WHERE id = ?`,
    [tokens.access_token, tokens.refresh_token, expiresAt, rowId],
    (err) => err ? console.error("DB update error:", err.message)
                 : console.log("🔄  Tokens refreshed (row", rowId + ")")
  );
}

// HELPERS OAuth ----------------------------------------------------
function buildAuthUrl(state = "netmgmt" + Date.now()) {
  const params = {
    response_type: "code",
    client_id: clientId,
    redirect_uri: redirectUri,
    scope: [
      "openid",
      "profile",
      "email",
      "offline_access",
      "accounting.transactions",
    ].join(" "),
    state,
  };
  return `https://login.xero.com/identity/connect/authorize?${qs.stringify(params)}`;
}
async function exchangeCodeForToken(code) {
  const data = { grant_type: "authorization_code", code, redirect_uri: redirectUri };
  const authHeader = Buffer.from(`${clientId}:${clientSecret}`).toString("base64");
  const res = await axios.post(
    "https://identity.xero.com/connect/token",
    qs.stringify(data),
    { headers: { "Content-Type": "application/x-www-form-urlencoded", Authorization: `Basic ${authHeader}` } }
  );
  return res.data; // {access_token, refresh_token, ...}
}
async function refreshAccessToken(userId, refreshToken, rowId) {
  const data = { grant_type: "refresh_token", refresh_token: refreshToken };
  const authHeader = Buffer.from(`${clientId}:${clientSecret}`).toString("base64");
  const res = await axios.post(
    "https://identity.xero.com/connect/token",
    qs.stringify(data),
    { headers: { "Content-Type": "application/x-www-form-urlencoded", Authorization: `Basic ${authHeader}` } }
  );
  updateTokens(rowId, res.data);
  return res.data;
}

// Xero API utilitaires ---------------------------------------------
async function getConnections(accessToken) {
  const res = await axios.get("https://api.xero.com/connections", { headers: { Authorization: `Bearer ${accessToken}` } });
  return res.data;
}
async function getOrganisation(accessToken, tenantId) {
  const res = await axios.get("https://api.xero.com/api.xro/2.0/Organisation", { headers: { Authorization: `Bearer ${accessToken}`, "xero-tenant-id": tenantId } });
  return res.data;
}
async function getInvoices(accessToken, tenantId) {
  const res = await axios.get("https://api.xero.com/api.xro/2.0/Invoices", { headers: { Authorization: `Bearer ${accessToken}`, "xero-tenant-id": tenantId } });
  return res.data?.Invoices || [];
}
async function gptInterpret(text, question) {
  const completion = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
      { role: "system", content: "You are a financial analyst who explains Xero invoices in plain language." },
      { role: "user", content: `Here are some invoices:\n\n${text}\n\nQuestion: ${question}` }
    ]
  });
  return completion.choices[0].message.content.trim();
}

// EXPRESS ----------------------------------------------------------
const app = express();

// 1) Callback initial OAuth ----------------------------------------
app.get("/xero/callback", async (req, res) => {
  const { code, state, error, error_description } = req.query;
  if (error) return res.status(400).send("OAuth error: " + error_description);
  try {
    const tokens = await exchangeCodeForToken(code);
    const connections = await getConnections(tokens.access_token);
    const tenantId = connections[0]?.tenantId;
    storeTokens(state, tokens, tenantId); // state = user_id
    const org = await getOrganisation(tokens.access_token, tenantId);
    res.json({ message: "Tokens stored & organisation fetched.", organisation: org });
  } catch (e) {
    console.error(e.response?.data || e.message);
    res.status(500).send("Token flow failed.");
  }
});

// 2) Refresh token route -------------------------------------------
app.get("/xero/refresh", (req, res) => {
  const userId = req.query.user_id || "default";
  getTokenRow(userId, async (err, row) => {
    if (err || !row) return res.status(404).send("No token for user.");
    if (Date.now() < row.expires_at - 60_000)
      return res.json({ message: "Token still valid." });
    try {
      const fresh = await refreshAccessToken(userId, row.refresh_token, row.id);
      res.json({ message: "Token refreshed!", fresh });
    } catch (e) {
      console.error(e.response?.data || e.message);
      res.status(500).send("Refresh failed.");
    }
  });
});

// 3) Invoices interpretation ---------------------------------------
app.get("/xero/invoices/interpret", (req, res) => {
  const userId   = req.query.user_id || "default";
  const question = req.query.question || "Summarise key insights.";
  getTokenRow(userId, async (err, row) => {
    if (err || !row) return res.status(404).send("No token.");
    try {
      let { access_token, refresh_token } = row;
      if (Date.now() >= row.expires_at - 60_000) {
        const fresh = await refreshAccessToken(userId, refresh_token, row.id);
        access_token  = fresh.access_token;
        refresh_token = fresh.refresh_token;
      }
      const invoices = await getInvoices(access_token, row.tenant_id);
      const short    = JSON.stringify(invoices.slice(0, 10), null, 2);
      const analysis = await gptInterpret(short, question);
      res.json({ invoices: invoices.length, analysis });
    } catch (e) {
      console.error(e.response?.data || e.message);
      res.status(500).send("Interpretation failed.");
    }
  });
});

// START ------------------------------------------------------------
app.listen(PORT, () => {
  console.log(`🚀  Xero OAuth helper listening on http://localhost:${PORT}`);
  console.log("Login URL:\n", buildAuthUrl());
});

module.exports = { buildAuthUrl, exchangeCodeForToken, refreshAccessToken };
