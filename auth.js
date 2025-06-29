const session = require('express-session');
const { ExpressOIDC } = require('@okta/oidc-middleware');

const oidc = new ExpressOIDC({
  issuer: 'https://your-okta-domain/oauth2/default',
  client_id: 'CLIENT_ID',
  client_secret: 'CLIENT_SECRET',
  redirect_uri: 'http://localhost:3000/authorization-code/callback',
  scope: 'openid profile email'
});

module.exports = oidc;
