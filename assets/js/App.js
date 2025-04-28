import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [xeroData, setXeroData] = useState(null);
  const [paymentStatus, setPaymentStatus] = useState(null);
  const [gptResponse, setGptResponse] = useState('');
  const [errorMessage, setErrorMessage] = useState(null);
  const [paymentValue, setPaymentValue] = useState(100);
  const [currency, setCurrency] = useState('EUR'); // Devise par défaut : EUR
  const [loading, setLoading] = useState(false);
  const [bgColor, setBgColor] = useState('bg-green-200');
  const [userQuestion, setUserQuestion] = useState('');

  const fetchXeroData = async () => {
    setLoading(true);
    try {
      const response = await axios.get('https://api.xero.com/api.xro/2.0/Invoices', {
        headers: { 'Authorization': 'Bearer YOUR_XERO_ACCESS_TOKEN' },
      });
      setXeroData(response.data);
    } catch (error) {
      setErrorMessage('Erreur lors de la récupération des données Xero.');
    } finally {
      setLoading(false);
    }
  };

  const processPayment = async (amount) => {
    setLoading(true);
    try {
      const response = await axios.post('https://www.saferpay.com/api/v1/payments', { 
        amount, 
        currency: currency // Utilisation de la devise sélectionnée
      });
      setPaymentStatus(response.data);
    } catch (error) {
      setErrorMessage('Erreur lors du traitement du paiement avec Saferpay.');
    } finally {
      setLoading(false);
    }
  };

  const fetchGptResponse = async (prompt) => {
    setLoading(true);
    try {
      const response = await axios.post('https://api.openai.com/v1/chat/completions', {
        model: 'gpt-4',
        messages: [{ role: 'user', content: prompt }],
      }, {
        headers: { 'Authorization': `Bearer YOUR_OPENAI_API_KEY` },
      });
      setGptResponse(response.data.choices[0].message.content);
    } catch (error) {
      setErrorMessage('Erreur lors de la communication avec GPT-4.');
    } finally {
      setLoading(false);
    }
  };

  const handleUserQuestion = () => {
    if (userQuestion.trim()) {
      fetchGptResponse(`Gère Xero Partner 2.0 : ${userQuestion}`);
      setUserQuestion('');
    }
  };

  return (
    <div className={`flex flex-col items-center justify-start min-h-screen py-10 px-4 ${bgColor} text-white`}>
      <div className="w-full max-w-4xl p-8 bg-gray-900 shadow-2xl rounded-2xl">
        <h1 className="mb-8 text-4xl font-bold text-center">Xero Partner 2.0</h1>

        {errorMessage && (
          <div className="p-4 mb-6 text-white bg-red-600 rounded-md">
            <strong>Erreur:</strong> {errorMessage}
          </div>
        )}

        <div className="flex flex-col gap-4 mb-6 md:flex-row">
          <button
            onClick={fetchXeroData}
            className="flex-1 px-6 py-3 text-black transition bg-white rounded-md hover:bg-gray-300"
            disabled={loading}
          >
            {loading ? 'Chargement...' : 'Connexion à Xero'}
          </button>
          <input
            type="number"
            value={paymentValue}
            onChange={(e) => setPaymentValue(e.target.value)}
            className="flex-1 px-4 py-3 text-black bg-white rounded-md"
          />
          <select
            value={currency}
            onChange={(e) => setCurrency(e.target.value)}
            className="flex-1 px-4 py-3 text-black bg-white rounded-md"
          >
            <option value="EUR">EUR (Euro)</option>
            <option value="USD">USD (Dollar)</option>
            <option value="GBP">GBP (Livre Sterling)</option>
            <option value="CHF">CHF (Franc Suisse)</option>
          </select>
          <button
            onClick={() => processPayment(paymentValue)}
            className="flex-1 px-6 py-3 text-black transition bg-white rounded-md hover:bg-gray-300"
            disabled={loading}
          >
            {loading ? 'Paiement...' : 'Procéder au Paiement'}
          </button>
        </div>

        {xeroData && (
          <div className="mb-6">
            <h2 className="mb-3 text-2xl font-semibold">Données Xero</h2>
            <pre className="p-4 overflow-x-auto bg-gray-800 rounded-md">{JSON.stringify(xeroData, null, 2)}</pre>
          </div>
        )}

        {paymentStatus && (
          <div className="mb-6">
            <h2 className="mb-3 text-2xl font-semibold">Statut du Paiement</h2>
            <pre className="p-4 overflow-x-auto bg-gray-800 rounded-md">{JSON.stringify(paymentStatus, null, 2)}</pre>
          </div>
        )}

        <div className="mb-6">
          <h2 className="mb-3 text-2xl font-semibold">Communication avec GPT-4</h2>
          <textarea
            value={userQuestion}
            onChange={(e) => setUserQuestion(e.target.value)}
            placeholder="Posez vos questions pour gérer Xero Partner 2.0..."
            className="w-full p-4 mb-4 text-white bg-gray-800 rounded-md"
            rows="4"
          />
          <button
            onClick={handleUserQuestion}
            className="w-full px-6 py-3 text-black transition bg-white rounded-md hover:bg-gray-300"
            disabled={loading}
          >
            Envoyer à GPT-4
          </button>
        </div>

        {gptResponse && (
          <div className="mb-6">
            <h2 className="mb-3 text-2xl font-semibold">Réponse de GPT-4</h2>
            <div className="p-4 whitespace-pre-line bg-gray-800 rounded-md">{gptResponse}</div>
          </div>
        )}

        <p className="mt-8 text-sm text-center">Powered by netmanagement.online © 2025</p>
      </div>
    </div>
  );
}

export default App;
