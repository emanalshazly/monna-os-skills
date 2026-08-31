# Governance Model

> **"Governance is not bureaucracy. It's the discipline that makes trust possible."**

## Roles

### Maintainer
- **Current:** monna (@emanalshazly)
- **Authority:** Final decisions on architecture, security advisories, and whether deterministic validation evidence is sufficient
- **Responsibility:** Sets direction, resolves conflicts, ensures security

### Reviewer
- **Requirements:** Relevant domain expertise disclosed in the review record
- **Authority:** Can request changes and publish a dated review receipt
- **Responsibility:** Reviews accuracy and scope honesty without granting certification

### Contributor
- **Requirements:** Anyone who submits a skill or tooling improvement
- **Authority:** Can submit PRs, open issues, participate in discussions
- **Responsibility:** Follows contribution guidelines, responds to feedback

### User
- **Requirements:** Anyone who installs and uses skills
- **Authority:** Can file issues, report security concerns, provide feedback
- **Responsibility:** Reports bugs honestly, respects skill licenses

## Decision Making

| Decision Type | Process | Authority |
|---------------|---------|-----------|
| New skill submission | PR + validation pipeline | Automated → Reviewer → Maintainer |
| Evidence tier change from draft to validated | Passing deterministic CI on the exact commit | Maintainer |
| Independent review claim | Dated public receipt with reviewer identity and scope | Reviewer |
| Security advisory | Immediate override | Maintainer |
| Architecture changes | RFC + 7-day comment period | Maintainer |
| Governance changes | RFC + 14-day comment period + community vote | Maintainer |
| Skill deprecation | Security or obsolescence assessment | Maintainer |

## Conflict Resolution

### Skill Overlap Disputes
1. Run the overlap checker on both skills
2. If overlap >60%, the newer skill must differentiate or merge into the existing one
3. If unresolved, Maintainer decides with community input

### Quality Disagreements
1. Reviewer A requests changes; Contributor disagrees
2. Reviewer B (independent) provides second opinion
3. If still unresolved, Maintainer arbitrates

### Security Concerns
- **Maintainer can downgrade evidence state immediately** for security issues
- No voting on security — safety first, discussion after
- Security advisory issued publicly; skill deprecated if warranted

## Scope Honesty

This project practices **scope honesty** — we acknowledge what we are and what we are not:

- **We ARE** a quality-governed skill collection for underserved domains
- **We ARE NOT** a commercial marketplace (that's [monna-skill-portfolio](https://promptbase.com/profile/monna))
- **We ARE** open-source
- **We ARE NOT** cross-runtime verified without per-runtime receipts
- **We ARE** deterministically checked for structure and overlap
- **We ARE NOT** independently certified or community-audited by default

Violations of scope honesty (e.g., trying to commercialize skills in this repo, misrepresenting quality tiers) are grounds for PR rejection or contributor suspension.

## Transparency

- All decisions are documented in GitHub issues/PRs
- Security advisories are public unless actively exploited
- Financial: This project accepts no donations, no sponsorships, no ads. It is maintained as a public good.

## Annual Review

Every year, the Maintainer conducts a governance review:
- Assess whether the governance model is working
- Review Reviewer roster
- Update domain priorities based on community needs
- Publish a public governance report

---

*Governance v1.0 — 2026-06-24*  
*Next review: 2027-06-24*
