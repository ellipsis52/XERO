const express = require('express');
const Stripe = require('stripe');
const cors = require('cors');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

const stripe = Stripe(process.env.STRIPE_SECRET_KEY);

app.post('/create-checkout-session', async (req, res) => {
  const session = await stripe.checkout.sessions.create({
    payment_method_types: ['card'],
    line_items: [{
      price_data: {
        currency: 'eur',
        product_data: {
          name: 'Accès Premium',
        },
        unit_amount: 2000,
      },
      quantity: 1,
    }],
    mode: 'payment',
    success_url: 'https://tonsite.com/success.html',
    cancel_url: 'https://tonsite.com/cancel.html',
  });

  res.json({ id: session.id });
});

app.listen(3000, () => console.log('Serveur Stripe démarré sur le port 3000'));

const express = require('express');
const Stripe = require('stripe');
const router = express.Router();

const stripe = Stripe(process.env.STRIPE_SECRET_KEY); // Stockée dans .env

router.post('/create-checkout-session', async (req, res) => {
  const session = await stripe.checkout.sessions.create({
    payment_method_types: ['card'],
    line_items: [{
      price_data: {
        currency: 'eur',
        product_data: {
          name: 'Produit magique',
        },
        unit_amount: 2000, // 20,00 €
      },
      quantity: 1,
    }],
    mode: 'payment',
    success_url: 'https://tonsite.com/success',
    cancel_url: 'https://tonsite.com/cancel',
  });

  res.json({ id: session.id });
});

module.exports = router;
