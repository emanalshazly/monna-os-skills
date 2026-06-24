# Example 02: Financial RAG System

## Scenario

A European investment bank is deploying a Retrieval-Augmented Generation (RAG) system to assist relationship managers in answering client questions about market trends, portfolio performance, and regulatory updates. The system retrieves documents from internal research, external market data, and regulatory filings, then generates responses using a large language model (LLM). The bank operates in the EU and is subject to MiFID II, GDPR, and the EU AI Act.

**Risk Classification:** Medium-risk under EU AI Act (limited-risk transparency obligations + financial sector operational risk). Not Annex III high-risk unless used for credit scoring (Annex III(6)) — this use case is client information, not credit decision-making.

---

## Phase 1: Scoping & Classification

### 1. System Inventory

| System | Description | Version | Owner |
|--------|-------------|---------|-------|
| RAG-Advisor-1 | RAG system for client-facing Q&A | v1.2.0 | Product Owner, Digital Banking |
| Document-Retriever | Vector DB + embedding model for document retrieval | v2.0.1 | Data Engineering |
| LLM-Engine | GPT-4 fine-tuned for financial domain | v1.1.0 | ML Engineering |
| Compliance-Filter | Post-generation compliance check layer | v1.0.0 | Compliance IT |

**Shadow AI identified:** One relationship manager was using a personal ChatGPT subscription for client queries. Action: Discontinue use; onboard to RAG-Advisor-1 with audit trail.

### 2. Stakeholder Mapping (RACI)

| Activity | Responsible | Accountable | Consulted | Informed |
|----------|-------------|-------------|-----------|----------|
| Risk assessment | AI Risk Committee | CRO | Legal, Compliance, Relationship Managers | Regulators (if requested) |
| Model validation | ML Engineering | Head of Model Risk | External model validator | Audit Committee |
| Human oversight | Relationship Managers | Head of Private Banking | Compliance | Clients (via disclaimers) |
| Content governance | Compliance | Head of Compliance | Legal, Research | Senior Management |
| Data governance | Data Steward | CDO | AI Risk Committee | Regulators |

### 3. Regulatory Classification

- **EU AI Act:** Limited-risk (transparency obligations under Art. 52). Not high-risk because it does not make autonomous credit decisions or profiling. However, financial sector operational risk requirements (ECB guidance) apply.
- **MiFID II:** Client communications must be fair, clear, and not misleading. RAG-generated content must be reviewed before client-facing use.
- **GDPR:** Personal data may be processed if clients have consented or contract requires it. RAG system must not leak personal data across client boundaries.
- **Market Abuse Regulation (MAR):** RAG system must not generate or leak insider information.

### 4. Standards Mapping

| Standard | Applicability | Priority |
|----------|--------------|----------|
| EU AI Act | Mandatory (transparency obligations) | High |
| MiFID II | Mandatory (client communication standards) | Critical |
| NIST AI RMF | Voluntary (risk management best practice) | Medium |
| ISO 42001 | Voluntary (AIMS certification goal) | Low |
| ECB Guidance on ICT Risk | Mandatory (operational resilience) | High |

### 5. Data Classification

| Data Type | Classification | Governance Obligation |
|-----------|----------------|----------------------|
| Internal research reports | Confidential | Access control; no unauthorized distribution |
| Client portfolio data | Personal data (special category if reveals investment preferences) | GDPR; client consent; data minimization |
| External market data | Licensed third-party data | License compliance; usage tracking |
| Regulatory filings | Public | Accuracy verification; source attribution |
| Generated responses | Derived content | MiFID II fairness; record-keeping |

### 6. Scope Statement

**In scope:**
- RAG-Advisor-1 system for relationship manager Q&A support
- Document retrieval pipeline and vector database
- LLM generation and post-processing
- Compliance filter layer
- Human oversight protocols for relationship managers

**Out of scope:**
- Autonomous trading or investment recommendation systems
- Credit scoring or loan decision systems
- Client-facing chatbots without human oversight
- General IT security (covered by bank ISMS)

**Known limitations:**
- RAG system may hallucinate or retrieve outdated information
- Compliance filter reduces but does not eliminate hallucination risk
- System does not replace relationship manager judgment or legal advice
- Multi-jurisdiction clients may have additional regulatory requirements not covered

**Deliverable:** Scope Statement Document v1.0 (signed off by CRO, Head of Compliance, Head of Private Banking)

---

## Phase 2: Risk Assessment

### Threat Identification

| Risk ID | Category | Threat Description | Source |
|---------|----------|---------------------|--------|
| R-101 | Technical | Hallucination: LLM generates false or fabricated information | Model limitation, retrieval gap |
| R-102 | Technical | Retrieval failure: relevant document not retrieved, causing incomplete answer | Embedding mismatch, document gap |
| R-103 | Technical | Data leakage: LLM reveals one client's information to another relationship manager | Prompt injection, context contamination |
| R-104 | Legal | MiFID II breach: generated content is misleading or unfair | Inadequate compliance filter, human oversight failure |
| R-105 | Legal | MAR breach: system surfaces or generates insider information | Retrieval from restricted documents |
| R-106 | Operational | Relationship manager over-reliance on RAG without independent verification | Human factors, training gap |
| R-107 | Reputational | Client receives incorrect market information and makes poor investment decisions | Hallucination + oversight failure |
| R-108 | Reputational | Media reports that bank uses AI for client advice without disclosure | Transparency failure |

### Risk Analysis (5x5 Matrix)

| Risk ID | Likelihood (1-5) | Impact (1-5) | Risk Score | Risk Level |
|---------|-----------------|--------------|------------|------------|
| R-101 | 4 (likely) | 3 (moderate: client financial harm) | 12 | High |
| R-102 | 3 (possible) | 3 (moderate: incomplete advice) | 9 | Medium |
| R-103 | 2 (unlikely) | 5 (catastrophic: GDPR fine + client harm) | 10 | High |
| R-104 | 3 (possible) | 4 (major: regulatory fine + license risk) | 12 | High |
| R-105 | 2 (unlikely) | 5 (catastrophic: criminal liability) | 10 | High |
| R-106 | 4 (likely) | 3 (moderate: suboptimal advice) | 12 | High |
| R-107 | 3 (possible) | 3 (moderate: reputational damage) | 9 | Medium |
| R-108 | 2 (unlikely) | 3 (moderate: reputational damage) | 6 | Medium |

### Risk Evaluation

**Above risk appetite (require treatment):** R-101, R-103, R-104, R-105, R-106
**Within risk appetite (require monitoring):** R-102, R-107, R-108

### Risk Register

| Risk ID | Risk Level | Treatment | Owner | Status |
|---------|------------|-----------|-------|--------|
| R-101 | High | Compliance filter + human verification + source attribution | Product Owner | Active |
| R-102 | Medium | Retrieval accuracy monitoring + document gap analysis | Data Engineering | Active |
| R-103 | High | Client data isolation + prompt sanitization + access controls | CDO | Active |
| R-104 | High | Compliance filter + human review + record-keeping | Head of Compliance | Active |
| R-105 | High | Document classification + restricted document exclusion | Head of Compliance | Active |
| R-106 | High | Training + UI design + override requirement | Head of Private Banking | Active |
| R-107 | Medium | Accuracy monitoring + client feedback loop | Product Owner | Active |
| R-108 | Medium | Transparency notice + internal communication | Communications | Active |

---

## Phase 3: Control Design

### Control Mapping

| Risk ID | Control ID | Control Description | Standard Mapping | Effectiveness Criteria |
|---------|------------|----------------------|------------------|------------------------|
| R-101 | C-101 | Compliance filter: post-generation check for factual accuracy, regulatory compliance, and hallucination indicators | MiFID II; NIST MEASURE | Filter pass rate ≥ 98%; false positive rate < 5% |
| R-101 | C-102 | Source attribution: every generated response includes source document references | EU AI Act Art. 52; NIST GOVERN | 100% of responses include ≥ 1 source reference |
| R-101 | C-103 | Human verification: relationship manager must review and approve response before sending to client | MiFID II; EU AI Act Art. 14 | 100% of client-facing responses human-reviewed |
| R-103 | C-104 | Client data isolation: separate vector DB namespaces per client; no cross-client retrieval | GDPR Art. 32; NIST GOVERN | Zero cross-client data retrieval events |
| R-103 | C-105 | Prompt sanitization: strip client-identifying information from prompts before LLM processing | GDPR Art. 25 | 100% of prompts sanitized; privacy audit pass |
| R-104 | C-106 | Compliance filter: MiFID II fairness, clarity, and non-misleading checks | MiFID II Art. 24 | Zero compliance filter failures for client-facing content |
| R-105 | C-107 | Document classification: restrict retrieval from insider information documents; flag restricted docs | MAR; NIST GOVERN | Zero retrieval from restricted documents |
| R-106 | C-108 | Relationship manager training: RAG limitations, hallucination recognition, override protocols | EU AI Act Art. 52; NIST GOVERN | 100% of users certified; override rate ≥ 10% |
| R-106 | C-109 | UI design: confidence scores, source highlighting, and override prompts visible to relationship manager | NIST GOVERN | UI usability score ≥ 4.0/5.0 |
| R-102 | C-110 | Retrieval accuracy monitoring: track precision, recall, and MRR (Mean Reciprocal Rank) for retriever | NIST MEASURE | MRR ≥ 0.7; precision ≥ 80% |

### Residual Risk Assessment

| Risk ID | Pre-Control Risk | Post-Control Risk | Residual Risk | Acceptable? |
|---------|-----------------|-------------------|---------------|-------------|
| R-101 | High | Medium (filter + human review) | 8 | Yes — 2-layer verification |
| R-103 | High | Low (isolation + sanitization) | 4 | Yes — technical controls proven |
| R-104 | High | Medium (compliance filter + human review) | 8 | Yes — MiFID II controls established |
| R-105 | High | Low (document classification) | 4 | Yes — restricted access proven |
| R-106 | High | Medium (training + UI design) | 8 | Yes — override rate monitored |

---

## Phase 4: Implementation Roadmap

### Foundation (Month 1-2)

| Work Package | Deliverable | Owner | Dependencies |
|--------------|-------------|-------|--------------|
| WP-1.1 | AI Risk Committee charter for RAG systems | CRO | None |
| WP-1.2 | Stakeholder onboarding: relationship managers, compliance, legal | Head of Private Banking | WP-1.1 |
| WP-1.3 | Policy draft: RAG governance, content standards, human oversight | Compliance | WP-1.2 |
| WP-1.4 | Baseline assessment: current state vs. MiFID II + EU AI Act | Legal + Compliance | WP-1.3 |

### Core Controls (Month 3-4)

| Work Package | Deliverable | Owner | Dependencies |
|--------------|-------------|-------|--------------|
| WP-2.1 | Compliance filter development and testing | Compliance IT | WP-1.4 |
| WP-2.2 | Document classification and restricted access implementation | Data Engineering | WP-2.1 |
| WP-2.3 | Client data isolation: separate namespaces, access controls | Data Engineering | WP-2.2 |
| WP-2.4 | Human oversight UI: review workflow, source attribution, override | Product Owner | WP-2.3 |
| WP-2.5 | Relationship manager training program | Head of Private Banking | WP-2.4 |
| WP-2.6 | Retrieval accuracy monitoring dashboard | Data Engineering | WP-2.5 |

### Compliance Layer (Month 5-6)

| Work Package | Deliverable | Owner | Dependencies |
|--------------|-------------|-------|--------------|
| WP-3.1 | Transparency mechanisms: client disclosure, internal communication | Communications | WP-2.6 |
| WP-3.2 | Record-keeping: all RAG interactions logged, auditable | Compliance IT | WP-3.1 |
| WP-3.3 | Internal audit of all controls | Internal Audit | WP-3.2 |
| WP-3.4 | Regulator notification (if required by national implementation) | Legal | WP-3.3 |

### Monitoring & Optimization (Month 7+)

| Work Package | Deliverable | Owner | Dependencies |
|--------------|-------------|-------|--------------|
| WP-4.1 | Continuous monitoring dashboard | Data Engineering | WP-3.4 |
| WP-4.2 | Feedback loop: client complaints, relationship manager feedback | Product Owner | WP-4.1 |
| WP-4.3 | Quarterly AI Risk Committee review | CRO | WP-4.2 |
| WP-4.4 | Annual external audit | External auditor | WP-4.3 |
| WP-4.5 | Model update cycle: LLM fine-tuning, retriever retraining | ML Engineering | WP-4.4 |

### Milestones

| Milestone | Definition | Deadline | Pass Criteria |
|-----------|-----------|----------|---------------|
| M-1 | Governance structure operational | End Month 2 | Committee charter signed; stakeholders onboarded |
| M-2 | Core controls deployed | End Month 4 | Compliance filter active; data isolation verified; UI deployed; training complete |
| M-3 | Compliance demonstrated | End Month 6 | Internal audit passed; record-keeping operational; transparency notices published |
| M-4 | Monitoring institutionalized | End Month 7 | Dashboard live; feedback loop active; quarterly review scheduled |
| M-5 | Continuous improvement active | Month 12 | Annual audit passed; model update cycle established |

---

## Phase 5: Continuous Monitoring & Audit

### KPIs and Metrics

| Control | Leading Indicator | Lagging Indicator | Frequency |
|---------|-------------------|-------------------|-----------|
| C-101 (Compliance filter) | Filter pass rate | Hallucination incidents | Real-time |
| C-102 (Source attribution) | Source inclusion rate | Client complaints about missing sources | Per response |
| C-103 (Human verification) | Review completion rate | Unreviewed client-facing responses | Per response |
| C-104 (Data isolation) | Namespace access checks | Cross-client data leakage incidents | Daily |
| C-108 (Training) | Certification completion rate | Override rate by relationship manager | Monthly |
| C-110 (Retrieval accuracy) | MRR, precision, recall | Retrieval failure rate | Weekly |

### Monitoring Cadence

| Review Type | Frequency | Participants | Outputs |
|-------------|-----------|--------------|---------|
| Performance dashboard | Daily | Data Engineering | Filter alerts, retrieval accuracy trends |
| Risk register review | Monthly | AI Risk Committee | Updated risk scores, control effectiveness |
| Governance committee review | Quarterly | CRO, Head of Compliance, Head of Private Banking | Policy decisions, improvement plans |
| External audit | Annual | External auditor + Legal | Audit report, findings, remediation |

### Incident Management

| Severity | Definition | Response Time | Escalation |
|----------|------------|---------------|------------|
| Critical | Client financial loss, regulatory breach, data breach | 1 hour | CRO, CISO, Legal, Regulator notification |
| High | Hallucination in client-facing response, compliance filter failure | 4 hours | Product Owner, Head of Compliance |
| Medium | Retrieval accuracy degradation, training gap | 24 hours | AI Risk Committee |
| Low | UI feedback, minor policy clarification | 5 days | Relevant control owner |

### Change Management

All changes to RAG-Advisor-1 require:
1. Change request with risk impact assessment
2. AI Risk Committee review
3. If affects compliance filter or data isolation: Compliance and Legal sign-off
4. Staged rollout: 10% of users → 50% → 100%
5. Post-deployment monitoring for 7 days at each stage

---

## Key Takeaways

1. **Medium-risk systems still require governance.** Limited-risk under EU AI Act does not mean "no governance." MiFID II, operational risk, and reputational concerns create substantial governance obligations.
2. **Hallucination is the defining risk for RAG systems.** Unlike traditional AI with deterministic outputs, LLMs can generate plausible-sounding false information. The governance framework must explicitly address this unique risk.
3. **Human oversight is the critical control.** For client-facing content, human review before transmission is non-negotiable. The AI assists; the human decides.
4. **Data isolation is a privacy imperative.** RAG systems retrieving across documents create novel data leakage risks. Technical controls must enforce strict boundaries.
5. **Transparency builds trust.** Clients and regulators should know when AI is involved in generating advice. Disclosure is not a weakness; it is a governance strength.

---

*This example is for governance illustration only. It does not constitute financial, legal, or regulatory advice. Financial AI deployments require qualified compliance, legal, and risk management expertise.*
