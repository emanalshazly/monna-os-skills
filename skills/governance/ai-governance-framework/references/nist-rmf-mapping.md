# NIST AI RMF Mapping

## Reference: NIST AI Risk Management Framework (AI RMF 1.0)

This document maps the AI Governance Framework Skill content to the NIST AI RMF 1.0 functions and categories. All citations reference NIST AI 100-1 (January 2023) and the AI RMF Playbook.

---

## Govern Function

| Skill Content | NIST AI RMF Category | Mapping Rationale |
|---------------|----------------------|-------------------|
| Core Principle 1: Risk-Based Proportional Governance | GOVERN 1.1: Legal and regulatory requirements involving AI are understood, managed, and documented | Proportionality requires understanding regulatory scope before scaling effort |
| Core Principle 4: Stakeholder-Inclusive Design | GOVERN 1.2: The characteristics of AI trustworthiness are understood and mapped to organizational principles | Stakeholder inclusion ensures trustworthiness characteristics reflect actual user needs |
| Phase 1: Stakeholder Mapping | GOVERN 2.1: Roles and responsibilities for AI risk management are clear and documented | RACI matrix and stakeholder inventory directly satisfy this category |
| Phase 4: Implementation Roadmap | GOVERN 3.1: Decision-making is informed by a diverse team | Roadmap requires cross-functional input; escalation protocols ensure diverse perspectives are heard |
| Phase 4: Escalation Protocols | GOVERN 3.2: Organizational decision-making about AI is informed by input from external experts | Conditions for external escalation are defined in the roadmap |
| Phase 5: Continuous Monitoring & Audit | GOVERN 4.1: Risk monitoring is planned and documented | Monitoring cadence and KPI definition directly map to this category |
| Phase 5: Incident Management | GOVERN 4.2: Risk responses are planned and documented | Incident response procedures and severity classification satisfy this |
| Phase 5: Change Management | GOVERN 5.1: Processes are in place for robust engagement with AI actors | Change management governs engagement with AI systems and their operators |
| Phase 5: Internal Audit Program | GOVERN 5.2: Policies are in place for third-party AI risks | Audit program includes vendor and third-party control assessment |

---

## Map Function

| Skill Content | NIST AI RMF Category | Mapping Rationale |
|---------------|----------------------|-------------------|
| Phase 1: System Inventory | MAP 1.1: Context is established and understood for each AI system | System inventory captures operational, business, and regulatory context |
| Phase 1: Regulatory Classification | MAP 1.2: Categorization of AI system is performed | EU AI Act risk classification is a form of categorization per AI RMF guidance |
| Phase 2: Risk Assessment | MAP 2.1: AI capabilities are identified and documented | Threat identification catalogs capabilities that could be misused or fail |
| Phase 2: Risk Analysis | MAP 2.2: AI benefits are identified and documented | Impact assessment considers both positive and negative outcomes |
| Phase 2: Human Rights & Fundamental Rights Impact Assessment | MAP 3.1: Impacts on individuals are identified and documented | Fundamental rights assessment is a specific form of individual impact assessment |
| Phase 2: Risk Register | MAP 3.2: Impacts on groups and society are identified and documented | Risk register includes societal and group-level harms (bias, fairness) |
| Phase 3: Control Mapping | MAP 4.1: AI risks and benefits are mapped to trustworthy characteristics | Controls are designed to address specific trustworthiness characteristics |
| Phase 3: Residual Risk Assessment | MAP 4.2: Practical remedies to address risks are identified | Residual risk assessment determines whether identified remedies are sufficient |

---

## Measure Function

| Skill Content | NIST AI RMF Category | Mapping Rationale |
|---------------|----------------------|-------------------|
| Phase 3: Technical Controls | MEASURE 1.1: Appropriate methods and metrics are identified and documented | Control effectiveness criteria define "appropriate" for each system |
| Phase 3: Control Effectiveness Criteria | MEASURE 1.2: AI systems are evaluated for trustworthy characteristics | Quantitative and qualitative criteria evaluate trustworthiness |
| Phase 5: KPI & Metric Definition | MEASURE 2.1: Test sets and evaluation metrics are documented | KPIs include test coverage and evaluation metrics |
| Phase 5: Monitoring Cadence | MEASURE 2.2: Mechanisms for tracking identified AI risks over time are in place | Review frequencies institutionalize risk tracking |
| Phase 5: Incident Management | MEASURE 3.1: Feedback processes are in place and documented | Incident reporting is a critical feedback channel |
| Core Principle 2: Continuous Monitoring | MEASURE 3.2: Measurement approaches for identifying and tracking AI risks are documented | Continuous monitoring principle is the organizational commitment to this category |
| Phase 3: Model Validation | MEASURE 4.1: Measurement results are documented and utilized | Validation results feed into risk register and control design |
| Phase 5: Internal Audit Program | MEASURE 4.2: Measurement results are shared with relevant AI actors | Audit findings are communicated to accountable parties |

---

## Manage Function

| Skill Content | NIST AI RMF Category | Mapping Rationale |
|---------------|----------------------|-------------------|
| Phase 2: Risk Treatment Plan | MANAGE 1.1: AI risk is managed based on assessments and prioritization | Risk treatment prioritizes risks based on assessment results |
| Phase 3: Control Design | MANAGE 1.2: Residual AI risk is documented and communicated | Residual risk assessment documents remaining exposure |
| Phase 4: Implementation Roadmap | MANAGE 2.1: AI risk response plans are implemented and executed | Roadmap operationalizes risk response plans |
| Phase 4: Escalation Protocols | MANAGE 2.2: AI risk response plans are documented and maintained | Escalation paths are documented response mechanisms |
| Phase 5: Incident Management | MANAGE 3.1: Incidents are documented and responses are planned | Incident classification and response procedures satisfy this |
| Phase 5: Change Management | MANAGE 3.2: Incidents are responded to and addressed | Change management governs incident-driven system changes |
| Phase 5: Continuous Improvement | MANAGE 4.1: AI risk is periodically reviewed and updated | Continuous improvement loop ensures periodic review |
| Phase 5: Internal Audit Program | MANAGE 4.2: AI risk management processes are assessed and updated | Audit program assesses and improves risk management processes |

---

## Cross-Cutting: Trustworthy Characteristics

| Trustworthy Characteristic | Skill Coverage |
|----------------------------|----------------|
| Valid & Reliable | Phase 3: Technical Controls (model validation, testing); Phase 5: KPIs (performance metrics) |
| Safe | Phase 2: Risk Assessment (safety risks); Phase 3: Technical Controls (robustness testing) |
| Secure & Resilient | Phase 2: Threat Identification (adversarial attack); Phase 3: Technical Controls (security controls) |
| Accountable & Transparent | Core Principle 3: Traceability; Phase 3: Documentation Controls; Phase 1: Scope Statement |
| Explainable & Interpretable | Phase 3: Technical Controls (explainability mechanisms); Phase 4: Transparency mechanisms |
| Privacy-Enhanced | Phase 1: Data Classification; Phase 3: Legal Controls (consent, data subject rights) |
| Fair — Harmful Bias Managed | Phase 2: Risk Assessment (bias, fairness); Phase 3: Technical Controls (bias testing) |

---

*Note: This mapping is based on NIST AI 100-1 (January 2023). Users should verify against the latest NIST AI RMF publications as updates may revise category definitions.*
