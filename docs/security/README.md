# Security Documentation

This directory contains security policies, guidelines, and incident reports for the 3V30OStudios repository.

## Documents

### 📋 Policies and Guidelines

- **[Branch Protection Guide](branch-protection-guide.md)** - Step-by-step instructions for configuring GitHub branch protection rules
- **[OAuth Security Guidelines](oauth-security-guidelines.md)** - Best practices for implementing OAuth 2.0, PKCE, and session management
- **[Quarantine Notice Template](quarantine-notice-template.md)** - Template for formally quarantining security threats

### 📊 Incident Reports

- **[November 2025 Incident](incident-report-nov-2025.md)** - Suspicious commit activity and code injection attempt

## Quick Links

- [Main Security Policy](../../SECURITY.md) - Repository security policy and reporting procedures
- [Pre-commit Configuration](../../.pre-commit-config.yaml) - Automated security checks before commits
- [Security Scanning Workflow](../../.github/workflows/security-scanning.yml) - CI/CD security automation

## Getting Started with Security

### For Developers

1. **Install Pre-commit Hooks**
   ```bash
   pip install pre-commit
   cd /path/to/3V30OStudios
   pre-commit install
   ```

2. **Set Up Commit Signing**
   - Follow the [Branch Protection Guide](branch-protection-guide.md#setting-up-commit-signing)
   - Choose either GPG or SSH signing

3. **Review Security Guidelines**
   - Read the [OAuth Security Guidelines](oauth-security-guidelines.md) before implementing authentication
   - Review [SECURITY.md](../../SECURITY.md) for secrets management

### For Repository Administrators

1. **Configure Branch Protection**
   - Follow the [Branch Protection Guide](branch-protection-guide.md)
   - Apply rules to `main` and `master` branches
   - Verify protection rules work as expected

2. **Enable Security Features**
   - Enable Dependabot alerts
   - Enable secret scanning
   - Enable code scanning (CodeQL)
   - Configure security advisories

3. **Review Security Workflow**
   - Ensure [security-scanning.yml](../../.github/workflows/security-scanning.yml) is active
   - Configure required status checks
   - Set up security notifications

## Security Incident Response

If you discover a security issue:

1. **DO NOT** create a public issue
2. Follow the reporting procedure in [SECURITY.md](../../SECURITY.md)
3. Use the [Quarantine Notice Template](quarantine-notice-template.md) if you're on the security team
4. Preserve evidence (commits, logs, screenshots)

## Security Requirements Summary

### ✅ Required for All Commits

- Signed with GPG or SSH key
- Pass secret detection checks
- Pass dependency vulnerability checks
- Pass CodeQL analysis (for applicable code)

### ✅ Required for All PRs

- At least 1 approval from maintainer
- All conversations resolved
- All CI checks passing
- Signed commits only

### ❌ Prohibited

- Committing secrets, keys, or credentials
- Using wildcard OAuth redirect URIs
- Force pushing to protected branches
- Bypassing security checks (without documented approval)

## Security Tools in Use

- **TruffleHog** - Secret scanning
- **CodeQL** - Static analysis security testing
- **Syft** - SBOM generation
- **Trivy** - Container vulnerability scanning
- **Bandit** - Python security linting
- **npm audit** - JavaScript dependency scanning
- **Safety** - Python dependency scanning

## Regular Security Tasks

### Daily
- Monitor security alerts
- Review failed security checks

### Weekly
- Review open security PRs
- Check dependency updates

### Monthly
- Audit branch protection settings
- Review access controls
- Test security configurations
- Update security documentation

## References

### External Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [OAuth 2.0 Security Best Current Practice](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics)

### Standards and Compliance

- RFC 6749 - OAuth 2.0 Authorization Framework
- RFC 7636 - Proof Key for Code Exchange (PKCE)
- RFC 6819 - OAuth 2.0 Threat Model and Security Considerations
- OWASP ASVS - Application Security Verification Standard

## Contact

For security questions or concerns:
- Security Team: [To be configured]
- Incident Response: [To be configured]

---

**Last Updated**: November 2025  
**Maintained By**: Security Team
