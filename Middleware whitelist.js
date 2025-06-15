// stripe/whitelist.js

const allowedOrigins = [
    'https://www.webtechnicom.net',
    'https://www.netmanagement.online'
  ];
  
  export function whitelistMiddleware(req, res, next) {
    const origin = req.headers.origin || req.headers.referer || '';
    
    if (allowedOrigins.some(allowed => origin.startsWith(allowed))) {
      next();
    } else {
      res.status(403).json({ error: 'Accès interdit : origine non autorisée.' });
    }
  }
  