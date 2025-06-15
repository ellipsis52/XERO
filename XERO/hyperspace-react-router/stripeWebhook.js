import express from 'express';
import Stripe from 'stripe';
import { Configuration, OpenAIApi } from 'openai';

const app = express();
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY, { apiVersion: '2022-11-15' });
const openai = new OpenAIApi(new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
}));

app.use(express.json());

app.post('/webhook', async (req, res) => {
  const event = req.body;

  // Extrait quelques données importantes pour GPT-4
  const eventSummary = `Event type: ${event.type}\n` +
                       `Amount: ${event.data.object.amount}\n` +
                       `Currency: ${event.data.object.currency}\n` +
                       `Customer: ${event.data.object.customer}\n`;

  try {
    // Appel à GPT-4 pour analyser l'événement Stripe
    const completion = await openai.createChatCompletion({
      model: "gpt-4",
      messages: [
        { role: "system", content: "Tu es un assistant expert en gestion de paiements Stripe. Analyse cet événement et dis-moi s'il faut autoriser la transaction, la rejeter, ou demander une vérification." },
        { role: "user", content: eventSummary }
      ],
    });

    const gptResponse = completion.data.choices[0].message.content.trim();
    console.log("Réponse GPT-4:", gptResponse);

    // Selon la réponse, exécute une action Stripe
    if (gptResponse.toLowerCase().includes("autoriser")) {
      // Par exemple, capture un paiement ou enregistre un événement
      console.log("Paiement autorisé, aucune action additionnelle nécessaire.");
    } else if (gptResponse.toLowerCase().includes("rejeter")) {
      // Exemple : annule un paiement (ici simplifié)
      await stripe.refunds.create({
        payment_intent: event.data.object.payment_intent,
      });
      console.log("Paiement rejeté, remboursement initié.");
    } else if (gptResponse.toLowerCase().includes("vérification")) {
      // Notifier l'équipe ou mettre en attente
      console.log("Paiement en attente de vérification manuelle.");
    }

    res.json({ received: true });
  } catch (error) {
    console.error("Erreur dans le webhook Stripe + GPT-4 :", error);
    res.status(500).send("Erreur serveur");
  }
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Serveur webhook Stripe + GPT-4 en écoute sur le port ${port}`);
});
import express from "express";
import Stripe from "stripe";
import { Configuration, OpenAIApi } from "openai";
import bodyParser from "body-parser";

const app = express();
const port = process.env.PORT || 4242;

// Tes clés secrètes à bien garder dans un fichier .env (ou variables d’environnement)
const stripeSecretKey = process.env.STRIPE_SECRET_KEY;
const openaiApiKey = process.env.OPENAI_API_KEY;
const endpointSecret = process.env.STRIPE_WEBHOOK_SECRET;

const stripe = new Stripe(stripeSecretKey, {
  apiVersion: "2023-08-16",
});

const configuration = new Configuration({
  apiKey: openaiApiKey,
});
const openai = new OpenAIApi(configuration);

// Stripe envoie les webhooks en raw, on utilise bodyParser.raw pour les routes Stripe webhook
app.use(
  "/webhook",
  bodyParser.raw({ type: "application/json" })
);

// Route Stripe webhook pour capter les événements
app.post("/webhook", (req, res) => {
  const sig = req.headers["stripe-signature"];

  let event;

  try {
    event = stripe.webhooks.constructEvent(req.body, sig, endpointSecret);
  } catch (err) {
    console.error("⚠️ Webhook signature verification failed.", err.message);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Ici tu peux gérer les événements Stripe
  if (event.type === "payment_intent.succeeded") {
    const paymentIntent = event.data.object;
    console.log(`💰 Paiement réussi pour ${paymentIntent.amount / 100} €`);

    // Exemple : envoyer un prompt à GPT-4 à chaque paiement réussi
    (async () => {
      try {
        const completion = await openai.createChatCompletion({
          model: "gpt-4",
          messages: [
            { role: "system", content: "Tu es un assistant financier très poétique." },
            { role: "user", content: `Un paiement de ${paymentIntent.amount / 100} € vient d'arriver.` }
          ],
        });
        console.log("GPT-4 répond :", completion.data.choices[0].message.content);
      } catch (error) {
        console.error("Erreur GPT-4 :", error);
      }
    })();
  }

  res.json({ received: true });
});

app.listen(port, () => {
  console.log(`✨ Serveur prêt sur http://localhost:${port}`);
});
await sendDiscordNotification(`✨ Nouvelle transaction poétique:\n${gptResponse.data.choices[0].message.content}`);
const poeticLogs = [];

async function sendDiscordNotification(message) {
  const url = process.env.DISCORD_WEBHOOK_URL;
  if (!url) return; // Pas de webhook configuré, on skip

  try {
    await axios.post(url, { content: message });
  } catch (error) {
    console.error('⚠️ Erreur en envoyant la notification Discord:', error.message);
  }
}

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

        const poem = gptResponse.data.choices[0].message.content;
        console.log('✨ GPT-4 murmure:', poem);

        // Sauvegarde
        poeticLogs.push({
          paymentId: event.data.object.id,
          message: poem,
          date: new Date().toISOString()
        });

        // Envoi Discord
        await sendDiscordNotification(`✨ Nouvelle transaction poétique:\n${poem}`);

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
