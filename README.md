# monna-os-skills

An open collection of five agent Skills with deterministic structure and overlap checks.

[![Validation](https://github.com/emanalshazly/monna-os-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/emanalshazly/monna-os-skills/actions/workflows/validate-skills.yml)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Evidence boundary

`validated` in this repository means that the committed Skill passes deterministic checks for required frontmatter, unique names and fingerprints, local links, obvious secret patterns, and the configured overlap threshold. It does **not** mean community audit, independent review, production use, cross-runtime compatibility, legal compliance, or market adoption.

No Skill in this repository is currently described as reviewed, certified, or universal. Runtime compatibility remains unverified until a dated execution receipt exists for that runtime.

<!-- SKILL_COUNT: 5 -->

## Current catalog

| Domain | Skill | Evidence state |
| --- | --- | --- |
| Data governance | [data-quality-auditor](skills/data-governance/data-quality-auditor/SKILL.md) | validated structure only |
| Governance | [ai-governance-framework](skills/governance/ai-governance-framework/SKILL.md) | validated structure only |
| Multilingual | [arabic-technical-translator](skills/multilingual/arabic-technical-translator/SKILL.md) | validated structure only |
| Security | [threat-modeling-guide](skills/security/threat-modeling-guide/SKILL.md) | validated structure only |
| Tooling | [skill-overlap-detector](skills/tooling/skill-overlap-detector/SKILL.md) | validated structure only |

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
