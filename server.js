<<<<<<< HEAD
const express = require("express");
const morgan = require("morgan");
const helmet = require("helmet");
const { join } = require("path");

const app = express();

const port = process.env.SERVER_PORT || 3000;

app.use(morgan("dev"));

app.use(
  helmet({
    contentSecurityPolicy: false,
  })
);

app.use(express.static(join(__dirname, "build")));

app.get('*', (req, res) => res.sendFile(join(__dirname, 'build', 'index.html')));

app.listen(port, () => console.log(`Server listening on port ${port}`));
=======
// server.js
import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import Stripe from 'stripe';
import axios from 'axios';

dotenv.config();

const app = express();
const port = process.env.PORT || 4000;

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY, { apiVersion: '2023-05-15' });

// Middleware pour autoriser les échanges et parser JSON
app.use(cors());
app.use(express.json({
  verify: (req, res, buf) => {
    req.rawBody = buf.toString();
  }
}));

// Route poétique de bienvenue
app.get('/api/hello', (req, res) => {
  res.json({ message: "Bienvenue au royaume secret du backend, où les données chantent." });
});

// Webhook Stripe : écouter la symphonie des événements
app.post('/webhook', express.raw({ type: 'application/json' }), (req, res) => {
  const sig = req.headers['stripe-signature'];
  let event;

  try {
    event = stripe.webhooks.constructEvent(req.rawBody, sig, process.env.STRIPE_WEBHOOK_SECRET);
  } catch (err) {
    console.error('❌ Échec de la validation webhook Stripe:', err.message);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  switch (event.type) {
    case 'payment_intent.succeeded':
      console.log('✅ Paiement réussi:', event.data.object.id);
      // Ici tu peux appeler GPT-4 pour sublimer la transaction
      break;
    case 'invoice.payment_failed':
      console.warn('⚠️ Paiement échoué:', event.data.object.id);
      break;
    default:
      console.log(`ℹ️ Événement Stripe reçu: ${event.type}`);
  }

  res.json({ received: true });
});

// Appel à GPT-4, la muse créative
app.post('/gpt4', async (req, res) => {
  const prompt = req.body.prompt;
  if (!prompt) return res.status(400).json({ error: 'Le prompt est requis.' });

  try {
    const response = await axios.post('https://api.openai.com/v1/chat/completions', {
      model: 'gpt-4o-mini',
      messages: [{ role: 'user', content: prompt }]
    }, {
      headers: {
        'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`,
        'Content-Type': 'application/json'
      }
    });

    res.json({ reply: response.data.choices[0].message.content });
  } catch (error) {
    console.error('🔥 Erreur GPT-4:', error.response?.data || error.message);
    res.status(500).json({ error: 'Erreur lors de l’appel à GPT-4.' });
  }
});

// Exemple d’appel à l’API Xero
app.get('/xero/invoices', async (req, res) => {
  try {
    const xeroAccessToken = process.env.XERO_ACCESS_TOKEN;
    const response = await axios.get('https://api.xero.com/api.xro/2.0/Invoices', {
      headers: { Authorization: `Bearer ${xeroAccessToken}` }
    });
    res.json(response.data);
  } catch (error) {
    console.error('⚠️ Erreur API Xero:', error.response?.data || error.message);
    res.status(500).json({ error: 'Erreur lors de la récupération des factures Xero.' });
  }
});

// Le chant final, le serveur écoute
app.listen(port, () => {
  console.log(`🌟 Le serveur chante sur le port ${port}...`);
});
app.post('/webhook', express.raw({ type: 'application/json' }), async (req, res) => {
    const sig = req.headers['stripe-signature'];
    let event;
  
    try {
      event = stripe.webhooks.constructEvent(req.rawBody, sig, process.env.STRIPE_WEBHOOK_SECRET);
    } catch (err) {
      console.error('❌ Échec de la validation webhook Stripe:', err.message);
      return res.status(400).send(`Webhook Error: ${err.message}`);
    }
  
    switch (event.type) {
      case 'payment_intent.succeeded':
        console.log('✅ Paiement réussi:', event.data.object.id);
  
        // Ici, le souffle lyrique de GPT-4
        try {
          const prompt = `Un paiement vient d'être effectué avec succès, ID: ${event.data.object.id}. Compose un message poétique pour célébrer cette transaction.`;
  
          const gptResponse = await axios.post('https://api.openai.com/v1/chat/completions', {
            model: 'gpt-4o-mini',
            messages: [{ role: 'user', content: prompt }]
          }, {
            headers: {
              'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`,
              'Content-Type': 'application/json'
            }
          });
  
          console.log('✨ GPT-4 murmure:', gptResponse.data.choices[0].message.content);
        } catch (error) {
          console.error('🔥 Erreur lors de l’appel GPT-4 après paiement:', error.response?.data || error.message);
        }
        break;
  
      case 'invoice.payment_failed':
        console.warn('⚠️ Paiement échoué:', event.data.object.id);
        break;
  
      default:
        console.log(`ℹ️ Événement Stripe reçu: ${event.type}`);
    }
  
    res.json({ received: true });
  });
  poeticLogs.push({
    paymentId: event.data.object.id,
    message: gptResponse.data.choices[0].message.content,
    date: new Date().toISOString()
  });
  
  import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import stripeRouter from './stripe/index.js';

dotenv.config();

const app = express();
const port = process.env.PORT || 4000;

app.use(cors());
app.use(express.json({
  verify: (req, res, buf) => {
    req.rawBody = buf.toString();
  }
}));

app.use('/stripe', stripeRouter);

app.listen(port, () => {
  console.log(`🌟 Le serveur chante sur le port ${port}...`);
});
app.use((req, res, next) => {
  const allowedOrigins = [
    'https://www.webtechnicom.net',
    'https://www.netmanagement.online',
    'http://localhost:5173' // pour tests locaux
  ];
  const origin = req.headers.origin;
  if (allowedOrigins.includes(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);
  }
  next();
});
app.use(cors()); // ← reste comme ça, sans origin spécifique
import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import nodemailer from 'nodemailer';
import { Configuration, OpenAIApi } from 'openai';

dotenv.config();
const app = express();
const port = process.env.PORT || 3001;

app.use(cors());
app.use(express.json());

// GPT-4 Configuration
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

// Endpoint GPT-4
app.post('/gpt4', async (req, res) => {
  const { prompt } = req.body;
  if (!prompt) return res.status(400).json({ error: 'Prompt requis.' });

  try {
    const completion = await openai.createChatCompletion({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: 'Tu es un assistant poétique et professionnel.' },
        { role: 'user', content: prompt }
      ],
      max_tokens: 600,
      temperature: 0.7,
    });

    const reply = completion.data.choices[0].message.content;
    res.json({ reply });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Erreur avec GPT-4." });
  }
});

// Envoi d’email magique
app.post('/send-email', async (req, res) => {
  const { to, subject, text } = req.body;
  if (!to || !subject || !text) return res.status(400).json({ error: 'Champs manquants.' });

  try {
    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: process.env.EMAIL_SENDER,
        pass: process.env.EMAIL_PASSWORD,
      },
    });

    await transporter.sendMail({
      from: `"Assistant GPT-4 🤖" <${process.env.EMAIL_SENDER}>`,
      to,
      subject,
      text,
    });

    res.json({ message: '📨 Email envoyé avec succès.' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Erreur lors de l'envoi de l'email." });
  }
});

app.listen(port, () => {
  console.log(`🌐 Serveur ouvert sur http://localhost:${port}`);
});
>>>>>>> 2f3f164 (Message clair expliquant les modifications)
