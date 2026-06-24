# Governance Model

> **"Governance is not bureaucracy. It's the discipline that makes trust possible."**

## Roles

### Maintainer
- **Current:** monna (@emanalshazly)
- **Authority:** Final decisions on architecture, security advisories, tier promotions to CERTIFIED/UNIVERSAL
- **Responsibility:** Sets direction, resolves conflicts, ensures security

### Reviewer
- **Requirements:** Contributed 3+ skills reaching REVIEWED tier; completed reviewer training
- **Authority:** Can promote skills to REVIEWED tier; can request changes on PRs
- **Responsibility:** Audits skills for quality, accuracy, and scope honesty

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
| Tier promotion to REVIEWED | Community audit + Reviewer approval | Reviewer |
| Tier promotion to CERTIFIED | Maintainer + 2 independent Reviewers | Maintainer |
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
- **Maintainer can override all tiers immediately** for security issues
- No voting on security — safety first, discussion after
- Security advisory issued publicly; skill deprecated if warranted

## Scope Honesty

This project practices **scope honesty** — we acknowledge what we are and what we are not:

- **We ARE** a quality-governed skill collection for underserved domains
- **We ARE NOT** a commercial marketplace (that's [monna-skill-portfolio](https://promptbase.com/profile/monna))
- **We ARE** cross-runtime and open-source
- **We ARE NOT** a runtime-specific tool or MCP server replacement
- **We ARE** community-audited
- **We ARE NOT** a zero-gatekeeping dump

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
