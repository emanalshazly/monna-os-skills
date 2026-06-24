# Example 01: Healthcare AI Diagnostic System

## Scenario

A mid-size hospital network (3 hospitals, 500 beds) is deploying a Computer-Aided Diagnosis (CAD) system for chest X-ray analysis to assist radiologists in detecting pulmonary nodules suggestive of lung cancer. The system is a deep learning model trained on 50,000 chest X-rays, integrated into the hospital's PACS (Picture Archiving and Communication System). The hospital operates in the EU.

**Risk Classification:** High-risk under EU AI Act Annex III(5) — "AI systems intended to be used for the purpose of assessing patients' health risks."

---

## Phase 1: Scoping & Classification

### 1. System Inventory

| System | Description | Version | Owner |
|--------|-------------|---------|-------|
| CAD-Pulmonary-1 | Chest X-ray nodule detection | v2.3.1 | Dr. Sarah Chen, Radiology AI Lead |
| PACS-Integration | API gateway to PACS | v1.0.4 | IT Clinical Systems |
| DICOM-Preprocessing | Image normalization pipeline | v3.1.0 | ML Engineering |

**Shadow AI identified:** None. Procurement confirmed all AI systems are registered.

### 2. Stakeholder Mapping (RACI)

| Activity | Responsible | Accountable | Consulted | Informed |
|----------|-------------|-------------|-----------|----------|
| Risk assessment | Clinical AI Committee | Chief Medical Officer | Legal, Ethics Board, Radiologists | Patients (via transparency notice) |
| Model validation | ML Engineering | Dr. Sarah Chen | External validation lab | Regulatory Affairs |
| Human oversight | Radiologists | Head of Radiology | Clinical AI Committee | Quality Assurance |
| Incident response | IT Security | CISO | Legal, Clinical AI Committee | Hospital Board |
| Data governance | Data Steward | DPO | Clinical AI Committee | Regulatory Affairs |

### 3. Regulatory Classification

- **EU AI Act:** High-risk (Annex III(5)). Requires full risk management system, data governance, human oversight, transparency, and conformity assessment.
- **GDPR:** Personal data processing (health data = special category). Requires DPIA.
- **Medical Device Regulation (MDR):** The system is a Class IIa medical device under MDR 2017/745. Requires CE marking.
- **ISO 13485:** Quality management for medical devices applies.

### 4. Standards Mapping

| Standard | Applicability | Priority |
|----------|--------------|----------|
| EU AI Act | Mandatory (EU market) | Critical |
| NIST AI RMF | Voluntary (US parent company requirement) | High |
| ISO 42001 | Voluntary (AIMS certification goal) | Medium |
| ISO 13485 | Mandatory (MDR compliance) | Critical |
| GDPR | Mandatory (EU data processing) | Critical |

### 5. Data Classification

| Data Type | Classification | Governance Obligation |
|-----------|----------------|----------------------|
| Chest X-ray images (DICOM) | Special category health data | GDPR Art. 9, DPIA required, pseudonymization mandatory |
| Radiologist labels | Special category health data | GDPR Art. 9, consent/legitimate interest assessment |
| Patient demographics | Personal data | GDPR, data minimization |
| Model predictions | Derived special category data | Same obligations as source data |

### 6. Scope Statement

**In scope:**
- CAD-Pulmonary-1 model development, validation, deployment, and monitoring
- Training, validation, and test data sets
- Human oversight protocols for radiologists
- PACS integration and API security
- Patient transparency mechanisms

**Out of scope:**
- Non-AI clinical decision support systems
- General IT security (covered by hospital ISMS)
- Radiologist clinical training (covered by medical education)

**Known limitations:**
- This framework does not cover AI systems in other departments (e.g., pathology, cardiology)
- Does not address clinical efficacy beyond governance structure
- Does not replace MDR technical documentation

**Deliverable:** Scope Statement Document v1.0 (signed off by CMO, DPO, Head of Radiology)

---

## Phase 2: Risk Assessment

### Threat Identification

| Risk ID | Category | Threat Description | Source |
|---------|----------|---------------------|--------|
| R-001 | Technical | False negative: model misses malignant nodule | Model error, data quality |
| R-002 | Technical | False positive: model flags benign finding as malignant | Model error, class imbalance |
| R-003 | Technical | Model drift due to new X-ray equipment or protocols | Operational change |
| R-004 | Legal | Non-compliance with EU AI Act high-risk requirements | Regulatory gap |
| R-005 | Legal | GDPR breach: unauthorized access to patient X-rays | Security failure |
| R-006 | Operational | Radiologist over-reliance on AI (automation bias) | Human factors |
| R-007 | Ethical | Systematic underperformance for underrepresented demographic groups | Training data bias |
| R-008 | Reputational | Media exposure of AI misdiagnosis | Public perception |

### Risk Analysis (5x5 Matrix)

| Risk ID | Likelihood (1-5) | Impact (1-5) | Risk Score | Risk Level |
|---------|-----------------|--------------|------------|------------|
| R-001 | 3 (possible) | 5 (catastrophic: death) | 15 | High |
| R-002 | 4 (likely) | 2 (minor: unnecessary procedures) | 8 | Medium |
| R-003 | 3 (possible) | 4 (major: delayed diagnosis) | 12 | High |
| R-004 | 2 (unlikely) | 5 (catastrophic: regulatory shutdown) | 10 | High |
| R-005 | 2 (unlikely) | 5 (catastrophic: fine + shutdown) | 10 | High |
| R-006 | 4 (likely) | 4 (major: missed diagnosis) | 16 | High |
| R-007 | 3 (possible) | 4 (major: discriminatory outcomes) | 12 | High |
| R-008 | 3 (possible) | 3 (moderate: reputational damage) | 9 | Medium |

### Risk Evaluation

**Above risk appetite (require treatment):** R-001, R-003, R-004, R-005, R-006, R-007
**Within risk appetite (require monitoring):** R-002, R-008

### Fundamental Rights Impact Assessment (EU AI Act Article 9)

| Fundamental Right | Impact | Mitigation |
|-------------------|--------|------------|
| Right to life (Art. 2 CFR) | Delayed cancer diagnosis could cause death | Human oversight mandatory; AI is decision support, not autonomous diagnosis |
| Right to health (Art. 35 CFR) | Misdiagnosis could harm health | Validation by external lab; performance monitoring |
| Right to non-discrimination (Art. 21 CFR) | Bias could disadvantage ethnic groups | Bias testing; demographic parity monitoring |
| Right to data protection (Art. 8 CFR) | Health data breach | GDPR compliance; pseudonymization; access controls |

### Risk Register

| Risk ID | Risk Level | Treatment | Owner | Status |
|---------|------------|-----------|-------|--------|
| R-001 | High | Technical controls + human oversight | Dr. Chen | Active |
| R-002 | Medium | Monitoring + patient communication | Dr. Chen | Active |
| R-003 | High | Drift detection + retraining protocol | ML Engineering | Active |
| R-004 | High | Full EU AI Act compliance program | Legal | Active |
| R-005 | High | Security controls + DPIA | DPO | Active |
| R-006 | High | Human oversight training + UI design | Head of Radiology | Active |
| R-007 | High | Bias testing + demographic monitoring | Ethics Board | Active |
| R-008 | Medium | Crisis communication plan | Communications | Active |

---

## Phase 3: Control Design

### Control Mapping

| Risk ID | Control ID | Control Description | Standard Mapping | Effectiveness Criteria |
|---------|------------|----------------------|------------------|------------------------|
| R-001 | C-001 | Sensitivity threshold tuned to achieve recall ≥ 95% for nodules > 5mm | NIST MEASURE; EU AI Act Art. 10 | Validation report; monthly performance audit |
| R-001 | C-002 | All AI outputs reviewed by certified radiologist before patient notification | EU AI Act Art. 14 | 100% review rate; review time ≤ 5 minutes per case |
| R-003 | C-003 | Automated drift detection: monitor input distribution, prediction distribution, and performance metrics daily | NIST MEASURE; EU AI Act Art. 9 | Alert if KS-test p-value < 0.01 or accuracy drop > 2% |
| R-003 | C-004 | Quarterly retraining schedule triggered by drift alert or calendar | ISO 42001 Annex A.5.2 | Retraining completed within 14 days of trigger |
| R-004 | C-005 | Conformity assessment with notified body for EU AI Act + MDR CE marking | EU AI Act Art. 43; MDR Art. 52 | CE marking obtained before deployment |
| R-005 | C-006 | DICOM data encrypted at rest (AES-256) and in transit (TLS 1.3); access controls (RBAC) | GDPR Art. 32; ISO 42001 Annex A.6 | Quarterly penetration test; zero critical vulnerabilities |
| R-006 | C-007 | Radiologist training: automation bias recognition, override protocols, confidence calibration | EU AI Act Art. 14(3); NIST GOVERN | 100% of radiologists certified annually; override rate tracked |
| R-007 | C-008 | Bias testing: demographic parity, equalized odds, calibration across age, sex, ethnicity | EU AI Act Art. 10(4); NIST MEASURE | Disparity ratio < 0.8 for any demographic group; quarterly audit |
| R-007 | C-009 | Data augmentation and re-sampling to address underrepresented groups | NIST MEASURE; DAMA-DMBOK Completeness | Training data demographic coverage within ±5% of population |

### Residual Risk Assessment

| Risk ID | Pre-Control Risk | Post-Control Risk | Residual Risk | Acceptable? |
|---------|-----------------|-------------------|---------------|-------------|
| R-001 | High | Medium (human oversight reduces false negative impact) | 8 | Yes — human oversight is mandatory backup |
| R-003 | High | Medium (drift detection + retraining) | 9 | Yes — 14-day retraining window |
| R-004 | High | Low (conformity assessment + legal review) | 5 | Yes — regulatory compliance demonstrated |
| R-005 | High | Low (encryption + access controls + DPIA) | 4 | Yes — GDPR compliance demonstrated |
| R-006 | High | Medium (training + UI design) | 8 | Yes — monitoring override rates |
| R-007 | High | Medium (bias testing + augmentation) | 8 | Yes — continuous monitoring |

---

## Phase 4: Implementation Roadmap

### Foundation (Month 1-2)

| Work Package | Deliverable | Owner | Dependencies |
|--------------|-------------|-------|--------------|
| WP-1.1 | Governance committee charter | CMO | None |
| WP-1.2 | Stakeholder onboarding (legal, ethics, radiologists) | Head of Radiology | WP-1.1 |
| WP-1.3 | Policy draft: AI governance, data quality, human oversight | Clinical AI Committee | WP-1.2 |
| WP-1.4 | Baseline assessment: current state vs. EU AI Act + ISO 42001 | Legal + External consultant | WP-1.3 |
| WP-1.5 | DPIA completion | DPO | WP-1.4 |

### Core Controls (Month 3-4)

| Work Package | Deliverable | Owner | Dependencies |
|--------------|-------------|-------|--------------|
| WP-2.1 | Risk management system (software + process) | Dr. Chen | WP-1.1 |
| WP-2.2 | Data quality framework: 6 dimensions implemented | Data Steward | WP-1.5 |
| WP-2.3 | Model validation pipeline: external lab validation | ML Engineering | WP-2.2 |
| WP-2.4 | Human oversight protocols: UI design, override workflow | Head of Radiology | WP-2.3 |
| WP-2.5 | Radiologist training program: automation bias, override | Head of Radiology | WP-2.4 |
| WP-2.6 | Drift detection system deployment | ML Engineering | WP-2.3 |

### Compliance Layer (Month 5-6)

| Work Package | Deliverable | Owner | Dependencies |
|--------------|-------------|-------|--------------|
| WP-3.1 | Conformity assessment: notified body engagement | Legal | WP-2.1, WP-2.3 |
| WP-3.2 | Technical documentation: model card, data sheet, risk assessment | Dr. Chen | WP-3.1 |
| WP-3.3 | Transparency mechanisms: patient notice, radiologist disclosure | Communications | WP-3.2 |
| WP-3.4 | Audit preparation: internal audit of all controls | Quality Assurance | WP-3.3 |
| WP-3.5 | CE marking application | Legal | WP-3.4 |

### Monitoring & Optimization (Month 7+)

| Work Package | Deliverable | Owner | Dependencies |
|--------------|-------------|-------|--------------|
| WP-4.1 | Continuous monitoring dashboard | ML Engineering | WP-2.6 |
| WP-4.2 | Feedback loop: incident reporting, root cause analysis | Quality Assurance | WP-4.1 |
| WP-4.3 | Quarterly governance committee review | CMO | WP-4.2 |
| WP-4.4 | Annual external audit | Legal + External auditor | WP-4.3 |
| WP-4.5 | Improvement cycle: control refinement based on monitoring | Clinical AI Committee | WP-4.4 |

### Milestones

| Milestone | Definition | Deadline | Pass Criteria |
|-----------|-----------|----------|---------------|
| M-1 | Governance structure operational | End Month 2 | Committee charter signed; all stakeholders onboarded |
| M-2 | Core controls deployed | End Month 4 | Validation report complete; drift detection active; training complete |
| M-3 | Compliance demonstrated | End Month 6 | CE marking obtained; DPIA approved; internal audit passed |
| M-4 | Monitoring institutionalized | End Month 7 | Dashboard live; incident response tested; quarterly review scheduled |
| M-5 | Continuous improvement active | Month 12 | Annual audit passed; improvement plan approved |

---

## Phase 5: Continuous Monitoring & Audit

### KPIs and Metrics

| Control | Leading Indicator | Lagging Indicator | Frequency |
|---------|-------------------|-------------------|-----------|
| C-001 (Sensitivity) | Validation sensitivity score | False negative rate in production | Weekly |
| C-002 (Human oversight) | Review completion rate | Radiologist override rate | Real-time |
| C-003 (Drift detection) | Drift alert count | Model performance drop events | Daily |
| C-007 (Training) | Training completion rate | Override rate by radiologist | Monthly |
| C-008 (Bias) | Bias test pass rate | Demographic parity disparity | Quarterly |
| C-006 (Security) | Access review completion | Security incident count | Monthly |

### Monitoring Cadence

| Review Type | Frequency | Participants | Outputs |
|-------------|-----------|--------------|---------|
| Performance dashboard | Daily | ML Engineering | Drift alerts, performance trends |
| Risk register review | Monthly | Clinical AI Committee | Updated risk scores, new risks |
| Governance committee review | Quarterly | CMO, DPO, Head of Radiology, Legal | Governance decisions, policy updates |
| External audit | Annual | External auditor + Legal | Audit report, findings, remediation plan |

### Incident Management

| Severity | Definition | Response Time | Escalation |
|----------|------------|---------------|------------|
| Critical | Patient safety impact, regulatory breach, data breach | 1 hour | CMO, CISO, Legal immediately |
| High | Performance degradation > 5%, drift alert | 4 hours | Dr. Chen, ML Engineering lead |
| Medium | Bias disparity > 0.8, training overdue | 24 hours | Clinical AI Committee |
| Low | Documentation update, minor policy clarification | 5 days | Relevant control owner |

### Change Management

All changes to CAD-Pulmonary-1 require:
1. Change request with risk impact assessment
2. Clinical AI Committee review
3. If high risk: DPO and Legal sign-off
4. Retraining and validation before deployment
5. Post-deployment monitoring for 14 days

---

## Key Takeaways

1. **High-risk systems require layered governance.** No single control is sufficient; human oversight + technical controls + legal compliance are all mandatory.
2. **Human oversight is not optional.** For high-risk healthcare AI, the radiologist must remain the decision-maker. The AI is decision support, not autonomous diagnosis.
3. **Data quality is a safety issue.** Inaccurate labels, missing demographics, or non-representative data directly cause patient harm.
4. **EU AI Act and MDR overlap.** The system must satisfy both. Conformity assessment should cover both frameworks simultaneously to avoid duplicate effort.
5. **Start with scope, not controls.** A well-defined scope statement prevents scope creep, ensures stakeholder alignment, and establishes accountability before any technical work begins.

---

*This example is for governance illustration only. It does not constitute clinical, legal, or regulatory advice. Healthcare AI deployments require qualified clinical, legal, and regulatory expertise.*
