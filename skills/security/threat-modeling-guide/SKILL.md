---
name: threat-modeling-guide
quality_tier: certified
fingerprint: sec-001-d2e4a7
compatibility:
  kimi: certified
  claude: certified
  copilot: certified
  cursor: certified
  openclaw: validated
author: Monna
version: 1.0.0
last_tested: 2026-06-24
license: MIT
---

# Threat Modeling Guide for AI Agent Systems

> A certified-level skill for building comprehensive threat models for AI agent systems, multi-agent platforms, and DePIN infrastructure using STRIDE + DREAD + MITRE ATT&CK frameworks.
> 
> **Quality Tier:** Certified — includes complete examples, references, and 55-item validation checklist.
> **Fingerprint:** sec-001-d2e4a7
> **Confidence Level:** High — evidence-based, traceable to DFD elements.

---

## When to Use This Skill

Use this skill when you need to:

- **Threat model an AI agent platform** before production deployment
- **Assess security risks** of multi-agent systems with inter-agent communication
- **Design security controls** for DePIN (Decentralized Physical Infrastructure) nodes
- **Audit existing systems** by building a formal threat model and reviewing it with a checklist
- **Educate security teams** on AI-specific threat vectors (prompt injection, model weights, jailbreaks)
- **Prepare for compliance** (SOC 2, ISO 27001, NIST RMF) with evidence-based threat documentation
- **Build a threat register** that can be updated as architecture evolves

## When NOT to Use This Skill

This skill is **not** for:
- **Penetration testing or vulnerability assessment** — this is a design-time threat model, not an active security test
- **Compliance gap analysis** — this identifies threats, not compliance gaps; use `ai-governance-framework` for compliance mapping
- **Real-time incident response** — threat models are living documents, not incident response playbooks
- **Physical security** — this skill addresses software and data threats, not physical facility security
- **Post-breach forensics** — use forensics frameworks; this is for proactive threat identification

## Core Principles

### Principle 1: Evidence-Based Threat Identification
Every threat must trace back to a specific Data Flow Diagram (DFD) element. If you cannot identify the DFD component where a threat manifests, the threat is not well-scoped.

### Principle 2: AI-Specific Threat Taxonomy
AI agents introduce unique threat vectors that do not exist in traditional software:
- **Prompt injection** as a spoofing/tampering vector
- **Model weights** as a supply chain target
- **Jailbreaks** as privilege escalation techniques
- **Agent-to-agent trust boundaries** as lateral movement paths
- **Tool use (MCP)** as an attack surface expansion

### Principle 3: Multi-Layer Threat Modeling
Threats are not just "in the agent." They exist at:
1. **Model layer** (weights, training data, inference APIs)
2. **Agent layer** (runtime, sandbox, memory, orchestration)
3. **Tool layer** (MCP endpoints, external APIs, databases)
4. **Infrastructure layer** (compute, storage, networking, blockchain)
5. **Human layer** (operators, developers, users, supply chain)

### Principle 4: Prioritization Over Paranoia
Not every threat is a High priority. Use DREAD scoring to objectively prioritize. If everything is High, the scoring is wrong. Use the "force a spread" rule in the DREAD reference.

### Principle 5: Living Document
Threat models are not "write once and forget." They must be reviewed:
- **On architecture change** (new agent, new tool, new model provider)
- **Quarterly** (even if nothing changes, the threat landscape does)
- **Post-incident** (within 48 hours of a security event or near-miss)
- **Pre-release** (every production deployment must have a current threat model)

---

## Step-by-Step Process

### Phase 1: Scope Definition

1. **Define the target system** — what is the system, its purpose, and its boundaries?
2. **Identify trust boundaries** — where does the trust model change? (user → agent, agent → tool, on-chain → off-chain)
3. **List external dependencies** — model providers, MCP tools, blockchains, oracles, external APIs
4. **Document assumptions** — what do you assume is true? (e.g., "We assume the model provider is not compromised")
5. **List exclusions** — what is out of scope? (e.g., "Physical security of data centers is out of scope")

**Output:** Scope document (1-2 pages) with system description, boundaries, assumptions, and exclusions.

### Phase 2: Data Flow Diagram (DFD)

1. **Level 0 — Context Diagram:** Draw a single box for the system. Show all external entities (users, model providers, blockchains, other systems) that interact with it. Show all data flows.
2. **Level 1 — Decomposition:** Break the system into its components. For an AI agent platform, this might include:
   - User Interface (web, API, chat)
   - API Gateway / Load Balancer
   - Agent Orchestrator / Runtime
   - Individual Agents (with their roles and tool access)
   - Message Bus / Inter-Agent Communication Layer
   - MCP Tool Registry and Endpoints
   - Vector Database / Memory Store
   - Model Proxy / Inference Layer
   - Audit Log Store
   - Secret Manager
3. **Label data flows** — every arrow must be numbered (DF-1, DF-2, ...) and described ("user chat message to agent runtime")
4. **Draw trust boundaries** — every DFD must have explicit trust boundaries where the trust model changes

**Output:** Level 0 and Level 1 DFDs with numbered flows, labeled components, and explicit trust boundaries.

**Critical Rule:** If a component is an AI agent, label it as such. Do not label it "System" or "Application."

### Phase 3: STRIDE Threat Identification

For each trust boundary and each data flow, walk through the six STRIDE categories and identify threats:

| STRIDE | Question | AI-Specific Focus |
|--------|----------|-------------------|
| **S**poofing | Who might pretend to be someone else? | Prompt injection, model impersonation, fake MCP tools, agent-to-agent spoofing |
| **T**ampering | What data or code might be modified? | Model weights, training data, RAG documents, tool responses, configurations |
| **R**epudiation | Who can deny doing something? | Agent actions without audit logs, ambiguous attribution between agents, model call disputes |
| **I**nformation Disclosure | What information might leak? | Training data, system prompts, agent memory, secrets in prompts, model outputs |
| **D**enial of Service | What can be made unavailable? | Infinite agent loops, inference flooding, vector DB poisoning, swarm saturation |
| **E**levation of Privilege | Who can gain unauthorized capabilities? | Sandbox escape, tool-use escalation, jailbreak, agent-to-agent privilege escalation |

**Process:**
1. Create a threat register table with columns: ID, STRIDE Category, Threat Name, DFD Element, Description, AI Context
2. Assign unique IDs: T-S01, T-T01, T-R01, T-I01, T-D01, T-E01 (where the prefix is S/T/R/I/D/E)
3. For each threat, write a specific description. Do not write "the system might be hacked." Write: "An attacker can cause the agent to execute arbitrary code by instructing it to write a Python script that opens a reverse shell."
4. Document AI-specific context: how does this threat manifest in an AI agent system specifically?

**Output:** Threat register with at least one threat per STRIDE category, all mapped to DFD elements.

**Reference:** See `references/stride-framework.md` for detailed AI-specific STRIDE mapping with examples and mitigations.

### Phase 4: DREAD Prioritization

For every threat in the register, apply DREAD scoring:

| Dimension | Score Range | Question |
|-----------|-------------|----------|
| **D**amage | 0-10 | How bad is the impact? |
| **R**eproducibility | 0-10 | How easy is it to reproduce? |
| **E**xploitability | 0-10 | How much effort/skill is required? |
| **A**ffected Users | 0-10 | How many users/systems are affected? |
| **D**iscoverability | 0-10 | How easy is it to discover? |

**Total Score:** 0-50

**Priority Tiers:**
- **High (35-50):** Immediate action required
- **Medium (20-34):** Planned mitigation within the next release cycle
- **Low (0-19):** Document and accept; revisit quarterly

**AI-Specific Adjustments:**
- **Privilege Amplification Bonus:** +1 Damage and +1 Exploitability if the threat involves an agent with elevated privileges (MCP tool access, code execution, blockchain signing)
- **Autonomy Multiplier:** +1 Reproducibility if the threat can be triggered autonomously (no human in the loop)
- **Multi-Agent Cascade Bonus:** +1 Affected Users and +1 Damage if the threat can spread from one agent to others
- **DePIN Consensus Bonus:** +1 Damage and +1 Discoverability if the threat affects consensus or economic incentives

**Critical Rules:**
1. Score the threat as if NO mitigations existed. Do not lower the score because you have a control in place. Document the control separately.
2. Force a spread. If everything is 25-30, identify the top 3 worst-case threats and score them higher.
3. Every score must have a 1-2 sentence rationale.

**Output:** Prioritized threat register with DREAD scores, justifications, and AI-specific adjustments.

**Reference:** See `references/dread-scoring-guide.md` for full scoring rubrics, adjustment rules, and example walkthroughs.

### Phase 5: Mitigation Design

For every High and Medium priority threat, design mitigations using the hierarchy:

1. **Eliminate:** Remove the threat entirely (e.g., remove code execution capability from agents that don't need it)
2. **Reduce:** Implement controls to lower the likelihood or impact (e.g., sandbox escape hardening, prompt injection detection)
3. **Transfer:** Shift the risk to another party (e.g., use a managed model security service, use institutional custody for validator keys)
4. **Accept:** Document and accept the residual risk (only for Low priority threats, or when the cost of mitigation exceeds the risk)

For every mitigation, specify:
- **Threat ID(s) it addresses**
- **Mitigation category** (Eliminate / Reduce / Transfer / Accept)
- **Specific control, technology, or process** (not "implement security best practices")
- **Verification method** (test, audit, metric, review)
- **Residual risk** (if applicable)

**Output:** Mitigation plan with specific controls, verification methods, and residual risk documentation.

### Phase 6: MITRE ATT&CK Mapping

Map the identified threats to MITRE ATT&CK tactics and techniques. This enables:
- Threat intelligence alignment (when your threat intel reports a MITRE technique, you know if it applies to your system)
- Detection engineering (map your SIEM/EDR rules to these techniques)
- Red team exercise design (test specific MITRE techniques against your agent system)

For AI agent systems, the adversary can be: external attacker, compromised insider, malicious model, poisoned data source, or rogue agent.

**Reference:** See `references/mitre-attack-mapping.md` for a complete mapping of AI/DePIN threats to MITRE ATT&CK tactics and techniques.

### Phase 7: Validation & Review

Use the `tests/validation-checklist.md` to validate the threat model before finalizing. The checklist covers:
- Document completeness (5 checks)
- DFD quality (8 checks)
- STRIDE coverage (9 checks)
- DREAD quality (6 checks)
- Mitigation design (6 checks)
- MITRE ATT&CK alignment (5 checks)
- Example quality (7 checks)
- Anti-patterns and boundaries (4 checks)
- Overall quality (5 checks)

**Total:** 55 checks. To pass certification: at least 48 must pass, including all checks in "Document Completeness" and "Anti-Patterns and Boundaries."

**Output:** Validated threat model with certification result.

---

## Anti-Patterns

### Anti-Pattern 1: "Black Box" DFD Components
**Mistake:** Labeling a component as "AI System" or "The Platform" instead of decomposing it into specific sub-components (agent, orchestrator, tool registry, etc.).
**Consequence:** Threats are missed because the DFD does not show the interfaces where threats manifest.
**Fix:** Every component must have a single, specific responsibility. If you cannot name what the component does, decompose it further.

### Anti-Pattern 2: Overlooking Agent-to-Agent Trust Boundaries
**Mistake:** Treating all agents as equally trusted within the platform. Drawing a single trust boundary around all agents.
**Consequence:** Lateral movement between agents is ignored. A compromised agent can freely communicate with other agents, escalate privileges, and exfiltrate data.
**Fix:** Draw trust boundaries between agents with different roles, tool access levels, and data access. Treat agent-to-agent communication as crossing a trust boundary.

### Anti-Pattern 3: Scoring Threats Based on Existing Mitigations
**Mistake:** Lowering a threat's DREAD score because "we already have a WAF" or "we use prompt injection detection."
**Consequence:** False confidence. The threat still exists if the mitigation fails or is bypassed.
**Fix:** Score every threat as if NO mitigations existed. Then document the mitigation's effectiveness separately. This is the "score the threat, not the control" rule.

### Anti-Pattern 4: Generic Threats
**Mistake:** Writing threats like "the system might be hacked" or "data might be stolen."
**Consequence:** The threat model is not actionable. No specific mitigations can be designed, and the model is useless for prioritization.
**Fix:** Every threat must be specific: name the attacker, the vector, the target DFD element, and the specific impact. Example: "An attacker can inject a prompt that causes the customer support agent to email customer records to attacker@example.com (T-S01, DF-1)."

### Anti-Pattern 5: Ignoring AI-Specific Threats
**Mistake:** Applying a generic web application threat model to an AI agent system without considering AI-specific vectors.
**Consequence:** Prompt injection, model weight tampering, jailbreaks, and agent-to-agent spoofing are completely missed.
**Fix:** For every STRIDE category, ask: "How does this threat manifest in an AI agent system?" If the answer is "it doesn't," you have missed something.

### Anti-Pattern 6: One-Time Threat Model
**Mistake:** Creating a threat model at design time and never reviewing it.
**Consequence:** The threat model becomes outdated as the system evolves (new agents, tools, model providers). Unaddressed threats emerge.
**Fix:** Schedule quarterly reviews. Trigger an immediate review on architecture change, new agent/tool/model provider, and within 48 hours of any security incident.

---

## References

- `references/stride-framework.md` — Full AI-specific STRIDE mapping with examples, mitigation patterns, and summary table
- `references/mitre-attack-mapping.md` — Complete mapping of AI/DePIN threats to MITRE ATT&CK tactics and techniques, including custom DePIN additions
- `references/dread-scoring-guide.md` — DREAD scoring rubrics, AI-specific adjustments, example walkthroughs, and calculator template

## Examples

- `examples/example-01-ai-agent-platform.md` — Complete threat model of a multi-agent platform with MCP tools, vector database, and model proxy (Level 1 DFD, STRIDE analysis, DREAD scoring, mitigations, MITRE mapping)
- `examples/example-02-depin-network.md` — Complete threat model of a DePIN wireless coverage network with node hardware, consensus, and smart contracts (Level 1 DFD, STRIDE analysis, DREAD scoring, mitigations, DePIN-specific extensions)

## Tests

- `tests/validation-checklist.md` — 55-item certification checklist for peer reviewers and auditors. Use this to validate any threat model built with this skill.

---

> **Quality Note:** This skill is certified under the MONNA quality framework. It has been tested with the validation checklist, includes two complete worked examples with specific technical details, and references three authoritative security frameworks (STRIDE, DREAD, MITRE ATT&CK). Every threat is traceable to a DFD element. Every mitigation is specific and verifiable. This is not a theoretical framework — it is a practical, executable threat modeling process for AI systems.
> 
> **Last Tested:** 2026-06-24
> **Next Review:** 2026-09-24
