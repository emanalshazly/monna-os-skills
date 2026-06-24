# Validation Checklist — Arabic Technical Translator

> Reviewer checklist for validating Arabic-English technical translations produced using the `arabic-technical-translator` skill. This checklist ensures quality, accuracy, and cultural appropriateness before delivery.

**Last Updated:** 2026-06-24
**Version:** 1.0
**Skill:** `arabic-technical-translator` (`multi-001-e8f3c5`)

---

## How to Use This Checklist

1. **Reviewer:** A second sub-agent or human reviewer should complete this checklist.
2. **For each item:** Mark `PASS` or `FAIL` with a brief note if `FAIL`.
3. **Action on FAIL:** If any item fails, the translation must be revised and rechecked before delivery.
4. **Critical items:** Marked with 🔴 — these are non-negotiable. A single 🔴 failure blocks delivery.
5. **Important items:** Marked with 🟡 — these should pass, but minor issues may be addressed with notes.
6. **Best-practice items:** Marked with 🟢 — these are quality enhancers; failure is noted but not blocking.

---

## Section A: Register & Tone (Critical)

| # | Checkpoint | Criteria | Result | Notes |
|---|-----------|----------|--------|-------|
| A1 🔴 | **Register matches target audience** | The chosen register (MSA / Egyptian Colloquial / Mixed) is appropriate for the target audience and market. | ☐ PASS ☐ FAIL | |
| A2 🔴 | **Register is consistent** | The register does not shift unintentionally between formal and colloquial within the same document. | ☐ PASS ☐ FAIL | |
| A3 🟡 | **Tone matches market expectations** | Saudi content is formal/prestige-conscious; Egyptian content is direct/humor-friendly; UAE content is cosmopolitan/innovation-focused. | ☐ PASS ☐ FAIL | |
| A4 🟡 | **Code-switching is natural** | English technical terms appear where they are standard in MENA; not forced in or forced out. | ☐ PASS ☐ FAIL | |
| A5 🟢 | **Hierarchical framing is appropriate** | Deferential language (e.g., "يسرنا") is used only where culturally appropriate (Saudi formal); removed where inappropriate (international English). | ☐ PASS ☐ FAIL | |

---

## Section B: Technical Accuracy (Critical)

| # | Checkpoint | Criteria | Result | Notes |
|---|-----------|----------|--------|-------|
| B1 🔴 | **No code was translated** | API endpoints, JSON keys, code snippets, CLI commands, parameter names, and configuration examples remain in their original language. | ☐ PASS ☐ FAIL | |
| B2 🔴 | **Technical terms are correct** | All technical terms match the glossary mappings. No mistranslations (e.g., "agent" ≠ "وكيل", "cloud" ≠ "غيمة"). | ☐ PASS ☐ FAIL | |
| B3 🔴 | **Terminology is consistent** | The same technical term is translated the same way throughout the document. No mixed translations for the same concept. | ☐ PASS ☐ FAIL | |
| B4 🔴 | **No technical meaning was lost** | Back-translation of key technical sections matches the source meaning. No ambiguity introduced. | ☐ PASS ☐ FAIL | |
| B5 🔴 | **Acronyms and abbreviations are handled correctly** | Standard acronyms (API, JSON, REST, ML, AI, PDPL, etc.) are kept in original form. Non-standard acronyms are defined on first use. | ☐ PASS ☐ FAIL | |
| B6 🟡 | **Numbers and units are correct** | Numbers use appropriate numerals (Arabic-Indic ٠١٢٣٤٥٦٧٨٩ for formal Arabic; Western Arabic 0123456789 acceptable in colloquial). Units are localized. | ☐ PASS ☐ FAIL | |
| B7 🟡 | **Dates and times are localized** | Dates use appropriate format for target market (e.g., Hijri alongside Gregorian for Saudi formal). Time zones referenced if applicable. | ☐ PASS ☐ FAIL | |
| B8 🟢 | **Technical precision is maintained** | Terms like "fairness," "explainability," "transparency" in AI contexts are used in their technical sense, not general sense. | ☐ PASS ☐ FAIL | |

---

## Section C: Cultural Adaptation (Critical)

| # | Checkpoint | Criteria | Result | Notes |
|---|-----------|----------|--------|-------|
| C1 🔴 | **No culturally inappropriate content** | No references to alcohol, gambling, or content that conflicts with Islamic values. No inappropriate religious references. | ☐ PASS ☐ FAIL | |
| C2 🔴 | **Local compliance frameworks are referenced** | Saudi content references PDPL; UAE content references NPDP; not just GDPR. Local frameworks are named correctly. | ☐ PASS ☐ FAIL | |
| C3 🟡 | **Currency is localized** | Pricing uses local currency (SAR, AED, EGP, QAR, KWD) where applicable, not just USD. | ☐ PASS ☐ FAIL | |
| C4 🟡 | **Examples are locally relevant** | Business examples reference local companies (Careem, Swvl, Fawry, Aramco, STC) rather than only Western examples. | ☐ PASS ☐ FAIL | |
| C5 🟡 | **Implicit context is made explicit** | Content written for one audience does not assume knowledge that another audience lacks (e.g., Vision 2030 explained for international readers). | ☐ PASS ☐ FAIL | |
| C6 🟢 | **Holidays and seasons are appropriate** | Ramadan and Eid acknowledged where relevant; Christmas references avoided or adapted; Friday respected as holy day. | ☐ PASS ☐ FAIL | |

---

## Section D: Arabic Language Quality (Critical for Arabic output)

| # | Checkpoint | Criteria | Result | Notes |
|---|-----------|----------|--------|-------|
| D1 🔴 | **Arabic grammar is correct for the chosen register** | MSA uses MSA grammar; Egyptian colloquial uses Egyptian grammar. No mixing of grammatical systems unintentionally. | ☐ PASS ☐ FAIL | |
| D2 🔴 | **Arabic script is correct** | No transliteration (Latin letters). Arabic script is used for Arabic content. Code/terms in Latin script are justified. | ☐ PASS ☐ FAIL | |
| D3 🟡 | **Arabic punctuation is correct** | Arabic question marks (؟), commas (،), and quotation marks («» or "" as appropriate) are used. | ☐ PASS ☐ FAIL | |
| D4 🟡 | **Definite articles are used correctly** | "الـ" prefix is correct; sun/moon letters (الحروف الشمسية والقمرية) are handled correctly. | ☐ PASS ☐ FAIL | |
| D5 🟢 | **Arabic typography is RTL-aware** | Arabic text renders correctly in RTL. Mixed Arabic-English content uses proper bidirectional marks or structural separation. | ☐ PASS ☐ FAIL | |
| D6 🟢 | **No spelling errors** | Arabic words are spelled correctly (e.g., "الاصطناعي" not "الاصطناعى"; "الحوسبة" not "الحوسبه"). | ☐ PASS ☐ FAIL | |

---

## Section E: English Language Quality (Critical for English output)

| # | Checkpoint | Criteria | Result | Notes |
|---|-----------|----------|--------|-------|
| E1 🔴 | **English is idiomatic and natural** | Translation does not read like "translated English." Sentences flow naturally for native English speakers. | ☐ PASS ☐ FAIL | |
| E2 🔴 | **No awkward literal translations** | Arabic idioms and structures are not translated word-for-word. Meaning is reconstructed in natural English. | ☐ PASS ☐ FAIL | |
| E3 🟡 | **Active voice is used where appropriate** | English business writing prefers active voice. Arabic passive constructions are converted to active where appropriate. | ☐ PASS ☐ FAIL | |
| E4 🟡 | **Sentence length is appropriate** | Long Arabic compound sentences are broken into shorter English sentences. No run-on sentences. | ☐ PASS ☐ FAIL | |
| E5 🟢 | **Technical English is precise** | English technical terms are the standard ones used in international business (not obscure or dated alternatives). | ☐ PASS ☐ FAIL | |

---

## Section F: Bidirectional Quality (Critical for both directions)

| # | Checkpoint | Criteria | Result | Notes |
|---|-----------|----------|--------|-------|
| F1 🔴 | **Arabic → English: implied context is reconstructed** | Arabic colloquial or formal content that leaves meaning implied is made explicit in English. | ☐ PASS ☐ FAIL | |
| F2 🔴 | **English → Arabic: cultural embedding is present** | English content is not just translated word-for-word; it is culturally embedded for the MENA audience. | ☐ PASS ☐ FAIL | |
| F3 🟡 | **Arabic → English: hierarchical tone is adapted** | Deferential Arabic framing is reduced to direct English where appropriate; preserved where culturally necessary. | ☐ PASS ☐ FAIL | |
| F4 🟡 | **English → Arabic: register is elevated or lowered correctly** | English formal content becomes MSA; English informal content becomes colloquial. No mismatch. | ☐ PASS ☐ FAIL | |
| F5 🟢 | **Direction-specific strategy is followed** | The translation follows the bidirectional strategy notes from Phase 4 of the skill process. | ☐ PASS ☐ FAIL | |

---

## Section G: Formatting & Structure (Important)

| # | Checkpoint | Criteria | Result | Notes |
|---|-----------|----------|--------|-------|
| G1 🔴 | **Code blocks are separate from Arabic text** | Code snippets, JSON, and CLI commands are in fenced blocks, not inline with Arabic text. | ☐ PASS ☐ FAIL | |
| G2 🟡 | **Headers and structure are preserved** | Document structure (H1, H2, H3, bullet points, tables) is preserved or improved for target language readability. | ☐ PASS ☐ FAIL | |
| G3 🟡 | **Tables and lists are formatted correctly** | RTL tables (Arabic) have correct alignment; LTR tables (English) are standard. | ☐ PASS ☐ FAIL | |
| G4 🟢 | **Links and references are functional** | Any hyperlinks, citations, or cross-references work in the translated version. | ☐ PASS ☐ FAIL | |
| G5 🟢 | **File naming and metadata are correct** | Output files are named correctly and include appropriate metadata (language, date, version). | ☐ PASS ☐ FAIL | |

---

## Section H: Anti-Pattern Check (Critical)

| # | Checkpoint | Criteria | Result | Notes |
|---|-----------|----------|--------|-------|
| H1 🔴 | **No literal translation without cultural context** | Technical terms are chosen based on audience and market, not dictionary definitions. | ☐ PASS ☐ FAIL | |
| H2 🔴 | **No register confusion** | Document does not mix formal and colloquial unintentionally. | ☐ PASS ☐ FAIL | |
| H3 🔴 | **No machine translation without review** | Technical terms were verified against the glossary, not blindly accepted from MT. | ☐ PASS ☐ FAIL | |
| H4 🔴 | **No "Arabic is one dialect" assumption** | Content specifies or defaults to the appropriate dialect/register for the target market. | ☐ PASS ☐ FAIL | |
| H5 🔴 | **No RTL/layout issues** | Arabic content is RTL-aware; code blocks are not broken by bidirectional text. | ☐ PASS ☐ FAIL | |
| H6 🟡 | **No forced translation of English terms** | English terms that are standard in MENA (API, JSON, cloud) are kept, not awkwardly translated. | ☐ PASS ☐ FAIL | |
| H7 🟡 | **No bidirectional strategy omission** | Arabic → English and English → Arabic were handled with their respective strategies. | ☐ PASS ☐ FAIL | |
| H8 🟡 | **No MENA market homogenization** | Content is adapted to specific market (Saudi/UAE/Egypt/etc.), not generic "Arabic." | ☐ PASS ☐ FAIL | |

---

## Final Review Summary

| Category | Total Checkpoints | Critical (🔴) | Important (🟡) | Best Practice (🟢) | Passed | Failed |
|----------|------------------|--------------|--------------|-------------------|--------|--------|
| A: Register & Tone | 5 | 2 | 2 | 1 | | |
| B: Technical Accuracy | 8 | 5 | 2 | 1 | | |
| C: Cultural Adaptation | 6 | 2 | 3 | 1 | | |
| D: Arabic Language Quality | 6 | 2 | 2 | 2 | | |
| E: English Language Quality | 5 | 2 | 2 | 1 | | |
| F: Bidirectional Quality | 5 | 2 | 2 | 1 | | |
| G: Formatting & Structure | 5 | 1 | 2 | 2 | | |
| H: Anti-Pattern Check | 8 | 5 | 3 | 0 | | |
| **TOTAL** | **48** | **21** | **18** | **9** | | |

---

## Pass/Fail Decision

| Criterion | Threshold | Result |
|-----------|-----------|--------|
| All critical (🔴) items pass | 0 failures | ☐ YES ☐ NO |
| Important (🟡) items: ≤ 2 failures | ≤ 2 failures | ☐ YES ☐ NO |
| Best-practice (🟢) items: ≤ 3 failures | ≤ 3 failures | ☐ YES ☐ NO |

**FINAL DECISION:** ☐ **APPROVED FOR DELIVERY** ☐ **REQUIRES REVISION**

**If REQUIRES REVISION:**
- List failed items: _________________________________
- Required changes: _________________________________
- Re-review date: _________________________________

---

## Reviewer Information

| Field | Value |
|-------|-------|
| Reviewer Role | |
| Review Date | |
| Source Language | |
| Target Language | |
| Target Market | |
| Document Type | |
| Skill Version | `multi-001-e8f3c5` |

**Reviewer Signature/ID:** _________________________________

---

*This checklist is part of the `arabic-technical-translator` skill (`multi-001-e8f3c5`). It is designed to enforce the quality and cultural authenticity standards that distinguish community-governed open-source skills from generic translation tools.*
