import React, { useState, useEffect } from 'react';

export default function Dashboard() {
  const [entries, setEntries] = useState([]);
  const [service, setService] = useState('Xero');

  useEffect(() => {
    fetch(`/api/entries/${service}`)
      .then(res => res.json())
      .then(data => setEntries(data));
  }, [service]);

  return (
    <div className="p-6">
      <h1 className="mb-4 text-3xl font-bold">📜 OpenSpace ePlanet</h1>

      <select value={service} onChange={e => setService(e.target.value)} className="mb-4">
        <option value="Stripe">Stripe</option>
        <option value="Xero">Xero</option>
        <option value="OKX">OKX</option>
        <option value="SaferPay">SaferPay</option>
        <option value="Solaris">Solaris</option>
      </select>

      <div className="grid gap-4">
        {entries.map((entry, index) => (
          <div key={index} className="p-4 border rounded shadow">
            <p><strong>Réf :</strong> {entry.reference}</p>
            <p><strong>Montant :</strong> {entry.amount} {entry.currency}</p>
            <p><strong>Par :</strong> {entry.initiated_by}</p>
            <p><strong>Date :</strong> {new Date(entry.date).toLocaleString()}</p>
            <p><strong>Statut :</strong> {entry.status}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
