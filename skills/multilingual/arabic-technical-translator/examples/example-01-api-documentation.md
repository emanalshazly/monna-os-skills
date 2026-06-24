# Example 01: English API Documentation → Arabic for Egyptian Developers

> **Direction:** English → Arabic (Egyptian Colloquial + Code-Switching)
> **Target Audience:** Egyptian developers (backend, full-stack, DevOps)
> **Register:** Egyptian Colloquial with heavy code-switching
> **Market:** Egypt, but applicable to any MENA developer community
> **Skill Phase Demonstrated:** All 6 phases (Source Analysis, Terminology Mapping, Cultural Adaptation, Draft, Review, Validation)

---

## Source Analysis & Register Detection (Phase 1)

**Document Type:** REST API documentation (authentication and user endpoints)
**Technical Domain:** Web development, APIs, authentication
**Target Audience:** Egyptian developers integrating a third-party API
**Target Market:** Egypt (primary), pan-MENA developer community (secondary)
**Register Decision:** Egyptian Colloquial — this is developer-facing documentation. Egyptian developers expect colloquial Arabic with heavy code-switching. Using MSA would feel distant and academic.

**Cultural Adaptation Notes:**
- Replace Western examples with MENA-relevant ones (e.g., local payment gateways if applicable)
- Keep code snippets in English — they are universal and must not be translated
- Use Egyptian pricing context if pricing is mentioned (EGP)

---

## Terminology Mapping (Phase 2)

| Source Term | Arabic Term | Decision Rationale |
|-------------|-------------|-------------------|
| API | الـ API | Universal in MENA tech; full Arabic "واجهة برمجة التطبيقات" is too long for colloquial |
| Authentication | الـ authentication / المصادقة | "الـ authentication" in colloquial body; "المصادقة" in formal headers if needed |
| API Key | الـ API key | Kept in English; universal term |
| Authorization header | الـ Authorization header | Kept in English; HTTP header names are standard |
| JSON | JSON | Kept in English; data format name |
| Endpoint | الـ endpoint | "الـ endpoint" dominates in Egyptian dev contexts |
| Request | الـ request | "الـ request" common; "الطلب" in formal |
| Response | الـ response | "الـ response" common; "الاستجابة" in formal |
| Parameter | الـ parameter / المعامل | "الـ parameter" in code context; "المعامل" if explaining |
| Status code | الـ status code | "الـ status code" standard; HTTP codes are universal |
| Error | الـ error / error | "الـ error" or just "error" in code context |
| User data | بيانات الـ user | "بيانات الـ user" — code-switched naturally |
| Base URL | الـ base URL | "الـ base URL" standard |
| Token | الـ token | "الـ token" standard in auth contexts |
| Bearer token | الـ Bearer token | Kept in English; HTTP standard |
| Base64 | Base64 | Kept in English; encoding standard |
| cURL | cURL | Kept in English; tool name |

---

## Cultural Adaptation (Phase 3)

**No major cultural adaptations needed** for this technical documentation — API docs are culturally neutral by nature. However:
- Ensure any pricing references use EGP for Egyptian context
- If referencing a payment gateway example, use Fawry or Paymob instead of Stripe (though Stripe is also known)
- Keep the tone direct and practical — Egyptian developers value "get to the point" content

---

## Draft Translation (Phase 4)

### Original English Source

```markdown
# Authentication

All API requests must include an API key in the Authorization header. 
The API key is a Base64-encoded string generated in your dashboard.

## Example Request

```bash
curl -X GET "https://api.example.com/v1/users" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Response Format

All responses are returned in JSON format. A successful response returns 
HTTP status code 200 with the following structure:

```json
{
  "status": "success",
  "data": {
    "user_id": 12345,
    "email": "user@example.com",
    "plan": "premium"
  }
}
```

## Error Handling

If the API key is invalid or missing, the API returns HTTP status code 401 
with an error message:

```json
{
  "status": "error",
  "message": "Invalid or missing API key"
}
```
```

---

### Arabic Translation (Egyptian Colloquial)

```markdown
# الـ Authentication

كل الـ requests اللي هتبعتها للـ API لازم تكون فيها الـ API key في الـ Authorization header.
الـ API key دي عبارة عن Base64-encoded string بتعملها من الـ dashboard بتاعتك.

## مثال على الـ Request

```bash
curl -X GET "https://api.example.com/v1/users" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## شكل الـ Response

كل الـ responses بترجع بصيغة JSON. لو الـ request نجح، الـ API بيرجع 
HTTP status code 200 مع البيانات دي:

```json
{
  "status": "success",
  "data": {
    "user_id": 12345,
    "email": "user@example.com",
    "plan": "premium"
  }
}
```

## إزاي تتعامل مع الـ Errors

لو الـ API key غلط أو مش موجودة، الـ API بيرجع 
HTTP status code 401 مع الـ error message دي:

```json
{
  "status": "error",
  "message": "Invalid or missing API key"
}
```
```

---

### Arabic Translation Breakdown (showing code-switching patterns)

| Arabic Phrase | Transliteration | English Equivalent | Pattern |
|---------------|------------------|--------------------|---------|
| كل الـ requests | kol el-requests | All requests | Definite article + English noun |
| اللي هتبعتها |elli hatb3atha | that you will send | Egyptian relative pronoun + Egyptian verb conjugation |
| لازم تكون فيها | lazm tkun fiha | must be in it | Egyptian modal + Egyptian verb |
| عبارة عن | 3ibara 3an | consisting of / is | Egyptian connector phrase |
| بتعملها | bt3mlha | you make it | Egyptian present verb + object suffix |
| من الـ dashboard | men el-dashboard | from the dashboard | Preposition + definite article + English noun |
| بتاعتك | bta3tak | yours (feminine) | Egyptian possessive suffix |
| لو الـ request نجح | law el-request naga7 | if the request succeeds | Egyptian conditional + English noun + Arabic verb |
| بيرجع | byerga3 | returns | Egyptian present verb |
| مع البيانات دي | ma3 el-bayanat di | with this data | Egyptian demonstrative + Arabic noun |
| إزاي تتعامل مع | ezzay tet3amel ma3 | how to deal with | Egyptian question word + reflexive verb + preposition |
| غلط أو مش موجودة | ghalat aw mish mawguda | wrong or not present | Egyptian adjective + negation + Egyptian adjective |

---

## Technical Accuracy Review (Phase 5)

### Back-Translation Check

| Arabic Section | Back-Translation to English | Matches Source? | Notes |
|----------------|----------------------------|-----------------|-------|
| "كل الـ requests اللي هتبعتها للـ API لازم تكون فيها الـ API key في الـ Authorization header" | "All requests that you send to the API must have the API key in the Authorization header" | ✅ Yes | Meaning preserved; register shifted to colloquial |
| "الـ API key دي عبارة عن Base64-encoded string بتعملها من الـ dashboard بتاعتك" | "The API key is a Base64-encoded string that you generate from your dashboard" | ✅ Yes | "generate" = "بتعملها" (you make it) — acceptable in colloquial |
| "لو الـ request نجح، الـ API بيرجع HTTP status code 200 مع البيانات دي" | "If the request succeeds, the API returns HTTP status code 200 with this data" | ✅ Yes | "data" pluralized as "البيانات" — correct |
| "لو الـ API key غلط أو مش موجودة، الـ API بيرجع HTTP status code 401 مع الـ error message دي" | "If the API key is wrong or not present, the API returns HTTP status code 401 with this error message" | ✅ Yes | Meaning preserved |

### Code Block Verification

| Code Block | Translated? | Correct? |
|-----------|-------------|----------|
| cURL command | ❌ No — kept as-is | ✅ Yes — must never translate code |
| JSON response example | ❌ No — kept as-is | ✅ Yes — must never translate code |
| HTTP headers | ❌ No — kept as-is | ✅ Yes — standard names |
| Error message | ❌ No — kept as-is | ✅ Yes — actual API response |

### Critical Check: Was anything translated that shouldn't be?
- ❌ `Authorization` header name → Kept in English ✅
- ❌ `Bearer` → Kept in English ✅
- ❌ `status` / `data` / `user_id` / `email` / `plan` JSON keys → Kept in English ✅
- ❌ `success` / `error` / `message` JSON values → Kept in English ✅
- ❌ API endpoint URL → Kept in English ✅

**Result: All technical elements preserved. No code was translated. Register appropriate for Egyptian developers.**

---

## Localization Validation (Phase 6)

### Readability Check
- [x] Sentences flow naturally in Egyptian colloquial
- [x] No awkward literal translations detected
- [x] Code-switching feels natural, not forced
- [x] Technical terms consistently handled
- [x] Code blocks properly separated from Arabic text (RTL considerations)

### Cultural Fit Check
- [x] Tone is direct and practical — matches Egyptian developer expectations
- [x] No culturally inappropriate content
- [x] Examples are universal (no Western-specific references to adapt)
- [x] Content feels like it was written for Egyptian developers, not translated at them

### RTL Formatting Check
- [x] Code blocks are in separate fenced blocks (not inline with Arabic text)
- [x] No bidirectional text issues expected — English code blocks are isolated
- [x] Arabic punctuation used (e.g., "؟" for questions, though not used here)
- [x] Mixed Arabic-English content is structured to avoid rendering issues

**Final Validation: PASS**

---

## Key Takeaways from This Example

1. **Code blocks are sacred.** Never translate code, JSON keys, API endpoints, or CLI commands. They are universal and must remain identical across languages.

2. **Code-switching is natural.** "الـ API" and "الـ Authorization header" are not mistakes — they are how Egyptian developers think and communicate. Forcing full Arabic equivalents creates distance, not clarity.

3. **Egyptian grammar is different from MSA.** "الـ requests اللي هتبعتها" (the requests that you will send) uses Egyptian relative pronouns (اللي) and verb conjugations (هتبعتها), not MSA (التي سترسلها). This is correct, not a mistake.

4. **Short, direct sentences work best.** Egyptian colloquial thrives on brevity. "لو الـ API key غلط" (if the API key is wrong) is more natural than "في حالة كانت مفتاح واجهة برمجة التطبيقات غير صحيح" (in the case that the API key is incorrect).

5. **The "Egyptian developer" persona:** This content is for someone who reads English documentation daily but prefers Arabic explanations because they process faster in their native language. They are not looking for a dictionary translation — they are looking for a colleague explaining it to them in a Slack message.

---

*This example demonstrates the full 6-phase workflow for translating English technical documentation into Egyptian Arabic. The result is not a literal translation — it is a cultural and technical reconstruction for the target audience.*
