---
name: skill-overlap-detector
version: 1.0.0
fingerprint: tool-001-d7e2b4
quality_tier: certified
author: monna
license: MIT
last_tested: 2026-06-24
compatibility:
  Kimi/Daimon: certified
  Claude: certified
  Copilot: certified
  Cursor: validated
  OpenClaw: validated
---

# Skill Overlap Detector

## Flagship Tooling Skill for the MONNA Open-Source Skill Collection

This skill governs the detection and prevention of semantic duplication within skill collections. It open-sources the fingerprint rotation and overlap validation system from the MONNA signature framework, making it available for community-driven skill governance.

---

## Trigger Phrases

Activate when you see or hear:
- "check skill overlap"
- "detect duplicate skills"
- "skill fingerprint validation"
- "prevent skill redundancy"
- "skill similarity analysis"
- "overlap check my skills"
- "are these skills too similar"
- "fingerprint my skill collection"
- "validate skill uniqueness"
- "find redundant skills"

---

## When to Use

| Scenario | Action |
|----------|--------|
| Building a new skill and want to verify it doesn't duplicate existing ones | Run overlap detection against the full corpus before committing |
| Reviewing a community pull request that adds new skills | Run overlap detection on the PR branch against main |
| Auditing an existing skill library after 6+ months of growth | Run a full corpus scan to find drift and accidental duplicates |
| Merging two skill collections (e.g., personal + community) | Run pairwise overlap detection across both collections |
| Before releasing a commercial skill derived from open-source work | Verify no unintended overlap with source-of-influence skills |
| After a major refactor of multiple skills | Re-check fingerprints to ensure differentiation was preserved |

---

## When NOT to Use

| Scenario | Why It Doesn't Apply |
|----------|---------------------|
| Judging the *quality* of a skill | This tool detects *overlap*, not merit. A skill can be excellent and still overlap. |
| Replacing human review | Overlap detection is an automated filter. Humans still decide whether overlap is acceptable or requires differentiation. |
| Comparing skills across different agent platforms with incompatible formats | Fingerprints are extracted from SKILL.md content. If formats are incompatible, semantic comparison may be meaningless. |
| Detecting plagiarism in general text | This is tuned for skill-specific content (triggers, principles, process steps). Use general duplicate detection for prose. |
| Enforcing overlap on *intentional* skill families | Some skills are designed to be variants (e.g., `seo-audit` and `seo-audit-ecommerce`). Flag these as family groups, not duplicates. |

---

## Core Principles

### Principle 1: Overlap > 60% Is a Hard Block — Not a Suggestion

The 60% threshold is derived from the MONNA framework's empirical experience with 50+ skill rotations. Above 60%, two skills start triggering on the same user intents and producing similar outputs. This creates user confusion and dilutes the collection's value. Below 60%, skills can coexist as legitimate variants.

**Hard block means:** the new skill is not merged until the overlap is resolved — either by differentiation or by explicit family-group designation.

### Principle 2: Semantic Similarity Matters More Than Lexical Similarity

Two skills can use completely different words and still overlap. Example:
- Skill A: "Audit technical SEO issues — crawl errors, meta tags, Core Web Vitals"
- Skill B: "Diagnose website performance — broken links, page titles, loading speed"

Lexically different. Semantically identical. The detector uses TF-IDF vectorization and cosine similarity to catch this.

### Principle 3: Fingerprints Must Be Stable Across Versions Unless Content Changes Significantly

A skill's fingerprint should not change when you fix a typo or add a reference. It *should* change when you add a new section, modify core principles, or expand trigger phrases. This stability is achieved by:
- Ignoring frontmatter metadata (version, date, author)
- Ignoring formatting artifacts (horizontal rules, ASCII tables if content is identical)
- Weighting semantic content (principles, triggers, steps) higher than framing text

### Principle 4: Trigger Phrases Are the Highest-Overlap Signal

If two skills share trigger phrases, they will be activated by the same user inputs. This is the most dangerous form of overlap because it happens *before* the skill content is even read. Always check trigger-phrase overlap separately from content overlap.

### Principle 5: The Tool Is a Gate, Not a Judge

The overlap detector reports *potential* duplication. It is the collection maintainer's job to decide:
- Is this overlap acceptable (intentional family)?
- Does one skill subsume the other?
- Should both be differentiated, or one deprecated?

The tool never deletes or modifies skills. It only produces evidence.

---

## Step-by-Step Process

### Step 1: Extract Fingerprints from Skill Corpus

For each `SKILL.md` file in the collection:

```
Input:  skills/<domain>/<skill-name>/SKILL.md
Output: {skill_id, fingerprint_vector, trigger_phrases[], content_hash}
```

**Extraction rules:**
1. Strip YAML frontmatter (between `---` delimiters)
2. Extract all H2/H3 section headers as structural tokens
3. Extract trigger phrases (bulleted or listed phrases under "Trigger" or "When to Use")
4. Extract numbered lists (process steps, rules, principles) as procedural tokens
5. Convert remaining body text to lowercase, remove punctuation, tokenize
6. Build a weighted document vector: headers 3×, triggers 2×, body 1×

**Reference implementation:** See `tools/overlap-checker/overlap_checker.py`

### Step 2: Compute Pairwise Similarity

For every pair of skills `(A, B)` in the corpus:

```
similarity(A, B) = cosine( tfidf_vector(A), tfidf_vector(B) )
```

Where:
- `tfidf_vector` is computed over the full corpus vocabulary
- Term frequency is weighted by section type (principles > triggers > body)
- Inverse document frequency downweights common terms (e.g., "skill", "agent", "use")

**Separate track:** Also compute Jaccard similarity on trigger-phrase sets:

```
trigger_overlap(A, B) = |triggers(A) ∩ triggers(B)| / |triggers(A) ∪ triggers(B)|
```

### Step 3: Apply Threshold Filtering

```
if similarity(A, B) > 0.60:
    flag as HIGH_OVERLAP
    add to report

if trigger_overlap(A, B) > 0.40:
    flag as TRIGGER_COLLISION
    add to report with warning

if similarity(A, B) > 0.45 and similarity(A, B) <= 0.60:
    flag as MEDIUM_OVERLAP
    add to watchlist
```

The 60% content threshold and 40% trigger threshold are based on MONNA framework calibration. See `references/threshold-rationale.md` for the derivation.

### Step 4: Generate Overlap Report

The report is a markdown file with three sections:

**Section A: High Overlap Pairs (Action Required)**
| Skill A | Skill B | Similarity | Shared Triggers | Recommendation |
|---------|---------|------------|-----------------|----------------|
| skill-a | skill-b | 0.73 | 2/5 | Differentiate or merge |

**Section B: Trigger Collisions (Warning)**
| Skill A | Skill B | Trigger Jaccard | Shared Triggers |
|---------|---------|-----------------|-----------------|
| skill-c | skill-d | 0.50 | "audit", "check" |

**Section C: Watchlist (Medium Overlap — Monitor)**
| Skill A | Skill B | Similarity | Notes |
|---------|---------|------------|-------|
| skill-e | skill-f | 0.52 | Both target SEO; acceptable family? |

### Step 5: Recommend Merge or Differentiation

For each HIGH_OVERLAP pair, recommend one of:

1. **Differentiate** — Expand one skill into a distinct domain, add unique sections, or narrow trigger phrases
2. **Merge** — Combine into a single skill with sub-modes or parameterization
3. **Family Group** — Explicitly mark as an intentional family (e.g., `seo-audit` and `seo-audit-ecommerce`) with a shared parent reference
4. **Deprecate** — Retire the older/lower-quality skill and redirect to the newer one

---

## Anti-Patterns

### Anti-Pattern 1: Use Exact String Matching — Misses Semantic Duplicates

❌ **Wrong:** `if "SEO" in skill_a and "SEO" in skill_b: flag_overlap()`

✅ **Right:** Use TF-IDF + cosine similarity to capture that "SEO audit" and "website health check" may describe the same thing with different words.

---

### Anti-Pattern 2: Ignore Trigger Phrase Overlap

❌ **Wrong:** Only compare body text, ignoring "Trigger Phrases" or "When to Use" sections.

✅ **Right:** Trigger overlap is the most user-visible form of duplication. Two skills that activate on the same inputs will confuse users even if their internal content differs.

---

### Anti-Pattern 3: Set Threshold Too Low — Blocks Legitimate Variants

❌ **Wrong:** Using 30% as the threshold. This will flag every skill in a domain as overlapping.

✅ **Right:** 60% is calibrated to allow domain variants (e.g., `seo-audit` vs `seo-audit-local`) while catching true duplicates. See `references/threshold-rationale.md`.

---

### Anti-Pattern 4: Run Only Once — Fingerprints Drift

❌ **Wrong:** Running overlap detection only at skill creation, never re-checking.

✅ **Right:** Refactors, content additions, and trigger expansions can cause previously-unique skills to converge. Re-run quarterly or after any batch update.

---

### Anti-Pattern 5: Compare Skills Without Normalizing Structure

❌ **Wrong:** Treating a 5-section skill and a 12-section skill as comparable documents without section weighting.

✅ **Right:** Weight structural elements (principles, triggers, steps) higher than narrative text. A skill with 10 pages of prose but unique triggers is less overlapping than a short skill with identical triggers.

---

### Anti-Pattern 6: Treat Overlap Detection as a Quality Score

❌ **Wrong:** "This skill has 55% overlap, so it's worse than the one with 30%."

✅ **Right:** Overlap is about *uniqueness*, not *quality*. A 55%-overlap skill may be the better-written one. The decision is which to keep/differentiate, not which is "good."

---

## References

| Reference | Purpose | Path |
|-----------|---------|------|
| Fingerprint Algorithm | How semantic fingerprints are computed | [`references/fingerprint-algorithm.md`](references/fingerprint-algorithm.md) |
| Threshold Rationale | Why 60% and 40% are the calibrated thresholds | [`references/threshold-rationale.md`](references/threshold-rationale.md) |
| Rotation System | How fingerprints evolve when skills are updated | [`references/rotation-system.md`](references/rotation-system.md) |

---

## Examples

| Example | Scenario | Path |
|---------|----------|------|
| Small Collection | Running overlap detection on a 10-skill collection | [`examples/example-01-small-collection.md`](examples/example-01-small-collection.md) |
| PR Submission | Checking a new PR for overlap before merge | [`examples/example-02-pr-submission.md`](examples/example-02-pr-submission.md) |

---

## Tests

See [`tests/validation-checklist.md`](tests/validation-checklist.md) for the validation checklist used to certify this skill.

---

## Metadata

| Field | Value |
|-------|-------|
| **Skill ID** | `tool-001-d7e2b4` |
| **Quality Tier** | `certified` |
| **Author** | `monna` |
| **License** | `MIT` |
| **Last Tested** | `2026-06-24` |
| **Compatibility** | Kimi/Daimon: certified, Claude: certified, Copilot: certified, Cursor: validated, OpenClaw: validated |

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-06-24 | Initial release. Open-sourced from MONNA signature framework v12.8. |
