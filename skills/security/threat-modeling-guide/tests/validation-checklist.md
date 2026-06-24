# Validation Checklist

> Use this checklist to validate a threat model built with the `threat-modeling-guide` skill. This checklist is designed for peer reviewers, security architects, and auditors. Each item must be checked and marked PASS or FAIL with justification.

---

## Section 1: Document Completeness

| ID | Check | Criteria | Result | Notes |
|----|-------|----------|--------|-------|
| V-01 | SKILL.md exists and is complete | The `SKILL.md` file is present and contains all required sections: When to Use, Core Principles, Step-by-Step Process, Anti-Patterns, References, Examples, and Tests. | ☐ PASS / ☐ FAIL | |
| V-02 | All reference files present | `references/stride-framework.md`, `references/mitre-attack-mapping.md`, and `references/dread-scoring-guide.md` are all present and non-empty. | ☐ PASS / ☐ FAIL | |
| V-03 | All example files present | `examples/example-01-ai-agent-platform.md` and `examples/example-02-depin-network.md` are present and non-empty. | ☐ PASS / ☐ FAIL | |
| V-04 | Test file present | `tests/validation-checklist.md` is present and contains at least 20 check items. | ☐ PASS / ☐ FAIL | |
| V-05 | Metadata complete | Fingerprint, quality tier, compatibility matrix, last tested date, author, and license are all specified. | ☐ PASS / ☐ FAIL | |

---

## Section 2: Data Flow Diagram (DFD) Quality

| ID | Check | Criteria | Result | Notes |
|----|-------|----------|--------|-------|
| V-06 | DFD exists at Level 0 and Level 1 | At minimum, a context diagram (Level 0) and a detailed diagram (Level 1) are provided. | ☐ PASS / ☐ FAIL | |
| V-07 | All external entities identified | Users, systems, cloud providers, model providers, blockchain networks, and oracles are explicitly listed. | ☐ PASS / ☐ FAIL | |
| V-08 | All processes identified | Agents, orchestrators, nodes, runtimes, services, and smart contracts are explicitly listed. | ☐ PASS / ☐ FAIL | |
| V-09 | All data stores identified | Databases, vector stores, memory, configuration stores, model weights, audit logs, and secret managers are listed. | ☐ PASS / ☐ FAIL | |
| V-10 | Data flows are numbered and described | Every flow has a unique ID and a brief description of what data moves and in which direction. | ☐ PASS / ☐ FAIL | |
| V-11 | Trust boundaries are explicit and justified | Every trust boundary is drawn at a point where privilege, ownership, or trust model changes. Boundaries are not arbitrary. | ☐ PASS / ☐ FAIL | |
| V-12 | No "black box" processes | Every process has a single responsibility. There are no boxes labeled "AI System" or "The Platform." | ☐ PASS / ☐ FAIL | |
| V-13 | Agent-to-agent flows are modeled | In multi-agent systems, inter-agent communication flows and trust boundaries are explicitly shown. | ☐ PASS / ☐ FAIL | |

---

## Section 3: STRIDE Coverage

| ID | Check | Criteria | Result | Notes |
|----|-------|----------|--------|-------|
| V-14 | All six STRIDE categories are covered | The threat register contains at least one threat per STRIDE category. | ☐ PASS / ☐ FAIL | |
| V-15 | Threats are mapped to DFD elements | Every threat explicitly references one or more DFD elements (component, flow, or boundary). | ☐ PASS / ☐ FAIL | |
| V-16 | Threats have unique IDs | Every threat has a unique, consistent identifier (e.g., T-S01, T-T01). | ☐ PASS / ☐ FAIL | |
| V-17 | Threats are specific, not vague | No threat reads like "the system might be hacked." Every threat describes a specific attack vector and impact. | ☐ PASS / ☐ FAIL | |
| V-18 | AI-specific context is present | Threats in agent systems include AI-specific interpretations (prompt injection, model weights, jailbreak, etc.). | ☐ PASS / ☐ FAIL | |
| V-19 | DePIN-specific context is present (if applicable) | For DePIN systems, threats include consensus, oracle, node, and economic incentive considerations. | ☐ PASS / ☐ FAIL | |
| V-20 | Insider threats are included | The threat model includes threats from compromised operators, malicious model providers, and rogue agents—not just external attackers. | ☐ PASS / ☐ FAIL | |
| V-21 | Supply chain threats are included | Model weights, firmware, training data, and tool supply chain tampering are addressed. | ☐ PASS / ☐ FAIL | |
| V-22 | STRIDE reference is complete | `references/stride-framework.md` contains all six categories with AI-specific examples and mitigation patterns. | ☐ PASS / ☐ FAIL | |

---

## Section 4: Threat Prioritization (DREAD) Quality

| ID | Check | Criteria | Result | Notes |
|----|-------|----------|--------|-------|
| V-23 | All high-priority threats are scored | Every threat rated High or Medium has a complete DREAD score with justification. | ☐ PASS / ☐ FAIL | |
| V-24 | Scores are justified per dimension | Each dimension (Damage, Reproducibility, Exploitability, Affected Users, Discoverability) has a 1-2 sentence rationale. | ☐ PASS / ☐ FAIL | |
| V-25 | Scores are not all "medium" | There is a spread across the priority tiers. At least 20% of threats are High and at least 20% are Low. | ☐ PASS / ☐ FAIL | |
| V-26 | AI-specific adjustments are applied | Privilege amplification, autonomy multiplier, multi-agent cascade, and DePIN consensus bonuses are applied where relevant. | ☐ PASS / ☐ FAIL | |
| V-27 | DREAD reference is complete | `references/dread-scoring-guide.md` contains scoring rubrics, AI-specific adjustments, examples, and a calculator template. | ☐ PASS / ☐ FAIL | |
| V-28 | No scores are lowered because mitigations exist | Threats are scored as if no mitigations were in place. Mitigation effectiveness is documented separately. | ☐ PASS / ☐ FAIL | |

---

## Section 5: Mitigation Design Quality

| ID | Check | Criteria | Result | Notes |
|----|-------|----------|--------|-------|
| V-29 | Every high/medium threat has a mitigation | No high or medium threat is left without a planned mitigation. | ☐ PASS / ☐ FAIL | |
| V-30 | Mitigations are specific, not generic | No mitigation reads like "implement security best practices." Every mitigation names a specific control, technology, or process. | ☐ PASS / ☐ FAIL | |
| V-31 | Mitigations map to threats | Every mitigation explicitly addresses one or more threat IDs. No orphaned mitigations. | ☐ PASS / ☐ FAIL | |
| V-32 | Mitigation hierarchy is applied | Mitigations are categorized as Eliminate, Reduce, Transfer, or Accept. | ☐ PASS / ☐ FAIL | |
| V-33 | Verification methods are specified | Every mitigation includes a method for verifying it works (test, audit, metric, review). | ☐ PASS / ☐ FAIL | |
| V-34 | Residual risk is documented | For mitigations that do not eliminate the threat, the residual risk is explicitly stated and accepted. | ☐ PASS / ☐ FAIL | |

---

## Section 6: MITRE ATT&CK Alignment

| ID | Check | Criteria | Result | Notes |
|----|-------|----------|--------|-------|
| V-35 | MITRE reference file is complete | `references/mitre-attack-mapping.md` maps agent/DePIN threats to MITRE ATT&CK tactics and techniques. | ☐ PASS / ☐ FAIL | |
| V-36 | Relevant tactics are covered | At minimum: Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Collection, and Impact are addressed. | ☐ PASS / ☐ FAIL | |
| V-37 | DePIN custom techniques are included | Custom DePIN techniques (consensus manipulation, Sybil attack, eclipse attack, long-range attack, oracle manipulation) are mapped. | ☐ PASS / ☐ FAIL | |
| V-38 | Examples are specific and realistic | Each MITRE mapping includes a concrete example scenario relevant to AI agents or DePIN nodes. | ☐ PASS / ☐ FAIL | |
| V-39 | Example threat models include MITRE mapping | `example-01` and `example-02` include a MITRE ATT&CK mapping section. | ☐ PASS / ☐ FAIL | |

---

## Section 7: Example Quality

| ID | Check | Criteria | Result | Notes |
|----|-------|----------|--------|-------|
| V-40 | Example-01 is AI-agent-specific | The example focuses on a multi-agent platform with MCP tools, not a generic web application. | ☐ PASS / ☐ FAIL | |
| V-41 | Example-02 is DePIN-specific | The example focuses on a decentralized physical infrastructure network, not a generic blockchain. | ☐ PASS / ☐ FAIL | |
| V-42 | Examples include full DFDs | Both examples include Level 1 DFDs with trust boundaries and numbered flows. | ☐ PASS / ☐ FAIL | |
| V-43 | Examples include complete STRIDE analysis | Both examples include threat tables for all six STRIDE categories with AI/DePIN-specific context. | ☐ PASS / ☐ FAIL | |
| V-44 | Examples include DREAD scoring | Both examples include prioritized threat registers with DREAD scores and detailed rationale. | ☐ PASS / ☐ FAIL | |
| V-45 | Examples include specific mitigations | Both examples include mitigation plans with hierarchy, verification methods, and residual risk. | ☐ PASS / ☐ FAIL | |
| V-46 | Examples are technically accurate | Technical details (MCP protocol, vector databases, PoC, smart contracts, TEE) are accurate and realistic. | ☐ PASS / ☐ FAIL | |

---

## Section 8: Anti-Patterns and Boundaries

| ID | Check | Criteria | Result | Notes |
|----|-------|----------|--------|-------|
| V-47 | When NOT to Use is explicit | The skill clearly states it does not replace formal audits, compliance certifications, or penetration tests. | ☐ PASS / ☐ FAIL | |
| V-48 | At least 5 anti-patterns are documented | The SKILL.md includes 5+ anti-patterns with explanations and consequences. | ☐ PASS / ☐ FAIL | |
| V-49 | Anti-patterns are AI-specific | At least 2 anti-patterns are specific to AI/agent systems (e.g., "Overlook Agent-to-Agent Trust Boundaries"). | ☐ PASS / ☐ FAIL | |
| V-50 | Scope boundaries are clear | Physical security, legal compliance, and real-time incident response are explicitly excluded. | ☐ PASS / ☐ FAIL | |

---

## Section 9: Overall Quality

| ID | Check | Criteria | Result | Notes |
|----|-------|----------|--------|-------|
| V-51 | Language is precise and actionable | No vague statements like "ensure security." Every instruction is specific and executable. | ☐ PASS / ☐ FAIL | |
| V-52 | Consistent terminology | Terms like "agent," "MCP tool," "orchestrator," "DePIN," "node," and "trust boundary" are used consistently. | ☐ PASS / ☐ FAIL | |
| V-53 | No fabricated data or claims | All framework references (STRIDE, MITRE ATT&CK, DREAD) are accurate. No made-up technique IDs or framework elements. | ☐ PASS / ☐ FAIL | |
| V-54 | Evidence-based approach | The skill emphasizes evidence over assumption. Threats must be traceable to DFD elements. Mitigations must be verifiable. | ☐ PASS / ☐ FAIL | |
| V-55 | Living document guidance | The skill instructs users to version the threat model, schedule reviews, and update on architecture changes. | ☐ PASS / ☐ FAIL | |

---

## Scoring Summary

| Category | Total Checks | Required Passes | Status |
|----------|--------------|-----------------|--------|
| Document Completeness | 5 | 5 | ☐ |
| DFD Quality | 8 | 7 | ☐ |
| STRIDE Coverage | 9 | 8 | ☐ |
| DREAD Quality | 6 | 5 | ☐ |
| Mitigation Design | 6 | 5 | ☐ |
| MITRE ATT&CK Alignment | 5 | 4 | ☐ |
| Example Quality | 7 | 6 | ☐ |
| Anti-Patterns and Boundaries | 4 | 4 | ☐ |
| Overall Quality | 5 | 5 | ☐ |
| **TOTAL** | **55** | **48** | ☐ |

---

## Validation Result

**Overall Result:** ☐ **CERTIFIED** / ☐ **REQUIRES REVISION** / ☐ **REJECTED**

**Certification Criteria:**
- All checks in "Document Completeness" and "Anti-Patterns and Boundaries" must pass.
- At least 90% of checks in each remaining category must pass.
- Total passing checks must be at least 48 out of 55.
- No critical finding (e.g., fabricated framework data, missing DFD, no STRIDE coverage) may be present.

**Reviewer:** _________________________  
**Date:** _________________________  
**Version Reviewed:** _________________________  
**Findings Summary:** _________________________

---

> **Usage:** This checklist is intended for peer reviewers and auditors. A threat model that passes this checklist is considered "certified" under the `threat-modeling-guide` skill standards. A model that fails should be revised and re-submitted for validation.
