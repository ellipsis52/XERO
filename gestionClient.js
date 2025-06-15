// stripe/gestionClient.js
import { callGpt4 } from './gpt4Bot.js';

/**
 * Requête pour gérer un client avec GPT-4.
 * @param {Object} clientData - Informations sur le client
 * @returns {Promise<string>} - Réponse poétique ou analytique
 */
export async function gererClient(clientData) {
  const prompt = `
  Tu es un assistant qui gère la relation client.
  Voici les données du client :
  ${JSON.stringify(clientData, null, 2)}

  Donne un résumé clair, une analyse et une suggestion pour améliorer la satisfaction client.
  Sois clair, poétique et précis.
  `;

  return await callGpt4(prompt);
}
