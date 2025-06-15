import React, { useState, useEffect } from 'react';

export default function ClientsTable() {
  const [clients, setClients] = useState([]);
  const [search, setSearch] = useState('');

  useEffect(() => {
    fetch('/api/clients')
      .then(res => res.json())
      .then(setClients)
      .catch(console.error);
  }, []);

  const filtered = clients.filter(c =>
    c.name.toLowerCase().includes(search.toLowerCase()) ||
    c.email.toLowerCase().includes(search.toLowerCase())
  );

  // Export CSV simple
  function exportCSV() {
    const csvRows = [
      ['Name', 'Email'],
      ...filtered.map(c => [c.name, c.email])
    ];
    const csvString = csvRows.map(e => e.join(',')).join('\n');
    const blob = new Blob([csvString], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = 'clients.csv'; a.click();
    URL.revokeObjectURL(url);
  }

  return (
    <div>
      <h2 className="mb-4 text-xl">Clients</h2>
      <input
        type="text"
        placeholder="Rechercher..."
        value={search}
        onChange={e => setSearch(e.target.value)}
        className="p-2 mb-4 border"
      />
      <button onClick={exportCSV} className="px-3 py-1 mb-4 text-white bg-green-600 rounded">Exporter CSV</button>
      <table className="w-full border border-collapse">
        <thead>
          <tr className="bg-gray-200">
            <th className="px-4 py-2 border">Nom</th>
            <th className="px-4 py-2 border">Email</th>
          </tr>
        </thead>
        <tbody>
          {filtered.map(c => (
            <tr key={c.id}>
              <td className="px-4 py-2 border">{c.name}</td>
              <td className="px-4 py-2 border">{c.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

import React, { useState, useEffect } from 'react';

export default function ClientsTable() {
  const [clients, setClients] = useState([]);
  const [search, setSearch] = useState('');

  useEffect(() => {
    fetch('/api/clients')
      .then(res => res.json())
      .then(setClients)
      .catch(console.error);
  }, []);

  const filtered = clients.filter(c =>
    c.name.toLowerCase().includes(search.toLowerCase()) ||
    c.email.toLowerCase().includes(search.toLowerCase())
  );

  function exportCSV() {
    const csvRows = [['Nom', 'Email'], ...filtered.map(c => [c.name, c.email])];
    const csvString = csvRows.map(row => row.join(',')).join('\n');
    const blob = new Blob([csvString], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = 'clients.csv'; a.click();
    URL.revokeObjectURL(url);
  }

  return (
    <div>
      <h2 className="mb-4 text-xl">Clients</h2>
      <input
        type="text"
        placeholder="Rechercher..."
        value={search}
        onChange={e => setSearch(e.target.value)}
        className="p-2 mb-4 border"
      />
      <button onClick={exportCSV} className="px-3 py-1 mb-4 text-white bg-green-700 rounded">Exporter CSV</button>
      <table className="w-full border border-collapse">
        <thead>
          <tr className="bg-gray-200">
            <th className="px-4 py-2 border">Nom</th>
            <th className="px-4 py-2 border">Email</th>
          </tr>
        </thead>
        <tbody>
          {filtered.map(c => (
            <tr key={c.id}>
              <td className="px-4 py-2 border">{c.name}</td>
              <td className="px-4 py-2 border">{c.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
