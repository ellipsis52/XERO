import React, { useState } from 'react';
import { loadStripe } from '@stripe/stripe-js';
import {
  Elements,
  CardElement,
  useStripe,
  useElements,
} from '@stripe/react-stripe-js';

const stripePromise = loadStripe('pk_test_...'); // Ta clé publique Stripe ici

function CheckoutForm() {
  const stripe = useStripe();
  const elements = useElements();
  const [message, setMessage] = useState('');

  async function handleSubmit(e) {
    e.preventDefault();
    if (!stripe || !elements) return;

    const amount = 5000; // 50€ en centimes

    // Appeler backend pour créer PaymentIntent
    const res = await fetch('/api/create-payment-intent', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ amount }),
    });
    const { clientSecret, error } = await res.json();
    if (error) {
      setMessage(error);
      return;
    }

    const result = await stripe.confirmCardPayment(clientSecret, {
      payment_method: { card: elements.getElement(CardElement) },
    });

    if (result.error) {
      setMessage(`Erreur: ${result.error.message}`);
    } else if (result.paymentIntent.status === 'succeeded') {
      setMessage('Paiement réussi, merci !');
    }
  }

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto">
      <CardElement className="p-3 mb-4 border rounded" />
      <button
        type="submit"
        disabled={!stripe}
        className="px-4 py-2 text-white bg-indigo-700 rounded"
      >
        Payer 50€
      </button>
      {message && <p className="mt-4">{message}</p>}
    </form>
  );
}

export default function PaymentsPage() {
  return (
    <div>
      <h2 className="mb-4 text-xl">Paiements</h2>
      <Elements stripe={stripePromise}>
        <CheckoutForm />
      </Elements>
    </div>
  );
}
