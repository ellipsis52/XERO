import { useState } from 'react';
import axios from 'axios';

export default function AdminLogin({ onLogin }) {
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async () => {
    try {
      const res = await axios.post('/api/admin/login', { password });
      if (res.data.success) {
        onLogin(true);
      } else {
        setError("Mot de passe incorrect.");
      }
    } catch {
      setError("Erreur serveur.");
    }
  };

  return (
    <div className="max-w-sm p-4 mx-auto">
      <h1 className="mb-4 text-xl">Connexion admin</h1>
      <input
        type="password"
        placeholder="Mot de passe"
        className="w-full p-2 border"
        onChange={(e) => setPassword(e.target.value)}
      />
      <button className="w-full p-2 mt-2 text-white bg-blue-600" onClick={handleLogin}>
        Se connecter
      </button>
      {error && <p className="mt-2 text-red-500">{error}</p>}
    </div>
  );
}
