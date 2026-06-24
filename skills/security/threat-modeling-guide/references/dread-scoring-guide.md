# DREAD Scoring Guide

> Reference for prioritizing threats using the DREAD scoring model, calibrated for AI agent systems, multi-agent platforms, and DePIN infrastructure. Includes scoring rubrics, examples, and a calculator template.

---

## DREAD Overview

DREAD is a risk assessment model that scores threats on five dimensions:

| Dimension | Question | Score Range |
|-----------|----------|-------------|
| **D**amage | How bad is the impact if this threat is exploited? | 0-10 |
| **R**eproducibility | How easy is it to reproduce the attack? | 0-10 |
| **E**xploitability | How much effort/skill is required to exploit? | 0-10 |
| **A**ffected Users | How many users/systems are affected? | 0-10 |
| **D**iscoverability | How easy is it for an attacker to discover this vulnerability? | 0-10 |

**Total Score = D + R + E + A + D** (range: 0-50)

**Priority Tiers:**
- **High (35-50):** Immediate action required. Assign resources, design mitigations, set a timeline.
- **Medium (20-34):** Planned mitigation within the next release cycle. Monitor actively.
- **Low (0-19):** Document and accept. Revisit during quarterly review.

---

## Scoring Rubrics

### Damage (0-10)

| Score | Description | AI/Agent Examples |
|-------|-------------|-------------------|
| 0-2 | Minimal impact. No data loss, no service disruption, no privilege gain. | Agent outputs a slightly incorrect but harmless response. |
| 3-4 | Low impact. Minor inconvenience, limited data exposure, contained to one component. | A single user's conversation history is exposed to another user in the same tenant. |
| 5-6 | Moderate impact. Service degradation, moderate data exposure, some privilege gain. | An agent is tricked into revealing its system prompt (no direct system compromise). |
| 7-8 | High impact. Significant data breach, service outage, major privilege escalation. | A compromised agent gains access to a production database and exfiltrates customer records. |
| 9-10 | Catastrophic impact. Complete system compromise, widespread data breach, financial loss, safety risk. | A DePIN network consensus is corrupted, leading to fraudulent reward distribution and collapse of network trust. |

### Reproducibility (0-10)

| Score | Description | AI/Agent Examples |
|-------|-------------|-------------------|
| 0-2 | Very difficult to reproduce. Requires rare conditions, insider knowledge, or sophisticated setup. | Exploiting a race condition in a custom agent runtime that only triggers under specific load patterns. |
| 3-4 | Difficult. Requires specific conditions or multiple steps. | A prompt injection that only works with a specific model version and a particular RAG document set. |
| 5-6 | Moderate. Reproducible with some effort and known tools. | A well-documented prompt injection technique that requires some crafting but works across multiple sessions. |
| 7-8 | Easy. Reproducible consistently with minimal effort. | A public MCP tool endpoint with no authentication—anyone can call it with a known API key format. |
| 9-10 | Trivial. Reproducible by anyone, any time, with no special tools. | Sending a prompt injection to a publicly exposed agent with no input validation. |

### Exploitability (0-10)

| Score | Description | AI/Agent Examples |
|-------|-------------|-------------------|
| 0-2 | Extremely difficult. Requires advanced expertise, zero-days, or nation-state resources. | Exploiting a novel vulnerability in a model's transformer architecture to extract training data. |
| 3-4 | Difficult. Requires skilled attacker, custom tools, or significant time. | Developing a targeted jailbreak against a model with strong safety training and multi-layer guardrails. |
| 5-6 | Moderate. Requires some skill and available tools. | Using a known prompt injection framework (e.g., Greshake-style indirect injection) against an unprotected agent. |
| 7-8 | Easy. Requires minimal skill and basic tools. | Calling an unauthenticated MCP tool endpoint with a crafted request. |
| 9-10 | Trivial. No skill required. A simple prompt or API call suffices. | Copy-pasting a public jailbreak prompt into a chat interface with no safety filters. |

### Affected Users (0-10)

| Score | Description | AI/Agent Examples |
|-------|-------------|-------------------|
| 0-2 | None or one user. | A local agent running on a single developer's machine. |
| 3-4 | Small group (2-10 users). | A small team using a shared agent for internal documentation. |
| 5-6 | Medium group (10-100 users) or one tenant. | A SaaS agent platform affecting all users in one enterprise tenant. |
| 7-8 | Large group (100-10,000 users) or multiple tenants. | A popular public agent service with thousands of users. |
| 9-10 | All users, entire network, or systemic impact. | A DePIN network with 100,000+ nodes where a consensus vulnerability affects the entire chain. |

### Discoverability (0-10)

| Score | Description | AI/Agent Examples |
|-------|-------------|-------------------|
| 0-2 | Nearly impossible to discover. Hidden in complex internals, no external indicators. | A subtle bias in model weights that only manifests with adversarial statistical testing. |
| 3-4 | Difficult. Requires deep analysis, source code access, or insider knowledge. | A vulnerability in an agent's custom sandbox escape logic that requires reviewing the sandbox implementation. |
| 5-6 | Moderate. Can be discovered with standard security testing or reconnaissance. | An unauthenticated MCP tool endpoint discovered through API documentation or simple probing. |
| 7-8 | Easy. Visible in public interfaces, documentation, or error messages. | A public API endpoint that returns verbose error messages revealing internal paths and configurations. |
| 9-10 | Trivial. Obvious to anyone using the system. | A publicly exposed agent with no authentication on a known URL. |

---

## AI/Agent-Specific Scoring Adjustments

Certain threat characteristics in AI systems warrant scoring adjustments:

### Privilege Amplification Bonus
If a threat involves an agent with elevated privileges (MCP tool access, code execution, blockchain signing), add **+1 to Damage** and **+1 to Exploitability** because the agent's autonomous action capability magnifies both impact and ease of exploitation.

### Autonomy Multiplier
If a threat can be triggered autonomously (no human in the loop), add **+1 to Reproducibility** because the attack can run continuously without attacker intervention.

### Multi-Agent Cascade Bonus
If a threat can spread from one agent to others in a multi-agent system, add **+1 to Affected Users** and **+1 to Damage** because the blast radius is larger than a single-component threat.

### DePIN Consensus Bonus
If a threat affects consensus or economic incentives in a DePIN network, add **+1 to Damage** and **+1 to Discoverability** because economic incentives drive attackers to discover and exploit these vulnerabilities.

> **Maximum Adjusted Score:** Any single dimension cannot exceed 10, even with adjustments. Cap at 10.

---

## Example Scoring Walkthroughs

### Example 1: Prompt Injection in a Customer Support Agent

**Threat:** A prompt injection attack causes the customer support agent to exfiltrate customer records to an attacker-controlled email address.

| Dimension | Base Score | Adjustment | Final Score | Rationale |
|-----------|------------|------------|-------------|-----------|
| Damage | 7 | +1 (privilege) | 8 | Customer records exposed = high impact. Agent has CRM access = privilege amplification. |
| Reproducibility | 6 | 0 | 6 | Standard prompt injection works with some crafting. |
| Exploitability | 7 | +1 (privilege) | 8 | Publicly exposed chat interface + agent has CRM tool = easy to exploit. |
| Affected Users | 5 | 0 | 5 | All customers of the single tenant using this agent. |
| Discoverability | 7 | 0 | 7 | Public chat interface is easily discoverable. |
| **Total** | | | **34** | **Medium-High. Requires planned mitigation within next release.** |

### Example 2: DePIN Node Sybil Attack

**Threat:** An attacker creates 10,000 fake nodes to gain disproportionate voting power and fraudulent rewards.

| Dimension | Base Score | Adjustment | Final Score | Rationale |
|-----------|------------|------------|-------------|-----------|
| Damage | 8 | +1 (consensus) | 9 | Corrupts consensus and drains reward pool = catastrophic. |
| Reproducibility | 7 | +1 (autonomy) | 8 | Scripts can spawn nodes automatically. |
| Exploitability | 6 | 0 | 6 | Requires some capital for stake/registration, but tools are public. |
| Affected Users | 9 | 0 | 9 | All legitimate node operators lose rewards; network trust collapses. |
| Discoverability | 6 | +1 (consensus) | 7 | Economic incentive drives discovery; node operators notice anomalies. |
| **Total** | | | **39** | **High. Immediate action required: anti-Sybil measures, identity verification, slashing.** |

### Example 3: Agent Sandbox Escape

**Threat:** A coding agent with Python execution escapes its sandbox and gains host shell access.

| Dimension | Base Score | Adjustment | Final Score | Rationale |
|-----------|------------|------------|-------------|-----------|
| Damage | 8 | +1 (privilege) | 9 | Host-level access = full system compromise possible. |
| Reproducibility | 5 | 0 | 5 | Requires a specific vulnerability in the sandbox runtime. |
| Exploitability | 5 | +1 (privilege) | 6 | Requires some skill to find the sandbox escape, but agent provides the execution vector. |
| Affected Users | 6 | 0 | 6 | All agents running on the same host/cluster are at risk. |
| Discoverability | 4 | 0 | 4 | Requires analysis of sandbox implementation; not obvious from public interfaces. |
| **Total** | | | **30** | **Medium-High. Mitigation: sandbox hardening, gVisor, restricted system calls.** |

### Example 4: Model Weights Tampering (Supply Chain)

**Threat:** A compromised model repository serves a backdoored version of a popular open-source LLM.

| Dimension | Base Score | Adjustment | Final Score | Rationale |
|-----------|------------|------------|-------------|-----------|
| Damage | 9 | 0 | 9 | Backdoored model affects all downstream users; trust collapse. |
| Reproducibility | 8 | 0 | 8 | Anyone who downloads the compromised model reproduces the threat. |
| Exploitability | 4 | 0 | 4 | Requires compromising the model repository (supply chain attack). |
| Affected Users | 8 | 0 | 8 | All users and downstream applications of the model. |
| Discoverability | 3 | 0 | 3 | Hard to discover without cryptographic verification or model behavior analysis. |
| **Total** | | | **32** | **Medium-High. Mitigation: signed models, checksum verification, reproducible builds.** |

---

## Scoring Calculator Template

Use this template for each threat in your register:

```markdown
### Threat ID: [THREAT-001]
**Name:** [Short name]
**Description:** [Detailed description]
**STRIDE Category:** [S/T/R/I/D/E]
**DFD Element(s):** [Component/Flow IDs]

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Damage | 0-10 | [Why this score] |
| Reproducibility | 0-10 | [Why this score] |
| Exploitability | 0-10 | [Why this score] |
| Affected Users | 0-10 | [Why this score] |
| Discoverability | 0-10 | [Why this score] |
| **Total** | **0-50** | |

**Adjustments Applied:** [List any adjustments with justification]
**Final Priority:** [High / Medium / Low]
**Mitigation Plan:** [Specific mitigation with verification method]
```

---

## Common Scoring Pitfalls

### 1. The "Everything Is Medium" Trap
Without forced distribution, teams tend to score everything 5-6 across all dimensions. This defeats the purpose of prioritization. If you find all your threats scoring 25-30, force a ranking: what are the *top 3* threats that would cause the most harm? Score those higher.

### 2. Ignoring AI-Specific Adjustments
A threat that would be "medium" in a traditional web app may be "high" in an AI agent system because of autonomy and privilege amplification. Apply the adjustments rigorously.

### 3. Scoring Based on Mitigation Existence
Do not lower a score because a mitigation *already exists*. Score the threat as if the mitigation were absent. Then, separately document the mitigation's effectiveness. This prevents false confidence from untested controls.

### 4. Averaging Instead of Summing
DREAD uses a sum, not an average. A threat with one catastrophic dimension (Damage = 10) and four low dimensions should still be taken seriously. The sum preserves this signal.

### 5. Inconsistent Raters
If multiple people score threats, calibrate with 2-3 example threats first. Different people will interpret "moderate impact" differently. Calibration ensures consistency.

> **Pro Tip:** After scoring, sort your threat register by total score descending. Review the top 10% with the full team. These are your "must address" items. The bottom 20% are your "accept and monitor" items. Everything in between is your planned backlog.
