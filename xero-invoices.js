import express from 'express';
import axios from 'axios';

const router = express.Router();

router.get('/xero/invoices', async (req, res) => {
  // Récupère ton access token stocké quelque part sécurisé
  const accessToken = process.env.XERO_ACCESS_TOKEN;

  try {
    const response = await axios.get('https://api.xero.com/api.xro/2.0/Invoices', {
      headers: {
        Authorization: `Bearer ${accessToken}`,
        Accept: 'application/json',
      },
    });
    res.json(response.data.Invoices);
  } catch (error) {
    console.error('Erreur récupération factures Xero:', error.response?.data || error.message);
    res.status(500).json({ error: 'Impossible de récupérer les factures' });
  }
});

import React, { useEffect, useState } from 'react';

const XeroInvoices = () => {
  const [invoices, setInvoices] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:4242/xero/invoices')
      .then((res) => {
        if (!res.ok) throw new Error('Erreur réseau');
        return res.json();
      })
      .then((data) => {
        setInvoices(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Chargement des factures...</p>;
  if (error) return <p>Erreur : {error}</p>;

  return (
    <div>
      <h2>Factures Xero</h2>
      <table border="1" cellPadding="5" style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th>Numéro</th>
            <th>Client</th>
            <th>Date</th>
            <th>Montant</th>
            <th>Statut</th>
          </tr>
        </thead>
        <tbody>
          {invoices.map((invoice) => (
            <tr key={invoice.InvoiceID}>
              <td>{invoice.InvoiceNumber}</td>
              <td>{invoice.Contact.Name}</td>
              <td>{new Date(invoice.Date).toLocaleDateString()}</td>
              <td>{invoice.Total.toFixed(2)} {invoice.CurrencyCode}</td>
              <td>{invoice.Status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
const axios = require('axios');

// Middleware pour vérifier et rafraîchir le token Xero
async function xeroAuthMiddleware(req, res, next) {
  try {
    // Ici, tu récupères ton token stocké quelque part (en base, cache, fichier...)
    let accessToken = process.env.XERO_ACCESS_TOKEN;
    let refreshToken = process.env.XERO_REFRESH_TOKEN;

    // Vérifier si token valide (exemple simplifié, idéalement vérifier expiry)
    // Si expiré, rafraîchir le token
    // (Exemple de requête refresh token Xero)
    /*
    const response = await axios.post('https://identity.xero.com/connect/token', new URLSearchParams({
      grant_type: 'refresh_token',
      refresh_token: refreshToken,
      client_id: process.env.XERO_CLIENT_ID,
      client_secret: process.env.XERO_CLIENT_SECRET,
    }).toString(), {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    });
    accessToken = response.data.access_token;
    refreshToken = response.data.refresh_token;
    // Mettre à jour les tokens stockés
    */

    // Pour l’instant, on passe directement
    req.xeroAccessToken = accessToken;
    next();
  } catch (error) {
    console.error('Erreur dans le middleware d’auth Xero:', error);
    res.status(401).json({ error: 'Authentification Xero échouée' });
  }
}
const express = require('express');
const router = express.Router();

router.use('/xero', xeroAuthMiddleware);

router.put('/xero/invoices/:invoiceId', async (req, res) => {
  const { invoiceId } = req.params;
  const updateData = req.body;
  const accessToken = req.xeroAccessToken;

  try {
    const response = await axios.post(
      `https://api.xero.com/api.xro/2.0/Invoices`,
      { Invoices: [{ InvoiceID: invoiceId, ...updateData }] },
      {
        headers: {
          Authorization: `Bearer ${accessToken}`,
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      }
    );
    res.json(response.data);
  } catch (error) {
    console.error('Erreur mise à jour facture:', error.response?.data || error.message);
    res.status(500).json({ error: 'Impossible de mettre à jour la facture' });
  }
});

router.post('/xero/invoices/:invoiceId/void', async (req, res) => {
  const { invoiceId } = req.params;
  const accessToken = req.xeroAccessToken;

  try {
    const response = await axios.post(
      'https://api.xero.com/api.xro/2.0/Invoices',
      {
        Invoices: [
          {
            InvoiceID: invoiceId,
            Status: "VOIDED",
          },
        ],
      },
      {
        headers: {
          Authorization: `Bearer ${accessToken}`,
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      }
    );
    res.json(response.data);
  } catch (error) {
    console.error('Erreur annulation facture:', error.response?.data || error.message);
    res.status(500).json({ error: 'Impossible d’annuler la facture' });
  }
});
const clientId = process.env.XERO_CLIENT_ID;
const redirectUri = encodeURIComponent('https://ton-domaine.com/callback-xero');
const scope = encodeURIComponent('accounting.transactions accounting.contacts');
const state = 'random_string_to_protect_against_csrf';

const authUrl = `https://login.xero.com/identity/connect/authorize?response_type=code&client_id=${clientId}&redirect_uri=${redirectUri}&scope=${scope}&state=${state}`;
const express = require('express');
const axios = require('axios');
const app = express();

app.get('/callback-xero', async (req, res) => {
  const { code, state } = req.query;

  // Vérifie le state pour éviter les trahisons (CSRF)
  if (state !== 'random_string_to_protect_against_csrf') {
    return res.status(403).send('Invalid state');
  }

  try {
    const tokenResponse = await axios.post('https://identity.xero.com/connect/token', new URLSearchParams({
      grant_type: 'authorization_code',
      code,
      redirect_uri: 'https://ton-domaine.com/callback-xero',
      client_id: process.env.XERO_CLIENT_ID,
      client_secret: process.env.XERO_CLIENT_SECRET,
    }).toString(), {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });

    // Ici, tu captures access_token et refresh_token
    const { access_token, refresh_token, expires_in } = tokenResponse.data;

    // Sauvegarde-les précieusement : base de données, cache, ou secrets
    // Pour l'exemple, on les stocke dans la session (attention, à adapter)
    req.session.xeroAccessToken = access_token;
    req.session.xeroRefreshToken = refresh_token;

    res.send('Authentification réussie, les clés du trésor sont à portée.');
  } catch (error) {
    console.error('Erreur lors de l’échange du code:', error.response?.data || error.message);
    res.status(500).send('Impossible d’obtenir le token');
  }
});
async function refreshXeroToken(refreshToken) {
    try {
      const response = await axios.post('https://identity.xero.com/connect/token', new URLSearchParams({
        grant_type: 'refresh_token',
        refresh_token: refreshToken,
        client_id: process.env.XERO_CLIENT_ID,
        client_secret: process.env.XERO_CLIENT_SECRET,
      }).toString(), {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });
  
      return {
        accessToken: response.data.access_token,
        refreshToken: response.data.refresh_token,
        expiresIn: response.data.expires_in,
      };
    } catch (error) {
      console.error('Erreur rafraîchissement token:', error.response?.data || error.message);
      throw error;
    }
  }
  async function xeroAuthMiddleware(req, res, next) {
    let accessToken = req.session.xeroAccessToken;
    let refreshToken = req.session.xeroRefreshToken;
  
    // Ici tu devrais vérifier l’expiration, pour l’exemple on rafraîchit toujours
    try {
      const tokens = await refreshXeroToken(refreshToken);
      req.session.xeroAccessToken = tokens.accessToken;
      req.session.xeroRefreshToken = tokens.refreshToken;
      req.xeroAccessToken = tokens.accessToken;
      next();
    } catch {
      res.status(401).send('Authentification Xero requise');
    }
  }
  
export default XeroInvoices;
