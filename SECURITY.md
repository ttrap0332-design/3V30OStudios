# Security Policy

## Reporting Security Vulnerabilities

If you discover a security vulnerability in this project, please report it responsibly:

1. **DO NOT** open a public issue
2. Email the maintainers directly at: [security contact to be added]
3. Include detailed information about the vulnerability
4. Allow reasonable time for a fix before public disclosure

## Security Incident Log

### November 2025 - Suspicious Commit Activity
**Status**: Under Investigation  
**Severity**: High  
**Description**: Suspicious commits detected with potential code theft attempts and OAuth vulnerabilities.

**Affected Components**:
- Go server code (removed/never merged)
- OAuth/Keycloak redirect configurations
- Branch protection policies

**Remediation Actions Taken**:
- Enhanced branch protection requirements
- Implemented pre-commit secret scanning
- Added dependency vulnerability scanning
- Enforced commit signing requirements
- Updated security documentation

## Security Requirements

### Code Contributions

#### Commit Signing
- **REQUIRED**: All commits MUST be signed with GPG or SSH keys
- Unsigned commits will be rejected by CI/CD pipeline
- See [GitHub's commit signing guide](https://docs.github.com/en/authentication/managing-commit-signature-verification)

#### Branch Protection
- Default branch requires:
  - At least 1 PR approval from maintainer
  - All CI checks must pass
  - Signed commits only
  - No force pushes
  - No deletions

#### Pre-commit Checks
- Secret scanning (prevents accidental token commits)
- Dependency vulnerability checks
- Code quality linting

### Secrets Management

#### ❌ NEVER commit:
- API keys or tokens
- Passwords or credentials
- Private keys (SSH, GPG, SSL/TLS)
- OAuth client secrets
- Database connection strings
- .env files with real credentials

#### ✅ ALWAYS use:
- Environment variables
- Secrets management tools (HashiCorp Vault, Azure Key Vault, AWS Secrets Manager)
- .env.example files with placeholder values only
- GitHub Secrets for CI/CD

### OAuth and Authentication Security

#### OAuth/Keycloak Configuration
- **REQUIRED**: Whitelist exact redirect URIs (no wildcards)
- **REQUIRED**: Enable PKCE (Proof Key for Code Exchange)
- **REQUIRED**: Use strong state/nonce values
- **REQUIRED**: Log all authentication events with request_id, client_id, and redirect_uri
- **PROHIBITED**: Using `localhost` or wildcard redirect URIs in production

#### Session Management
- Implement proper session timeout policies
- Rotate tokens/sessions regularly
- Invalidate sessions on logout
- Monitor for session hijacking attempts

### Dependency Security

#### Package Management
- Keep dependencies up to date
- Review security advisories regularly
- Use `npm audit`, `go mod tidy`, `pip-audit` etc.
- Pin dependency versions in production

#### Supply Chain Security
- Verify package checksums
- Use lock files (package-lock.json, go.sum, requirements.txt)
- Review dependency changes in PRs
- Generate and publish SBOMs (Software Bill of Materials)

### Build and Deployment Security

#### Artifacts
- Sign all release artifacts
- Generate SBOM for each release
- Use reproducible builds where possible
- Verify artifact signatures before deployment

#### CI/CD Security
- Use minimal permission tokens
- Audit CI/CD logs regularly
- Scan container images for vulnerabilities
- Never log secrets or sensitive data

### Content Security Policy (CSP)

When serving web content:
- Implement strict CSP headers
- Use Subresource Integrity (SRI) for CDN resources
- Set proper CORS policies
- Use HTTPS only (HSTS enabled)

### Monitoring and Incident Response

#### Detection
- Monitor for unusual commit patterns
- Track authentication anomalies
- Review access logs regularly
- Set up alerts for security events

#### Response Procedure
1. **Contain**: Immediately revoke compromised credentials
2. **Investigate**: Collect evidence and analyze scope
3. **Remediate**: Fix vulnerabilities and patch systems
4. **Document**: Record incident details and lessons learned
5. **Communicate**: Notify affected parties as appropriate

### Security Contacts

- **Security Team**: [To be configured]
- **Incident Response**: [To be configured]

### References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)
- [CWE Top 25](https://cwe.mitre.org/top25/)

---

**Last Updated**: November 2025  
**Version**: 1.0
