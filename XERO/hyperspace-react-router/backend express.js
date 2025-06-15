import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import { Configuration, OpenAIApi } from 'openai';

dotenv.config();

const app = express();
const port = process.env.PORT || 3001;

app.use(cors());
app.use(express.json());

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

app.post('/gpt4', async (req, res) => {
  const { prompt } = req.body;
  if (!prompt) {
    return res.status(400).json({ error: "Le prompt est requis." });
  }

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
    console.error("Erreur OpenAI:", error.response?.data || error.message);
    res.status(500).json({ error: "Erreur lors de la communication avec GPT-4." });
  }
});

app.listen(port, () => {
  console.log(`🌟 Backend GPT-4 prêt sur http://localhost:${port}`);
});
// Middleware de sécurité
app.use((req, res, next) => {
  const key = req.headers['x-api-key'];
  if (key !== process.env.API_SECRET_KEY) {
    return res.status(403).json({ error: '⛔ Clé API invalide.' });
  }
  next();
});
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
import { PrismaClient } from '@prisma/client';
const prisma = new PrismaClient();
app.post('/resend-message', async (req, res) => {
  const { messageId } = req.body;
  const message = await prisma.message.findUnique({ where: { id: messageId }, include: { client: true } });
  if (!message) return res.status(404).send("Message introuvable");
  
  await sendEmail({
    to: message.client.email,
    subject: "Message renvoyé",
    text: message.response
  });

  res.send("Email renvoyé.");
});
