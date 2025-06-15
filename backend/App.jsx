import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginXero from './components/LoginXero';
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginXero />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </Router>
  );
}

export default App;

