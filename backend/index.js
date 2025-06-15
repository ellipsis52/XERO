import express from 'express';
import { handlePaymentIntent } from './stripeController.js';

const app = express();
app.use(express.json());

app.post('/paiement', handlePaymentIntent);

app.listen(3000, () => {
  console.log('🎼 Le système de paiement écoute sur le port 3000...');
});
