import React, { useState, useEffect } from 'react';

export default function MessagesPage() {
  const [messages, setMessages] = useState([]);
  const [prompt, setPrompt] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetch('/api/messages')
      .then(res => res.json())
      .then(setMessages)
      .catch(console.error);
  }, []);

  async function sendPrompt() {
    if (!prompt.trim()) return;
    setLoading(true);
    try {
      const res = await fetch('/api/gpt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, clientId: '1' }), // clientId fixe pour l'exemple
      });

      