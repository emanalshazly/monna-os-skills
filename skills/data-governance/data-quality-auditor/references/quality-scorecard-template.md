# Data Quality Scorecard Template

> **Purpose:** A reusable template for scoring data quality across DAMA-DMBOK dimensions. Copy this template for each audit and fill in the scored values.
> 
> **Usage:** Complete one scorecard per dataset. If auditing multiple datasets, create one scorecard per dataset. Do not aggregate across datasets.

---

## Scorecard Header

| Field | Value |
|-------|-------|
| **Dataset Name** | |
| **Dataset Description** | |
| **Audit Date** | |
| **Auditor Name** | |
| **Business Owner** | |
| **Technical Owner** | |
| **Intended Use Cases** | |
| **System of Record** | |
| **Data Freshness (as of audit)** | |

---

## Severity Threshold Definitions

Define these thresholds at the start of the audit, before any scoring. Do not adjust thresholds after scoring.

| Severity | Score Range | Meaning | Required Action |
|----------|-------------|---------|---------------|
| **Critical** | 0-49 | Data is not fit for purpose. Do not use for intended use cases. | Immediate remediation required. Halt dependent processes if necessary. |
| **Warning** | 50-74 | Data has significant quality issues. Use with caution and documented limitations. | Root cause analysis and remediation roadmap required. |
| **Acceptable** | 75-89 | Data has minor quality issues. Suitable for most use cases with awareness of limitations. | Monitor and address issues in next maintenance cycle. |
| **Good** | 90-97 | Data has negligible quality issues. Suitable for all intended use cases. | Continue current practices. |
| **Excellent** | 98-100 | Data meets or exceeds all quality requirements. | Maintain and benchmark against this standard. |

---

## Dimension Scoring Table

### Dimension 1: Accuracy

| Field | Entry |
|-------|-------|
| **Score (0-100)** | |
| **Measurement Method** | ☐ System of Record Comparison ☐ Physical Verification ☐ External Reference Match ☐ Business Rule Validation ☐ Expert Review |
| **Sample Size** | |
| **Error Count** | |
| **Error Rate (%)** | |
| **System of Record Used** | |
| **Key Finding** | |
| **Business Impact** | |
| **Severity** | ☐ Critical ☐ Warning ☐ Acceptable ☐ Good ☐ Excellent |
| **Evidence Link** | |

---

### Dimension 2: Completeness

| Field | Entry |
|-------|-------|
| **Score (0-100)** | |
| **Measurement Method** | ☐ Required Field Null Check ☐ Schema Coverage Analysis ☐ Record-Level Completeness ☐ Conditional Completeness ☐ Temporal Completeness |
| **Required Fields Defined** | |
| **Total Records** | |
| **Fully Complete Records** | |
| **Completeness Rate (%)** | |
| **Key Finding** | |
| **Business Impact** | |
| **Severity** | ☐ Critical ☐ Warning ☐ Acceptable ☐ Good ☐ Excellent |
| **Evidence Link** | |

---

### Dimension 3: Consistency

| Field | Entry |
|-------|-------|
| **Score (0-100)** | |
| **Measurement Method** | ☐ Cross-System Comparison ☐ Reference Data Alignment ☐ Temporal Stability Check ☐ Format Standardization Check ☐ Semantic Equivalence Test |
| **Systems Compared** | |
| **Mismatched Records** | |
| **Consistency Rate (%)** | |
| **Key Finding** | |
| **Business Impact** | |
| **Severity** | ☐ Critical ☐ Warning ☐ Acceptable ☐ Good ☐ Excellent |
| **Evidence Link** | |

---

### Dimension 4: Timeliness

| Field | Entry |
|-------|-------|
| **Score (0-100)** | |
| **Measurement Method** | ☐ Latency Measurement ☐ Currency Check ☐ SLA Compliance ☐ End-to-End Pipeline Timing ☐ Business Process Alignment |
| **Latency Requirement** | |
| **Actual Latency (avg/max)** | |
| **SLA Compliance Rate (%)** | |
| **Key Finding** | |
| **Business Impact** | |
| **Severity** | ☐ Critical ☐ Warning ☐ Acceptable ☐ Good ☐ Excellent |
| **Evidence Link** | |

---

### Dimension 5: Validity

| Field | Entry |
|-------|-------|
| **Score (0-100)** | |
| **Measurement Method** | ☐ Syntax Validation ☐ Range Validation ☐ Enumeration Check ☐ Cross-Field Validation ☐ Format Validation ☐ Referential Integrity |
| **Validation Rules Tested** | |
| **Total Records** | |
| **Valid Records** | |
| **Validity Rate (%)** | |
| **Key Finding** | |
| **Business Impact** | |
| **Severity** | ☐ Critical ☐ Warning ☐ Acceptable ☐ Good ☐ Excellent |
| **Evidence Link** | |

---

### Dimension 6: Uniqueness

| Field | Entry |
|-------|-------|
| **Score (0-100)** | |
| **Measurement Method** | ☐ Exact Duplicate Detection ☐ Fuzzy Duplicate Detection ☐ Key-Based Uniqueness ☐ Business Entity Resolution ☐ Golden Record Analysis |
| **Unique Entity Count** | |
| **Total Record Count** | |
| **Duplication Rate (%)** | |
| **Key Finding** | |
| **Business Impact** | |
| **Severity** | ☐ Critical ☐ Warning ☐ Acceptable ☐ Good ☐ Excellent |
| **Evidence Link** | |

---

## Overall Assessment

### Summary Dashboard

| Dimension | Score | Severity | Trend* |
|-----------|-------|----------|--------|
| Accuracy | | | ☐ Improving ☐ Stable ☐ Declining ☐ N/A |
| Completeness | | | ☐ Improving ☐ Stable ☐ Declining ☐ N/A |
| Consistency | | | ☐ Improving ☐ Stable ☐ Declining ☐ N/A |
| Timeliness | | | ☐ Improving ☐ Stable ☐ Declining ☐ N/A |
| Validity | | | ☐ Improving ☐ Stable ☐ Declining ☐ N/A |
| Uniqueness | | | ☐ Improving ☐ Stable ☐ Declining ☐ N/A |
| **Weighted Average** | | | |

\* *Trend requires comparison to a previous audit scorecard. If this is the first audit, mark N/A.*

### Weighting Guidance

If you choose to calculate a weighted average, define weights explicitly and document the rationale. Do not default to equal weighting.

| Use Case | Recommended Weighting | Rationale |
|----------|----------------------|-----------|
| **Financial Reporting** | Accuracy 30%, Completeness 25%, Consistency 20%, Validity 15%, Timeliness 5%, Uniqueness 5% | Accuracy and completeness are paramount for financial trust |
| **Real-Time Operations** | Timeliness 30%, Accuracy 25%, Validity 20%, Consistency 15%, Completeness 5%, Uniqueness 5% | Latency is critical for operational decisions |
| **Customer Analytics** | Uniqueness 25%, Accuracy 25%, Completeness 20%, Consistency 15%, Validity 10%, Timeliness 5% | Duplicate customers and incorrect profiles drive bad analytics |
| **IoT/DePIN Monitoring** | Timeliness 30%, Validity 25%, Accuracy 20%, Consistency 15%, Completeness 5%, Uniqueness 5% | Sensor data must arrive on time and be structurally valid |

### Key Findings Summary

| # | Finding | Dimension | Severity | Business Impact | Recommended Action |
|---|---------|-----------|----------|-----------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

### Executive Summary (1-2 paragraphs)

*Write a concise summary for non-technical stakeholders. Include the overall score range, the most critical finding, and the highest-priority recommended action.*

---

## Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Auditor** | | | |
| **Business Owner** | | | |
| **Technical Owner** | | | |
| **Data Governance Lead** | | | |

---

> **Template Version:** 1.0.0 | **Aligned with:** DAMA-DMBOK Second Edition, Chapter 13 | **License:** MIT
