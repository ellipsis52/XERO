// src/components/LoginXero.jsx
import React from 'react';

const LoginXero = () => {
  const handleLogin = () => {
    window.location.href = 'http://localhost:3000/api/xero/auth'; // redirige vers ton backend
  };

  return (
    <section className="wrapper style1">
      <div className="inner">
        <h2>Connexion à Xero</h2>
        <p>Connecte ton compte pour accéder à tes données comptables.</p>
        <button className="button primary" onClick={handleLogin}>
          Se connecter à Xero
        </button>
      </div>
    </section>
  );
};

export default LoginXero;
