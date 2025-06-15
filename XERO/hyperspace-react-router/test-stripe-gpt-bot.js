const axios = require('axios');

const fakePaymentIntent = {
  id: 'pi_test_12345',
  object: 'payment_intent',
  amount: 4999, // 49.99 €
  currency: 'eur',
  status: 'succeeded'
};

const fakeEvent = {
  id: 'evt_test_webhook',
  type: 'payment_intent.succeeded',
  data: {
    object: fakePaymentIntent
  }
};

async function sendFakeWebhook() {
  try {
    const res = await axios.post(
      'http://localhost:4242/webhook',
      fakeEvent,
      {
        headers: { 'Content-Type': 'application/json' }
      }
    );
    console.log('✅ Webhook simulé avec succès !', res.status);
  } catch (err) {
    console.error('❌ Erreur lors de l’envoi du webhook :', err.message);
  }
}

sendFakeWebhook();
