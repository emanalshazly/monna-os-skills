# Rotation System

## How Fingerprints Evolve When Skills Are Updated

Skills are not static. They evolve: new examples are added, triggers are expanded, principles are refined. The rotation system ensures that a skill's fingerprint changes meaningfully when its content changes — and stays stable when it doesn't.

---

## What Is a Fingerprint Rotation?

In the MONNA framework, a **rotation** is a versioned fingerprint assignment. Each skill has:
- A **base fingerprint** (e.g., `tool-001-d7e2b4`) — assigned at creation
- A **rotation history** — a log of when and why the fingerprint changed

When a skill is updated significantly, it may receive a **new rotation** — a new fingerprint that reflects its changed identity.

---

## When Does a Fingerprint Rotate?

| Change Type | Rotate? | Reason |
|-------------|---------|--------|
| Fix typos, formatting | No | Content intent unchanged |
| Add a new reference link | No | Semantic content unchanged |
| Expand examples (1→3) | No | Supporting material, not core identity |
| Add new trigger phrases | Yes | Activation surface changes; may collide with other skills |
| Add/remove core principles | Yes | Skill purpose changes |
| Modify step-by-step process | Yes | Functional behavior changes |
| Merge with another skill | Yes | New combined identity |
| Split into two skills | Yes | Both children need new fingerprints |

### The "Significant Content Change" Rule

> A fingerprint rotates when the semantic TF-IDF vector would change by > 15% relative to the previous version.

This 15% threshold is a proxy for "would this skill overlap with different skills now?"

---

## How Rotation Is Detected

```python
def should_rotate(old_skill, new_skill):
    old_vector = extract_fingerprint(old_skill)
    new_vector = extract_fingerprint(new_skill)
    drift = cosine_distance(old_vector, new_vector)
    
    if drift > 0.15:
        return True  # Significant change — rotate
    
    # Also rotate if trigger set changed by > 25%
    old_triggers = set(old_skill.triggers)
    new_triggers = set(new_skill.triggers)
    trigger_jaccard = len(old_triggers & new_triggers) / len(old_triggers | new_triggers)
    if trigger_jaccard < 0.75:
        return True  # Trigger surface changed significantly
    
    return False
```

---

## The Rotation Log

Each skill maintains a rotation log in its metadata:

```yaml
---
name: skill-overlap-detector
version: 1.0.0
fingerprint: tool-001-d7e2b4
rotations:
  - fingerprint: tool-001-d7e2b4
    version: 1.0.0
    date: 2026-06-24
    reason: initial release
---
```

If a rotation occurs:

```yaml
rotations:
  - fingerprint: tool-001-d7e2b4
    version: 1.0.0
    date: 2026-06-24
    reason: initial release
  - fingerprint: tool-001-e8f3c5
    version: 1.1.0
    date: 2026-09-15
    reason: added 3 new trigger phrases; expanded anti-patterns section
    drift_from_previous: 0.18
```

---

## Why Rotation Matters for Overlap Detection

### Scenario: Drift-Based Collision

1. **Day 0:** Skill A and Skill B have 55% overlap. They pass. Both are published.
2. **Day 90:** Skill A adds a new principle and two examples. Its fingerprint rotates.
3. **Day 90:** Skill B expands its trigger phrases to cover a new use case. Its fingerprint rotates.
4. **Result:** The new fingerprints have 68% overlap. A collision that didn't exist at creation time.

**Without rotation tracking:** The collision is never detected because both skills were "already approved."

**With rotation tracking:** The tool re-checks both skills after their rotation and flags the new collision.

---

## Rotation and the D1–D7 System

The MONNA commercial framework uses a 7-letter fingerprint (`D1–D7`) from an alphabet of {A, B, C, D}. Each letter represents a dimension of the skill's content:

| Dimension | Represents | Example Values |
|-----------|-----------|----------------|
| D1 | Domain category | A=tooling, B=marketing, C=analysis, D=governance |
| D2 | Interaction mode | A=chat, B=document, C=code, D=mixed |
| D3 | Depth tier | A=quick, B=standard, C=deep, D=comprehensive |
| D4 | Output type | A=text, B=structured, C=visual, D=mixed |
| D5 | Evidence requirement | A=none, B=light, C=moderate, D=strict |
| D6 | Audience level | A=beginner, B=intermediate, C=advanced, D=expert |
| D7 | Language scope | A=English, B=multilingual, C=Arabic-primary, D=adaptive |

When a skill rotates, its D1–D7 fingerprint may change if any dimension changed. For example, adding Arabic-language support would flip D7 from A to C.

The open-source `skill-overlap-detector` uses a simpler hex fingerprint (`tool-001-d7e2b4`) but the principle is the same: **a fingerprint encodes identity, and identity changes require a new fingerprint.**

---

## Family Groups and Rotation

When two skills are intentionally a family (e.g., `seo-audit` and `seo-audit-local`), they share a **family prefix** but have distinct suffixes:

```
seo-audit:         mar-023-a1b2c3
seo-audit-local:   mar-023-a1b2c4  ← same family, different suffix
seo-audit-mobile:  mar-023-a1b2c5  ← same family, different suffix
```

Family-grouped skills are excluded from the 60% overlap block *if* explicitly declared in metadata:

```yaml
family_group: seo-audit-family
family_parent: false  # true for the parent skill
```

However, they still appear in the overlap report with a `[FAMILY]` tag so maintainers can monitor family bloat.

---

## Practical Rotation Workflow

```
1. Developer edits SKILL.md
2. Tool computes new fingerprint and compares to old
3. If drift > 15% or trigger change > 25%:
   a. Generate new fingerprint
   b. Add entry to rotation log
   c. Re-run overlap detection against full corpus
   d. If new overlap > 60%: block merge until resolved
4. If no rotation needed: update version, keep fingerprint
```

---

## Summary

| Concept | Meaning |
|---------|---------|
| Fingerprint | A skill's semantic identity |
| Rotation | Assigning a new fingerprint when identity changes significantly |
| Drift threshold | 15% cosine distance = significant change |
| Trigger threshold | 25% trigger change = significant change |
| Family group | Intentionally related skills that share a prefix |

Rotation prevents "drift-based collisions" — the silent overlap that emerges when two previously-unique skills evolve toward each other.
