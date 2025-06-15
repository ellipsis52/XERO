import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function AdminMessages() {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    axios.get('/messages', {
      headers: { 'x-api-key': 'clef-secrete-celeste' }
    }).then(res => setMessages(res.data));
  }, []);

  return (
    <div className="min-h-screen p-6 text-black bg-white">
      <h2 className="mb-4 text-2xl font-bold">📚 Archive des Messages GPT</h2>
      <ul className="divide-y divide-gray-400">
        {messages.map((msg, idx) => (
          <li key={idx} className="py-3">
            <p className="text-sm text-gray-500">👤 {msg.client.name} ({msg.client.email})</p>
            <p className="mt-1 text-gray-800 whitespace-pre-wrap">📝 {msg.response}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

<button onClick={() => resendEmail(msg)} className="text-blue-600 hover:underline">📧 Renvoyer</button>
<button onClick={() => editMessage(msg)} className="text-green-600 hover:underline">✏️ Modifier</button>
