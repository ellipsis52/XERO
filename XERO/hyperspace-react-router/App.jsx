import { BrowserRouter as Router, Routes, Route, Link, Navigate } from 'react-router-dom';

import ClientsTable from './pages/ClientsTable';
import PaymentsTable from './pages/PaymentsTable';
import MessagesTable from './pages/MessagesTable';

export default function App() {
  return (
    <Router>
      <nav className="flex gap-6 p-4 text-white bg-blue-900">
        <Link to="/clients" className="hover:underline">Clients</Link>
        <Link to="/payments" className="hover:underline">Paiements</Link>
        <Link to="/messages" className="hover:underline">Messages GPT</Link>
      </nav>
      <main className="p-6">
        <Routes>
          <Route path="/" element={<Navigate to="/clients" replace />} />
          <Route path="/clients" element={<ClientsTable />} />
          <Route path="/payments" element={<PaymentsTable />} />
          <Route path="/messages" element={<MessagesTable />} />
        </Routes>
      </main>
    </Router>
  );
}
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from 'react-router-dom';
import ClientsTable from './pages/ClientsTable';
import PaymentsPage from './pages/PaymentsPage';
import MessagesPage from './pages/MessagesPage';

export default function App() {
  return (
    <Router>
      <nav className="flex gap-6 p-4 text-white bg-indigo-800">
        <Link to="/clients" className="hover:underline">Clients</Link>
        <Link to="/payments" className="hover:underline">Paiements</Link>
        <Link to="/messages" className="hover:underline">Messages GPT</Link>
      </nav>
      <main className="p-6">
        <Routes>
          <Route path="/" element={<Navigate to="/clients" replace />} />
          <Route path="/clients" element={<ClientsTable />} />
          <Route path="/payments" element={<PaymentsPage />} />
          <Route path="/messages" element={<MessagesPage />} />
        </Routes>
      </main>
    </Router>
  );
}
