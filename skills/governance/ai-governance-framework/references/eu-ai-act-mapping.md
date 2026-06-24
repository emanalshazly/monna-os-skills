# EU AI Act Mapping

## Reference: Regulation (EU) 2024/1689 — Artificial Intelligence Act

This document maps the AI Governance Framework Skill content to the EU AI Act. All article references are to the final text of Regulation (EU) 2024/1689 as published in the Official Journal of the European Union.

---

## Article 9 — Risk Management System

| Skill Content | EU AI Act Requirement | Mapping Rationale |
|---------------|----------------------|-------------------|
| Phase 2: Risk Assessment | Art. 9(1): "A risk management system shall be established, implemented, documented and maintained" | The entire Phase 2 process constitutes the risk management system establishment |
| Phase 2: Risk Analysis | Art. 9(2): Risk management shall "identify and analyse the known and foreseeable risks" | Threat identification and risk analysis steps directly satisfy this |
| Phase 2: Risk Evaluation | Art. 9(2): "estimate and evaluate the risks that may emerge when the high-risk AI system is used" | Risk evaluation against risk appetite maps to estimating and evaluating risks |
| Phase 3: Control Design | Art. 9(3): "The risk management system shall consist of a continuous iterative process" | Control design is part of the iterative risk treatment loop |
| Phase 5: Continuous Monitoring & Audit | Art. 9(3): Risk management shall be run "throughout the entire lifecycle of a high-risk AI system" | Monitoring and audit phases ensure lifecycle continuity |
| Phase 5: Incident Management | Art. 9(4): "The risk management system shall adopt the most appropriate risk management measures" | Incident response is a risk management measure for emergent risks |
| Phase 2: Risk Register | Art. 9(5): "High-risk AI systems shall be tested for the purpose of identifying the most appropriate and targeted risk management measures" | Risk register documents tested risks and selected measures |
| Phase 3: Residual Risk Assessment | Art. 9(6): "When implementing the risk management system... the most appropriate risk management measures shall be adopted" | Residual risk assessment determines appropriateness of measures |
| Phase 5: Change Management | Art. 9(7): "Testing shall be performed at any point in time throughout the development process, and in any event prior to placing on the market or putting into service" | Change management ensures pre-deployment testing for modifications |

---

## Article 10 — Data and Data Governance

| Skill Content | EU AI Act Requirement | Mapping Rationale |
|---------------|----------------------|-------------------|
| Core Principle 5: Data Quality as a Governance Input | Art. 10(1): "High-risk AI systems which make use of techniques involving the training of models with data shall be developed on the basis of training, validation and testing data sets that meet certain quality criteria" | Data quality dimensions are the operationalization of quality criteria |
| Phase 1: Data Classification | Art. 10(2): "Training, validation and testing data sets shall be subject to appropriate data governance and management practices" | Data classification is the first step in data governance |
| Phase 3: Technical Controls — Data Quality Checks | Art. 10(3): "Training, validation and testing data sets shall be relevant, representative, free of errors and complete" | Data quality checks verify relevance, representativeness, accuracy, and completeness |
| Phase 3: Technical Controls — Bias Testing | Art. 10(4): "To the extent applicable, data sets shall take into account the characteristics or elements that are particular to the specific geographical, contextual, behavioural or functional setting" | Bias testing ensures contextual appropriateness |
| Phase 3: Documentation Controls — Data Sheets | Art. 10(5): "Training, validation and testing data sets shall be appropriate for the intended purpose or purposes of the AI system" | Data sheets document intended purpose and data set appropriateness |
| Phase 5: Monitoring Cadence | Art. 10(6): "Where data is collected directly from data subjects, the AI system shall be designed to ensure data quality" | Monitoring ensures ongoing data quality in production |
| Phase 2: Risk Register — Data Risks | Art. 10(7): "All of the above requirements shall not apply to AI systems that do not use techniques involving the training of models with data" | Risk register identifies whether data quality requirements apply |

---

## Article 14 — Human Oversight

| Skill Content | EU AI Act Requirement | Mapping Rationale |
|---------------|----------------------|-------------------|
| Phase 3: Organizational Controls — Human Oversight Protocols | Art. 14(1): "High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which the AI system is in use" | Human oversight protocols operationalize this requirement |
| Phase 3: Technical Controls — Explainability | Art. 14(2): "Human oversight shall be ensured by one or more natural persons" who have "competence, training and authority" | Explainability mechanisms enable competent oversight |
| Phase 4: Resource Allocation — Training | Art. 14(3): "The individuals to whom human oversight is assigned shall be granted specific authority and competence | Training requirements ensure competence |
| Phase 5: Incident Management — Human Override | Art. 14(4): Human oversight measures shall include "the ability to correctly interpret the high-risk AI system's output" and "decide not to use the high-risk AI system in a particular situation" | Incident response includes human override and interpretation protocols |
| Phase 3: Control Effectiveness Criteria | Art. 14(5): "The individuals to whom human oversight is assigned shall not be subject to automation bias" | Effectiveness criteria include checks for automation bias |
| Phase 1: Stakeholder Mapping — Oversight Roles | Art. 14(6): "The individuals to whom human oversight is assigned shall be in a position to ensure that input data is relevant" | RACI assigns responsibility for data relevance to oversight roles |

---

## Article 52 — Transparency Obligations for Certain AI Systems

| Skill Content | EU AI Act Requirement | Mapping Rationale |
|---------------|----------------------|-------------------|
| Phase 1: Regulatory Classification | Art. 52(1): "AI systems intended to interact with natural persons shall be designed and developed in such a way that the natural persons are informed that they are interacting with an AI system" | Classification determines whether transparency obligations apply |
| Phase 3: Documentation Controls — Transparency Mechanisms | Art. 52(2): "Users of an AI system that generates or manipulates image, audio or video content... shall disclose that the content has been artificially generated or manipulated" | Documentation controls include synthetic content disclosure procedures |
| Phase 4: Compliance Layer | Art. 52(3): "Deployers of AI systems that generate or manipulate text shall disclose that the text has been artificially generated" | Compliance layer includes text-generation disclosure |
| Phase 3: Control Effectiveness Criteria | Art. 52(4): Exceptions for "artistic, creative, satirical, fictional or analogous work" | Effectiveness criteria determine when exceptions apply |
| Phase 5: Monitoring — Transparency Compliance | Art. 52(5): "The transparency obligations... shall not apply to AI systems used for purposes of law enforcement" | Monitoring includes checking for applicable exceptions |

---

## Annex III — High-Risk AI Systems (Sectoral List)

| Skill Content | EU AI Act Reference | Mapping Rationale |
|---------------|----------------------|-------------------|
| Example 01: Healthcare AI | Annex III(1): "Remote biometric identification systems" and Annex III(5): "AI systems intended to be used for the purpose of assessing patients' health risks" | Healthcare AI example is mapped to Annex III(5) high-risk category |
| Phase 1: Regulatory Classification | Annex III(2-8): Critical infrastructure, education, employment, credit scoring, law enforcement, migration, justice | Classification matrix includes all Annex III categories |
| Phase 2: Fundamental Rights Impact Assessment | Annex III + Art. 9: High-risk systems require full risk management and human oversight | All Annex III systems trigger Phase 2 requirements |

---

## Annex II — High-Risk AI Systems (Harmonized Standards)

| Skill Content | EU AI Act Reference | Mapping Rationale |
|---------------|----------------------|-------------------|
| Phase 1: Standards Mapping | Annex II: Products covered by EU harmonization legislation | Standards mapping identifies whether Annex II applies |
| Phase 3: Control Design | Annex II + Art. 43: Conformity assessment based on internal control or third-party assessment | Control design includes conformity assessment procedures |
| Phase 4: Compliance Layer | Art. 43: Conformity assessment procedures | Compliance layer includes Annex II conformity assessment |

---

## Prohibited AI Practices (Article 5)

| Skill Content | EU AI Act Reference | Mapping Rationale |
|---------------|----------------------|-------------------|
| Phase 1: Regulatory Classification | Art. 5: Prohibited AI practices | Classification matrix includes prohibited category |
| Phase 2: Threat Identification | Art. 5(1): Subliminal techniques, exploitation of vulnerabilities, social scoring, real-time remote biometric identification in public spaces | Threat identification includes prohibited practice risks |
| Phase 3: Control Design | Art. 5(1): "The following AI practices shall be prohibited" | Controls do not apply — prohibited systems must not be deployed |
| Phase 4: Escalation Protocols | Art. 5(1): Prohibited systems trigger legal escalation | Escalation path includes legal review for prohibited classification |

---

*Note: This mapping is based on Regulation (EU) 2024/1689 as published in the OJ. Users should verify against the latest official text and any delegated acts or implementing acts that may supplement the regulation.*
