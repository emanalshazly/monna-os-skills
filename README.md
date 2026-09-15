# monna-os-skills

An open collection of seven agent Skills with deterministic structure and overlap checks.

[![Validation](https://github.com/emanalshazly/monna-os-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/emanalshazly/monna-os-skills/actions/workflows/validate-skills.yml)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Evidence boundary

`validated` in this repository means that the committed Skill passes deterministic checks for required frontmatter, unique names and fingerprints, local links, obvious secret patterns, and the configured overlap threshold. It does **not** mean community audit, independent review, production use, cross-runtime compatibility, legal compliance, or market adoption.

No Skill in this repository is currently described as reviewed, certified, or universal. Runtime compatibility remains unverified until a dated execution receipt exists for that runtime.

<!-- SKILL_COUNT: 7 -->

## Current catalog

| Domain | Skill | Evidence state |
| --- | --- | --- |
| Data governance | [data-quality-auditor](skills/data-governance/data-quality-auditor/SKILL.md) | validated structure only |
| Governance | [ai-governance-framework](skills/governance/ai-governance-framework/SKILL.md) | validated structure only |
| Multilingual | [arabic-technical-translator](skills/multilingual/arabic-technical-translator/SKILL.md) | validated structure only |
| Security | [threat-modeling-guide](skills/security/threat-modeling-guide/SKILL.md) | validated structure only |
| Tooling | [skill-overlap-detector](skills/tooling/skill-overlap-detector/SKILL.md) | validated structure only |
| Governance | [audit-finding-closure-reviewer](skills/governance/audit-finding-closure-reviewer/SKILL.md) | draft; model evaluation not run |
| Multilingual | [arabic-release-change-reviewer](skills/multilingual/arabic-release-change-reviewer/SKILL.md) | draft; model evaluation not run |

## Follow an existing audit or translation with a focused review

- **After an audit:** give the closure reviewer the existing findings and remediation evidence. It returns a closure matrix, surviving failures and the smallest missing observation. It does not certify compliance or close records.
- **After a product text update:** give the Arabic release reviewer old/current English and Arabic strings. It returns stale-meaning findings, a proposed correction patch and regression checks. Rendering and runtime behavior need separate evidence.

Both companion Skills are complete single-file workflows with embedded demonstrations. They do not require another Skill, a paid service or a connector. [Acceptance cases](docs/companion-skill-evaluations.md) are defined; actual model runs remain unperformed. [Scope and alternatives](docs/companion-skill-scope.md) explain the intended distinctions without claiming market novelty.

## Install

Copy the selected Skill directory into the Skills location supported by your agent runtime. The repository does not claim a universal installation command because runtime conventions differ.

## Validate

```bash
python tools/validator/validate.py --skills-dir skills --check-catalog
python -m pip install -r tools/overlap-checker/requirements.txt
python tools/overlap-checker/overlap_checker.py --skills-dir skills --output overlap-report.md
```

The first command is dependency-free. The overlap check uses scikit-learn and exits with code `2` when the configured collision threshold is exceeded.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), and the [Skill authoring guide](docs/skill-authoring-guide.md). New submissions start as `draft`; they can be marked `validated` only after the repository checks pass.

## Security and license

Report security issues through [SECURITY.md](SECURITY.md). Repository materials are licensed under [MIT](LICENSE).
