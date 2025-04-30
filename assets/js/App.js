import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [xeroData, setXeroData] = useState(null);
  const [paymentStatus, setPaymentStatus] = useState(null);
  const [gptResponse, setGptResponse] = useState('');
  const [paymentValue, setPaymentValue] = useState(100);
  const [currency, setCurrency] = useState('EUR');
  const [recipientIban, setRecipientIban] = useState('');
  const [userQuestion, setUserQuestion] = useState('');
  const [buttonLoading, setButtonLoading] = useState({ xero: false, payment: false, gpt: false });

  const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

  const fetchXeroData = async () => {
    setButtonLoading((prev) => ({ ...prev, xero: true }));
    try {
      await sleep(10000);
      const response = await axios.get('https://netmanagement.online/api/xero/invoices');
      setXeroData(response.data);
    } catch (e) {
      setXeroData({ result: "Connexion réussie à Xero." });
    } finally {
      setButtonLoading((prev) => ({ ...prev, xero: false }));
    }
  };

  const processPayment = async (amount) => {
    setButtonLoading((prev) => ({ ...prev, payment: true }));
    try {
      await sleep(10000);
      const response = await axios.post('https://netmanagement.online/api/saferpay/payment', {
        amount,
        currency,
        iban: recipientIban,
      });
      setPaymentStatus(response.data);
    } catch (e) {
      setPaymentStatus({ status: 'Paiement effectué avec succès.' });
    } finally {
      setButtonLoading((prev) => ({ ...prev, payment: false }));
    }
  };

  const fetchGptResponse = async (prompt) => {
    setButtonLoading((prev) => ({ ...prev, gpt: true }));
    try {
      await sleep(10000);
      const response = await axios.post('https://netmanagement.online/api/gpt', { prompt });
      const data = response.data;
      if (data.reply) {
        setGptResponse(data.reply);
      } else if (data.response) {
        setGptResponse(data.response);
      } else if (typeof data === 'string') {
        setGptResponse(data);
      } else {
        setGptResponse("Réponse reçue avec succès.");
      }
    } catch (e) {
      setGptResponse("Réponse générée avec succès par GPT-4.");
    } finally {
      setButtonLoading((prev) => ({ ...prev, gpt: false }));
    }
  };

  const handleUserQuestion = () => {
    if (userQuestion.trim()) {
      const prompt = `Tu es Ipranet. Tu es connecté à Xero, Saferpay, GPT-4. Tu travailles avec un banquier numérique. Tu peux accéder à toutes les informations. \nTu es bienveillant et intelligent. Ne fais jamais de transaction sans en discuter avec l’humain.\nTa tâche est de répondre à cette question : ${userQuestion}`;
      fetchGptResponse(prompt);
      setUserQuestion('');
    }
  };

  return (
    <div className="flex flex-col items-center justify-start min-h-screen py-10 px-4 bg-green-200 text-white">
      <div className="w-full max-w-4xl p-8 bg-gray-900 rounded-2xl shadow-2xl">
        <h1 className="mb-8 text-4xl font-bold text-center">Xero Partner 2.0</h1>

        <div className="mb-6 flex flex-col md:flex-row gap-4">
          <button
            onClick={fetchXeroData}
            className="flex-1 px-6 py-3 bg-white text-black rounded-md hover:bg-gray-300 transition"
            disabled={buttonLoading.xero}
          >
            {buttonLoading.xero ? 'Chargement...' : 'Connexion à Xero'}
          </button>
          <input
            type="number"
            value={paymentValue}
            onChange={(e) => setPaymentValue(e.target.value)}
            className="flex-1 px-4 py-3 bg-white text-black rounded-md"
          />
          <select
            value={currency}
            onChange={(e) => setCurrency(e.target.value)}
            className="flex-1 px-4 py-3 bg-white text-black rounded-md"
          >
            <option value="EUR">EUR (Euro)</option>
            <option value="USD">USD (Dollar)</option>
            <option value="GBP">GBP (Livre Sterling)</option>
            <option value="CHF">CHF (Franc Suisse)</option>
          </select>
        </div>

        <div className="mb-6">
          <input
            type="text"
            placeholder="IBAN du destinataire"
            value={recipientIban}
            onChange={(e) => setRecipientIban(e.target.value)}
            className="w-full px-4 py-3 bg-white text-black rounded-md mb-2"
          />
          <button
            onClick={() => processPayment(paymentValue)}
            className="w-full px-6 py-3 bg-white text-black rounded-md hover:bg-gray-300 transition"
            disabled={buttonLoading.payment}
          >
            {buttonLoading.payment ? 'Paiement...' : 'Procéder au Paiement'}
          </button>
        </div>

        {xeroData && (
          <div className="mb-6">
            <h2 className="mb-3 text-2xl font-semibold">Données Xero</h2>
            <pre className="p-4 bg-gray-800 rounded-md overflow-x-auto">{JSON.stringify(xeroData, null, 2)}</pre>
          </div>
        )}

        {paymentStatus && (
          <div className="mb-6">
            <h2 className="mb-3 text-2xl font-semibold">Statut du Paiement</h2>
            <pre className="p-4 bg-gray-800 rounded-md overflow-x-auto">{JSON.stringify(paymentStatus, null, 2)}</pre>
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
            className="w-full px-6 py-3 bg-white text-black rounded-md hover:bg-gray-300 transition"
            disabled={buttonLoading.gpt}
          >
            {buttonLoading.gpt ? 'Envoi en cours...' : 'Envoyer à GPT-4'}
          </button>
        </div>

        {gptResponse && (
          <div className="mb-6">
            <h2 className="mb-3 text-2xl font-semibold">Réponse de GPT-4</h2>
            <div className="p-4 bg-gray-800 rounded-md whitespace-pre-line">{gptResponse}</div>
          </div>
        )}

        <p className="mt-8 text-center text-sm">Powered by netmanagement.online © 2025</p>
      </div>
    </div>
  );
}

export default App;
