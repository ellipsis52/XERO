export async function envoyerPrompt(prompt) {
    const res = await fetch('/api/gpt4', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt })
    });
  
    const data = await res.json();
    return data.reply;
  }
  import { Configuration, OpenAIApi } from 'openai';

  const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
  });
  const openai = new OpenAIApi(configuration);
  
  app.post('/api/gpt', async (req, res) => {
    try {
      const { prompt } = req.body;
      const completion = await openai.createChatCompletion({
        model: 'gpt-4',
        messages: [{ role: 'user', content: prompt }],
      });
      res.json({ response: completion.data.choices[0].message.content });
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
  });
    