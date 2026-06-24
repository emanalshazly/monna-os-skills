# Example 1: Running Overlap Detection on a 10-Skill Collection

## Scenario

You maintain a small open-source skill collection with 10 skills. You want to check if any of them overlap before publishing v1.0.

## Collection

| # | Skill ID | Name | Domain |
|---|----------|------|--------|
| 1 | `mar-001` | ad-creative | Marketing |
| 2 | `mar-002` | copywriting | Marketing |
| 3 | `mar-003` | seo-audit | Marketing |
| 4 | `mar-004` | campaign-plan | Marketing |
| 5 | `too-001` | skill-overlap-detector | Tooling |
| 6 | `fin-001` | pricing-strategy | Finance |
| 7 | `fin-002` | saas-metrics-coach | Finance |
| 8 | `tec-001` | report-writing | Technical |
| 9 | `tec-002` | paper-writing | Technical |
| 10 | `tec-003` | content-research-writer | Technical |

## Command

```bash
cd ~/monna-os-skills
python tools/overlap-checker/overlap_checker.py \
  --skills-dir skills/ \
  --threshold 0.60 \
  --output report.md
```

## Output

```
================================================================================
SKILL OVERLAP DETECTION REPORT
Generated: 2026-06-24T14:32:00
Corpus: 10 skills
Threshold: 0.60 (content), 0.40 (triggers)
================================================================================

--- HIGH OVERLAP (Action Required) ---

┌─────────────┬─────────────┬────────────┬─────────────┬────────────────────┐
│ Skill A     │ Skill B     │ Similarity │ Trig. Jacc. │ Recommendation     │
├─────────────┼─────────────┼────────────┼─────────────┼────────────────────┤
│ report-w... │ paper-w...  │ 0.72       │ 0.33        │ MERGE or DIFFERENTI│
│             │             │            │             │ IATE — both are    │
│             │             │            │             │ long-form writing  │
│             │             │            │             │ skills; one is     │
│             │             │            │             │ reports, one is    │
│             │             │            │             │ academic papers    │
├─────────────┼─────────────┼────────────┼─────────────┼────────────────────┤
│ copywrit... │ ad-creat... │ 0.64       │ 0.45        │ DIFFERENTIATE —    │
│             │             │            │             │ overlap is in      │
│             │             │            │             │ marketing          │
│             │             │            │             │ fundamentals;    │
│             │             │            │             │ narrow triggers    │
│             │             │            │             │ to distinct        │
│             │             │            │             │ channels (ads vs   │
│             │             │            │             │ web copy)          │
└─────────────┴─────────────┴────────────┴─────────────┴────────────────────┘

--- TRIGGER COLLISIONS (Warning) ---

┌─────────────┬─────────────┬─────────────┬──────────────────────────────────┐
│ Skill A     │ Skill B     │ Trig. Jacc. │ Shared Triggers                  │
├─────────────┼─────────────┼─────────────┼──────────────────────────────────┤
│ copywrit... │ ad-creat... │ 0.45        │ "write copy", "headline", "CTA"  │
│             │             │             │                                  │
│ campaign... │ ad-creat... │ 0.40        │ "campaign", "ad", "creative"     │
│             │             │             │                                  │
│ content-... │ report-w... │ 0.42        │ "write", "research", "content"     │
└─────────────┴─────────────┴─────────────┴──────────────────────────────────┘

--- WATCHLIST (Medium Overlap — Monitor) ---

┌─────────────┬─────────────┬────────────┬──────────────────────────────────┐
│ Skill A     │ Skill B     │ Similarity │ Notes                            │
├─────────────┼─────────────┼────────────┼──────────────────────────────────┤
│ content-... │ copywrit... │ 0.53       │ Both writing skills; content-    │
│             │             │            │ research-writer is research-     │
│             │             │            │ focused, copywriting is          │
│             │             │            │ conversion-focused. Monitor for  │
│             │             │            │ scope creep.                     │
│             │             │            │                                  │
│ saas-met... │ pricing-... │ 0.51       │ Both SaaS finance; pricing is    │
│             │             │            │ upfront monetization, metrics is │
│             │             │            │ ongoing health. Acceptable as    │
│             │             │            │ family.                          │
└─────────────┴─────────────┴────────────┴──────────────────────────────────┘

--- PASS (No Overlap) ---

seo-audit ✓
skill-overlap-detector ✓

(7/10 skills have at least one overlap or warning)
```

## Analysis

### report-writing vs paper-writing (0.72 similarity)

Both are long-form writing skills. The overlap is structural: they share sections like "Outline design," "Structured content writing," and "Review and assembly." The recommendation is to either:
- **Merge** into a single `academic-and-professional-writing` skill with mode switches
- **Differentiate** by making `report-writing` strictly business/consulting and `paper-writing` strictly academic/research

### copywriting vs ad-creative (0.64 similarity, 0.45 trigger overlap)

These are both marketing skills but serve different channels. The trigger overlap is concerning because both respond to "write copy" and "headline." The fix is to narrow triggers:
- `copywriting`: "website copy," "landing page text," "product description"
- `ad-creative`: "ad headline," "Facebook ad," "Google ad text," "creative testing"

### saas-metrics-coach vs pricing-strategy (0.51 similarity)

This is an intentional family. Both are SaaS finance skills but at different lifecycle stages. No action needed — just monitor that pricing doesn't expand into ongoing metrics, and metrics doesn't expand into pricing recommendations.

## Resolution

After the report, the maintainer takes action:

1. **Merges** `report-writing` and `paper-writing` into a single `long-form-writing` skill with `mode: report` vs `mode: academic` parameter
2. **Differentiates** `copywriting` and `ad-creative` triggers as recommended
3. **Family-groups** `pricing-strategy` and `saas-metrics-coach` with explicit metadata
4. **Re-runs** overlap detection to verify all flags are resolved

## Re-run Verification

```bash
python tools/overlap-checker/overlap_checker.py \
  --skills-dir skills/ \
  --threshold 0.60
```

```
--- HIGH OVERLAP ---
(no entries)

--- TRIGGER COLLISIONS ---
(no entries above 0.40)

--- WATCHLIST ---
content-research-writer vs long-form-writing: 0.48 (acceptable)

All checks passed. Ready to publish v1.0.
```
