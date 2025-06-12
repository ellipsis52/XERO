import React, { useState } from "react";

const GPTAssistant = () => {
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const res = await fetch("/api/gpt", {
        method: "POST",
        body: JSON.stringify({ prompt: "Some prompt data" }),
        headers: { "Content-Type": "application/json" },
      });

      if (!res.ok) {
        throw new Error("Failed to fetch response");
      }

      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Enter prompt" required />
        <button type="submit" disabled={loading}>
          {loading ? "Loading..." : "Submit"}
        </button>
      </form>

      {error && <div>Error: {error}</div>}
      {response && <div>Response: {response}</div>}
    </div>
  );
};
import React, { useState } from "react";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function VanillaApp() {
  const [iban, setIban] = useState("");
  const [amount, setAmount] = useState("");
  const [xeroContactId, setXeroContactId] = useState("");
  const [xeroDescription, setXeroDescription] = useState("");
  const [selectedCurrency, setSelectedCurrency] = useState("BTC");
  const [loading, setLoading] = useState({
    xeroPaymentOut: false,
    cryptoPayment: false,
    gptQuery: false,
  });
  const [xeroPaymentOutResponse, setXeroPaymentOutResponse] = useState(null);
  const [cryptoPayments, setCryptoPayments] = useState([]);
  const [gptResponse, setGptResponse] = useState(null);
  const [question, setQuestion] = useState("");
  const [errors, setErrors] = useState({
    xeroPaymentOut: null,
    cryptoPayment: null,
    gptQuery: null,
  });

  const handleGptQuery = async () => {
    setLoading((prev) => ({ ...prev, gptQuery: true }));
    setErrors((prev) => ({ ...prev, gptQuery: null }));
    try {
      const response = await fetch("/api/gpt4", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });
      if (!response.ok) throw new Error("Échec de la requête GPT-4.");
      const data = await response.json();
      setGptResponse(data.result);
    } catch (error) {
      setErrors((prev) => ({ ...prev, gptQuery: error.message }));
    } finally {
      setLoading((prev) => ({ ...prev, gptQuery: false }));
    }
  };

  const handleXeroPaymentOut = async () => {
    setLoading((prev) => ({ ...prev, xeroPaymentOut: true }));
    setErrors((prev) => ({ ...prev, xeroPaymentOut: null }));
    try {
      const response = await fetch("/api/xero/payment-out", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          iban,
          amount,
          contactId: xeroContactId,
          description: xeroDescription,
        }),
      });
      if (!response.ok) throw new Error("Échec du paiement Xero.");
      const data = await response.json();
      setXeroPaymentOutResponse(data);
    } catch (error) {
      setErrors((prev) => ({ ...prev, xeroPaymentOut: error.message }));
    } finally {
      setLoading((prev) => ({ ...prev, xeroPaymentOut: false }));
    }
  };

  const handleCryptoPayment = async () => {
    setLoading((prev) => ({ ...prev, cryptoPayment: true }));
    setErrors((prev) => ({ ...prev, cryptoPayment: null }));
    try {
      const response = await fetch("/api/okx/payment", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          iban,
          amount,
          currency: selectedCurrency,
        }),
      });
      if (!response.ok) throw new Error("Échec du paiement OKX.");
      const data = await response.json();
      setCryptoPayments((prev) => [...prev, data]);
    } catch (error) {
      setErrors((prev) => ({ ...prev, cryptoPayment: error.message }));
    } finally {
      setLoading((prev) => ({ ...prev, cryptoPayment: false }));
    }
  };

  return (
    <div className="grid grid-cols-1 gap-4 p-8 md:grid-cols-3">
      {/* Paiement Xero */}
      {/* ... Xero form unchanged ... */}

      {/* Paiement vers OKX */}
      {/* ... Crypto form unchanged ... */}

      {/* GPT-4 Interaction */}
      <Card>
        <CardContent className="p-4 space-y-4">
          <h2 className="text-xl font-bold">Interagir avec GPT-4</h2>
          <Label htmlFor="question">Posez une question à GPT-4</Label>
          <Input
            id="question"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Votre question ici"
          />
          <Button onClick={handleGptQuery} disabled={loading.gptQuery}>
            {loading.gptQuery ? "Chargement..." : "Poser la question"}
          </Button>
          {errors.gptQuery && (
            <p className="text-sm text-red-500">{errors.gptQuery}</p>
          )}
          {gptResponse && (
            <div className="p-4 mt-4 bg-gray-100 border rounded">
              <h3 className="mb-2 font-bold">Réponse de GPT-4 :</h3>
              <table className="min-w-full border border-collapse table-auto">
                <thead>
                  <tr>
                    <th className="p-2 border">Texte</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td className="p-2 whitespace-pre-wrap border">{gptResponse}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          )}
        </CardContent>
      </Card>

      {/* Historique des paiements */}
      {/* ... Tableau inchangé ... */}
    </div>
  );
}

export default GPTAssistant;
