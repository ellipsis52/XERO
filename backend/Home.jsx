// PayButton.jsx
import { useState } from 'react';
import axios from 'axios';

export default function PayButton() {
  const [redirectUrl, setRedirectUrl] = useState(null);

  const handlePayment = async () => {
    try {
      const res = await axios.post('https://xero.netmanagement.online/saferpay/payment');
      setRedirectUrl(res.data.redirectUrl);
      window.location.href = res.data.redirectUrl;
    } catch (err) {
      console.error('Erreur paiement:', err);
      alert('Échec du paiement');
    }
  };

  return (
    <button onClick={handlePayment} className="p-4 text-white bg-green-600 rounded-xl">
      Payer l’abonnement Xero Accountant – CHF 1000
    </button>
  );
}
