# SKILL.md — Arabic Technical Translator

## Skill: `arabic-technical-translator`

> **Multi-agent Skill** — Orchestrates a bilingual technical translation workflow between Arabic and English, optimized for MENA tech ecosystems. Deploys specialist sub-agents for terminology, cultural adaptation, register detection, and technical accuracy review.

---

### Identity & Purpose

**SkillBuilder:** SkillBuilder_Multilingual
**Quality Tier:** `certified`
**Fingerprint:** `multi-001-e8f3c5`
**Compatibility:** Kimi/Daimon: certified | Claude: certified | Copilot: certified | Cursor: validated | OpenClaw: validated
**Last Tested:** 2026-06-24
**Author:** monna
**License:** MIT

**Purpose:** Bridge Arabic and English technical communication for MENA tech markets, leveraging code-switching, dialect awareness, and cultural context as competitive advantages. This skill is **distinct from commercial translation tools** — it is an open-source, quality-governed resource for the community.

**Trigger Phrases:**
- "translate technical Arabic to English"
- "Arabic technical documentation translation"
- "Egyptian Arabic technical writing"
- "Arabic-English code-switching for tech"
- "localize technical content for MENA region"
- "bilingual technical communication Arabic English"

---

### When to Use / When NOT to Use

**Use when:**
- Translating technical content between Arabic and English for MENA tech audiences
- Localizing API documentation, developer guides, or technical specs for Egyptian, Saudi, UAE, or Gulf developer communities
- Creating bilingual technical content that naturally code-switches between Arabic and English technical terms
- Adapting AI governance, DePIN, or infrastructure documentation for Arabic-speaking stakeholders
- Writing technical blog posts, tutorials, or onboarding materials for MENA developers
- Preparing pitch decks or product descriptions for Arabic-speaking investors or enterprise clients
- Producing RTL-aware technical layouts with accurate Arabic typography

**Do NOT use when:**
- General literary or poetic translation (this is a **technical** translator, not a literary one)
- Legal contracts, medical documents, or certified official translations that require human legal/medical expertise
- Non-technical colloquial Arabic (social media slang, poetry, song lyrics, creative fiction)
- High-stakes regulatory submissions where a sworn translator is legally required
- Purely marketing copy without technical substance (use a dedicated copywriting skill instead)
- Translations for non-MENA Arabic dialects (Maghrebi, Levantine non-Egyptian, Iraqi) unless the user explicitly requests adaptation

---

### Core Principles

1. **Code-switching is a feature, not a bug.**
   Egyptian Arabic + English technical terms is the standard in MENA tech. A sentence like "الـ cloud computing هنا بيستخدم Azure" is not broken — it's how Egyptian developers actually communicate. Embrace it. Don't force full Arabic translations of terms that the audience already knows in English.

2. **Preserve technical accuracy over fluency.**
   A wrong term is worse than an awkward sentence. "Neural network" translated as "شبكة عصبية" is correct; "شبكة أعصاب" is wrong. If the Arabic term is ambiguous, keep the English term in parentheses. Clarity beats elegance in technical translation.

3. **Cultural context matters.**
   "Cloud computing" means different things to a Saudi enterprise buyer vs. an Egyptian startup founder. The Saudi market may expect formal Arabic with full English glossaries; the Egyptian startup scene expects colloquial Arabic with heavy code-switching. Know your audience before you translate.

4. **Register awareness is non-negotiable.**
   - **Formal Arabic (Modern Standard Arabic / MSA):** Official docs, government RFPs, academic papers, AI governance policies
   - **Egyptian Colloquial:** Developer tutorials, UI microcopy, Slack communities, informal blog posts
   - **Mixed Register:** Technical blog posts, pitch decks, onboarding flows — colloquial body with formal headers
   Choose the register before you write the first sentence.

5. **Bidirectional translation requires different strategies.**
   - **Arabic → English:** Extract the technical meaning, often buried in colloquial phrasing; don't translate the filler words literally; reconstruct for an international technical audience
   - **English → Arabic:** Decide on register first, then map terminology, then adapt culturally — don't just translate words; translate the *intent* for the MENA context

---

### Step-by-Step Process

#### Phase 1: Source Analysis & Register Detection

**Goal:** Understand what you're translating, for whom, and in what register.

**Actions:**
1. Read the source material and identify:
   - Document type (API docs, governance policy, UI strings, blog post, pitch deck)
   - Technical domain (AI/ML, cloud, blockchain/DePIN, infrastructure, SaaS, dev tools)
   - Target audience (enterprise, startup, developer, investor, government)
   - Target MENA market (Saudi, UAE, Egypt, Qatar, Kuwait, broader GCC)
2. Determine the appropriate register:
   - Formal/MSA for official, legal, or academic content
   - Colloquial Egyptian for developer-facing, informal, or community content
   - Mixed register for hybrid content (e.g., formal headers + colloquial body)
3. Flag any content that requires cultural adaptation (references to Western business practices, holidays, or legal frameworks)

**Output:** `register-decision.md` — a one-page brief stating: document type, target audience, chosen register, cultural adaptation notes, and any ambiguity risks.

#### Phase 2: Terminology Mapping

**Goal:** Build a domain-specific glossary before translating a single sentence.

**Actions:**
1. Extract all technical terms from the source material
2. Map each term using the reference glossary (`references/technical-glossary.md`)
3. For terms not in the glossary, decide:
   - Does an established Arabic technical term exist? (Use it.)
   - Is the English term universally used in MENA? (Keep it, optionally Arabic-glossed.)
   - Is the term ambiguous or new? (Use English + Arabic explanation.)
4. Document any term decisions that may be controversial or market-specific

**Output:** `glossary-mapping.md` — a table of: source term, Arabic term, English term (if kept), decision rationale, and market applicability.

#### Phase 3: Cultural Adaptation (MENA Market Context)

**Goal:** Adapt content so it feels native to the target MENA market, not translated.

**Actions:**
1. Identify content that assumes Western cultural context:
   - Business examples (e.g., "like Uber" → "like Careem" or "like Swvl")
   - Legal references (e.g., GDPR → PDPL for Saudi, NPDP for UAE)
   - Currency and pricing (USD → SAR, AED, or EGP with appropriate conversion context)
   - Holidays and seasons (Christmas → Ramadan or Eid Al-Fitr where relevant)
2. Adapt tone to match local business culture:
   - Saudi enterprise: formal, respectful, hierarchical
   - Egyptian startup: direct, informal, humor-friendly
   - UAE tech hub: cosmopolitan, English-friendly, innovation-focused
   - Qatar/GCC: prestige-aware, formal, relationship-oriented
3. Check for any content that may be culturally sensitive or inappropriate in the target market

**Output:** `cultural-adaptation-notes.md` — list of adaptations made, with rationale and market justification.

#### Phase 4: Draft Translation

**Goal:** Produce a complete first draft in the target language.

**Actions:**
1. Translate section by section, following the register decision and glossary mapping
2. For English → Arabic:
   - Use the chosen register consistently
   - Code-switch naturally where MENA developers would
   - Preserve all technical accuracy; never "smooth over" ambiguity
   - Write RTL-aware content: use proper Arabic punctuation, avoid Latin-only parentheses in Arabic text, check for bidirectional text issues
3. For Arabic → English:
   - Extract the technical core meaning; strip colloquial filler
   - Reconstruct for an international technical audience
   - Expand implied context that Arabic colloquial may leave unstated
   - Ensure acronyms and abbreviations are defined for non-Arabic speakers
4. Mark any sections where you are uncertain with `[REVIEW NEEDED]`

**Output:** `draft-translation.md` — complete translated document with `[REVIEW NEEDED]` flags.

#### Phase 5: Technical Accuracy Review

**Goal:** Verify that the translation preserves all technical meaning and no errors were introduced.

**Actions:**
1. Back-translate key technical sections to English (if Arabic → English was the direction) or verify Arabic terms against authoritative sources
2. Check that:
   - All API endpoints, parameter names, and code snippets are preserved exactly (never translated)
   - All technical terms are consistent with the glossary
   - No technical meaning was lost or added
   - Numbers, units, and dates are correctly formatted for the target locale
3. Verify that code blocks, CLI commands, and configuration examples remain unchanged
4. Have a technical reviewer (or sub-agent) validate the output

**Output:** `technical-review-report.md` — list of verified sections, any issues found, and resolutions.

#### Phase 6: Localization Validation

**Goal:** Final quality check for cultural fit, readability, and professional polish.

**Actions:**
1. Read the final translation aloud (or have a sub-agent simulate reading)
2. Check for:
   - Natural flow in the chosen register
   - No awkward literal translations
   - Consistent terminology throughout
   - Proper RTL formatting and Arabic typography
   - Cultural appropriateness for the target market
3. Verify that the translation feels like it was written *for* the MENA audience, not *at* them
4. Run the validation checklist (`tests/validation-checklist.md`)

**Output:** `localization-validation-report.md` — pass/fail checklist results with any final edits.

---

### Anti-Patterns

| Anti-Pattern | Why It Fails | How to Avoid |
|-------------|-------------|--------------|
| **Translate literally without cultural context** | "Cloud computing" → "الحوسبة السحابية" may be correct technically, but if your audience is Egyptian developers who say "الـ cloud" in daily conversation, it sounds robotic and foreign. | Always know your audience. Check the market context guide before choosing terms. |
| **Ignore register differences between formal and colloquial Arabic** | Using MSA in a developer tutorial makes it feel like a government textbook; using colloquial in an AI governance policy makes it look unprofessional. | Decide register in Phase 1 and enforce it ruthlessly. |
| **Use machine translation without human review for technical terms** | MT will translate "agent" as "وكيل" (real estate agent) instead of "عامل ذكي" or keep it as "agent" in AI contexts. MT has no domain awareness. | Always build a glossary first. Never trust MT for technical terms without verification. |
| **Treat Arabic as a single dialect** | Maghrebi Arabic, Egyptian, Levantine, and Gulf Arabic are mutually unintelligible in colloquial form. One size does not fit all. | This skill targets Egyptian + MSA. If the user needs Maghrebi or Gulf colloquial, flag it as out of scope. |
| **Forget that Arabic is RTL — layout implications matter** | Mixed Arabic-English content can cause bidirectional text issues. Parentheses, punctuation, and code snippets can render incorrectly. | Always test RTL rendering. Use proper Unicode bidirectional marks. Keep code snippets in separate blocks. |
| **Force-translate every English term into Arabic** | "API", "JSON", "Kubernetes" — these are universal in MENA tech. Forcing Arabic equivalents that no one uses creates confusion. | Code-switching is a feature. Keep English terms where they are standard, and gloss them in Arabic if needed. |
| **Omit the bidirectional strategy** | Arabic → English and English → Arabic are not mirror processes. Arabic → English often requires reconstructing implied meaning; English → Arabic requires cultural embedding. | Follow the bidirectional strategy notes in Phase 4. |
| **Ignore MENA market differences** | What works in Egypt may not work in Saudi Arabia. Business culture, formality levels, and English proficiency vary dramatically. | Use the MENA market context guide to adapt per-country. |

---

### References

- [`references/technical-glossary.md`](./references/technical-glossary.md) — Common Arabic-English technical term mappings
- [`references/mena-market-context.md`](./references/mena-market-context.md) — Cultural and business context for MENA tech markets
- [`references/arabic-dialects-guide.md`](./references/arabic-dialects-guide.md) — When to use Egyptian colloquial, MSA, or formal Arabic in technical contexts

---

### Examples

- [`examples/example-01-api-documentation.md`](./examples/example-01-api-documentation.md) — English API docs → Arabic for Egyptian developers
- [`examples/example-02-ai-governance-arabic.md`](./examples/example-02-ai-governance-arabic.md) — Arabic AI governance policy → English for international stakeholders

---

### Tests

- [`tests/validation-checklist.md`](./tests/validation-checklist.md) — Reviewer checklist with pass/fail criteria

---

### Meta

| Attribute | Value |
|-----------|-------|
| `skill_name` | `arabic-technical-translator` |
| `fingerprint` | `multi-001-e8f3c5` |
| `quality_tier` | `certified` |
| `author` | `monna` |
| `license` | `MIT` |
| `last_tested` | `2026-06-24` |
| `compatibility` | Kimi/Daimon: certified; Claude: certified; Copilot: certified; Cursor: validated; OpenClaw: validated |
| `domain` | multilingual, technical translation, MENA tech, Arabic-English, code-switching |
| `requires_human_review` | Yes — technical accuracy review and cultural validation are mandatory |
| `language` | Arabic (Egyptian colloquial, MSA), English |
| `target_markets` | Saudi Arabia, UAE, Egypt, Qatar, Kuwait, broader GCC |
| `distinct_from_commercial` | Yes — this is an open-source, quality-governed skill. Commercial translation services are separate. |
