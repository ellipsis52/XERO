import React, { useState, useEffect } from "react";
import axios from "axios";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

const Loader = ({ text }) => (
  <div className="flex items-center justify-center py-4">
    <div className="w-6 h-6 mr-3 border-b-2 border-white rounded-full animate-spin"></div>
    <span>{text}</span>
  </div>
);

const Home = ({
  fetchXeroData,
  testAuthAPI,
  authStatus,
  authTested,
  xeroData,
  selectedInvoice,
  setSelectedInvoice,
  paymentValue,
  setPaymentValue,
  currency,
  setCurrency,
  recipientIban,
  setRecipientIban,
  processPayment,
  paymentStatus,
  gptResponse,
  userQuestion,
  setUserQuestion,
  handleUserQuestion,
  buttonLoading,
  errorNote,
}) => (
  <div className="w-full max-w-4xl p-8 bg-gray-900 shadow-2xl rounded-2xl">
    <h1 className="mb-8 text-4xl font-bold text-center">Xero Partner 2.0</h1>

    <div className="flex flex-col gap-4 mb-6 md:flex-row">
      <button onClick={fetchXeroData} className="flex-1 px-6 py-3 text-black bg-white rounded-md hover:bg-gray-300" disabled={buttonLoading.xero}>
        {buttonLoading.xero ? <Loader text="Connecting..." /> : "Connect to Xero"}
      </button>
      <button onClick={testAuthAPI} className="flex-1 px-6 py-3 text-black bg-white rounded-md hover:bg-gray-300" disabled={buttonLoading.auth || authTested}>
        {buttonLoading.auth ? <Loader text="Testing Auth..." /> : authTested ? "✅ Auth Verified" : "Test API Auth"}
      </button>
    </div>

    {authStatus && <pre className="p-4 mb-6 whitespace-pre-wrap bg-gray-800 rounded-md">{authStatus}</pre>}

    {xeroData && (
      <div className="mb-6">
        <h2 className="mb-3 text-2xl font-semibold">Xero Data</h2>
        <div className="space-y-2">
          {xeroData.map((invoice) => (
            <div key={invoice.InvoiceID} className="p-4 bg-gray-800 rounded-md cursor-pointer hover:bg-gray-700" onClick={() => setSelectedInvoice(invoice)}>
              <p><strong>{invoice.Contact?.Name}</strong> — {invoice.Total} {invoice.CurrencyCode}</p>
            </div>
          ))}
        </div>
      </div>
    )}

    {selectedInvoice && (
      <div className="mb-6">
        <h2 className="mb-2 text-xl font-semibold">Selected Invoice Details</h2>
        <pre className="p-4 bg-gray-800 rounded-md">{JSON.stringify(selectedInvoice, null, 2)}</pre>
      </div>
    )}

    <div className="flex flex-col gap-4 mb-6 md:flex-row">
      <input type="number" value={paymentValue} onChange={(e) => setPaymentValue(e.target.value)} className="flex-1 px-4 py-3 text-black bg-white rounded-md" />
      <select value={currency} onChange={(e) => setCurrency(e.target.value)} className="flex-1 px-4 py-3 text-black bg-white rounded-md">
        <option value="EUR">EUR</option><option value="USD">USD</option><option value="GBP">GBP</option><option value="CHF">CHF</option>
      </select>
    </div>

    <input type="text" placeholder="Recipient IBAN" value={recipientIban} onChange={(e) => setRecipientIban(e.target.value)} className="w-full px-4 py-3 mb-2 text-black bg-white rounded-md" />
    <button onClick={() => processPayment(paymentValue)} className="w-full px-6 py-3 text-black bg-white rounded-md hover:bg-gray-300" disabled={buttonLoading.payment}>
      {buttonLoading.payment ? <Loader text="Processing Payment..." /> : `Submit ${paymentValue} ${currency}`}
    </button>

    {paymentStatus && <pre className="p-4 mt-6 bg-gray-800 rounded-md">{JSON.stringify(paymentStatus, null, 2)}</pre>}
    {gptResponse && <pre className="p-4 mt-6 bg-gray-800 rounded-md">{gptResponse}</pre>}
    {errorNote && <div className="mt-6 text-red-500">{errorNote}</div>}

    <div className="mt-8">
      <textarea value={userQuestion} onChange={(e) => setUserQuestion(e.target.value)} className="w-full px-4 py-3 mb-2 text-black bg-white rounded-md" placeholder="Ask GPT-4 a question" />
      <button onClick={handleUserQuestion} className="w-full px-6 py-3 text-black bg-white rounded-md hover:bg-gray-300" disabled={buttonLoading.gpt}>
        {buttonLoading.gpt ? <Loader text="Thinking..." /> : "Ask GPT-4"}
      </button>
    </div>
  </div>
);

const App = () => {
  const [xeroData, setXeroData] = useState(null);
  const [paymentStatus, setPaymentStatus] = useState(null);
  const [gptResponse, setGptResponse] = useState("");
  const [paymentValue, setPaymentValue] = useState(100);
  const [currency, setCurrency] = useState("EUR");
  const [recipientIban, setRecipientIban] = useState("");
  const [userQuestion, setUserQuestion] = useState("");
  const [buttonLoading, setButtonLoading] = useState({ xero: false, payment: false, gpt: false, auth: false });
  const [errorNote, setErrorNote] = useState("");
  const [authStatus, setAuthStatus] = useState("");
  const [selectedInvoice, setSelectedInvoice] = useState(null);
  const [authTested, setAuthTested] = useState(false);

  const getAuthHeaders = () => {
    const token = localStorage.getItem("authToken");
    return token ? { Authorization: `Bearer ${token}` } : {};
  };

  const logEvent = async (type, message, status) => {
    try {
      await axios.post("https://netmanagement.online/api/logs", { type, message, status, timestamp: new Date().toISOString() }, { headers: getAuthHeaders() });
    } catch (e) {
      console.error("Logging error:", e.response?.data || e.message);
    }
  };

  const fetchXeroData = async () => {
    setButtonLoading((prev) => ({ ...prev, xero: true }));
    setErrorNote("");
    try {
      const response = await axios.get("https://netmanagement.online/api/xero/invoices", { headers: getAuthHeaders() });
      setXeroData(response.data);
      setErrorNote("Successfully connected to Xero.");
      logEvent("Xero", "Connection successful.", "success");
    } catch (e) {
      setErrorNote("Error connecting to Xero.");
      logEvent("Xero", e.message, "error");
    } finally {
      setButtonLoading((prev) => ({ ...prev, xero: false }));
    }
  };

  const processPayment = async (amount) => {
    setButtonLoading((prev) => ({ ...prev, payment: true }));
    setErrorNote("");
    try {
      if (!recipientIban || !currency || !amount) throw new Error("Missing payment details.");
      const response = await axios.post("https://netmanagement.online/api/saferpay/payment", { amount, currency, iban: recipientIban }, { headers: getAuthHeaders() });
      setPaymentStatus(response.data);
      setErrorNote("Payment successfully sent.");
      logEvent("Payment", "Completed.", "success");
    } catch (e) {
      setErrorNote(e.message || "Payment error.");
      logEvent("Payment", e.message, "error");
    } finally {
      setButtonLoading((prev) => ({ ...prev, payment: false }));
    }
  };

  const fetchGptResponse = async (prompt) => {
    setButtonLoading((prev) => ({ ...prev, gpt: true }));
    setErrorNote("");
    try {
      const response = await axios.post("https://netmanagement.online/api/gpt", { prompt }, { headers: getAuthHeaders() });
      setGptResponse(response.data.reply || response.data.response || "Response received.");
      setErrorNote("GPT-4 response received.");
      logEvent("GPT", "Response received.", "success");
    } catch (e) {
      setErrorNote("GPT-4 error.");
      logEvent("GPT", e.message, "error");
    } finally {
      setButtonLoading((prev) => ({ ...prev, gpt: false }));
    }
  };

  const testAuthAPI = async () => {
    setButtonLoading((prev) => ({ ...prev, auth: true }));
    setAuthStatus("");
    try {
      const response = await axios.get('https://netmanagement.online/api/test-auth', { headers: getAuthHeaders() });
      setAuthStatus('✅ Valid authentication: ' + JSON.stringify(response.data));
      setAuthTested(true);
      logEvent('AuthTest', 'Success.', 'success');
    } catch (e) {
      setAuthStatus('❌ Authentication failed: ' + (e.response?.data?.message || e.message));
      logEvent('AuthTest', e.message, 'error');
    } finally {
      setButtonLoading((prev) => ({ ...prev, auth: false }));
    }
  };

  const handleUserQuestion = () => {
    if (userQuestion.trim()) {
      const prompt = `You are Ipranet, an assistant connected to Xero, Saferpay, and GPT-4.\nYou are responding to: ${userQuestion}`;
      fetchGptResponse(prompt);
      setUserQuestion("");
    } else {
      setErrorNote("Please enter a question.");
    }
  };

  return (
    <Router>
      <div className="min-h-screen px-4 py-10 text-white bg-green-200">
        <nav className="flex justify-center mb-8 space-x-6">
          <Link to="/" className="text-xl font-semibold text-white hover:underline">Dashboard</Link>
        </nav>
        <Routes>
          <Route path="/" element={
            <Home
              fetchXeroData={fetchXeroData}
              testAuthAPI={testAuthAPI}
              authStatus={authStatus}
              authTested={authTested}
              xeroData={xeroData}
              selectedInvoice={selectedInvoice}
              setSelectedInvoice={setSelectedInvoice}
              paymentValue={paymentValue}
              setPaymentValue={setPaymentValue}
              currency={currency}
              setCurrency={setCurrency}
              recipientIban={recipientIban}
              setRecipientIban={setRecipientIban}
              processPayment={processPayment}
              paymentStatus={paymentStatus}
              gptResponse={gptResponse}
              userQuestion={userQuestion}
              setUserQuestion={setUserQuestion}
              handleUserQuestion={handleUserQuestion}
              buttonLoading={buttonLoading}
              errorNote={errorNote}
            />
          } />
        </Routes>
      </div>
    </Router>
  );
};
gptResponse={gptResponse}
userQuestion={userQuestion}
setUserQuestion={setUserQuestion}
handleUserQuestion={handleUserQuestion}
buttonLoading={buttonLoading}
errorNote={errorNote}
/>
} />
</Routes>
</div>
</Router>
);
};

export default App;
