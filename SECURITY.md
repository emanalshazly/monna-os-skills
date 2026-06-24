# Security Policy

## Our Stance

**Skills are code that executes with agent privileges.** A malicious skill can read files, execute commands, access credentials, and exfiltrate data. We take security as seriously as any software project — because it is one.

## Reporting Security Issues

If you discover a security vulnerability in any skill or tool in this repository:

1. **DO NOT open a public issue.**
2. Email **monna** at [security contact — update when available] with:
   - Description of the vulnerability
   - Affected skill(s) and version(s)
   - Steps to reproduce
   - Your assessment of severity
3. We will respond within 48 hours.
4. After remediation, we will publish a security advisory and credit you (if desired).

## Security Measures

### Validation Pipeline
Every skill passes these automated checks before reaching VALIDATED tier:
- **Structure validation** — frontmatter, required fields, format compliance
- **Overlap detection** — prevents duplicate/redundant skills
- **Security scan** — detects known malicious patterns, suspicious script references, prompt injection vectors
- **Dependency audit** — checks referenced external packages for known vulnerabilities

### Content Review
- No skills that encourage illegal, harmful, or unethical behavior
- No skills with hidden instructions or obfuscated payloads
- No skills that request unnecessary system privileges
- All external references (scripts, APIs, packages) must be documented and auditable

### Runtime Security
- Skills are Markdown instructions, not executable code — but they may reference scripts
- We recommend running skills in sandboxed environments
- We publish a capability manifest for each skill declaring what it needs access to

## Known Threats We Defend Against

| Threat | Mitigation |
|--------|------------|
| Prompt injection via SKILL.md | Security scan + manual review |
| Supply chain attacks (typosquatting) | Dependency audit + trusted sources only |
| Skill conflicts (conflicting instructions) | Overlap detection + compatibility matrix |
| Stale skills (outdated, broken) | Lifecycle management + deprecation |
| Ranking manipulation | Quality tiers based on audit, not downloads |

## Security Advisories

When a security issue is confirmed:
1. Skill is immediately deprecated (DANGER tier)
2. Security advisory published in `security/advisories/`
3. Community notified via GitHub security alerts
4. Fix or replacement skill developed
5. After fix, skill can be re-audited for promotion

## Skill Security Checklist (For Contributors)

Before submitting a skill, verify:
- [ ] No hidden instructions or obfuscated text
- [ ] All external references are documented and from trusted sources
- [ ] Skill only requests access it actually needs
- [ ] No hardcoded credentials or secrets
- [ ] No encouragement of illegal or harmful behavior
- [ ] Examples are safe and reproducible

## Security Credits

We maintain a [SECURITY_CREDITS.md](SECURITY_CREDITS.md) file listing security researchers and contributors who have responsibly disclosed vulnerabilities. Thank you for keeping the ecosystem safe.

---

*Security Policy v1.0 — 2026-06-24*
