## Description
<!-- Provide a brief description of your changes -->

## Type of Change
<!-- Check all that apply -->
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Security fix
- [ ] Dependency update
- [ ] Configuration change

## Security Checklist
<!-- All items must be checked before merging -->
- [ ] I have signed my commits with GPG or SSH key
- [ ] I have not committed any secrets, keys, or credentials
- [ ] I have reviewed the code for security vulnerabilities
- [ ] I have updated security documentation if applicable
- [ ] I have run pre-commit hooks and all checks passed
- [ ] I have tested OAuth/authentication changes thoroughly (if applicable)
- [ ] I have validated all user inputs (if applicable)
- [ ] I have not introduced any hardcoded secrets or API keys

## Testing
<!-- Describe the tests you ran and how to reproduce -->
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] I have tested on multiple environments (if applicable)

## Code Quality
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings or errors

## Dependencies
<!-- List any new dependencies and why they are needed -->
- [ ] I have checked new dependencies for known vulnerabilities
- [ ] I have updated package.json/requirements.txt/go.mod (if applicable)
- [ ] I have verified dependency licenses are compatible

## Breaking Changes
<!-- List any breaking changes and migration steps -->
<!-- If none, write "None" -->

## Screenshots (if applicable)
<!-- Add screenshots to help explain your changes -->

## Additional Notes
<!-- Add any other context about the PR here -->

## Related Issues
<!-- Link related issues: Closes #123, Fixes #456, Related to #789 -->

---

## For Reviewers

### Security Review
- [ ] No secrets or credentials exposed
- [ ] OAuth/auth flows properly secured (if applicable)
- [ ] Input validation and sanitization adequate
- [ ] No new security vulnerabilities introduced
- [ ] Security documentation updated if needed

### Code Review
- [ ] Code is readable and maintainable
- [ ] Tests are comprehensive
- [ ] Documentation is clear and accurate
- [ ] No unnecessary complexity

### Deployment Review
- [ ] Changes are backward compatible or migration path is clear
- [ ] Configuration changes are documented
- [ ] Deployment impact is minimal
