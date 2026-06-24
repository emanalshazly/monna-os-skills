# Example 2: Auditing IoT Sensor Data Quality for a DePIN Network

> **Domain:** Decentralized Physical Infrastructure Networks (DePIN) / IoT  
> **Dataset:** Sensor telemetry from distributed environmental monitoring nodes  
> **Systems:** ESP32 sensor nodes (500+), LoRaWAN gateway, MQTT broker, TimescaleDB, Grafana dashboard, on-chain reward oracle  
> **Dimensions Audited:** Timeliness, Validity, Accuracy, Consistency  
> **Difficulty:** Advanced  
> **Time to Complete:** 5-7 days

---

## Phase 1: Scope Definition & Dimension Selection

### Dataset Boundary

| Attribute | Definition |
|-----------|------------|
| **Data source** | Environmental sensor nodes (temperature, humidity, PM2.5, noise level, GPS) |
| **Nodes included** | 487 active nodes out of 512 deployed (25 offline or decommissioned) |
| **Time range** | Last 30 days of telemetry (approx. 14M readings) |
| **Readings included** | All sensor readings with valid node_id and timestamp |
| **Readings excluded** | Test mode readings (node_id starts with "TEST_"), calibration records |
| **Systems in scope** | Sensor firmware, LoRaWAN gateway, MQTT broker, TimescaleDB, Grafana, on-chain oracle |
| **Data flow** | Sensor → LoRaWAN → Gateway → MQTT → Ingestion Service → TimescaleDB → Grafana / Oracle |

### Dimension Selection Rationale

| Dimension | Selected? | Rationale |
|-----------|-----------|-----------|
| **Accuracy** | ✅ Yes | Sensor drift, calibration errors, and environmental interference degrade measurement accuracy. Rewards depend on accurate readings. |
| **Completeness** | ❌ No | Expected reading cadence is every 5 minutes. Missing readings are primarily due to node downtime (a hardware/ops issue, not a data quality issue). |
| **Consistency** | ✅ Yes | Nodes report in different units, formats, and firmware versions. Cross-node consistency is required for network-level aggregation and reward fairness. |
| **Timeliness** | ✅ Yes | Reward calculation depends on readings arriving within a 15-minute window. Delayed readings are penalized and may be rejected by the oracle. |
| **Validity** | ✅ Yes | Sensor readings must fall within physically plausible ranges. Invalid readings (e.g., temperature = 999°C) must be detected and rejected before reward calculation. |
| **Uniqueness** | ❌ No | Each reading has a unique (node_id, timestamp) composite key. No duplication has been observed. |

### Severity Thresholds

| Dimension | Critical (0-49) | Warning (50-74) | Acceptable (75-89) | Good (90-97) | Excellent (98-100) |
|-----------|-----------------|-----------------|-------------------|--------------|-------------------|
| Accuracy | >10% readings outside tolerance | 5-10% outside tolerance | 2-5% outside tolerance | 0.5-2% outside tolerance | <0.5% outside tolerance |
| Timeliness | >20% readings delayed >15 min | 10-20% delayed >15 min | 5-10% delayed >15 min | 1-5% delayed >15 min | <1% delayed >15 min |
| Validity | >5% readings outside physical range | 2-5% outside range | 1-2% outside range | 0.5-1% outside range | <0.5% outside range |
| Consistency | >15% unit/format mismatch | 5-15% mismatch | 2-5% mismatch | 0.5-2% mismatch | <0.5% mismatch |

### Stakeholders

| Role | Name | Responsibility |
|------|------|--------------|
| Business Owner | DePIN Network Operator | Owns network health, token reward policy, and node operator relations |
| Technical Owner | Firmware Lead | Manages sensor firmware, calibration protocols, and OTA updates |
| Data Consumer | Reward Oracle Operator | Consumes validated readings for on-chain reward calculation |
| Data Consumer | Network Analyst | Uses data for network performance dashboards and anomaly detection |
| Data Engineer | Infrastructure Team | Manages LoRaWAN gateway, MQTT broker, TimescaleDB, and ingestion pipeline |
| External Stakeholder | Node Operators (500+) | Deploy and maintain physical sensors; affected by reward fairness |

---

## Phase 2: Baseline Assessment

### Timeliness Assessment

**Measurement Method:** Latency Measurement + SLA Compliance

| Stage | Expected Latency | Actual Latency (avg) | Actual Latency (p99) | SLA Compliance |
|-------|------------------|---------------------|---------------------|----------------|
| Sensor → LoRaWAN | <2 min | 1.2 min | 4.5 min | 98.2% |
| LoRaWAN → Gateway | <1 min | 0.8 min | 2.1 min | 99.5% |
| Gateway → MQTT | <30 sec | 0.4 min | 1.8 min | 99.1% |
| MQTT → Ingestion | <2 min | 1.5 min | 8.2 min | 96.4% |
| Ingestion → TimescaleDB | <1 min | 0.6 min | 3.5 min | 98.7% |
| **End-to-end (Sensor → DB)** | **<5 min** | **4.5 min** | **18.2 min** | **94.3%** |

| Oracle Window | Readings On-Time | Readings Delayed 15-30 min | Readings Delayed >30 min | Rejected by Oracle |
|---------------|-----------------|---------------------------|-------------------------|-------------------|
| 15-minute window | 94.3% | 3.2% | 2.5% | 2.5% |

**Timeliness Score: 76/100 (Acceptable)**

**Key Finding:** End-to-end latency exceeds the 5-minute expectation for 5.7% of readings. P99 latency is 18.2 minutes, which exceeds the 15-minute oracle window. The primary bottleneck is the MQTT → Ingestion stage, where a queue backlog occurs during peak hours (8-10 AM local time). 2.5% of readings are rejected by the oracle entirely, resulting in lost reward eligibility for node operators.

### Validity Assessment

**Measurement Method:** Range Validation + Cross-Field Validation

| Sensor | Physical Range | Readings Outside Range | % Invalid | Primary Invalid Value |
|--------|---------------|----------------------|-----------|----------------------|
| Temperature | -40°C to +60°C | 8,421 | 0.06% | 85.0°C (sensor in direct sunlight, no shielding) |
| Humidity | 0% to 100% | 2,105 | 0.02% | 102.0% (sensor malfunction) |
| PM2.5 | 0 to 500 μg/m³ | 14,247 | 0.10% | 999 μg/m³ (default error value from firmware) |
| Noise Level | 30 to 120 dB | 42,105 | 0.30% | 0 dB (microphone disconnected) |
| GPS Latitude | -90 to +90 | 1,247 | 0.009% | 999.0 (GPS fix failure) |
| GPS Longitude | -180 to +180 | 1,247 | 0.009% | 999.0 (GPS fix failure) |

**Validity Score: 82/100 (Acceptable)**

**Key Finding:** Noise level has the highest invalid rate (0.30%) due to disconnected microphones. The firmware sends `0` as a default value when the microphone is disconnected, which is within the valid range but physically impossible. This is a **validity rule gap** — the range check passes, but the value is semantically invalid.

PM2.5 has a similar issue: the firmware sends `999` as an error code, but the range check does not flag it because the upper bound is 500. This is a **range threshold issue**.

### Accuracy Assessment

**Measurement Method:** Physical Verification + External Reference Match

| Sensor | Tolerance | Calibration Age (avg) | Drift Test (vs. reference) | Error Rate | Score |
|--------|-----------|----------------------|---------------------------|------------|-------|
| Temperature | ±0.5°C | 4.2 months | 42/100 nodes >0.5°C drift | 8.6% | 91.4 |
| Humidity | ±3% RH | 4.2 months | 38/100 nodes >3% drift | 7.2% | 92.8 |
| PM2.5 | ±10% or ±10 μg/m³ | 6.1 months | 61/100 nodes out of tolerance | 12.4% | 87.6 |
| Noise Level | ±2 dB | N/A (no calibration protocol) | 78/100 nodes >2 dB deviation | 15.8% | 84.2 |
| GPS | ±10m | N/A | 23/100 nodes >10m offset | 4.6% | 95.4 |

**Accuracy Score: 88/100 (Acceptable)**

**Key Finding:** Noise level and PM2.5 accuracy are the weakest areas. Noise sensors have **no calibration protocol** — they were never calibrated since deployment. PM2.5 sensors are calibrated but the average calibration age is 6.1 months, and the manufacturer recommends recalibration every 3 months. Temperature and humidity sensors are within acceptable limits but approaching drift thresholds.

### Consistency Assessment

**Measurement Method:** Format Standardization Check + Cross-System Comparison

| Attribute | Expected Standard | Variations Found | Inconsistent Rate |
|-----------|------------------|------------------|-------------------|
| Temperature unit | Celsius | 3 nodes report Fahrenheit | 0.6% |
| Timestamp format | ISO 8601 UTC | 12 nodes use local time without timezone offset | 2.5% |
| Firmware version | SemVer (e.g., 2.1.4) | 47 nodes on v1.x (legacy format), 440 on v2.x | 9.7% |
| Node ID format | `DEPIN-XXXX` (hex) | 23 nodes use legacy `NODE_XXXX` format | 4.7% |
| PM2.5 reporting interval | 5 minutes | 34 nodes report every 1 minute (firmware bug), 8 nodes every 10 minutes | 8.6% |
| Sensor payload schema | JSON with defined keys | 5 nodes omit `gps_altitude` key; 2 nodes add `battery_voltage` in nested object | 1.4% |

**Consistency Score: 79/100 (Acceptable)**

**Key Finding:** Three consistency issues are caused by **firmware version fragmentation:**
1. v1.x nodes use different timestamp formats, node ID formats, and payload schemas
2. A firmware bug in v2.3.1 causes 34 nodes to report every minute instead of every 5 minutes
3. The ingestion service handles all variations, but the oracle applies inconsistent validation rules per format

---

## Phase 3: Root Cause Analysis

### Issue Mapping

| Issue ID | Dimension | Description | Root Cause | Category | Impact |
|----------|-----------|-------------|------------|----------|--------|
| DEPIN-001 | Timeliness | 5.7% readings delayed >15 min; 2.5% rejected by oracle | MQTT ingestion queue backlog during peak hours; no auto-scaling | Pipeline/ETL | Lost reward eligibility; node operator complaints |
| DEPIN-002 | Validity | 0.30% noise readings = 0 dB (disconnected mic) | Firmware sends 0 as default; no semantic invalidity check | Pipeline/ETL | Inaccurate network noise maps; false "quiet zone" alerts |
| DEPIN-003 | Validity | 0.10% PM2.5 readings = 999 μg/m³ (error code) | Firmware error code not excluded by range check | Business Rule | Inaccurate air quality alerts; inflated max values |
| DEPIN-004 | Accuracy | 15.8% noise sensors out of tolerance | No calibration protocol ever established | Human Process | Completely unreliable noise data; network reputation risk |
| DEPIN-005 | Accuracy | 12.4% PM2.5 sensors out of tolerance | Calibration schedule is 6+ months vs. 3-month recommendation | Human Process | Degraded air quality accuracy; regulatory reporting risk |
| DEPIN-006 | Consistency | 9.7% nodes on legacy firmware v1.x | OTA update campaign incomplete; some nodes unreachable | Source System | Inconsistent parsing; oracle validation gaps |
| DEPIN-007 | Consistency | 7.0% reporting interval mismatch | Firmware bug in v2.3.1; no forced update policy | Source System | Ingestion rate spikes; storage cost inflation |

### Lineage Tracing (Selected: DEPIN-001 — Timeliness Failure)

```
[Origin: ESP32 Sensor Node]
  ↓ Reading captured every 5 minutes (firmware loop)
  ↓ LoRaWAN radio transmission (SF7, 125kHz)
  ↓ [LoRaWAN Gateway]
    ↓ Packet forwarder (UDP to ChirpStack)
    ↓ Gateway buffer: holds up to 100 packets
  ↓ [ChirpStack Network Server]
    ↓ MQTT publish to topic "application/+/device/+/event/up"
    ↓ MQTT QoS 0 (at most once delivery)
  ↓ [MQTT Broker — Mosquitto]
    ↓ Single-node instance; no clustering
    ↓ Queue depth: 10,000 messages max
    ↓ Peak load: 8-10 AM = 1,620 messages/min (3x normal)
    ↓ During peak, queue fills in ~6 minutes
    ↓ Overflow messages dropped silently (QoS 0, no retry)
  ↓ [Ingestion Service — Python consumer]
    ↓ Single-threaded consumer; processes 120 messages/min
    ↓ During peak, consumer falls behind by 500+ messages
    ↓ Recovery takes 20-45 minutes after peak ends
  ↓ [TimescaleDB]
    ↓ Ingestion is fine; DB is not the bottleneck
  ↓ [Consumption: Grafana + On-Chain Oracle]
    ↓ Oracle reads last 15-minute window every 15 minutes
    ↓ Readings that arrive after window close are rejected

Point of Degradation: MQTT Broker queue overflow during peak hours
  - QoS 0 means dropped messages are lost forever
  - No monitoring alert for queue depth
  - No auto-scaling or consumer parallelism
Root Cause: Infrastructure under-provisioned for peak load; no message persistence
Scope: 2.5% of all readings (approx. 350K readings/month) rejected by oracle
Business Impact: Node operators lose rewards for valid readings; 47 complaints in last 30 days
```

---

## Phase 4: Remediation Roadmap

| Priority | Issue | Action | Owner | Effort | Dependencies | Milestone |
|----------|-------|--------|-------|--------|--------------|-----------|
| P0 | DEPIN-001 (Timeliness) | Upgrade MQTT to QoS 1; deploy clustered MQTT broker (HiveMQ/EMQX); add auto-scaling ingestion consumers | Infrastructure Team | L | Budget approval, broker selection | Day 30 |
| P0 | DEPIN-001 (Timeliness) | Add queue depth monitoring and alerting (PagerDuty) | Infrastructure Team | S | Monitoring stack | Day 15 |
| P1 | DEPIN-004 (Noise Accuracy) | Establish noise sensor calibration protocol; deploy calibrated reference stations per region | Firmware Lead | L | Reference station procurement | Day 60 |
| P1 | DEPIN-005 (PM2.5 Accuracy) | Enforce 3-month calibration schedule; notify node operators 2 weeks before due date | Firmware Lead | M | Calibration kit logistics | Day 45 |
| P2 | DEPIN-006 (Firmware Consistency) | Force OTA update for all v1.x nodes; sunset v1.x support after 30-day grace period | Firmware Lead | M | Node operator communication | Day 45 |
| P2 | DEPIN-007 (Interval Consistency) | Deploy v2.3.2 hotfix for interval bug; force update within 7 days | Firmware Lead | S | Hotfix validation | Day 14 |
| P2 | DEPIN-002 (Noise Validity) | Update ingestion validation: reject 0 dB readings as invalid; log for ops review | Infrastructure Team | S | Validation rule deployment | Day 7 |
| P2 | DEPIN-003 (PM2.5 Validity) | Update range check: reject 999 μg/m³ as error code; log for ops review | Infrastructure Team | S | Validation rule deployment | Day 7 |

---

## Phase 5: Continuous Monitoring & KPI Dashboard

### Monitoring KPIs

| KPI | Target | Warning Threshold | Critical Threshold | Measurement Method | Owner |
|-----|--------|-------------------|-------------------|-------------------|-------|
| % readings arriving within 15 min | >99% | 97% | 95% | Oracle acceptance log | Infrastructure Team |
| MQTT queue depth (max) | <5,000 | 7,000 | 9,000 | MQTT broker metrics | Infrastructure Team |
| % sensors within calibration window | >95% | 90% | 85% | Calibration registry | Firmware Lead |
| % readings passing validity checks | >99.5% | 99.0% | 98.5% | Ingestion service logs | Infrastructure Team |
| Firmware version consistency | >99% | 98% | 95% | Node heartbeat registry | Firmware Lead |
| Node operator complaint rate | <1% | 2% | 5% | Support ticket analysis | Network Operator |

### Alerting
- **Real-time:** PagerDuty alert if MQTT queue depth > 7,000
- **Daily:** Email report on oracle rejection rate and reasons
- **Weekly:** Firmware lead reviews calibration due list
- **Monthly:** Network operator reviews node operator complaint trends
- **Quarterly:** Full re-audit using this scorecard

---

## Executive Summary

The DePIN sensor network audit reveals a **functional but fragile data pipeline** with one critical infrastructure issue and two significant accuracy gaps. The **critical issue** is MQTT broker queue overflow during peak hours, causing 2.5% of valid readings to be rejected by the oracle and resulting in lost rewards for node operators. This is a **reputation and retention risk** — 47 complaints in 30 days indicates node operators are actively monitoring reward fairness.

The **accuracy gaps** in noise level (15.8% out of tolerance) and PM2.5 (12.4% out of tolerance) are caused by **missing calibration discipline**. Noise sensors have never been calibrated. PM2.5 sensors are 2x overdue for recalibration. These gaps degrade the network's data product value and create regulatory reporting risk if the data is used for environmental compliance.

Firmware fragmentation (9.7% on legacy v1.x) and a reporting interval bug (7.0% affected) create consistency issues that the ingestion service handles but the oracle does not fully validate. A forced OTA update campaign is required.

**Recommended immediate actions:**
1. **Day 7:** Deploy validity rule fixes (reject 0 dB and 999 μg/m³)
2. **Day 14:** Deploy firmware hotfix v2.3.2 for interval bug
3. **Day 15:** Add MQTT queue monitoring and alerting
4. **Day 30:** Upgrade to clustered MQTT broker with QoS 1 and auto-scaling consumers
5. **Day 45:** Enforce PM2.5 calibration schedule and begin noise sensor calibration protocol

---

> **Example Version:** 1.0.0 | **Aligned with:** DAMA-DMBOK Second Edition, Chapter 13 | **License:** MIT
> 
> **DePIN Context Note:** This example demonstrates how data quality auditing applies to decentralized infrastructure. The stakes are higher than traditional enterprise data because node operators are economically incentivized and will exit the network if data quality issues affect their rewards. The audit must balance technical rigor with operational practicality — a 100% perfect sensor network is economically impossible, but "fit for purpose" quality is essential for network sustainability.
