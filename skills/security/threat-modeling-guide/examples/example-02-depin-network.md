# Example 02: DePIN Network Node Threat Model

> **System:** A decentralized physical infrastructure network (DePIN) node that provides wireless coverage (e.g., a Helium-like network) and earns token rewards based on validated coverage proofs.  
> **Scope:** Node hardware, firmware, network communication, consensus participation, token economics, and oracle dependencies.  
> **Frameworks:** STRIDE, DREAD, MITRE ATT&CK (with DePIN custom extensions)  
> **Classification:** Certified example — for skill reference and training

---

## 1. System Overview

**Network Description:**
A DePIN wireless coverage network where participants deploy physical nodes (hotspots) that provide connectivity to IoT devices. Nodes submit periodic coverage proofs to the blockchain, which are validated by the network. Valid proofs earn token rewards. The network uses:
- Proof-of-Coverage (PoC) protocol for validating wireless coverage claims
- On-chain smart contracts for reward distribution and staking
- Off-chain oracles for verifying coverage quality and location data
- Decentralized governance for protocol upgrades and parameter changes

**Key Components:**
1. **Node Hardware** — Physical hotspot device with radio, CPU, storage, and networking
2. **Node Firmware** — Embedded software running on the node (Linux-based, containerized services)
3. **Node Operator** — Human who owns/operates the node, stakes tokens, and manages the device
4. **Radio Module** — Wireless transceiver for beaconing and IoT device communication
5. **GPS Module** — Location verification for coverage proof claims
6. **Local Data Store** — SQLite database for local telemetry and proof history
7. **Network Daemon** — Service that communicates with the blockchain and peer nodes
8. **Blockchain Validator** — Participates in consensus, submits transactions, validates blocks
9. **Smart Contracts** — On-chain reward distribution, staking, slashing, and governance
10. **Oracle Services** — Off-chain services verifying coverage data, location, and radio spectrum usage
11. **Peer Nodes** — Other nodes in the mesh network (gossip protocol)
12. **Token Holders / Governance** — Stakeholders who vote on protocol changes
13. **IoT Devices** — End devices that connect to the network via nodes

---

## 2. Data Flow Diagram (Level 1)

### Trust Boundaries
- **TB-1:** Internet → Node Hardware (untrusted → physical boundary)
- **TB-2:** Node Hardware → Node Firmware (physical → software boundary)
- **TB-3:** Node Firmware → Local Data Store (trusted internal → data boundary)
- **TB-4:** Node Firmware → Network Daemon (trusted internal → network boundary)
- **TB-5:** Network Daemon → Peer Nodes (trusted node → untrusted peer network)
- **TB-6:** Network Daemon → Blockchain (node → decentralized consensus)
- **TB-7:** Network Daemon → Oracle Services (node → trusted but centralized external)
- **TB-8:** Node Operator → Node Firmware (human → administrative boundary)
- **TB-9:** IoT Devices → Radio Module (untrusted device → physical radio boundary)
- **TB-10:** Smart Contracts → Token Holders (on-chain → human governance boundary)

### Data Flows (Selected Key Flows)

**DF-1: Coverage Proof Submission**
Node Hardware → Radio Module (beacon) → Peer Nodes (witness) → Network Daemon → Blockchain (transaction) → Smart Contracts (validation) → Oracle Services (verification) → Reward distribution

**DF-2: Peer Gossip / Sync**
Network Daemon → Peer Nodes → Network Daemon (blockchain state sync, transaction gossip)

**DF-3: Firmware Update**
Node Operator → Node Firmware → Network Daemon → Blockchain (governance proposal) → Firmware download → Node Firmware (update execution)

**DF-4: IoT Data Relay**
IoT Device → Radio Module → Node Firmware → Network Daemon → External Data Consumer (via API or smart contract event)

**DF-5: Staking / Governance Vote**
Node Operator → Wallet → Blockchain (stake transaction) → Smart Contracts (lock tokens) → Governance proposal voting

---

## 3. Threat Identification (STRIDE)

### S — Spoofing

| ID | Threat | DFD Element | Description | DePIN Context |
|----|--------|-------------|-------------|---------------|
| T-S01 | Fake node identity | TB-5 | An attacker registers a node with a stolen or fabricated identity key. | Attacker copies a legitimate node's public key and claims its identity on the network. |
| T-S02 | GPS spoofing | GPS Module | An attacker falsifies GPS coordinates to claim coverage in a location where no physical node exists. | A "virtual farmer" uses GPS spoofing to claim 100 nodes are in high-reward locations while the hardware is in a warehouse. |
| T-S03 | Oracle impersonation | TB-7 | An attacker intercepts oracle queries and responds with falsified verification data. | DNS hijacking of oracle endpoint causes nodes to accept fake coverage verification. |
| T-S04 | Compromised operator wallet | Node Operator | An attacker steals the operator's private key and controls the node on-chain identity. | Phishing attack on operator's wallet leads to loss of stake and node control. |
| T-S05 | Sybil node swarm | TB-5 | An attacker creates thousands of fake nodes from a single physical location. | 10,000 nodes registered from one IP/datacenter, gaming the reward distribution. |

### T — Tampering

| ID | Threat | DFD Element | Description | DePIN Context |
|----|--------|-------------|-------------|---------------|
| T-T01 | Falsified coverage proofs | DF-1 | A node submits fabricated coverage proof data to claim rewards for non-existent coverage. | Node operator modifies firmware to submit fake PoC beacons without actually transmitting radio signals. |
| T-T02 | Firmware tampering | DF-3 | An attacker modifies node firmware to introduce malicious behavior or backdoors. | Compromised firmware update server distributes backdoored firmware that exfiltrates operator keys. |
| T-T03 | Blockchain state manipulation | TB-6 | An attacker attempts to rewrite blockchain history or create a fraudulent fork. | Long-range attack using old validator keys to create a parallel chain with fraudulent rewards. |
| T-T04 | Local telemetry tampering | Local Data Store | A node operator modifies local telemetry before it is submitted to the network. | Operator edits SQLite database to hide downtime periods and maintain uptime reputation. |
| T-T05 | Smart contract exploitation | Smart Contracts | An attacker exploits a vulnerability in the reward distribution or staking contract. | Reentrancy bug in the staking contract allows an attacker to withdraw more stake than deposited. |
| T-T06 | Oracle data tampering | Oracle Services | An attacker feeds false data to the oracle to manipulate coverage verification. | A malicious oracle operator is bribed to approve falsified coverage proofs for a specific region. |

### R — Repudiation

| ID | Threat | DFD Element | Description | DePIN Context |
|----|--------|-------------|-------------|---------------|
| T-R01 | Unattributable coverage proof | DF-1 | A node submits a proof, but there is no cryptographic link between the proof and the node's physical hardware. | A node claims a coverage proof, but the network cannot verify that the physical device actually transmitted the beacon. |
| T-R02 | Missing operator action logs | Node Operator | An operator takes a destructive action (unstaking, slashing) with no immutable audit trail. | Operator initiates an emergency unstake. The reason is not recorded on-chain, making governance review impossible. |
| T-R03 | Tampered node logs | Local Data Store | A node operator deletes or modifies local logs to hide misbehavior. | Operator deletes logs showing the node was offline during a critical period. |
| T-R04 | Disputed oracle verification | Oracle Services | An oracle claims a coverage proof is invalid, but the node operator disputes this with no way to resolve. | Oracle rejects a proof due to a bug. Operator has no recourse because the oracle decision is final and unauditable. |
| T-R05 | Unverifiable IoT data relay | DF-4 | IoT data is relayed through the node, but there is no proof the node did not modify it. | A sensor sends temperature data. The node modifies the reading before relaying it to the data consumer. |

### I — Information Disclosure

| ID | Threat | DFD Element | Description | DePIN Context |
|----|--------|-------------|-------------|---------------|
| T-I01 | Node location exposure | GPS Module, TB-5 | A node's precise physical location is exposed through network metadata or gossip. | An attacker analyzes beacon timing and signal strength to triangulate the exact location of a node operator's home. |
| T-I02 | Operator wallet linkage | Node Operator | The on-chain identity of a node is linked to the operator's real-world identity. | Chain analysis correlates staking transactions with a KYC exchange, exposing the operator's identity. |
| T-I03 | IoT device data exposure | DF-4 | IoT data relayed through the network is intercepted or exposed. | Unencrypted IoT sensor data is visible to all nodes in the relay path, exposing business-sensitive information. |
| T-I04 | Firmware vulnerability exposure | Node Firmware | Firmware vulnerabilities are publicly disclosed before patches are deployed. | A CVE is published for the node's Linux kernel. 50% of nodes remain unpatched for 30 days, creating a large attack surface. |
| T-I05 | Stake concentration exposure | Smart Contracts | Public blockchain data reveals which operators hold large stakes, making them targets. | An attacker identifies the top 10 operators by stake and launches targeted phishing campaigns against them. |
| T-I06 | Peer network topology exposure | TB-5 | Gossip protocol metadata reveals the network topology and node relationships. | An attacker maps the entire network graph, identifying critical nodes for targeted attacks or eclipse attacks. |

### D — Denial of Service

| ID | Threat | DFD Element | Description | DePIN Context |
|----|--------|-------------|-------------|---------------|
| T-D01 | Network spam / congestion | TB-5 | An attacker floods the network with invalid transactions or gossip messages. | 1,000 fake nodes submit invalid coverage proofs, forcing validators to waste resources on verification. |
| T-D02 | Radio jamming | Radio Module | An attacker physically jams the radio frequency used by the network. | A competitor deploys radio jammers in a city, preventing legitimate nodes from transmitting beacons and earning rewards. |
| T-D03 | Blockchain congestion | TB-6 | An attacker floods the blockchain with transactions to increase fees and delay legitimate operations. | A spam attack raises transaction fees 100x, making it uneconomical for small operators to submit coverage proofs. |
| T-D04 | Node hardware sabotage | Node Hardware | An attacker physically damages or disables node hardware. | A vandal destroys outdoor node equipment, causing a coverage gap in a specific neighborhood. |
| T-D05 | Oracle service outage | Oracle Services | The oracle service becomes unavailable, halting coverage verification. | A DDoS attack on the oracle API prevents all nodes from receiving coverage verification for 24 hours. |
| T-D06 | Eclipse attack | TB-5 | An attacker isolates a target node by controlling all its peer connections. | An attacker spins up 50 malicious peers that become the only connections for a victim node, feeding it false blockchain state. |

### E — Elevation of Privilege

| ID | Threat | DFD Element | Description | DePIN Context |
|----|--------|-------------|-------------|---------------|
| T-E01 | Validator key compromise | Blockchain Validator | An attacker gains control of a validator's private key and manipulates consensus. | A top validator's key is stolen. The attacker creates fraudulent blocks, double-signs, and attempts to rewrite reward distribution. |
| T-E02 | Governance manipulation | Smart Contracts | An attacker accumulates voting power to pass malicious protocol changes. | An attacker buys 30% of governance tokens, passes a proposal to redirect 50% of rewards to their address. |
| T-E03 | Node privilege escalation | Node Firmware | A vulnerability in the node firmware allows an attacker to gain root access. | An attacker exploits an unpatched SSH vulnerability in the node's firmware to gain root and control the device. |
| T-E04 | Smart contract privilege escalation | Smart Contracts | An attacker exploits a contract to gain unauthorized administrative privileges. | An attacker discovers a missing `onlyOwner` check in the governance contract and self-appoints as admin. |
| T-E05 | Cross-node privilege escalation | TB-5 | A compromised node exploits trust relationships to control other nodes. | A compromised peer sends a malicious firmware update via the gossip protocol, infecting all connected nodes. |
| T-E06 | Stake manipulation | Smart Contracts | An attacker manipulates the staking mechanism to gain disproportionate influence. | A flash loan is used to temporarily acquire a large stake, vote on a governance proposal, and unstake immediately. |

---

## 4. Threat Prioritization (DREAD)

### Top 5 Threats (Highest Priority)

| Rank | Threat ID | Name | D | R | E | A | D | Total | Priority |
|------|-----------|------|---|---|---|---|---|-------|----------|
| 1 | T-E01 | Validator key compromise | 9 | 6 | 5 | 9 | 5 | 34 | High |
| 2 | T-T01 | Falsified coverage proofs | 8 | 8 | 7 | 8 | 7 | 38 | High |
| 3 | T-S05 | Sybil node swarm | 8 | 7 | 6 | 9 | 6 | 36 | High |
| 4 | T-E02 | Governance manipulation | 9 | 5 | 5 | 7 | 5 | 31 | High |
| 5 | T-T05 | Smart contract exploitation | 9 | 5 | 4 | 8 | 4 | 30 | High |

### DREAD Scoring Detail: T-E01 (Validator Key Compromise)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Damage | 9 | Validator key compromise enables block manipulation, double-signing, and consensus corruption. |
| Reproducibility | 6 | Key compromise requires specific targeting (phishing, malware) but is reproducible with known techniques. |
| Exploitability | 5 | Requires social engineering or malware. Not trivial but achievable with moderate resources. |
| Affected Users | 9 | A top validator may control 5-10% of network stake. Compromise affects all network participants. |
| Discoverability | 5 | Validators are public on-chain. Their identities may be discoverable through community participation or KYC. |
| **Total** | **34** | **High priority — immediate action: hardware security modules, multi-sig, key rotation.** |

### DREAD Scoring Detail: T-T01 (Falsified Coverage Proofs)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Damage | 8 | Falsified proofs drain rewards from legitimate operators and degrade network coverage quality. |
| Reproducibility | 8 | Proof-faking tools are publicly discussed in DePIN communities; scripts are readily available. |
| Exploitability | 7 | Requires firmware modification or GPS spoofing. Moderate technical skill. Tools are available. |
| Affected Users | 8 | All legitimate operators lose rewards. Network users experience degraded coverage. |
| Discoverability | 7 | High economic incentive drives discovery. Operators actively seek ways to maximize rewards. |
| **Total** | **38** | **High priority — immediate action: multi-source verification, slashing, hardware attestation.** |

### DREAD Scoring Detail: T-S05 (Sybil Node Swarm)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Damage | 8 | Sybil nodes distort reward distribution, reduce network quality, and enable other attacks (e.g., eclipse). |
| Reproducibility | 7 | Scripts to register multiple nodes from one location are widely shared. |
| Exploitability | 6 | Requires some capital for hardware/stake, but can be done at scale with cloud resources. |
| Affected Users | 9 | All legitimate node operators and network users are affected. |
| Discoverability | 6 | Economic incentive drives discovery. Network analytics can detect anomalies, but attackers adapt. |
| **Total** | **36** | **High priority — immediate action: proof-of-location, hardware attestation, stake requirements.** |

---

## 5. Mitigation Design

### T-E01: Validator Key Compromise

**Mitigation:**
- **Reduce:** Require hardware security modules (HSMs) or secure enclaves for validator key storage. Keys never leave the HSM.
- **Reduce:** Implement multi-signature validation for critical validator actions (block signing, reward distribution changes).
- **Reduce:** Enforce key rotation policies (e.g., quarterly) with automated rotation via threshold cryptography.
- **Transfer:** Use a validator key custody service (e.g., institutional custody) for operators who cannot manage HSMs.
- **Verify:** Quarterly key custody audits. HSM attestation logs reviewed monthly.

**Verification Method:**
- On-chain analysis confirms all validator keys are HSM-protected (no hot wallet signers).
- Key rotation logs show 100% compliance with quarterly rotation policy.

### T-T01: Falsified Coverage Proofs

**Mitigation:**
- **Reduce:** Multi-source verification: coverage proofs require independent witness nodes, oracle verification, and on-chain consensus.
- **Reduce:** Hardware attestation: nodes must provide Trusted Execution Environment (TEE) attestation proving the firmware and hardware are genuine.
- **Reduce:** Slashing: nodes caught submitting falsified proofs lose a portion of their stake.
- **Eliminate:** Remove single-source proof submission. Require at least 3 independent witnesses for each proof.
- **Verify:** Automated anomaly detection on proof patterns. Human review of flagged proofs.

**Verification Method:**
- Monthly audit: percentage of proofs with 3+ independent witnesses. Target: 100%.
- TEE attestation failure rate monitored daily. Target: <0.1%.
- Slashing events reviewed quarterly. Trend should be downward.

### T-S05: Sybil Node Swarm

**Mitigation:**
- **Reduce:** Proof-of-location: require nodes to pass cryptographic location verification (e.g., using cell tower triangulation, GPS + WiFi fingerprinting).
- **Reduce:** Minimum stake requirement: nodes must lock a significant token stake, making Sybil attacks economically expensive.
- **Reduce:** Hardware attestation: only approved hardware devices can join the network, preventing virtual node farming.
- **Reduce:** Rate limiting and uniqueness checks on node registration per IP/geography.
- **Verify:** Network analytics team monitors node distribution. Unusual clustering triggers investigation.

**Verification Method:**
- Network topology analysis shows geographic distribution. No more than 5% of nodes from any single /24 IP block.
- Hardware attestation pass rate: >99% of active nodes.
- Stake-weighted node count shows no single entity controls >10% of network.

### T-E02: Governance Manipulation

**Mitigation:**
- **Reduce:** Governance quorum requirements: proposals require high participation (e.g., 40% of staked tokens) to pass.
- **Reduce:** Time-delayed execution: passed proposals have a 7-day delay before execution, allowing review and veto.
- **Reduce:** Veto power: a security council or multi-sig can emergency-veto malicious proposals.
- **Reduce:** Voting power caps: no single address can control more than 5% of voting power (via quadratic voting or delegation limits).
- **Verify:** All governance proposals reviewed by the security council before execution delay expires.

**Verification Method:**
- Governance proposal logs show 100% security council review before execution.
- No emergency vetoes in the last 90 days (or if any, documented and justified).
- Voting power concentration analysis: Gini coefficient of voting power < 0.6.

### T-T05: Smart Contract Exploitation

**Mitigation:**
- **Eliminate:** Use formal verification for critical smart contracts (staking, rewards, governance).
- **Reduce:** Multiple independent audits by reputable firms before deployment.
- **Reduce:** Bug bounty program with significant rewards for critical findings.
- **Reduce:** Upgradeable proxy pattern with time-delayed upgrades and multi-sig control.
- **Verify:** Pre-deployment audit reports with all critical and high findings resolved.

**Verification Method:**
- All smart contracts have at least 2 independent audit reports on file.
- Formal verification certificates for staking and reward contracts.
- Bug bounty program has been active for >90 days with no unaddressed critical findings >30 days old.

---

## 6. Validation & Continuous Review

**Validation Activities:**
- Smart contract audit by at least 2 independent security firms
- Node firmware penetration testing (sandbox escape, privilege escalation, key extraction)
- Network-level red team: Sybil attack simulation, eclipse attack, consensus manipulation
- Oracle integrity testing: feed false data to test oracle rejection
- Physical security review of node hardware supply chain

**Review Schedule:**
- **Quarterly:** Full threat model review and DREAD rescoring
- **Pre-upgrade:** Review before any smart contract upgrade, firmware update, or protocol parameter change
- **Post-incident:** Update within 48 hours of any slashing event, consensus anomaly, or exploit attempt
- **Annual:** Comprehensive third-party security audit of the entire network stack

**Version:** v1.0.0  
**Last Reviewed:** 2026-06-24  
**Next Review:** 2026-09-24

---

## 7. MITRE ATT&CK Mapping (Selected)

| Threat ID | MITRE Technique | Tactic |
|-----------|----------------|--------|
| T-S01 | T1078 (Valid Accounts) | Initial Access, Privilege Escalation |
| T-S02 | T1591 (Gather Victim Network Information) | Reconnaissance |
| T-S05 | T1583 (Acquire Infrastructure) | Resource Development |
| T-T01 | T1565 (Data Manipulation) | Impact |
| T-T02 | T1495 (Firmware Corruption) | Impact |
| T-T03 | T1495 (Firmware Corruption) / custom CT-DePIN-004 | Impact |
| T-T05 | T1495 (Firmware Corruption) / T1659 (Content Injection) | Impact |
| T-R01 | T1070 (Indicator Removal) | Defense Evasion |
| T-D01 | T1490 (Network Denial of Service) | Impact |
| T-D02 | T1465 (Radio Frequency Hijacking) | Impact |
| T-D06 | T1490 (Network Denial of Service) / custom CT-DePIN-003 | Impact |
| T-E01 | T1078 (Valid Accounts) | Initial Access, Privilege Escalation |
| T-E02 | T1495 (Firmware Corruption) / T1659 (Content Injection) | Impact |
| T-E03 | T1611 (Escape to Host) | Privilege Escalation |
| T-E06 | T1495 (Firmware Corruption) | Impact |

---

> **Note:** This threat model addresses the unique risks of decentralized physical infrastructure. Traditional data center security models do not apply. The threat model must account for physical device integrity, economic incentive structures, and decentralized consensus mechanisms.
