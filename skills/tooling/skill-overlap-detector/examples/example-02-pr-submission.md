# Example 2: Checking a New PR for Overlap Before Merge

## Scenario

A community contributor has opened a pull request adding a new skill: `churn-prevention`. Before merging, you need to verify it doesn't overlap with existing skills in the collection.

## PR Details

| Field | Value |
|-------|-------|
| PR | #42 |
| Author | @contributor-alex |
| New skill | `skills/retention/churn-prevention/SKILL.md` |
| Claim | "Reduces voluntary and involuntary churn through cancel flow design, save offers, exit surveys, and dunning sequences" |
| Triggers | "cancel flow", "churn reduction", "save offers", "dunning", "exit survey", "payment recovery", "win-back", "involuntary churn", "failed payments", "cancel page" |

## Existing Skills in Collection

The collection already has:
- `saas-metrics-coach` (finance — SaaS metrics)
- `campaign-plan` (marketing — campaign planning)
- `pricing-strategy` (finance — SaaS pricing)
- `ad-creative` (marketing — ad copy)

No existing skill explicitly targets "churn" or "retention."

## Command

The overlap checker supports comparing a single new skill against an existing corpus without adding it to the corpus first:

```bash
python tools/overlap-checker/overlap_checker.py \
  --skills-dir skills/ \
  --new-skill skills/retention/churn-prevention/SKILL.md \
  --threshold 0.60 \
  --output pr-42-overlap-report.md
```

## Output

```
================================================================================
PR OVERLAP DETECTION REPORT
PR: #42
New Skill: churn-prevention
Corpus: 4 existing skills
Threshold: 0.60 (content), 0.40 (triggers)
================================================================================

--- NEW SKILL FINGERPRINT ---

Skill ID: churn-prevention
Fingerprint: 7a3f9e2b1d4c8e5f
Trigger Count: 10
Section Count: 8
Estimated Quality: HIGH (comprehensive structure, 5 anti-patterns, 3 examples)

--- OVERLAP WITH EXISTING SKILLS ---

┌────────────────────┬────────────┬─────────────┬──────────────────────────────┐
│ Existing Skill     │ Similarity │ Trig. Jacc. │ Verdict                      │
├────────────────────┼────────────┼─────────────┼──────────────────────────────┤
│ saas-metrics-coach │ 0.38       │ 0.09        │ ✅ PASS — Related domain but │
│                    │            │             │ distinct focus (retention    │
│                    │            │             │ vs metrics)                  │
├────────────────────┼────────────┼─────────────┼──────────────────────────────┤
│ campaign-plan      │ 0.22       │ 0.00        │ ✅ PASS — No overlap         │
├────────────────────┼────────────┼─────────────┼──────────────────────────────┤
│ pricing-strategy   │ 0.31       │ 0.05        │ ✅ PASS — Related domain but │
│                    │            │             │ distinct focus (retention  │
│                    │            │             │ vs pricing)                  │
├────────────────────┼────────────┼─────────────┼──────────────────────────────┤
│ ad-creative        │ 0.15       │ 0.00        │ ✅ PASS — No overlap         │
└────────────────────┴────────────┴─────────────┴──────────────────────────────┘

Max similarity with any existing skill: 0.38 (saas-metrics-coach)
Max trigger overlap with any existing skill: 0.09 (saas-metrics-coach)

--- RECOMMENDATION ---

✅ APPROVED FOR MERGE

No overlap detected. The new skill is well-differentiated from all existing skills.

It shares a domain (SaaS/tech) with saas-metrics-coach and pricing-strategy but has a
unique focus (churn/retention) with no trigger collisions. The trigger phrase set is
distinct and specific.

Suggested action: Add to `retention/` domain directory and merge PR #42.
```

## Edge Case: What If the PR Had Overlapped?

Suppose the contributor had submitted a skill called `customer-retention` with these triggers:
- "churn reduction", "save offers", "customer retention", "cancel page", "win-back campaign"

And the collection already had `churn-prevention` with:
- "cancel flow", "churn reduction", "save offers", "dunning", "exit survey", "payment recovery", "win-back", "involuntary churn", "failed payments", "cancel page"

The report would look like:

```
┌────────────────────┬────────────┬─────────────┬──────────────────────────────┐
│ Existing Skill     │ Similarity │ Trig. Jacc. │ Verdict                      │
├────────────────────┼────────────┼─────────────┼──────────────────────────────┤
│ churn-prevention   │ 0.71       │ 0.55        │ 🔴 BLOCK — High overlap +    │
│ (already in main)  │            │             │ trigger collision            │
└────────────────────┴────────────┴─────────────┴──────────────────────────────┘

--- RECOMMENDATION ---

🔴 BLOCKED — DO NOT MERGE

The new skill 'customer-retention' has 71% content overlap and 55% trigger overlap
with the existing skill 'churn-prevention'. They are effectively duplicates.

Options for the contributor:
1. DIFFERENTIATE: Narrow 'customer-retention' to a specific vertical (e.g.,
   'customer-retention-b2b-saas' or 'customer-retention-mobile-apps')
2. MERGE: Add the new content as an expansion to the existing 'churn-prevention'
   skill rather than creating a new skill
3. DEPRECATE: Propose replacing 'churn-prevention' if 'customer-retention' is
   strictly better and more comprehensive

Action: Request changes on PR #42. Provide the contributor with the overlap report
and suggest one of the three resolution paths.
```

## PR Comment Template

When you block a PR due to overlap, use this comment template:

```markdown
## Overlap Detection Result: 🔴 Blocked

This PR has been flagged by the automated overlap detector.

**Overlap detected with:** `skills/retention/churn-prevention`
- Content similarity: 71%
- Trigger overlap: 55%

### Why this is blocked

Skills with >60% overlap compete for the same user inputs and produce similar
outputs. This creates confusion and dilutes the collection.

### How to resolve

Please choose one of:

1. **Differentiate** — Narrow the scope to a specific vertical or use case that
doesn't overlap with the existing skill
2. **Merge** — Add your content as an expansion to the existing skill rather than
creating a new one
3. **Replace** — If your skill is strictly better, propose deprecating the existing
one instead

See the overlap report attached: `pr-42-overlap-report.md`

Questions? Tag @monna or comment on this thread.
```

## CI Integration

Add this to your `.github/workflows/overlap-check.yml` to run automatically on PRs:

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
            --threshold 0.60 \
            --output overlap-report.md
      - if: failure()
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '🔴 Overlap detected. See the attached report for details.'
            })
```
