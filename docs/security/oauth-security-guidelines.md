# OAuth and Authentication Security Guidelines

## Overview

This document outlines security requirements for implementing OAuth 2.0, OpenID Connect, and other authentication mechanisms in the 3V30OStudios ecosystem.

## OAuth 2.0 Security Requirements

### Redirect URI Security

#### ✅ REQUIRED

1. **Exact Match Whitelisting**
   ```json
   {
     "redirect_uris": [
       "https://app.3v30ostudios.com/auth/callback",
       "https://app.3v30ostudios.com/auth/silent-callback"
     ]
   }
   ```
   - ❌ NEVER use wildcards: `https://*.3v30ostudios.com/*`
   - ❌ NEVER allow `localhost` in production
   - ❌ NEVER allow `http://` (non-HTTPS) in production

2. **Redirect URI Validation**
   ```javascript
   function validateRedirectUri(requestedUri, allowedUris) {
     // Exact string match only - no pattern matching
     if (!allowedUris.includes(requestedUri)) {
       throw new Error('Invalid redirect_uri');
     }
     
     // Additional checks
     const url = new URL(requestedUri);
     
     // Must be HTTPS in production
     if (process.env.NODE_ENV === 'production' && url.protocol !== 'https:') {
       throw new Error('HTTPS required in production');
     }
     
     // No fragments allowed
     if (url.hash) {
       throw new Error('Fragments not allowed in redirect_uri');
     }
     
     return true;
   }
   ```

3. **State Parameter**
   - REQUIRED for all authorization requests
   - Must be cryptographically random (minimum 128 bits)
   - Must be bound to user session
   - Must be single-use
   ```javascript
   const crypto = require('crypto');
   
   function generateState() {
     return crypto.randomBytes(32).toString('hex');
   }
   
   function validateState(receivedState, sessionState) {
     if (!receivedState || !sessionState) {
       throw new Error('Missing state parameter');
     }
     
     if (receivedState !== sessionState) {
       throw new Error('State parameter mismatch - possible CSRF attack');
     }
     
     // Mark state as used
     session.state = null;
     return true;
   }
   ```

### PKCE (Proof Key for Code Exchange)

#### ✅ REQUIRED for all OAuth flows

```javascript
const crypto = require('crypto');

// Generate code verifier
function generateCodeVerifier() {
  return base64URLEncode(crypto.randomBytes(32));
}

// Generate code challenge
function generateCodeChallenge(verifier) {
  const hash = crypto.createHash('sha256')
    .update(verifier)
    .digest();
  return base64URLEncode(hash);
}

// Authorization request
const codeVerifier = generateCodeVerifier();
const codeChallenge = generateCodeChallenge(codeVerifier);

// Store verifier in session
session.codeVerifier = codeVerifier;

// Include in authorization URL
const authUrl = `${authEndpoint}?` +
  `client_id=${clientId}&` +
  `redirect_uri=${redirectUri}&` +
  `response_type=code&` +
  `code_challenge=${codeChallenge}&` +
  `code_challenge_method=S256&` +
  `state=${state}`;

// Token exchange
const tokenResponse = await fetch(tokenEndpoint, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  body: new URLSearchParams({
    grant_type: 'authorization_code',
    code: authorizationCode,
    redirect_uri: redirectUri,
    client_id: clientId,
    code_verifier: session.codeVerifier
  })
});
```

### Token Security

#### Access Tokens

1. **Storage**
   - ❌ NEVER store in localStorage (XSS vulnerable)
   - ✅ Use httpOnly, secure cookies OR
   - ✅ Use in-memory storage only

2. **Transmission**
   - ✅ Always use HTTPS
   - ✅ Use Authorization header: `Authorization: Bearer <token>`
   - ❌ NEVER send in URL parameters

3. **Validation**
   ```javascript
   async function validateAccessToken(token) {
     // Verify signature
     const decoded = jwt.verify(token, publicKey, {
       algorithms: ['RS256'],
       issuer: 'https://auth.3v30ostudios.com',
       audience: 'https://api.3v30ostudios.com'
     });
     
     // Check expiration
     if (decoded.exp < Date.now() / 1000) {
       throw new Error('Token expired');
     }
     
     // Check scopes
     if (!decoded.scope.includes(requiredScope)) {
       throw new Error('Insufficient permissions');
     }
     
     return decoded;
   }
   ```

#### Refresh Tokens

1. **Storage**
   - ✅ Store encrypted in secure database
   - ✅ Use httpOnly, secure, SameSite=Strict cookies
   - ❌ NEVER store in client-side storage

2. **Rotation**
   - ✅ Implement refresh token rotation
   - ✅ Invalidate old token immediately after use
   - ✅ Revoke family on suspicious activity

3. **Lifetime**
   - Maximum lifetime: 90 days (recommended: 30 days)
   - Must require re-authentication after expiry

### Session Management

#### Session Creation

```javascript
function createSession(userId, tokens) {
  const sessionId = crypto.randomBytes(32).toString('hex');
  
  return {
    id: sessionId,
    userId: userId,
    accessToken: tokens.access_token,
    refreshToken: encrypt(tokens.refresh_token),
    createdAt: new Date(),
    expiresAt: new Date(Date.now() + 3600 * 1000), // 1 hour
    lastActivity: new Date(),
    ipAddress: req.ip,
    userAgent: req.headers['user-agent']
  };
}
```

#### Session Validation

```javascript
function validateSession(sessionId) {
  const session = getSession(sessionId);
  
  if (!session) {
    throw new Error('Session not found');
  }
  
  // Check expiration
  if (session.expiresAt < new Date()) {
    deleteSession(sessionId);
    throw new Error('Session expired');
  }
  
  // Check for suspicious activity
  if (session.ipAddress !== req.ip) {
    logSecurityEvent('ip_change', { sessionId, oldIp: session.ipAddress, newIp: req.ip });
    // Optionally: require re-authentication
  }
  
  // Update last activity
  session.lastActivity = new Date();
  saveSession(session);
  
  return session;
}
```

#### Session Termination

```javascript
function logout(sessionId) {
  const session = getSession(sessionId);
  
  if (session) {
    // Revoke tokens
    revokeAccessToken(session.accessToken);
    revokeRefreshToken(decrypt(session.refreshToken));
    
    // Delete session
    deleteSession(sessionId);
    
    // Clear cookies
    res.clearCookie('session_id');
    
    logSecurityEvent('logout', { sessionId, userId: session.userId });
  }
}
```

## Keycloak-Specific Configuration

### Client Configuration

```json
{
  "clientId": "3v30ostudios-app",
  "clientAuthenticatorType": "client-secret",
  "secret": "USE_SECRETS_MANAGER",
  "redirectUris": [
    "https://app.3v30ostudios.com/auth/callback"
  ],
  "webOrigins": [
    "https://app.3v30ostudios.com"
  ],
  "protocol": "openid-connect",
  "publicClient": false,
  "standardFlowEnabled": true,
  "implicitFlowEnabled": false,
  "directAccessGrantsEnabled": false,
  "serviceAccountsEnabled": false,
  "authorizationServicesEnabled": false,
  "fullScopeAllowed": false,
  "consentRequired": false,
  "attributes": {
    "pkce.code.challenge.method": "S256",
    "access.token.lifespan": "300",
    "client.session.idle.timeout": "1800",
    "client.session.max.lifespan": "36000"
  }
}
```

### Security Headers

```javascript
app.use((req, res, next) => {
  // Content Security Policy
  res.setHeader(
    'Content-Security-Policy',
    "default-src 'self'; " +
    "script-src 'self' 'unsafe-inline' 'unsafe-eval'; " +
    "style-src 'self' 'unsafe-inline'; " +
    "img-src 'self' data: https:; " +
    "font-src 'self' data:; " +
    "connect-src 'self' https://auth.3v30ostudios.com https://api.3v30ostudios.com; " +
    "frame-ancestors 'none';"
  );
  
  // Other security headers
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-XSS-Protection', '1; mode=block');
  res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains; preload');
  res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');
  
  next();
});
```

## Logging and Monitoring

### Required Authentication Events

Log the following events with full context:

```javascript
const authEvents = {
  LOGIN_SUCCESS: 'login_success',
  LOGIN_FAILURE: 'login_failure',
  LOGOUT: 'logout',
  TOKEN_ISSUED: 'token_issued',
  TOKEN_REFRESHED: 'token_refreshed',
  TOKEN_REVOKED: 'token_revoked',
  INVALID_REDIRECT_URI: 'invalid_redirect_uri',
  STATE_MISMATCH: 'state_mismatch',
  PKCE_FAILURE: 'pkce_failure',
  SESSION_EXPIRED: 'session_expired',
  SUSPICIOUS_ACTIVITY: 'suspicious_activity'
};

function logAuthEvent(event, context) {
  console.log(JSON.stringify({
    timestamp: new Date().toISOString(),
    event: event,
    request_id: context.requestId,
    client_id: context.clientId,
    user_id: context.userId,
    redirect_uri: context.redirectUri,
    ip_address: context.ipAddress,
    user_agent: context.userAgent,
    session_id: context.sessionId
  }));
}
```

### Alerting Thresholds

- 5+ failed login attempts in 5 minutes → Alert
- Invalid redirect_uri attempt → Immediate alert
- State mismatch → Immediate alert
- Token used after revocation → Immediate alert
- Unusual geographic location for user → Alert

## Testing Checklist

- [ ] Redirect URI validation rejects wildcards
- [ ] Redirect URI validation rejects http:// in production
- [ ] State parameter required and validated
- [ ] State parameter is single-use
- [ ] PKCE code_challenge validated correctly
- [ ] Access tokens expire appropriately
- [ ] Refresh tokens rotate correctly
- [ ] Sessions expire after timeout
- [ ] Logout revokes all tokens
- [ ] Security headers present on all responses
- [ ] All auth events logged with full context
- [ ] CSRF protection enabled
- [ ] XSS protection enabled
- [ ] Rate limiting on auth endpoints

## References

- [RFC 6749 - OAuth 2.0](https://tools.ietf.org/html/rfc6749)
- [RFC 7636 - PKCE](https://tools.ietf.org/html/rfc7636)
- [RFC 6819 - OAuth 2.0 Threat Model](https://tools.ietf.org/html/rfc6819)
- [OAuth 2.0 Security Best Current Practice](https://tools.ietf.org/html/draft-ietf-oauth-security-topics)
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

---

**Last Updated**: November 2025  
**Version**: 1.0
