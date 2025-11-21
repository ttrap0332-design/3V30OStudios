# Branch Protection Configuration Guide

## Overview

This document provides step-by-step instructions for configuring branch protection rules to secure the 3V30OStudios repository against unauthorized changes.

## Why Branch Protection?

Branch protection prevents:
- Unauthorized direct commits to critical branches
- Force pushes that can rewrite history
- Deletion of important branches
- Merging code without review
- Deploying untested code
- Introducing secrets or vulnerabilities

## Quick Start

For repository administrators, apply these settings to `main` and `master` branches:

### GitHub Web UI

1. Navigate to: Repository → Settings → Branches
2. Click "Add branch protection rule"
3. Enter branch name pattern: `main` (or `master`)
4. Apply the configuration below

## Required Protection Rules

### 1. Require Pull Request Reviews

```yaml
Settings to enable:
✅ Require a pull request before merging
  ✅ Require approvals: 1 (minimum)
  ✅ Dismiss stale pull request approvals when new commits are pushed
  ✅ Require review from Code Owners (if CODEOWNERS file exists)
  ❌ Allow specified actors to bypass required pull requests (DISABLED)
```

**Why**: Ensures all changes are reviewed by at least one other person before merging.

### 2. Require Status Checks

```yaml
Settings to enable:
✅ Require status checks to pass before merging
  ✅ Require branches to be up to date before merging
  
Required status checks (select these):
  ✅ Secret Detection
  ✅ Dependency Vulnerability Scan  
  ✅ CodeQL Analysis
  ✅ Verify Commit Signatures
  ✅ Build / Lint / Test (if applicable)
```

**Why**: Prevents merging broken, vulnerable, or malicious code.

### 3. Require Commit Signatures

```yaml
Settings to enable:
✅ Require signed commits
  → Only commits signed with verified GPG or SSH keys can be pushed
```

**Why**: Ensures commit authenticity and prevents impersonation.

#### Setting Up Commit Signing

**For GPG:**
```bash
# Generate GPG key
gpg --full-generate-key

# List keys
gpg --list-secret-keys --keyid-format=long

# Export public key
gpg --armor --export YOUR_KEY_ID

# Configure Git
git config --global user.signingkey YOUR_KEY_ID
git config --global commit.gpgsign true

# Add to GitHub
# Go to Settings → SSH and GPG keys → New GPG key
# Paste the exported public key
```

**For SSH:**
```bash
# Generate SSH signing key (Ed25519 recommended)
ssh-keygen -t ed25519 -C "your_email@example.com" -f ~/.ssh/id_ed25519_signing

# Configure Git
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519_signing.pub
git config --global commit.gpgsign true

# Add to GitHub
# Go to Settings → SSH and GPG keys → New SSH key
# Select "Signing Key" as key type
# Paste the public key content
```

### 4. Require Linear History

```yaml
Settings to enable:
✅ Require linear history
  → Prevent merge commits from being pushed to matching branches
```

**Why**: Keeps commit history clean and easier to audit. Use "Squash and merge" or "Rebase and merge" instead.

### 5. Restrict Who Can Push

```yaml
Settings to enable:
✅ Restrict who can push to matching branches
  → Add administrators and maintainers only
  → Do NOT include bots (unless absolutely necessary and vetted)
```

**Why**: Limits blast radius of compromised accounts.

### 6. Prevent Force Pushes and Deletions

```yaml
Settings to enable:
✅ Do not allow force pushes
  → Nobody can force push (includes administrators)

✅ Do not allow deletions  
  → Branch cannot be deleted
```

**Why**: Protects against history rewriting and accidental branch deletion.

### 7. Additional Recommended Settings

```yaml
Settings to enable:
✅ Require conversation resolution before merging
  → All PR comments must be resolved

✅ Lock branch (optional for critical branches)
  → Make branch read-only

✅ Restrict who can dismiss pull request reviews
  → Only administrators can dismiss reviews
```

## GitHub CLI Configuration

Automate branch protection with GitHub CLI:

```bash
# Install GitHub CLI
# Visit: https://cli.github.com/

# Authenticate
gh auth login

# Enable branch protection
gh api repos/:owner/:repo/branches/main/protection \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  --input - <<EOF
{
  "required_status_checks": {
    "strict": true,
    "contexts": [
      "Secret Detection",
      "Dependency Vulnerability Scan",
      "CodeQL Analysis",
      "Verify Commit Signatures"
    ]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "dismissal_restrictions": {},
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": true,
    "required_approving_review_count": 1,
    "require_last_push_approval": false
  },
  "restrictions": null,
  "required_linear_history": true,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "block_creations": false,
  "required_conversation_resolution": true,
  "lock_branch": false,
  "allow_fork_syncing": true,
  "required_signatures": true
}
EOF
```

## Terraform Configuration

For infrastructure-as-code approach:

```hcl
resource "github_branch_protection" "main" {
  repository_id = github_repository.repo.node_id
  pattern       = "main"

  required_status_checks {
    strict   = true
    contexts = [
      "Secret Detection",
      "Dependency Vulnerability Scan",
      "CodeQL Analysis",
      "Verify Commit Signatures"
    ]
  }

  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    require_code_owner_reviews      = true
    required_approving_review_count = 1
  }

  enforce_admins         = true
  require_signed_commits = true
  require_linear_history = true

  allows_force_pushes = false
  allows_deletions    = false

  require_conversation_resolution = true
}
```

## Rulesets (New Feature)

GitHub's newer "Rulesets" feature provides more flexible branch protection:

```yaml
# .github/rulesets/production.yml
name: Production Branch Protection
target: branch
enforcement: active

conditions:
  ref_name:
    include:
      - "refs/heads/main"
      - "refs/heads/master"
    exclude: []

rules:
  - type: pull_request
    parameters:
      required_approving_review_count: 1
      dismiss_stale_reviews_on_push: true
      require_code_owner_review: true
      require_last_push_approval: false

  - type: required_status_checks
    parameters:
      strict_required_status_checks_policy: true
      required_status_checks:
        - context: "Secret Detection"
        - context: "Dependency Vulnerability Scan"
        - context: "CodeQL Analysis"
        - context: "Verify Commit Signatures"

  - type: required_signatures
    parameters: {}

  - type: non_fast_forward
    parameters: {}

  - type: deletion
    parameters: {}
```

## Verification

After configuring branch protection, verify it works:

### Test 1: Direct Push (Should Fail)
```bash
git checkout main
echo "test" >> test.txt
git add test.txt
git commit -m "test direct push"
git push origin main
# Expected: ❌ Push rejected by branch protection
```

### Test 2: Unsigned Commit (Should Fail)
```bash
git config --global commit.gpgsign false
git checkout -b test-branch
git commit --allow-empty -m "unsigned commit"
git push origin test-branch
# Create PR
# Expected: ❌ PR blocked due to unsigned commit
```

### Test 3: Without PR Approval (Should Fail)
```bash
git checkout -b test-branch-2
git commit -s --allow-empty -m "signed commit"
git push origin test-branch-2
# Create PR and try to merge immediately
# Expected: ❌ Merge blocked, requires approval
```

### Test 4: With Failing Check (Should Fail)
```bash
# Push code that fails security scan
# Create PR
# Expected: ❌ Merge blocked until checks pass
```

## Troubleshooting

### Issue: Can't push even after signing commits

**Solution**: Verify your GPG/SSH key is properly added to GitHub:
```bash
# Test GPG
echo "test" | gpg --clearsign

# Verify Git config
git config --global --get user.signingkey
git config --global --get commit.gpgsign

# Check GitHub key
# Visit: https://github.com/settings/keys
```

### Issue: Status checks not appearing

**Solution**: Ensure GitHub Actions workflows are triggered:
```yaml
# .github/workflows/security-scanning.yml
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```

### Issue: Too restrictive for emergency fixes

**Solution**: Create emergency bypass procedure:
1. Document in SECURITY.md
2. Require multiple administrator approvals
3. Log all bypass events
4. Review bypasses in post-incident review

## Monitoring and Alerts

Set up notifications for branch protection events:

```yaml
# .github/workflows/branch-protection-monitor.yml
name: Branch Protection Monitor

on:
  push:
    branches: [ main ]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - name: Check if push was forced
        run: |
          if [ "${{ github.event.forced }}" == "true" ]; then
            echo "⚠️  Force push detected on protected branch!"
            # Send alert
          fi

      - name: Verify commit signature
        run: |
          git verify-commit HEAD || {
            echo "❌ Unsigned commit merged to protected branch!"
            # Send alert
          }
```

## Exceptions and Special Cases

### Bot Accounts

If you must allow bot commits:
1. Use a dedicated bot account
2. Grant minimal permissions
3. Require bot commits to be signed
4. Audit bot actions regularly
5. Implement bot-specific checks

### Automated Releases

For automated release workflows:
1. Use GitHub Actions with `GITHUB_TOKEN`
2. Sign commits with bot GPG key
3. Require manual approval for major versions
4. Tag releases instead of committing to main

## Regular Audits

Monthly checklist:
- [ ] Review branch protection settings
- [ ] Verify all required checks are active
- [ ] Audit bypass events (if any)
- [ ] Review and update required checks
- [ ] Test branch protection effectiveness
- [ ] Update this document if settings change

## References

- [GitHub: Branch Protection Rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [GitHub: Signing Commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits)
- [GitHub: Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)

---

**Last Updated**: November 2025  
**Version**: 1.0
