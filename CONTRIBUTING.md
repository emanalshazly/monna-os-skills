# Contributing to monna-os-skills

Thank you for considering contributing! This project is the quality infrastructure layer for the agent skill ecosystem — and we need your help.

## What We're Looking For

### Skills in These Domains (Priority)
- **AI Governance & Compliance** (NIST RMF, EU AI Act, ISO 42001, DAMA-DMBOK)
- **Security & Risk Assessment** (threat modeling, red-teaming, compliance auditing)
- **Data Governance** (data quality, lineage, stewardship)
- **Infrastructure & DePIN** (decentralized physical networks, node operations)
- **Multilingual & Cross-Cultural** (technical translation, localization governance)
- **Open-Source Tooling** (skill validation, overlap detection, quality scoring)

### What We DON'T Want
- Skills that overlap with the commercial [monna-skill-portfolio](https://promptbase.com/profile/monna) (sold on PromptBase/Gumroad)
- Generic "best practices" skills that duplicate existing open-source skills
- Skills without evidence-based validation or worked examples
- Skills that promote harmful, illegal, or unethical behavior

## Contribution Workflow

### 1. Check Before You Build

Before creating a new skill:

1. **Search existing skills** — check if a similar skill already exists
2. **Run overlap check** — use the [overlap checker](tools/overlap-checker/) to verify your skill's fingerprint is unique (<60% overlap with existing skills)
3. **Check domain alignment** — does your skill fit our domain priorities?

### 2. Create Your Skill

Use the [SKILL.md template](templates/SKILL.md.template) and follow the [Skill Authoring Guide](docs/skill-authoring-guide.md).

```
skills/<domain>/<skill-name>/
├── SKILL.md              # Required: skill definition
├── references/           # Optional: supporting docs
├── examples/             # Optional: worked examples
└── tests/                # Optional: validation checklist
```

### 3. Validate Locally

```bash
# Install validation tools
pip install -r tools/validator/requirements.txt

# Run structure check
python tools/validator/validate.py skills/<domain>/<skill-name>/

# Run overlap check
python tools/overlap-checker/check.py skills/<domain>/<skill-name>/SKILL.md
```

### 4. Submit a Pull Request

- Follow the [PR template](.github/PULL_REQUEST_TEMPLATE.md)
- One skill per PR (unless it's a related skillset)
- All automated checks must pass
- Be responsive to reviewer feedback

## Review Process

```
PR Submitted
    ↓
[CI: structure check] → FAIL → Request changes
    ↓ PASS
[CI: overlap check] → FAIL → Reject or merge into existing skill
    ↓ PASS
[CI: security scan] → FAIL → Security review required
    ↓ PASS
→ Quality Tier: VALIDATED (automated)
    ↓
[Community audit] → FAIL → Request changes
    ↓ PASS
→ Quality Tier: REVIEWED
    ↓
[Maintainer review] → FAIL → Request changes
    ↓ PASS
→ Quality Tier: CERTIFIED (or stays at REVIEWED)
```

## Becoming a Reviewer

After contributing 3+ skills that reach REVIEWED tier, you can apply to become a Reviewer:

1. Complete the [Reviewer Training](docs/reviewer-training.md) (read the guide, complete the quiz)
2. Submit a reviewer application issue
3. Maintainer approval

Reviewers can:
- Promote skills to REVIEWED tier
- Request changes on PRs
- Participate in governance discussions

## Code of Conduct

- **Evidence over opinion** — back claims with sources
- **Scope honesty** — if you don't know, say so; if you made a mistake, fix it
- **Constructive critique** — review skills to improve them, not to block them
- **Respect boundaries** — this is an open-source community project, not a commercial marketplace

## Questions?

- Open a [Discussion](https://github.com/emanalshazly/monna-os-skills/discussions) for general questions
- Open an [Issue](https://github.com/emanalshazly/monna-os-skills/issues) for bugs or feature requests
- Check the [Skill Authoring Guide](docs/skill-authoring-guide.md) for format questions

## Recognition

All contributors are listed in [CONTRIBUTORS.md](CONTRIBUTORS.md). Thank you for helping build the governance layer!

---

*Last updated: 2026-06-24*
