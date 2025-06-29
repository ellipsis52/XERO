// auth.js
require('dotenv').config();
const { ExpressOIDC } = require('@okta/oidc-middleware');

/**
 * Construit le middleware OIDC basé sur les variables d'environnement
 * et le retourne pour l'utiliser dans l'app Express.
 */
function createOIDC() {
  return new ExpressOIDC({
    issuer: process.env.OKTA_ISSUER,                 // ex. https://dev-123456.okta.com/oauth2/default
    client_id: process.env.OKTA_CLIENT_ID,
    client_secret: process.env.OKTA_CLIENT_SECRET,
    redirect_uri: process.env.OKTA_REDIRECT_URI      // ex. http://localhost:3000/authorization-code/callback
                  || 'http://localhost:3000/authorization-code/callback',
    scope: 'openid profile email',
  });
}

module.exports = createOIDC;
