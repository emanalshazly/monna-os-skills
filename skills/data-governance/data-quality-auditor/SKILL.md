# Skill: Data Quality Auditor

---

**Name:** `data-quality-auditor`
**Domain:** Data Governance
**Quality Tier:** `certified`
**Fingerprint:** `data-001-b4e8d2`
**Compatibility:** Kimi/Daimon: certified, Claude: certified, Copilot: certified, Cursor: validated, OpenClaw: validated
**Last Tested:** 2026-06-24
**Author:** monna
**License:** MIT
**Home:** `skills/data-governance/data-quality-auditor/`

---

## Trigger Phrases

> Use this skill when the user says any of the following:

- "audit data quality dimensions"
- "DAMA-DMBOK data quality assessment"
- "data quality scorecard"
- "data lineage audit"
- "data stewardship review"
- "assess data quality of [dataset/system]"
- "evaluate completeness/accuracy/timeliness of our data"
- "data quality issues in [source/system]"
- "build a data quality framework"
- "run a data quality check"
- "data quality KPI dashboard"
- "trace data quality problems through lineage"
- "root cause analysis for bad data"
- "data quality remediation roadmap"

---

## When to Use

Use this skill when you need to **audit, assess, or improve data quality** for any structured dataset or data system. It is designed for:

- **Data stewards** and **analysts** who need a repeatable framework for evaluating data quality
- **Teams preparing for governance reviews** who need to document current state and remediation plans
- **Engineers** who need to understand *why* data quality matters before they implement fixes
- **Business stakeholders** who need to translate data quality issues into business impact
- **AI/ML practitioners** who need clean data for model training and inference
- **DePIN and infrastructure operators** who need to validate sensor, node, or telemetry data quality

The skill provides a **practical, evidence-based process** for scoring data quality across DAMA-DMBOK dimensions, identifying root causes, and building a remediation roadmap.

---

## When NOT to Use

> **Scope boundaries are mandatory.** This skill does NOT replace the following:

1. **Formal data governance audits by certified professionals** — This is a self-assessment and planning tool. It does not confer compliance certification, legal defensibility, or third-party audit readiness. If you need a certified audit (e.g., for regulatory filing or enterprise risk management), engage a licensed data governance consultant or certified DAMA professional.

2. **Technical data pipeline fixes** — This skill identifies *what* is wrong and *why* it matters. It does NOT write ETL code, implement data validation rules, or configure pipeline observability. The remediation roadmap it produces should be handed off to data engineering for implementation.

3. **Data privacy compliance (GDPR, CCPA, PII handling)** — Data quality and data privacy are adjacent but distinct domains. This skill does not assess legal compliance, consent management, right-to-deletion, or cross-border data transfer rules. Use a dedicated privacy/compliance skill for those needs.

4. **Production incident response** — If data quality issues are causing an active outage, revenue loss, or safety incident, follow your incident response playbook first. This skill is for *planned audits and continuous improvement*, not emergency firefighting.

5. **Unstructured data quality (images, audio, video)** — This skill is designed for **structured and semi-structured data** (tables, CSVs, JSON records, relational databases). Unstructured data quality (e.g., image labeling accuracy, audio transcription quality) requires different frameworks and is out of scope.

---

## Core Principles

These five principles are grounded in DAMA-DMBOK (Data Management Body of Knowledge) and govern every step of the audit process. They prevent the most common failure modes in data quality work.

### Principle 1: Accuracy Is Measured Against a System of Record

> *DAMA-DMBOK Reference:* Accuracy is defined as the degree to which data correctly describes the real-world object or event it represents.

You cannot assess accuracy without a **defined reference point**. This may be a source system, a physical measurement, a verified external dataset, or a business rule. "Looks right" is not a valid accuracy test. Always document:
- What is the system of record?
- How was the reference data validated?
- What is the acceptable tolerance or deviation threshold?

### Principle 2: Timeliness Is Relative to the Business Process

> *DAMA-DMBOK Reference:* Timeliness is the degree to which data is available when expected and needed for its intended use.

Data that is "too old" for real-time fraud detection may be perfectly timely for quarterly financial reporting. Timeliness must be defined **per use case**, not globally. Document the business process, the decision point, and the latency requirement.

### Principle 3: Completeness Must Be Defined Per Dataset, Not Globally

> *DAMA-DMBOK Reference:* Completeness is the degree to which all required data is present.

"100% complete" is meaningless without a schema definition. Completeness is measured against a **specific, agreed-upon set of required fields** for a specific dataset in a specific context. A customer record may be complete for marketing but incomplete for billing. Always define the required field set before measuring.

### Principle 4: Consistency Requires Context of What, Where, and When

> *DAMA-DMBOK Reference:* Consistency is the degree to which data is represented the same way across systems and over time.

Consistency is not about forcing all data to look identical. It is about ensuring that **semantic equivalence is preserved** across systems and time. If two systems store customer status as "Active" vs. "1", that is consistent *if* the mapping is documented and maintained. Inconsistency is only a problem when it causes ambiguity, duplication, or integration failure.

### Principle 5: Uniqueness and Validity Are Data-Dependent, Not Universal

> *DAMA-DMBOK Reference:* Uniqueness is the degree to which there is only one representation of an entity. Validity is the degree to which data conforms to defined syntax and business rules.

Uniqueness rules must account for legitimate duplicates (e.g., a customer with two accounts). Validity rules must be drawn from business rules, not arbitrary assumptions. A phone number is "valid" if it matches the business rule for your region, not because it matches every possible global format.

---

## Step-by-Step Process

The audit process follows five phases. Each phase produces a concrete artifact that feeds into the next phase. Do not skip phases. Do not combine phases.

### Phase 1: Scope Definition & Dimension Selection

**Goal:** Define exactly what you are auditing, why, and which DAMA-DMBOK dimensions apply.

**Inputs:**
- Dataset name and description
- Business owner and technical owner
- Known data quality complaints or incidents
- Intended use cases for this data

**Actions:**
1. **Document the dataset boundary** — Which tables, fields, time range, and records are included? What is excluded?
2. **Select relevant dimensions** — Not all 6 DAMA-DMBOK dimensions apply to every dataset. Use the reference: `references/dama-dmbok-dimensions.md`
3. **Define severity thresholds** — What score constitutes "Critical," "Warning," and "Acceptable" for each dimension? Document these before you measure.
4. **Identify stakeholders** — Who owns the data? Who consumes it? Who will act on the findings?
5. **Output:** `01-scope-definition.md` — A signed-off document with dataset boundary, selected dimensions, thresholds, and stakeholder list.

### Phase 2: Baseline Assessment

**Goal:** Measure the current state of each selected dimension and produce a quantitative scorecard.

**Inputs:**
- `01-scope-definition.md`
- Access to the dataset (read-only)
- Any existing data quality monitoring or logs

**Actions:**
1. **Execute dimension-specific tests** — For each selected dimension, run the measurement approach defined in `references/dama-dmbok-dimensions.md`
2. **Score each dimension** — Use the 0-100 scale in `references/quality-scorecard-template.md`
3. **Document methodology** — For each score, record the exact query, test, or sample used. Scores must be **reproducible**.
4. **Capture sample evidence** — Store 5-10 representative examples of each failure type (anonymized if necessary)
5. **Output:** `02-quality-scorecard.md` — Completed scorecard with scores, evidence, and methodology for each dimension.

### Phase 3: Root Cause Analysis

**Goal:** For each dimension scoring below threshold, determine *why* the data is low quality.

**Inputs:**
- `02-quality-scorecard.md`
- Data lineage documentation (or ability to trace sources)
- Interviews with data owners, engineers, and consumers

**Actions:**
1. **Map each issue to its source** — Use `references/lineage-mapping-guide.md` to trace upstream
2. **Classify root causes** — Use the standard taxonomy:
   - **Source System:** The data was wrong when it entered the pipeline
   - **Pipeline/ETL:** The data was corrupted during transformation, migration, or integration
   - **Business Rule:** The business rule is ambiguous, outdated, or inconsistently applied
   - **Human Process:** Manual entry, review, or approval errors
   - **External:** Third-party data feed issues, API changes, or vendor problems
   - **Temporal:** The data was correct at one time but has decayed
3. **Prioritize by business impact** — Rank root causes by the number of records affected, the severity of downstream impact, and the cost of inaction
4. **Output:** `03-root-cause-analysis.md` — Issue-by-issue mapping with root cause classification, business impact, and priority ranking.

### Phase 4: Remediation Roadmap

**Goal:** Produce a prioritized, time-bound plan to address each root cause.

**Inputs:**
- `03-root-cause-analysis.md`
- Stakeholder availability and engineering capacity
- Budget constraints

**Actions:**
1. **Define remediation actions** — For each root cause, specify the exact action, owner, and acceptance criteria
2. **Estimate effort and cost** — T-shirt size (S/M/L) or hours. Be honest about unknowns.
3. **Sequence by dependency** — Some fixes must happen before others (e.g., fix source system before building monitoring on top of it)
4. **Set milestones** — 30/60/90 day targets with check-in dates
5. **Output:** `04-remediation-roadmap.md` — Gantt-style or tabular roadmap with actions, owners, effort, dependencies, and milestones.

### Phase 5: Continuous Monitoring & KPI Dashboard

**Goal:** Ensure data quality does not regress after remediation. Build observability into the data lifecycle.

**Inputs:**
- `04-remediation-roadmap.md`
- Existing monitoring infrastructure (if any)

**Actions:**
1. **Select monitoring KPIs** — Choose 3-5 metrics that are proxy indicators for overall quality (e.g., % records passing all dimension thresholds, mean time to detect quality degradation, mean time to resolve)
2. **Define alerting thresholds** — When does a KPI trigger a warning? An escalation?
3. **Assign ownership** — Who monitors? Who responds to alerts? Who reviews the dashboard weekly?
4. **Schedule periodic re-audit** — Recommend quarterly or bi-annual full re-audit cadence
5. **Output:** `05-monitoring-dashboard.md` — KPI definitions, thresholds, alert routing, ownership, and re-audit schedule.

---

## Anti-Patterns

> The following patterns are common, destructive, and explicitly prohibited by this skill. If you recognize one in your current process, stop and correct it before proceeding.

### Anti-Pattern 1: Treat 100% Quality as the Goal

**Why it fails:** 100% data quality is often economically irrational. The cost of achieving the last 1% frequently exceeds the business value. DAMA-DMBOK explicitly frames data quality as a **risk-cost tradeoff**, not a perfection target.

**What to do instead:** Define "fit for purpose" thresholds per use case. Document the business case for each threshold. Accept that some datasets will operate at 85% quality because the cost of improvement exceeds the benefit.

### Anti-Pattern 2: Audit Dimensions Without Business Context

**Why it fails:** A dimension score without business context is noise. If you report "Completeness: 72%" without explaining that the missing 28% is in a non-critical field used only for analytics, stakeholders will panic and misallocate resources.

**What to do instead:** Every score must be accompanied by a business impact statement. "Completeness: 72%. Impact: Low. Missing fields are optional demographic data used only for segmentation; no operational or financial processes depend on them."

### Anti-Pattern 3: Ignore Data Lineage in Root Cause Analysis

**Why it fails:** If you only look at the final dataset, you will treat symptoms as causes. A customer record with invalid phone numbers may trace back to a third-party API that changed its format six months ago. Fixing the record locally is a waste of time.

**What to do instead:** Use `references/lineage-mapping-guide.md` to trace every quality issue to its origin. If you cannot trace lineage, document that as a gap and add "build lineage documentation" to the remediation roadmap.

### Anti-Pattern 4: Measure Once and Never Again

**Why it fails:** Data quality is dynamic. New sources, new code deployments, new business rules, and temporal decay all degrade quality over time. A single audit is a snapshot, not a safeguard.

**What to do instead:** Build continuous monitoring (Phase 5) from the start. Even if you only have manual checks, schedule them. The goal is to detect degradation before it becomes a crisis.

### Anti-Pattern 5: Confuse Data Quality with Data Privacy

**Why it fails:** PII data can be perfectly accurate, complete, and timely while still violating GDPR or CCPA. Conflating the two domains leads to compliance gaps and legal exposure.

**What to do instead:** Keep quality and privacy assessments separate. If privacy is a concern, run a parallel privacy assessment. Cross-reference findings where relevant (e.g., "Customer records are 100% complete, but 15% of phone numbers are collected without documented consent"), but do not substitute one for the other.

### Anti-Pattern 6: Skip the Remediation Roadmap and Jump to Fixes

**Why it fails:** Ad-hoc fixes without a roadmap create technical debt, misaligned priorities, and incomplete solutions. Teams fix what is easy instead of what is important.

**What to do instead:** Always produce a formal remediation roadmap (Phase 4) with prioritized actions, owners, and milestones. Get stakeholder sign-off before any engineering work begins.

---

## References

| File | Description |
|------|-------------|
| `references/dama-dmbok-dimensions.md` | Full mapping of DAMA-DMBOK data quality dimensions (Accuracy, Completeness, Consistency, Timeliness, Validity, Uniqueness) with definitions, measurement approaches, and scoring guidance |
| `references/quality-scorecard-template.md` | Reusable template for scoring data quality across dimensions. Includes 0-100 scale, severity thresholds, and evidence capture fields |
| `references/lineage-mapping-guide.md` | Step-by-step guide for tracing data quality issues through upstream systems, pipelines, and external sources |

---

## Examples

| File | Description |
|------|-------------|
| `examples/example-01-customer-crm.md` | Auditing customer data quality in a CRM system — covers Accuracy, Completeness, and Consistency across sales, marketing, and support touchpoints |
| `examples/example-02-iot-sensor.md` | Auditing IoT sensor data quality for a DePIN network — covers Timeliness, Validity, and Accuracy across distributed sensor nodes with intermittent connectivity |

---

## Tests

| File | Description |
|------|-------------|
| `tests/validation-checklist.md` | Reviewer checklist with pass/fail criteria for validating that a data quality audit was conducted correctly and completely |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-06-24 | Initial certified release |

---

## Contributing

This skill is part of the `monna-os-skills` open-source collection. Contributions must:
1. Maintain DAMA-DMBOK alignment
2. Pass the `tests/validation-checklist.md`
3. Not introduce overlap with commercial skills (fingerprint checked)
4. Include evidence-based examples, not theoretical speculation

---

> **Scope Honesty Note:** This skill is a self-assessment and planning framework. It does not replace certified data governance professionals, formal audits, or legal compliance review. Use it to build internal capability, identify gaps, and prepare for deeper engagement — not as a substitute for professional expertise.
