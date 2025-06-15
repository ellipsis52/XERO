import adminRoutes from './routes/admin.js';
app.use('/api/admin', adminRoutes);
import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

// Données simulées — à remplacer par une vraie DB (Prisma par ex)
const clients = [
  { id: '1', name: 'Alice', email: 'alice@example.com' },
  { id: '2', name: 'Bob', email: 'bob@example.com' },
];

app.get('/api/clients', (req, res) => {
  res.json(clients);
});

// Plus tard : routes Stripe, GPT, messages...

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Server runs sur http://localhost:${PORT}`);
});
import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import Stripe from 'stripe';
import { Configuration, OpenAIApi } from 'openai';

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

// Données simulées clients/messages (à remplacer par DB)
const clients = [
  { id: '1', name: 'Alice', email: 'alice@example.com' },
  { id: '2', name: 'Bob', email: 'bob@example.com' },
];

const messages = [
  { id: '1', prompt: 'Bonjour', response: 'Salut, comment puis-je t’aider ?', clientId: '1', createdAt: new Date() },
];

// Routes

// Clients
app.get('/api/clients', (req, res) => res.json(clients));

// Messages GPT
app.get('/api/messages', (req, res) => res.json(messages));

// Créer un prompt GPT
app.post('/api/gpt', async (req, res) => {
  try {
    const { prompt, clientId } = req.body;
    const completion = await openai.createChatCompletion({
      model: 'gpt-4',
      messages: [{ role: 'user', content: prompt }],
    });
    const response = completion.data.choices[0].message.content;

    // Sauvegarder le message (simulation)
    messages.push({
      id: (messages.length + 1).toString(),
      prompt,
      response,
      clientId,
      createdAt: new Date(),
    });

    res.json({ response });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Stripe - créer PaymentIntent
app.post('/api/create-payment-intent', async (req, res) => {
  try {
    const { amount } = req.body; // en cents
    const paymentIntent = await stripe.paymentIntents.create({
      amount,
      currency: 'eur',
      automatic_payment_methods: { enabled: true },
    });
    res.json({ clientSecret: paymentIntent.client_secret });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`✨ Serveur rayonnant sur http://localhost:${PORT}`);
});
