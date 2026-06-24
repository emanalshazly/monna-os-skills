# AI Governance Framework Skill

## Metadata

- **Name:** `ai-governance-framework`
- **Trigger phrases:**
  - `design AI governance framework`
  - `NIST AI RMF implementation`
  - `EU AI Act compliance roadmap`
  - `ISO 42001 gap analysis`
  - `AI risk management system`
- **Quality tier:** `certified`
- **Fingerprint:** `gov-001-a7f3c9`
- **Compatibility:**
  - `certified`: Kimi/Daimon, Claude, Copilot
  - `validated`: Cursor, OpenClaw
- **Last tested:** 2026-06-24
- **Author:** monna
- **License:** MIT

---

## When to Use / When NOT to Use

### When to Use

Use this skill when you need to:
- Design a structured, standards-based AI governance framework for an organization.
- Map AI risk management to recognized frameworks (NIST AI RMF, EU AI Act, ISO 42001).
- Perform gap analysis between current AI practices and regulatory or standards requirements.
- Build implementation roadmaps for AI governance, risk management, and compliance.
- Create risk classification, control design, and monitoring systems for AI deployments.
- Translate high-level regulatory obligations into actionable organizational processes.
- Assess data quality dimensions as inputs to AI governance (per DAMA-DMBOK).

### When NOT to Use

**This skill does NOT:**
- **Provide legal advice.** Regulatory interpretation is provided for operational guidance only; consult qualified legal counsel for binding legal opinions.
- **Replace certified auditors.** Gap analysis outputs are preparatory self-assessment tools, not substitute for formal external audit or certification.
- **Cover non-AI systems.** This skill is scoped to AI systems, AI models, and AI-based decision-making workflows. Traditional IT governance, general software development lifecycle, and non-AI data governance are outside scope.
- **Generate technical model architectures.** It does not design ML pipelines, select algorithms, or optimize hyperparameters.
- **Substitute for organizational change management.** While stakeholder mapping is included, full HR, culture, or training program design is out of scope.
- **Address sector-specific clinical, safety, or financial advice** beyond governance structure recommendations. A healthcare example is provided for governance illustration, not clinical validation.

---

## Core Principles

### 1. Risk-Based Proportional Governance (per EU AI Act Article 9)

Governance intensity must be proportional to the risk level of the AI system. High-risk systems (e.g., Annex III, Annex II) require full conformity assessment, risk management systems, and human oversight. Limited-risk and minimal-risk systems require lighter-touch governance. **Governance effort must scale with risk, not with system complexity.**

### 2. Continuous Monitoring (per NIST AI RMF Monitor function, AI RMF 1.0)

AI systems are non-deterministic and context-dependent. Governance is not a milestone; it is a continuous function. Metrics, drift detection, performance thresholds, and feedback loops must be institutionalized and re-evaluated at defined intervals. **What is safe at deployment may not be safe in production.**

### 3. Traceability and Accountability (per EU AI Act Articles 10, 12, 14; ISO 42001 Clause 6.1.2)

Every governance decision must be documented, attributable, and auditable. This includes data lineage, model versioning, risk assessment rationale, control selection, and human oversight records. **If it is not documented, it is not governed.**

### 4. Stakeholder-Inclusive Design (per NIST AI RMF Govern function, AI RMF 1.0)

Governance structures designed by technical teams alone fail. Legal, operational, ethical, domain-expert, and end-user perspectives must be embedded in governance design. Stakeholder mapping is not optional; it is a prerequisite for valid risk assessment. **Risk is a social construct, not a technical metric.**

### 5. Data Quality as a Governance Input (per DAMA-DMBOK Data Quality Dimensions)

AI governance cannot be separated from data governance. Accuracy, completeness, consistency, timeliness, validity, and uniqueness of training and operational data directly determine model risk exposure. Data quality dimensions must be mapped to AI risk categories before control design. **Garbage in, governed garbage out is still failure.**

---

## Step-by-Step Process

### Phase 1: Scoping & Classification

**Objective:** Determine what you are governing and how risky it is.

1. **System Inventory.** List all AI systems, models, and automated decision-making workflows in scope. Include shadow AI systems identified by procurement or legal review.
2. **Stakeholder Mapping.** Identify owners, operators, affected parties, and oversight bodies. Use a RACI matrix where: Responsible = engineering team; Accountable = AI System Owner; Consulted = legal, ethics, domain experts; Informed = end users, regulators.
3. **Regulatory Classification.** Determine if the system is prohibited, high-risk (Annex III/Annex II EU AI Act), limited-risk (transparency obligations), or minimal-risk. For high-risk systems, confirm if a derogation applies.
4. **Standards Mapping.** Identify which standards apply (NIST AI RMF, EU AI Act, ISO 42001) based on jurisdiction, industry, and contractual requirements.
5. **Data Classification.** Map data types (personal, sensitive, special category) to governance obligations under GDPR, sectoral rules, and internal data policies.
6. **Scope Statement.** Document the boundaries of the governance framework: in-scope systems, out-of-scope items, applicable standards, and known limitations.

**Deliverable:** Scope Statement Document with Classification Matrix and RACI table.

**Transition to Phase 2:** The classification matrix directly feeds risk tiering.

---

### Phase 2: Risk Assessment

**Objective:** Identify, analyze, and evaluate AI-specific risks.

1. **Threat Identification.** Catalog risks across categories: technical (model drift, adversarial attack), legal (regulatory non-compliance, liability), operational (deployment failure, dependency risk), ethical (bias, fairness), and reputational (misuse, public backlash).
2. **Risk Analysis.** For each identified risk, assess likelihood and impact using a 5x5 matrix. Likelihood considers data quality, model maturity, and operational environment. Impact considers harm to individuals, organizations, and society.
3. **Risk Evaluation.** Compare risk levels against organizational risk appetite. Risks above appetite require treatment. Risks within appetite require monitoring.
4. **Human Rights & Fundamental Rights Impact Assessment (for high-risk systems).** Per EU AI Act Article 9, high-risk systems require a dedicated assessment of impacts on fundamental rights.
5. **Risk Register.** Document all risks, assessments, owners, and treatment decisions in a structured risk register.

**Deliverable:** Risk Register with Risk Treatment Plan.

**Transition to Phase 3:** High-priority risks determine control priority.

---

### Phase 3: Control Design

**Objective:** Design controls that treat identified risks and satisfy standard requirements.

1. **Control Mapping.** Map required controls to standard clauses and risk register items. For example: "Model validation before deployment" maps to NIST AI RMF Measure function and EU AI Act Article 10 (Data and Governance).
2. **Control Categories:**
   - **Technical Controls:** Data quality checks, model validation, testing protocols, drift detection, adversarial robustness testing, explainability mechanisms.
   - **Organizational Controls:** Governance committees, human oversight protocols, escalation procedures, training requirements, vendor management.
   - **Documentation Controls:** Model cards, data sheets, risk assessment reports, audit logs, change management records.
   - **Legal/Regulatory Controls:** Consent management, data subject rights procedures, transparency obligations, conformity assessment procedures.
3. **Control Effectiveness Criteria.** Define what "good enough" looks like for each control. Include quantitative thresholds (e.g., "False positive rate < 2%") and qualitative criteria (e.g., "Human override available within 3 seconds").
4. **Residual Risk Assessment.** After controls are designed, re-evaluate risk levels. If residual risk exceeds appetite, redesign controls or escalate.

**Deliverable:** Control Framework Document with mapped controls, effectiveness criteria, and residual risk assessment.

**Transition to Phase 4:** Controls define the work packages for the implementation roadmap.

---

### Phase 4: Implementation Roadmap

**Objective:** Operationalize the control framework in a phased, accountable manner.

1. **Work Package Definition.** Break controls into actionable work packages with defined deliverables, owners, and dependencies.
2. **Phase Planning:**
   - **Foundation (Month 1-2):** Governance structure, stakeholder onboarding, policy drafting, baseline assessment.
   - **Core Controls (Month 3-4):** Risk management system, data quality framework, model validation pipeline, human oversight protocols.
   - **Compliance Layer (Month 5-6):** Conformity assessment, documentation suite, transparency mechanisms, audit preparation.
   - **Monitoring & Optimization (Month 7+):** Continuous monitoring, feedback loops, incident management, improvement cycles.
3. **Resource Allocation.** Assign budget, personnel, and tooling to each work package. Identify gaps where external expertise (legal, audit, technical) is required.
4. **Milestone Definition.** Define clear, verifiable milestones for each phase. Milestones should be binary (pass/fail) to avoid subjective progress reporting.
5. **Escalation Protocols.** Define conditions under which implementation is blocked (e.g., unresolved high residual risk, missing legal sign-off) and escalation paths.

**Deliverable:** Implementation Roadmap Document with Gantt chart, resource plan, and milestone checklist.

**Transition to Phase 5:** Milestones feed into continuous monitoring KPIs.

---

### Phase 5: Continuous Monitoring & Audit

**Objective:** Ensure governance remains effective as systems and contexts evolve.

1. **KPI & Metric Definition.** Define metrics for each control: leading indicators (e.g., data quality scores, test coverage) and lagging indicators (e.g., incident count, audit findings).
2. **Monitoring Cadence.** Establish review frequencies: real-time (drift detection), weekly (performance dashboards), monthly (risk register review), quarterly (governance committee review), annual (external audit).
3. **Incident Management.** Define incident classification (severity levels), response procedures, root cause analysis requirements, and reporting obligations (internal and regulatory).
4. **Change Management.** Govern changes to AI systems, data pipelines, and governance controls themselves. Changes must be assessed for risk impact before deployment.
5. **Internal Audit Program.** Plan and execute audits against the control framework. Audit findings must be tracked to closure with defined timelines.
6. **Continuous Improvement.** Use monitoring data, incident reports, and audit findings to refine governance controls. Close the loop back to Phase 2 (Risk Assessment) when significant changes occur.

**Deliverable:** Monitoring & Audit Plan with KPI dashboard specifications and incident response playbooks.

---

## Anti-Patterns

### 1. Treat Governance as a One-Time Project

Governance is not a "set it and forget it" deliverable. AI systems degrade, contexts shift, and regulations evolve. Treating governance as a project with a defined end date leads to control decay and compliance gaps. **Governance is a continuous function, not a milestone.**

### 2. Skip Stakeholder Mapping

Building governance purely from a technical perspective misses legal, ethical, and operational risks. Stakeholders who will be governed by the framework must be involved in designing it. **Governance without stakeholder buy-in is compliance theater.**

### 3. Conflate AI Risk with General IT Risk

AI risk has distinct characteristics: model opacity, data dependency, non-deterministic behavior, and emergent failure modes. Applying generic IT risk frameworks (e.g., standard cybersecurity risk matrices) without AI-specific adaptations underweights model and data risks. **AI risk is not a subset of IT risk; it is a distinct domain.**

### 4. Ignore Data Quality in Governance Design

Organizations often design elaborate governance committees while neglecting the data that feeds AI systems. If training data is biased, incomplete, or stale, governance controls downstream cannot compensate. **Data quality is a governance prerequisite, not an afterthought.**

### 5. Document Only Success Cases

Governance requires honest documentation of failures, near-misses, and risks that exceed appetite. Selective documentation creates blind spots for auditors and regulators. **What you hide from governance, you hide from yourself.**

### 6. Design for Perfect Compliance, Not Operational Reality

Over-engineering governance to achieve theoretical perfection can paralyze operations. Governance must be implementable by the teams who execute it. **The best governance framework is the one that is actually followed.**

---

## References

All standard references are mapped in detail in the `references/` directory:

- [`references/nist-rmf-mapping.md`](references/nist-rmf-mapping.md) — NIST AI RMF 1.0 function mapping
- [`references/eu-ai-act-mapping.md`](references/eu-ai-act-mapping.md) — EU AI Act article mapping
- [`references/iso-42001-mapping.md`](references/iso-42001-mapping.md) — ISO/IEC 42001:2023 clause mapping
- [`references/dama-dmbok-dimensions.md`](references/dama-dmbok-dimensions.md) — DAMA-DMBOK data quality dimensions mapped to AI governance

---

## Examples

Worked examples are provided in the `examples/` directory:

- [`examples/example-01-healthcare-ai.md`](examples/example-01-healthcare-ai.md) — High-risk healthcare AI diagnostic system (EU AI Act Annex III)
- [`examples/example-02-finance-rag.md`](examples/example-02-finance-rag.md) — Medium-risk financial RAG system

---

## Tests

Validation criteria are provided in the `tests/` directory:

- [`tests/validation-checklist.md`](tests/validation-checklist.md) — Reviewer checklist with pass/fail criteria for each major section of this skill.

---

*End of SKILL.md. This skill is part of monna-os-skills, an open-source quality-governed skill collection. See LICENSE for terms.*
