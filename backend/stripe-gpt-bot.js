require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const { Configuration, OpenAIApi } = require('openai');
const Stripe = require('stripe');

const app = express();
const port = process.env.PORT || 4242;

// Initialisation de Stripe
const stripe = Stripe(process.env.STRIPE_SECRET_KEY);

// Configuration de GPT-4
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

// Pour lire les événements webhook
app.use(bodyParser.raw({ type: 'application/json' }));

// Le cœur du gardien : réception des webhooks Stripe
app.post('/webhook', async (req, res) => {
  const sig = req.headers['stripe-signature'];

  let event;

  try {
    event = stripe.webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET);
  } catch (err) {
    console.error('❌ Erreur de signature webhook:', err.message);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  // 💬 Traitement intelligent via GPT-4
  if (event.type === 'payment_intent.succeeded') {
    const paymentIntent = event.data.object;
    console.log(`💰 Paiement réussi : ${paymentIntent.amount} ${paymentIntent.currency}`);

    const gptResponse = await openai.createChatCompletion({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: "Tu es un assistant de monitoring de paiements Stripe pour une banque numérique." },
        {
          role: 'user',
          content: `Un paiement a été effectué. Détail:\nMontant: ${paymentIntent.amount}\nDevise: ${paymentIntent.currency}\nClient: ${paymentIntent.customer}`
        }
      ]
    });

    console.log('🤖 GPT-4 a répondu :', gptResponse.data.choices[0].message.content);
  }

  res.status(200).send();
});

app.listen(port, () => {
  console.log(`⚡ Stripe + GPT bot en écoute sur le port ${port}`);
});
const axios = require('axios'); // en haut si ce n’est pas déjà importé

// Notification Discord
await axios.post(process.env.DISCORD_WEBHOOK_URL, {
  content: `✅ Paiement reçu : ${paymentIntent.amount / 100} ${paymentIntent.currency.toUpperCase()}\nRéponse de GPT : ${gptResponse.data.choices[0].message.content}`
});
const nodemailer = require('nodemailer');

const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST,
  port: process.env.SMTP_PORT,
  secure: false,
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASS
  }
});

await transporter.sendMail({
  from: `"StripeBot 🤖" <${process.env.EMAIL_USER}>`,
  to: process.env.EMAIL_TO,
  subject: "💸 Nouveau paiement reçu",
  text: `Montant : ${paymentIntent.amount / 100} ${paymentIntent.currency.toUpperCase()}\nRéponse de GPT : ${gptResponse.data.choices[0].message.content}`
});
require('dotenv').config();
const express = require('express');
const Stripe = require('stripe');
const axios = require('axios');
const { OpenAI } = require('openai');
const nodemailer = require('nodemailer');

const stripe = Stripe(process.env.STRIPE_SECRET_KEY);
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const app = express();
app.use(express.json());

// Notification Email setup
const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST,
  port: process.env.SMTP_PORT,
  secure: false,
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASS,
  },
});

app.post('/webhook', express.raw({ type: 'application/json' }), async (req, res) => {
  let event;

  try {
    event = JSON.parse(req.body);
  } catch (err) {
    console.error('⚠️  Webhook error:', err.message);
    return res.sendStatus(400);
  }

  if (event.type === 'payment_intent.succeeded') {
    const paymentIntent = event.data.object;

    const gptResponse = await openai.chat.completions.create({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: 'Tu es un assistant de paiement intelligent.' },
        { role: 'user', content: `Un paiement de ${paymentIntent.amount / 100} ${paymentIntent.currency.toUpperCase()} vient d’être effectué.` },
      ],
    });

    const messageContent = gptResponse.choices[0].message.content;
    const finalMessage = `💸 Paiement reçu : ${paymentIntent.amount / 100} ${paymentIntent.currency.toUpperCase()}\n🧠 GPT : ${messageContent}`;

    // Notification Discord
    await axios.post(process.env.DISCORD_WEBHOOK_URL, {
      content: finalMessage,
    });

    // Notification Email
    await transporter.sendMail({
      from: `"StripeBot 🤖" <${process.env.EMAIL_USER}>`,
      to: process.env.EMAIL_TO,
      subject: "💳 Nouveau paiement reçu",
      text: finalMessage,
    });

    console.log('✅ Paiement notifié à Discord & Email');
  }

  res.sendStatus(200);
});

app.listen(4242, () => console.log('🌐 Stripe GPT Bot à l’écoute sur le port 4242'));
require('dotenv').config({ path: __dirname + '/.env' });
const express = require('express');
const Stripe = require('stripe');
const axios = require('axios');
const { OpenAI } = require('openai');
const nodemailer = require('nodemailer');

const stripe = Stripe(process.env.STRIPE_SECRET_KEY);
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const app = express();
app.use(express.json());

const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST,
  port: parseInt(process.env.SMTP_PORT),
  secure: false,
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASS,
  },
});

app.post('/webhook', express.raw({ type: 'application/json' }), async (req, res) => {
  let event;

  try {
    event = JSON.parse(req.body);
  } catch (err) {
    console.error('⚠️ Webhook error:', err.message);
    return res.sendStatus(400);
  }

  if (event.type === 'payment_intent.succeeded') {
    const pi = event.data.object;

    const gptResponse = await openai.chat.completions.create({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: 'Tu es un assistant de paiement intelligent.' },
        { role: 'user', content: `Un paiement de ${pi.amount / 100} ${pi.currency.toUpperCase()} a été reçu.` }
      ]
    });

    const content = gptResponse.choices[0].message.content;
    const message = `💸 Paiement reçu : ${pi.amount / 100} ${pi.currency.toUpperCase()}\n🧠 GPT : ${content}`;

    await axios.post(process.env.DISCORD_WEBHOOK_URL, { content: message });

    await transporter.sendMail({
      from: `"StripeBot" <${process.env.EMAIL_USER}>`,
      to: process.env.EMAIL_TO,
      subject: '💳 Nouveau paiement Stripe',
      text: message,
    });

    console.log("✅ Notifications envoyées.");
  }

  res.sendStatus(200);
});

app.listen(4242, () => {
  console.log('🔌 Stripe GPT Bot en écoute sur le port 4242');
});
import express from 'express';
import Stripe from 'stripe';
import cors from 'cors';

const app = express();
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY, { apiVersion: '2022-11-15' });

app.use(cors());
app.use(express.json({
  verify: (req, res, buf) => {
    req.rawBody = buf.toString();
  }
}));

// Webhook endpoint Stripe
app.post('/webhook', express.raw({ type: 'application/json' }), async (req, res) => {
  const sig = req.headers['stripe-signature'];
  let event;

  try {
    event = stripe.webhooks.constructEvent(req.rawBody, sig, process.env.STRIPE_WEBHOOK_SECRET);
  } catch (err) {
    console.log(`⚠️ Webhook signature verification failed: ${err.message}`);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Ici on va appeler GPT-4 pour interpréter ou agir sur l’événement
  await handleStripeEventWithGPT(event);

  res.json({ received: true });
});
