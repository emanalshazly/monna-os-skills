# DAMA-DMBOK Data Quality Dimensions Mapping

## Reference: DAMA International — DAMA-DMBOK Data Management Body of Knowledge (2nd Edition)

This document maps DAMA-DMBOK data quality dimensions to AI governance requirements. Data quality is not a separate concern from AI governance; it is a prerequisite for valid AI risk management.

---

## Why Data Quality Dimensions Matter for AI Governance

AI systems learn from data. If the data is flawed, the governance framework governing the AI system is governing a flawed system. DAMA-DMBOK defines data quality dimensions as measurable characteristics of data. Mapping these dimensions to AI governance ensures that data risks are treated before they become model risks.

**Key Insight:** NIST AI RMF and ISO 42001 both require data quality controls, but neither standard specifies *which* data quality dimensions to measure. DAMA-DMBOK fills this gap by providing a standardized, operationalizable framework.

---

## Dimension 1: Accuracy

### DAMA-DMBOK Definition

"The degree to which data correctly describes the 'real world' object or event being described." (DAMA-DMBOK 2nd Ed., Chapter 13)

### AI Governance Relevance

- **Training Data:** Inaccurate labels directly produce inaccurate models. A mislabeled medical image trains a diagnostic model to misdiagnose.
- **Inference Data:** Inaccurate input data at inference time produces unreliable outputs regardless of model quality.
- **Risk Manifestation:** Accuracy failures appear as systematic prediction errors, false positives/negatives, and degraded trustworthiness.

### Governance Mapping

| Standard | Requirement | How Accuracy Maps |
|----------|-------------|-----------------|
| NIST AI RMF | MEASURE 1.1: Appropriate methods and metrics are identified | Accuracy metrics (label correctness, sensor calibration) are required data quality metrics |
| EU AI Act | Art. 10(3): Data shall be "free of errors" | Accuracy is the operational definition of "free of errors" |
| ISO 42001 | Annex A.5.2: Data quality management | Accuracy is a primary data quality dimension to be managed |
| DAMA-DMBOK | DQ Dimension 1 | Foundation dimension for all downstream governance |

### Control Example

- **Technical:** Implement label verification protocols (e.g., double-annotation with adjudication for medical images).
- **Organizational:** Define accuracy thresholds per data type (e.g., "Label accuracy ≥ 95% for diagnostic training data").
- **Monitoring:** Track accuracy drift using ground-truth audits at defined intervals.

---

## Dimension 2: Completeness

### DAMA-DMBOK Definition

"The proportion of stored data against the potential of '100% complete'." (DAMA-DMBOK 2nd Ed., Chapter 13)

### AI Governance Relevance

- **Missing Data:** Incomplete training data can introduce sampling bias. If a demographic group is underrepresented, the model may perform poorly for that group.
- **Missing Features:** Incomplete feature sets reduce model capability and can shift decision boundaries unpredictably.
- **Risk Manifestation:** Completeness failures appear as coverage gaps, demographic bias, and reduced model generalizability.

### Governance Mapping

| Standard | Requirement | How Completeness Maps |
|----------|-------------|----------------------|
| NIST AI RMF | MAP 3.1: Impacts on individuals are identified | Completeness gaps in demographic data directly cause individual-level impacts |
| EU AI Act | Art. 10(3): Data shall be "complete" | Completeness is the operational definition of "complete" |
| ISO 42001 | Annex A.5.2: Data quality management | Completeness is a primary data quality dimension to be managed |
| DAMA-DMBOK | DQ Dimension 2 | Foundation dimension for coverage and representativeness |

### Control Example

- **Technical:** Implement completeness checks (e.g., "All required fields present in ≥ 99% of records").
- **Organizational:** Define representativeness requirements (e.g., "Training data matches population demographics within ± 5%").
- **Monitoring:** Track missing data rates and demographic coverage over time.

---

## Dimension 3: Consistency

### DAMA-DMBOK Definition

"The absence of difference when comparing two or more representations of a thing against a definition." (DAMA-DMBOK 2nd Ed., Chapter 13)

### AI Governance Relevance

- **Data Integration:** Inconsistent formats, units, or coding schemes across data sources create training data noise.
- **Temporal Consistency:** Data definitions that change over time (e.g., ICD code revisions) create hidden model drift.
- **Risk Manifestation:** Consistency failures appear as integration errors, temporal instability, and silent model degradation.

### Governance Mapping

| Standard | Requirement | How Consistency Maps |
|----------|-------------|----------------------|
| NIST AI RMF | MAP 4.1: AI risks and benefits are mapped to trustworthy characteristics | Consistency directly affects model reliability and validity |
| EU AI Act | Art. 10(3): Data shall be "complete" and meet quality criteria | Consistency is a quality criterion for integrated data sets |
| ISO 42001 | Annex A.5.2: Data quality management | Consistency is a primary data quality dimension to be managed |
| DAMA-DMBOK | DQ Dimension 3 | Foundation dimension for data integration and temporal stability |

### Control Example

- **Technical:** Implement schema validation and unit conversion checks in data pipelines.
- **Organizational:** Maintain a data dictionary with version control for all data elements used in AI training.
- **Monitoring:** Track schema drift and data definition changes across pipeline versions.

---

## Dimension 4: Timeliness

### DAMA-DMBOK Definition

"The degree to which data represent reality from the required point in time." (DAMA-DMBOK 2nd Ed., Chapter 13)

### AI Governance Relevance

- **Stale Training Data:** Models trained on outdated data become less accurate as the real world changes.
- **Delayed Inference Data:** Real-time AI systems using stale inputs produce decisions based on past states.
- **Risk Manifestation:** Timeliness failures appear as model drift, reduced accuracy over time, and delayed response to emerging threats.

### Governance Mapping

| Standard | Requirement | How Timeliness Maps |
|----------|-------------|----------------------|
| NIST AI RMF | MEASURE 2.2: Mechanisms for tracking identified AI risks over time | Timeliness is a key risk tracking mechanism — data freshness affects model risk |
| EU AI Act | Art. 10(3): Data shall be "relevant" | Relevance requires data to be current and contextually appropriate |
| ISO 42001 | Annex A.5.2: Data quality management | Timeliness is a primary data quality dimension to be managed |
| DAMA-DMBOK | DQ Dimension 4 | Foundation dimension for temporal validity and drift detection |

### Control Example

- **Technical:** Implement data freshness checks (e.g., "Training data age ≤ 90 days for rapidly changing domains").
- **Organizational:** Define retraining schedules based on data staleness thresholds.
- **Monitoring:** Track data age distributions and correlate with model performance metrics.

---

## Dimension 5: Validity

### DAMA-DMBOK Definition

"Data are valid if it conforms to the syntax (format, type, range) of its definition." (DAMA-DMBOK 2nd Ed., Chapter 13)

### AI Governance Relevance

- **Input Validation:** Invalid inputs (e.g., negative age, out-of-range values) can cause model failures or unexpected behavior.
- **Adversarial Inputs:** Adversarial actors may intentionally submit invalid inputs to probe system boundaries.
- **Risk Manifestation:** Validity failures appear as model crashes, adversarial exploitation, and unexpected prediction behavior.

### Governance Mapping

| Standard | Requirement | How Validity Maps |
|----------|-------------|----------------------|
| NIST AI RMF | MEASURE 1.1: Appropriate methods and metrics are identified | Validity checks (range, format, type) are required data quality metrics |
| EU AI Act | Art. 10(3): Data shall meet "quality criteria" | Validity is a fundamental quality criterion |
| ISO 42001 | Annex A.5.2: Data quality management | Validity is a primary data quality dimension to be managed |
| DAMA-DMBOK | DQ Dimension 5 | Foundation dimension for input integrity and adversarial robustness |

### Control Example

- **Technical:** Implement input validation gates (e.g., "Age ∈ [0, 120], Blood pressure ∈ [50, 300] mmHg").
- **Organizational:** Define data validation rules per feature and update them when clinical knowledge evolves.
- **Monitoring:** Track invalid input rates and flag adversarial patterns (e.g., boundary probing).

---

## Dimension 6: Uniqueness

### DAMA-DMBOK Definition

"No thing will be recorded more than once based upon how that thing is identified." (DAMA-DMBOK 2nd Ed., Chapter 13)

### AI Governance Relevance

- **Duplicate Training Data:** Duplicate records inflate training metrics without improving generalization. A model may appear accurate because it memorized duplicates rather than learning patterns.
- **Data Leakage:** Duplicates between training and test sets create inflated performance estimates that do not reflect real-world performance.
- **Risk Manifestation:** Uniqueness failures appear as overfitting, inflated performance metrics, and false confidence in model capability.

### Governance Mapping

| Standard | Requirement | How Uniqueness Maps |
|----------|-------------|----------------------|
| NIST AI RMF | MEASURE 2.1: Test sets and evaluation metrics are documented | Uniqueness between training and test sets is a test set integrity requirement |
| EU AI Act | Art. 10(3): Data shall be "representative" | Uniqueness ensures representation is not artificially inflated by duplicates |
| ISO 42001 | Annex A.5.2: Data quality management | Uniqueness is a primary data quality dimension to be managed |
| DAMA-DMBOK | DQ Dimension 6 | Foundation dimension for training integrity and evaluation validity |

### Control Example

- **Technical:** Implement deduplication pipelines (e.g., "Training set deduplication rate ≥ 99% before model training").
- **Organizational:** Define deduplication keys and policies for each data source.
- **Monitoring:** Track duplicate rates and ensure train/test set overlap = 0%.

---

## Summary Table: Data Quality Dimensions → AI Risk Categories

| Data Quality Dimension | Primary AI Risk Category | NIST AI RMF Function | EU AI Act Article | ISO 42001 Clause |
|------------------------|--------------------------|----------------------|-------------------|------------------|
| Accuracy | Prediction reliability | MEASURE | Art. 10 | Annex A.5.2 |
| Completeness | Bias, coverage gaps | MAP | Art. 10 | Annex A.5.2 |
| Consistency | Integration failure, drift | MAP / MEASURE | Art. 10 | Annex A.5.2 |
| Timeliness | Model drift, staleness | MEASURE | Art. 10 | Annex A.5.2 |
| Validity | Adversarial vulnerability, crashes | MEASURE | Art. 10 | Annex A.5.2 |
| Uniqueness | Overfitting, data leakage | MEASURE | Art. 10 | Annex A.5.2 |

---

## Implementation Recommendation

Before designing AI governance controls, conduct a **Data Quality Assessment** using these six dimensions. Score each dimension on a 1-5 scale for:
- Training data
- Validation data
- Test data
- Production inference data

**Rule:** No AI governance control design should proceed before the Data Quality Assessment is complete. If data quality scores are below 3 for any dimension, data remediation must be the first control, not an afterthought.

---

*Note: This mapping is based on DAMA-DMBOK 2nd Edition (2017). Users should verify against the latest DAMA publications and any organization-specific data quality frameworks.*
