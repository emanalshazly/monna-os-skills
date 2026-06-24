# Fingerprint Algorithm

## How Semantic Fingerprints Are Computed

The `skill-overlap-detector` uses a **hybrid TF-IDF + cosine similarity** approach. It is designed to be:
- **Explainable** — every step maps to a concrete linguistic property
- **Stable** — minor edits don't change fingerprints; structural edits do
- **Domain-tuned** — weights are calibrated for skill-specific content, not general text

---

## Overview

```
SKILL.md → Extract Sections → Weighted Tokens → TF-IDF Vector → Cosine Similarity
```

---

## Step 1: Document Preprocessing

### Input
A `SKILL.md` file containing:
- YAML frontmatter (metadata)
- Markdown sections (headers, lists, paragraphs)
- Examples, references, tables

### What Gets Stripped

| Element | Action | Reason |
|---------|--------|--------|
| YAML frontmatter | Remove entirely | Metadata changes (version, date) should not affect semantic fingerprint |
| Markdown formatting | Remove `**`, `##`, `---`, etc. | Formatting is not content |
| Code blocks (fenced) | Remove or tokenize as `CODE_BLOCK` | Implementation details are not skill semantics |
| URLs | Remove or tokenize as `URL` | Links change; content intent does not |
| Numbers in isolation | Remove | "v1.2.3" is not semantic content |

### What Gets Preserved

| Element | Treatment | Reason |
|---------|-----------|--------|
| Section headers (H2, H3) | Tokenize as `SECTION:<header_text>` | Structure is highly discriminative |
| Trigger phrases | Tokenize as `TRIGGER:<phrase>` | Highest user-impact signal |
| Numbered lists (steps, rules) | Tokenize items individually | Process content is core to skill identity |
| Body paragraphs | Lowercase, remove punctuation, tokenize | Semantic content |

---

## Step 2: Section Weighting

Not all text in a skill is equally important. The algorithm applies section-specific weights:

```python
SECTION_WEIGHTS = {
    "triggers": 3.0,        # "Trigger Phrases", "When to Use", "Activate when"
    "principles": 2.5,      # "Core Principles", "Rules", "Constraints"
    "steps": 2.0,           # "Step-by-Step", "Process", "Workflow"
    "anti_patterns": 2.0,   # "Anti-Patterns", "Pitfalls", "Don't"
    "examples": 1.5,        # "Examples", "Use Cases"
    "references": 1.0,      # "References", "See Also"
    "body": 1.0,            # Everything else
}
```

**Why this weighting?**

- **Triggers (3×):** If two skills activate on the same inputs, they compete regardless of internal quality. This is the highest-stakes overlap.
- **Principles (2.5×):** Core principles define what a skill *does*. Identical principles mean identical purpose.
- **Steps (2×):** Process steps reveal functional overlap. Two skills with the same 5-step workflow are likely duplicates.
- **Body (1×):** Narrative text provides semantic context but is the most variable and least discriminative.

---

## Step 3: TF-IDF Vectorization

### Term Frequency (TF)

For each skill document, compute:

```
tf(t, d) = (count of term t in document d) × (section_weight of t) / (total weighted term count in d)
```

### Inverse Document Frequency (IDF)

```
idf(t, D) = log( |D| / (1 + |{d ∈ D : t ∈ d}|) )
```

Where `|D|` is the total number of skills in the corpus.

### TF-IDF Weight

```
tfidf(t, d, D) = tf(t, d) × idf(t, D)
```

This produces a sparse vector per skill document, with one dimension per unique term in the corpus vocabulary.

### Common-Term Downweighting

Terms that appear in >80% of skills are downweighted by an additional 0.5×:

| Term | Typical IDF Impact |
|------|-------------------|
| "skill", "agent", "use", "when" | Heavily downweighted |
| "trigger", "overlap", "detect" | Moderately downweighted |
| "fingerprint", "cosine", "tf-idf" | Preserved (domain-specific) |

---

## Step 4: Cosine Similarity

Given two skill vectors `A` and `B`:

```
cosine_similarity(A, B) = (A · B) / (||A|| × ||B||)
```

Result is a value in `[0, 1]`:
- `1.0` = identical semantic content
- `0.0` = completely disjoint content
- `0.6` = calibrated overlap threshold (see `threshold-rationale.md`)

### Why Cosine?

- **Length invariant:** A 10-page skill and a 3-page skill can be compared fairly.
- **Direction-sensitive:** Captures "about the same thing" regardless of verbosity.
- **Well-understood:** Standard in information retrieval; easy to explain to non-technical reviewers.

---

## Step 5: Trigger-Phrase Jaccard (Separate Track)

Trigger phrases are compared separately using Jaccard similarity:

```
Jaccard(A, B) = |triggers(A) ∩ triggers(B)| / |triggers(A) ∪ triggers(B)|
```

This is a set operation, not a vector operation. It answers: "What fraction of trigger phrases do these two skills share?"

**Why separate?** Because a skill can have unique body content but overlapping triggers — and vice versa. Both signals matter.

---

## Alternative: Sentence Embeddings

The reference implementation uses TF-IDF for portability (no neural model required). For higher accuracy on large corpora (>100 skills), you can substitute:

```python
# Using sentence-transformers (see requirements.txt optional deps)
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode([skill_text_a, skill_text_b])
similarity = cosine_similarity(embeddings[0], embeddings[1])
```

**Trade-offs:**

| Approach | Accuracy | Speed | Dependencies | Explainability |
|----------|----------|-------|---------------|----------------|
| TF-IDF | Good | Fast | `scikit-learn` only | High — every term is inspectable |
| Sentence Embeddings | Better | Slower | `sentence-transformers`, PyTorch | Lower — latent space, not term-level |
| Hybrid (recommended) | Best | Medium | Both | Medium — TF-IDF for triggers, embeddings for body |

The scaffold tool supports both. Set `USE_EMBEDDINGS=true` to enable the hybrid mode.

---

## Fingerprint Hash

For quick identity checks (e.g., "did this file change?"), a non-semantic hash is also computed:

```python
import hashlib
fingerprint_hash = hashlib.sha256(semantic_text.encode()).hexdigest()[:16]
```

This is **not** used for overlap detection — only for change detection and caching.

---

## Calibration Notes

The TF-IDF parameters in this algorithm were calibrated on the MONNA commercial skill portfolio (50+ skills across 12 domains):

- `min_df=2` (ignore terms that appear in only 1 skill)
- `max_df=0.8` (downweight terms in >80% of skills)
- `ngram_range=(1, 2)` (unigrams + bigrams capture short phrases)
- `sublinear_tf=True` (log-scale term frequency to reduce impact of long documents)

These values are defaults in the scaffold tool and can be overridden via CLI arguments.
