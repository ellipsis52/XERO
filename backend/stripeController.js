import Stripe from 'stripe';
import dotenv from 'dotenv';
import { analysePayment } from './gptBot.js';

dotenv.config();
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

export async function handlePaymentIntent(req, res) {
  try {
    const paymentIntent = await stripe.paymentIntents.create({
      amount: 2000,
      currency: 'eur',
      payment_method_types: ['card'],
    });

    const analysis = await analysePayment(paymentIntent);

    res.json({
      paymentIntent,
      gptAnalysis: analysis,
    });

  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}

export async function handlePaymentIntent(req, res) {
    try {
      const amount = req.body.amount || 2000; // 👈 pour tests dynamiques
  
      const paymentIntent = await stripe.paymentIntents.create({
        amount,
        currency: 'eur',
        payment_method_types: ['card'],
      });
  
      const gptResponse = await analysePayment(paymentIntent);
      const { risque, raison, action } = gptResponse;
  
      // 🎯 Action selon le verdict
      if (action === "bloquer") {
        return res.status(403).json({
          message: "Paiement bloqué par GPT",
          risque,
          raison,
        });
      }
  
      if (action === "alerter") {
        // TODO: envoyer une alerte par mail/Discord
        console.log("🚨 ALERTE :", raison);
      }
  
      // 🟢 Sinon, on autorise
      res.json({
        paymentIntent,
        gpt: gptResponse,
      });
  
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
  }
  async function envoyerAlerteDiscord(message) {
    const webhookURL = process.env.DISCORD_WEBHOOK_URL;
  
    if (!webhookURL) return console.warn("Webhook Discord manquant.");
  
    await axios.post(webhookURL, {
      content: `🛑 Alerte paiement : ${message}`,
    });
  }
  import { sendAlertEmail } from './mailer.js';

if (action === "alerter") {
  await sendAlertEmail(
    "🚨 Alerte GPT-4 sur un paiement",
    `GPT détecte un risque : ${raison}\nNiveau : ${risque}`
  );
}
