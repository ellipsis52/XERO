import { OpenAI } from 'openai';
import dotenv from 'dotenv';
dotenv.config();

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

export async function analysePayment(paymentInfo) {
  const prompt = `
Tu es un bot de contrôle de paiements pour une banque numérique. Voici les détails d'un paiement Stripe :
${JSON.stringify(paymentInfo, null, 2)}
Analyse cette transaction. Y a-t-il un risque de fraude ? Est-ce conforme aux règles de sécurité ? Réponds de façon concise.`;

  const response = await openai.chat.completions.create({
    model: "gpt-4",
    messages: [{ role: "user", content: prompt }],
  });

  return response.choices[0].message.content.trim();
}
export async function analysePayment(paymentInfo) {
    const prompt = `
  Tu es un contrôleur de paiements pour une banque numérique.
  Voici une transaction Stripe :
  
  ${JSON.stringify(paymentInfo, null, 2)}
  
  Analyse-la et réponds en JSON comme ceci :
  {
    "risque": "faible | modéré | élevé",
    "raison": "...",
    "action": "accepter | bloquer | alerter"
  }`;
  
    const response = await openai.chat.completions.create({
      model: "gpt-4",
      messages: [{ role: "user", content: prompt }],
    });
  
    const content = response.choices[0].message.content.trim();
  
    try {
      return JSON.parse(content); // On retourne un objet actionnable
    } catch (err) {
      console.error("❗Erreur de parsing GPT :", content);
      return { risque: "inconnu", raison: "Erreur GPT", action: "alerter" };
    }
  }
  