---
name: Skill Submission
about: Submit a new skill to the monna-os-skills collection
title: '[Skill] <skill-name>'
labels: skill-submission
type: Feature
---

## Skill Summary

**Name:** 
**Domain:** (governance / security / data-governance / infrastructure / multilingual / tooling)
**Description:** (one sentence)
**Trigger conditions:** (3–7 phrases)

## Quality Checklist

- [ ] I have read the [Skill Authoring Guide](docs/skill-authoring-guide.md)
- [ ] I have used the [SKILL.md template](templates/SKILL.md.template)
- [ ] I have checked for existing skills in the same domain
- [ ] I have run the overlap checker (if available)
- [ ] This skill is distinct from the commercial monna-skill-portfolio
- [ ] I have included at least one worked example (if targeting Reviewed+)
- [ ] I have included a "When NOT to Use" section
- [ ] I have cited sources for significant claims

## Skill Structure

```
skills/<domain>/<skill-name>/
├── SKILL.md
├── references/          # (if included)
├── examples/            # (if included)
└── tests/               # (if included)
```

## Target Quality Tier

- [ ] Draft
- [ ] Validated
- [ ] Reviewed
- [ ] Certified

## Additional Notes

[Any context, dependencies, or special considerations]
