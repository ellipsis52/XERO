import { useState } from 'react';
import { envoyerPrompt } from '../api/gpt4Api';

export default function GptBotInterface() {
  const [prompt, setPrompt] = useState('');
  const [reply, setReply] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await envoyerPrompt(prompt);
    setReply(response);
  };

  return (
    <div className="max-w-xl p-6 mx-auto mt-12 bg-white shadow-md rounded-xl">
      <h2 className="mb-4 text-xl font-bold text-center">🤖 GPT-4 : Robot en chef</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          className="w-full p-2 mb-2 border border-gray-300 rounded"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Pose ta question ou donne une mission au robot..."
          rows={5}
        />
        <button className="w-full px-4 py-2 text-white bg-indigo-600 rounded hover:bg-indigo-700">
          Interroger GPT-4
        </button>
      </form>
      {reply && (
        <div className="p-4 mt-4 border rounded bg-gray-50">
          <h3 className="font-semibold">Réponse :</h3>
          <p className="text-sm whitespace-pre-line">{reply}</p>
        </div>
      )}
    </div>
  );
}
