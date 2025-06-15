// stripe/gpt4Bot.js
import axios from 'axios';

const OPENAI_API_KEY = process.env.OPENAI_API_KEY;

export async function callGpt4(prompt) {
  if (!prompt) throw new Error('Le prompt est nécessaire pour invoquer la muse GPT-4.');

  try {
    const response = await axios.post('https://api.openai.com/v1/chat/completions', {
      model: 'gpt-4o-mini',
      messages: [{ role: 'user', content: prompt }]
    }, {
      headers: {
        'Authorization': `Bearer ${OPENAI_API_KEY}`,
        'Content-Type': 'application/json',
      },
    });

    return response.data.choices[0].message.content;
  } catch (error) {
    console.error('🔥 GPT-4 bot error:', error.response?.data || error.message);
    throw error;
  }
}
app.post('/gpt4', async (req, res) => {
  // ...
});
await axios.post('/gpt4', {
  prompt: promptText,
  name: selectedClient.name,
  email: selectedClient.email,
}, {
  headers: { 'x-api-key': 'clef-secrete-celeste' }
});
