# Skill Overlap Detector

A Python CLI tool for detecting semantic duplication within agent skill collections.

Part of the [MONNA Open-Source Skill Collection](https://github.com/emanalshazly/monna-os-skills).

## What It Does

This tool analyzes all `SKILL.md` files in a collection and computes:
- **Content overlap** via TF-IDF + cosine similarity (semantic comparison)
- **Trigger-phrase collision** via Jaccard similarity (activation overlap)
- **Fingerprint generation** for change detection and rotation tracking

## Installation

```bash
cd tools/overlap-checker
pip install -r requirements.txt
```

## Usage

### Full Corpus Scan

Check all skills in a collection for pairwise overlap:

```bash
python overlap_checker.py \
  --skills-dir ../../skills/ \
  --threshold 0.60 \
  --output report.md
```

### PR Mode (Single New Skill)

Check a new skill before merging it into the collection:

```bash
python overlap_checker.py \
  --skills-dir ../../skills/ \
  --new-skill ../../skills/marketing/new-skill/SKILL.md \
  --threshold 0.60 \
  --output pr-report.md
```

The tool returns exit code `2` if overlap is detected, making it suitable for CI integration.

## How It Works

1. **Parse** each `SKILL.md` — strip frontmatter, extract sections, identify triggers
2. **Weight** sections by importance (triggers 3×, principles 2.5×, body 1×)
3. **Vectorize** using TF-IDF with common-term downweighting
4. **Compare** using cosine similarity for content, Jaccard for triggers
5. **Report** as markdown with three tiers: high overlap, trigger collisions, watchlist

## Thresholds

| Threshold | Default | Action |
|-----------|---------|--------|
| Content overlap | 0.60 | Hard block — merge must be resolved |
| Trigger overlap | 0.40 | Warning — review trigger distinctiveness |
| Medium overlap | 0.45 | Watchlist — monitor for drift |

Calibrated on the MONNA commercial skill portfolio (50+ skills). See `skills/tooling/skill-overlap-detector/references/threshold-rationale.md` for the full derivation.

## CI Integration

```yaml
name: Skill Overlap Check
on:
  pull_request:
    paths:
      - 'skills/**/SKILL.md'
jobs:
  overlap-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r tools/overlap-checker/requirements.txt
      - run: |
          python tools/overlap-checker/overlap_checker.py \
            --skills-dir skills/ \
            --find-new-skills \
            --threshold 0.60
```

## License

MIT — see the repository root `LICENSE` file.
