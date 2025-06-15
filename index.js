import express from 'express';
import { handleStripeWebhook } from './webhookHandler.js';
import { whitelistMiddleware } from './whitelist.js';
import { gererClient } from './gestionClient.js';

const router = express.Router();

router.use(whitelistMiddleware); // Applique la whitelist à toutes les routes Stripe

router.post('/webhook', express.raw({ type: 'application/json' }), async (req, res) => {
  const signature = req.headers['stripe-signature'];

  try {
    const { event, message } = await handleStripeWebhook(req.body, signature, process.env.STRIPE_WEBHOOK_SECRET);

    if (message) {
      console.log('Message poétique généré:', message);
    }

    // Supposons que l'event contient des infos client dans event.data.object.customer_details (à adapter selon le webhook)
    const clientData = event.data.object.customer_details || null;

    if (clientData) {
      const clientMessage = await gererClient(clientData);
      console.log('Gestion client par GPT-4:', clientMessage);
      // Tu peux enregistrer ou envoyer ce message ailleurs
    }

    res.json({ received: true });
  } catch (err) {
    res.status(400).send(err.message);
  }
});

export default router;
