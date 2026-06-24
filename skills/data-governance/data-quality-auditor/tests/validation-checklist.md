# Data Quality Audit Validation Checklist

> **Purpose:** This checklist is used by reviewers to validate that a data quality audit was conducted correctly and completely according to the `data-quality-auditor` skill. Each item must be checked before an audit is considered valid.
>
> **Usage:** Reviewers should work through this checklist in order. Any item marked **FAIL** requires remediation and re-review before the audit can be signed off.
>
> **Version:** 1.0.0 | **Aligned with:** DAMA-DMBOK Second Edition, Chapter 13

---

## Checklist Instructions

For each item, mark one of:
- **PASS** — The requirement is fully met with evidence
- **PARTIAL** — The requirement is partially met; document gaps
- **FAIL** — The requirement is not met; must be remediated
- **N/A** — The requirement does not apply to this specific audit (document why)

---

## Section 1: Scope Definition (Phase 1)

| # | Checklist Item | Criteria | Result | Notes |
|---|---------------|----------|--------|-------|
| 1.1 | Dataset boundary is documented | The audit document clearly states which tables, fields, records, time periods, and systems are included and excluded | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 1.2 | Business owner is identified | A named business owner with authority over the dataset is documented | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 1.3 | Technical owner is identified | A named technical owner with access to the dataset and pipeline is documented | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 1.4 | Intended use cases are documented | At least one business use case for the data is described; the use case determines dimension relevance | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 1.5 | Dimensions are selected with rationale | Not all 6 DAMA-DMBOK dimensions are selected by default; each selected dimension has a documented rationale | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 1.6 | Severity thresholds are defined before scoring | Thresholds (Critical/Warning/Acceptable/Good/Excellent) are documented with score ranges before any measurement occurs | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 1.7 | Thresholds are not all 100% | At least one threshold acknowledges that 100% is not the goal; economic rationality is demonstrated | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 1.8 | Stakeholders are identified with roles | A stakeholder list includes names, roles, and responsibilities | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |

**Section 1 Result:** ☐ PASS ☐ PARTIAL ☐ FAIL

---

## Section 2: Baseline Assessment (Phase 2)

| # | Checklist Item | Criteria | Result | Notes |
|---|---------------|----------|--------|-------|
| 2.1 | Measurement methods are documented | For each dimension, the specific measurement method (from `references/dama-dmbok-dimensions.md`) is named and described | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 2.2 | Sample sizes are documented | Where sampling is used, the sample size is stated and justified as statistically appropriate | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 2.3 | Scores are reproducible | Another auditor with the same data and method should arrive at the same score; methodology is specific enough to replicate | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 2.4 | Evidence is captured | At least 3-5 representative examples of each failure type are documented (anonymized if necessary) | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 2.5 | Scores use the 0-100 scale | All dimension scores are numeric values between 0 and 100, not vague labels ("good", "bad") | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 2.6 | Severity is assigned per dimension | Each scored dimension is assigned a severity level based on the pre-defined thresholds | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 2.7 | Business impact is stated for each dimension | Every score below "Excellent" includes a sentence explaining the business impact of the quality gap | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 2.8 | The scorecard template is used or referenced | The audit either uses `references/quality-scorecard-template.md` directly or explains why a modified format is needed | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 2.9 | No dimension is scored without measurement | Every score is backed by a documented test, query, or sample; no "gut feel" scores | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 2.10 | System of record is identified for accuracy | The accuracy assessment names the specific system or reference used for comparison | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |

**Section 2 Result:** ☐ PASS ☐ PARTIAL ☐ FAIL

---

## Section 3: Root Cause Analysis (Phase 3)

| # | Checklist Item | Criteria | Result | Notes |
|---|---------------|----------|--------|-------|
| 3.1 | Every below-threshold dimension has root cause analysis | If a dimension scored Warning or Critical, there is a corresponding root cause entry | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 3.2 | Root causes are classified | Each root cause is classified using the standard taxonomy: Source System, Pipeline/ETL, Business Rule, Human Process, External, Temporal | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 3.3 | Data lineage is traced or documented as a gap | For each root cause, the audit either traces lineage to the source or explicitly documents "lineage gap — cannot trace further" | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 3.4 | The lineage mapping guide is used or referenced | The audit either follows `references/lineage-mapping-guide.md` or explains why an alternative approach was needed | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 3.5 | Point of degradation is identified | For each issue, the specific stage, system, or process where quality first degraded is named | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 3.6 | Scope of impact is quantified | The number of affected records, percentage of dataset, or business process impact is estimated | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 3.7 | Root causes are prioritized by business impact | Issues are ranked by a combination of records affected, downstream impact, and cost of inaction | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 3.8 | No root cause is "the data is bad" | Root causes are specific and actionable; vague explanations like "data quality is poor" are rejected | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 3.9 | Human process causes are considered | The audit does not assume all issues are technical; manual entry, approval, and communication gaps are investigated | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 3.10 | Temporal causes are checked | The audit verifies whether the issue is recent (suggesting a change) or long-standing (suggesting a systemic gap) | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |

**Section 3 Result:** ☐ PASS ☐ PARTIAL ☐ FAIL

---

## Section 4: Remediation Roadmap (Phase 4)

| # | Checklist Item | Criteria | Result | Notes |
|---|---------------|----------|--------|-------|
| 4.1 | Remediation actions are specific | Each action describes exactly what will be done, not just "improve data quality" | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 4.2 | Each action has an owner | A named individual or team is responsible for each action | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 4.3 | Effort is estimated | Each action has an effort estimate (S/M/L, hours, or story points) | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 4.4 | Dependencies are documented | Actions that must happen before others are explicitly noted | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 4.5 | Milestones are time-bound | The roadmap includes specific dates (e.g., Day 30, Day 60, Day 90) or calendar dates | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 4.6 | Prioritization is justified | P1/P2/P3 or equivalent ranking is explained by business impact, not just ease of implementation | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 4.7 | No action is assigned to "the team" | Every owner is a specific person or named role, not a vague group | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 4.8 | Roadmap includes both quick wins and structural fixes | At least one action can be completed in <7 days; at least one addresses systemic root causes | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 4.9 | Roadmap is signed off by stakeholders | Business owner and technical owner have reviewed and approved the roadmap | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 4.10 | Acceptance criteria are defined for major actions | For P1 actions, there is a clear definition of "done" | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |

**Section 4 Result:** ☐ PASS ☐ PARTIAL ☐ FAIL

---

## Section 5: Continuous Monitoring (Phase 5)

| # | Checklist Item | Criteria | Result | Notes |
|---|---------------|----------|--------|-------|
| 5.1 | KPIs are selected and defined | 3-5 monitoring KPIs are chosen with clear definitions | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 5.2 | Alert thresholds are defined | Each KPI has a warning threshold and a critical threshold | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 5.3 | Ownership is assigned | A specific person or team is responsible for monitoring each KPI | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 5.4 | Alert routing is documented | It is clear who receives alerts and how (email, Slack, PagerDuty, etc.) | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 5.5 | Re-audit schedule is defined | A cadence for full re-audit is recommended (e.g., quarterly, bi-annually) | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 5.6 | Monitoring is feasible with current resources | The monitoring plan does not require tools or headcount that are not available | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 5.7 | Dashboard or reporting mechanism is specified | There is a named tool, report, or process for reviewing KPIs | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |

**Section 5 Result:** ☐ PASS ☐ PARTIAL ☐ FAIL

---

## Section 6: Anti-Patterns & Scope Honesty

| # | Checklist Item | Criteria | Result | Notes |
|---|---------------|----------|--------|-------|
| 6.1 | Anti-pattern 1 is avoided (100% as goal) | The audit does not state or imply that 100% quality is the goal for all dimensions | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 6.2 | Anti-pattern 2 is avoided (no business context) | Every score and finding includes a business impact statement | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 6.3 | Anti-pattern 3 is avoided (ignore lineage) | The audit traces lineage or explicitly documents lineage gaps | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 6.4 | Anti-pattern 4 is avoided (measure once) | The audit includes a continuous monitoring plan (Phase 5) | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 6.5 | Anti-pattern 5 is avoided (confuse quality with privacy) | The audit does not substitute data quality assessment for privacy compliance | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 6.6 | Anti-pattern 6 is avoided (skip roadmap) | A formal remediation roadmap (Phase 4) exists with prioritized actions | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 6.7 | Scope boundaries are documented | The audit clearly states what it does NOT cover (privacy, technical fixes, certified audits) | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 6.8 | No certified audit claims | The audit does not claim to be a certified, regulatory, or third-party audit | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |

**Section 6 Result:** ☐ PASS ☐ PARTIAL ☐ FAIL

---

## Section 7: Documentation & Completeness

| # | Checklist Item | Criteria | Result | Notes |
|---|---------------|----------|--------|-------|
| 7.1 | All 5 phases are present | The audit includes Scope, Assessment, Root Cause, Roadmap, and Monitoring | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 7.2 | Artifacts are named and linked | Each phase output is named (e.g., `01-scope-definition.md`) and referenced | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 7.3 | Evidence is preserved | Sample records, test queries, and supporting data are stored and referenced (anonymized if needed) | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 7.4 | Executive summary is included | A 1-2 paragraph summary for non-technical stakeholders is present | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 7.5 | DAMA-DMBOK alignment is explicit | The audit references DAMA-DMBOK dimensions and principles; does not invent competing definitions | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 7.6 | Date and version are recorded | The audit document includes the date conducted and version number | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 7.7 | Sign-off section is present | Business owner and technical owner sign-off sections exist, even if not yet signed | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |
| 7.8 | No fabricated data | All scores, percentages, and findings are derived from actual measurement; no placeholders or hypothetical values | ☐ PASS ☐ PARTIAL ☐ FAIL ☐ N/A | |

**Section 7 Result:** ☐ PASS ☐ PARTIAL ☐ FAIL

---

## Overall Validation

| Section | Result | Items Checked | Items Passed | Items Failed | Items N/A |
|---------|--------|---------------|--------------|--------------|-----------|
| 1. Scope Definition | | 8 | | | |
| 2. Baseline Assessment | | 10 | | | |
| 3. Root Cause Analysis | | 10 | | | |
| 4. Remediation Roadmap | | 10 | | | |
| 5. Continuous Monitoring | | 7 | | | |
| 6. Anti-Patterns & Scope | | 8 | | | |
| 7. Documentation & Completeness | | 8 | | | |
| **TOTAL** | | **61** | | | |

### Final Determination

| Criteria | Threshold | Actual | Result |
|----------|-----------|--------|--------|
| All sections must be PASS or PARTIAL | No FAIL sections | | ☐ MET ☐ NOT MET |
| At least 50 of 61 items must be PASS | 50/61 | | ☐ MET ☐ NOT MET |
| No critical item (marked with *) may be FAIL | 0 critical FAILs | | ☐ MET ☐ NOT MET |

**Overall Result:** ☐ **CERTIFIED** — Audit meets all quality standards  
☐ **CONDITIONAL** — Minor gaps; address PARTIAL items within 14 days  
☐ **REJECTED** — Significant gaps; remediate FAIL items and re-submit

---

## Reviewer Sign-Off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| **Reviewer** | | | |
| **Data Governance Lead** | | | |

---

> **Checklist Version:** 1.0.0 | **Aligned with:** DAMA-DMBOK Second Edition, Chapter 13 | **License:** MIT
> 
> **Critical Items:** Items 1.6 (thresholds defined before scoring), 2.3 (reproducible scores), 3.5 (point of degradation identified), 4.2 (actions have owners), and 6.8 (no certified audit claims) are critical. A FAIL on any critical item results in automatic REJECTED status regardless of overall score.
