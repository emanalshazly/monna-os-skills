# monna-os-skills

> **The quality-governed, cross-runtime skill collection.**
> Agent skills as first-class software assets — with evidence-based validation, community audit, and lifecycle governance.

[![Quality Tier](https://img.shields.io/badge/quality-certified-blue)](#quality-tiers)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Standard](https://img.shields.io/badge/skill--spec-Anthropic%20Agent%20Skills-orange)](https://agentskills.io)

---

## What This Is

**monna-os-skills** is a curated, open-source collection of AI agent skills that treats skills as **auditable software assets** — not disposable prompts.

Every skill in this collection passes a rigorous validation pipeline: structure checks, overlap detection, security scanning, content review, and community audit. Skills are organized by quality tier, not by download count.

### Why This Exists

The agent skill ecosystem is exploding — but **quality is cratering**. Most registries (52K+ skills on some platforms) are open dumps with zero gatekeeping. Documented malware exists. Conflicting skills bloat agent context. No one treats skills as governed, versioned, lifecycle-managed assets.

**monna-os-skills** fixes that by building the infrastructure layer the ecosystem desperately needs:
- **Evidence-gated validation** — every claim traceable, every overlap blocked
- **Quality tiers** — Draft → Validated → Reviewed → Certified → Universal
- **Lifecycle governance** — deprecation, migration, sunset paths
- **Cross-runtime compatibility** — tested on Kimi/Daimon, Claude, Copilot, Cursor, OpenClaw, Gemini

## Quick Start

### Install a Skill

```bash
# Using Vercel skills CLI (universal)
npx skills add emanalshazly/monna-os-skills

# Using GitHub CLI (GitHub Copilot)
gh skill add emanalshazly/monna-os-skills

# Or manually copy the SKILL.md file to your agent's skills directory
```

### Browse Skills by Domain

| Domain | Skills | Quality Tier |
|--------|--------|--------------|
| [AI Governance & Compliance](skills/governance/) | 3 | 🏆 Certified |
| [Security & Risk Assessment](skills/security/) | 2 | 🔍 Reviewed |
| [Data Governance](skills/data-governance/) | 1 | ✅ Validated |
| [Infrastructure & DePIN](skills/infrastructure/) | 1 | 🏗️ Draft |
| [Multilingual & Cross-Cultural](skills/multilingual/) | 1 | ✅ Validated |
| [Open-Source Tooling](skills/tooling/) | 2 | 🏆 Certified |

## Quality Tiers

| Tier | Badge | What It Means |
|------|-------|---------------|
| 🏗️ Draft | `draft` | Submitted, under review. Not yet validated. |
| ✅ Validated | `validated` | Passes automated structure, overlap, and security checks. |
| 🔍 Reviewed | `reviewed` | Community audit completed. No structural or security issues. |
| 🏆 Certified | `certified` | Multiple independent audits. Real-world usage confirmed. |
| 🌐 Universal | `universal` | Certified AND tested on 5+ runtimes. |

## Skill Format

All skills follow the [Anthropic Agent Skills spec](https://agentskills.io) with MONNA extensions for quality governance:

```yaml
---
name: example-skill
version: 1.0.0
description: "Use when..."
categories: [governance, compliance]
quality_tier: certified
compatibility:
  kimi: certified
  claude: certified
  copilot: validated
fingerprint: "gov-001-a7f3c9"
last_tested: 2026-06-24
---
```

See [Skill Authoring Guide](docs/skill-authoring-guide.md) for full details.

## Contributing

We welcome contributions! Please read our [Contributing Guide](CONTRIBUTING.md) and [Governance Model](GOVERNANCE.md) before submitting.

**Key rule:** All skills must be **distinct from the commercial monna-skill-portfolio** (sold on PromptBase/Gumroad). This repo is permanently free and open-source.

## Security

Found a security issue in a skill? See our [Security Policy](SECURITY.md). We take security seriously — skills execute with agent privileges, so we audit them like code.

## License

[MIT](LICENSE) — permanently free, no attribution required for usage.

## Maintainer

Built and maintained by **monna** ([@emanalshazly](https://github.com/emanalshazly)) — prompt engineer, AI governance practitioner, and open-source contributor.

> "Power without governance is chaos. Let's build the governance layer together."
