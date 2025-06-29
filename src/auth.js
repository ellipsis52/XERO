const { ExpressOIDC } = require('@okta/oidc-middleware');

const oidc = new ExpressOIDC({
  issuer: 'https://your-okta-domain/oauth2/default',
  client_id: 'YOUR_CLIENT_ID',
  client_secret: 'YOUR_CLIENT_SECRET',
  redirect_uri: 'https://netmanagement.online/authorization-code/callback',
  scope: 'openid profile email',
});

module.exports = oidc;
