// stripe/webhookHandler.js
import Stripe from 'stripe';
import { callGpt4 } from './gpt4Bot.js';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY, { apiVersion: '2023-05-15' });

export async function handleStripeWebhook(rawBody, signature, webhookSecret) {
  let event;

  try {
    event = stripe.webhooks.constructEvent(rawBody, signature, webhookSecret);
  } catch (err) {
    console.error('❌ Validation webhook Stripe échouée:', err.message);
    throw new Error(`Webhook Error: ${err.message}`);
  }

  if (event.type === 'payment_intent.succeeded') {
    const paymentId = event.data.object.id;
    console.log('✅ Paiement réussi:', paymentId);

    // Le robot GPT-4 compose un chant en l'honneur du paiement
    const prompt = `Un paiement vient d'être effectué avec succès, ID: ${paymentId}. Compose un message poétique pour célébrer cette transaction.`;

    try {
      const message = await callGpt4(prompt);
      console.log('✨ GPT-4 murmure:', message);
      return { event, message };
    } catch (err) {
      console.error('🔥 Erreur lors de l’appel GPT-4:', err.message);
      return { event, message: null };
    }
  }

  console.log(`ℹ️ Événement Stripe reçu: ${event.type}`);
  return { event, message: null };
}
