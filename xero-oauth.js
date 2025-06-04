import express from 'express';
import axios from 'axios';
import dotenv from 'dotenv';

dotenv.config();

const router = express.Router();

const client_id = process.env.XERO_CLIENT_ID;
const client_secret = process.env.XERO_CLIENT_SECRET;
const redirect_uri = process.env.XERO_REDIRECT_URI;

router.get('/xero/connect', (req, res) => {
  const url = `https://login.xero.com/identity/connect/authorize?response_type=code&client_id=${client_id}&redirect_uri=${encodeURIComponent(redirect_uri)}&scope=openid profile email accounting.transactions offline_access&state=12345`;
  res.redirect(url);
});

router.get('/xero/callback', async (req, res) => {
  const code = req.query.code;

  try {
    const tokenRes = await axios.post('https://identity.xero.com/connect/token', new URLSearchParams({
      grant_type: 'authorization_code',
      code,
      redirect_uri,
      client_id,
      client_secret,
    }));

    const tokens = tokenRes.data;

    // Ici, tu peux stocker tokens.access_token et tokens.refresh_token selon ton système
    console.log('Tokens Xero reçus:', tokens);

    res.send('Connexion Xero réussie ! Tu peux fermer cette fenêtre.');
  } catch (error) {
    console.error('Erreur OAuth Xero:', error.response?.data || error.message);
    res.status(500).send('Erreur lors de la connexion à Xero');
  }
});
app.get('/xero/contacts', async (req, res) => {
    const state = req.query.state;
    if (!state) return res.status(400).send("Manque la clef d’état.");
  
    try {
      const accessToken = await refreshXeroToken(state);
  
      const response = await axios.get('https://api.xero.com/api.xro/2.0/Contacts', {
        headers: {
          Authorization: `Bearer ${accessToken}`,
          Accept: 'application/json',
        }
      });
  
      res.json(response.data);
    } catch (error) {
      console.error("Erreur récupération contacts :", error.response?.data || error.message);
      res.status(500).send("Les contacts restent cachés dans l’ombre.");
    }
  });
  
export default router;
