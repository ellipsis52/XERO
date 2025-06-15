import React, { useEffect, useState } from 'react';

export default function PoetryList() {
  const [poems, setPoems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchPoems() {
      try {
        const res = await fetch('/poetry');
        if (!res.ok) throw new Error(`Erreur ${res.status}`);

        const data = await res.json();
        setPoems(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchPoems();
  }, []);

  if (loading) return <p style={{ fontStyle: 'italic', color: '#666' }}>Chargement des vers en cours...</p>;
  if (error) return <p style={{ color: 'crimson' }}>Erreur : {error}</p>;

  return (
    <div style={{
      background: 'linear-gradient(135deg, #1e3c72, #2a5298)',
      color: '#e0e7ff',
      minHeight: '100vh',
      padding: '2rem',
      fontFamily: "'Georgia', serif",
      display: 'flex',
      flexDirection: 'column',
      gap: '1.5rem'
    }}>
      <h1 style={{ textAlign: 'center', fontSize: '2.5rem', marginBottom: '1rem' }}>
        Poèmes des Transactions
      </h1>
      {poems.length === 0 && <p>Aucun poème n'a encore été tissé.</p>}
      {poems.map(({ paymentId, message, date }) => (
        <div key={paymentId + date} style={{
          background: 'rgba(255, 255, 255, 0.1)',
          borderRadius: '12px',
          padding: '1rem 1.5rem',
          boxShadow: '0 4px 15px rgba(0,0,0,0.2)',
          whiteSpace: 'pre-wrap',
          fontSize: '1.1rem',
          lineHeight: '1.5',
          userSelect: 'text'
        }}>
          <div style={{ fontSize: '0.8rem', opacity: 0.7, marginBottom: '0.5rem' }}>
            Transaction ID : <code>{paymentId}</code> — {new Date(date).toLocaleString()}
          </div>
          <blockquote style={{ margin: 0, fontStyle: 'italic' }}>
            {message}
          </blockquote>
        </div>
      ))}
    </div>
  );
}
