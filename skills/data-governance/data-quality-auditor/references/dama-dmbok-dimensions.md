# DAMA-DMBOK Data Quality Dimensions Reference

> **Purpose:** This reference provides a complete mapping of the six DAMA-DMBOK data quality dimensions used by the `data-quality-auditor` skill. Each dimension includes a formal definition, measurement approaches, common failure modes, and scoring guidance.
> 
> **Source:** Aligned with DAMA International, *Data Management Body of Knowledge (DAMA-DMBOK)*, Second Edition, Chapter 13: Data Quality.

---

## Dimension Overview

| Dimension | DAMA-DMBOK Definition | Core Question |
|-----------|----------------------|---------------|
| **Accuracy** | The degree to which data correctly describes the real-world object or event it represents | Does this data match reality? |
| **Completeness** | The degree to which all required data is present | Are all required fields populated? |
| **Consistency** | The degree to which data is represented the same way across systems and over time | Is this data represented uniformly? |
| **Timeliness** | The degree to which data is available when expected and needed for its intended use | Is this data available when needed? |
| **Validity** | The degree to which data conforms to defined syntax and business rules | Does this data conform to the rules? |
| **Uniqueness** | The degree to which there is only one representation of an entity in a dataset | Is each entity represented only once? |

---

## Dimension 1: Accuracy

### Definition
Accuracy measures whether data correctly describes the real-world object or event it represents. It is the most business-critical dimension because inaccurate data leads to incorrect decisions, regardless of how complete or timely it is.

### Key Insight from DAMA-DMBOK
Accuracy is **context-dependent**. A customer's address may be accurate for billing but inaccurate for delivery if they have a separate shipping location. Always specify the use case when measuring accuracy.

### Measurement Approaches

| Approach | Method | Best For |
|----------|--------|----------|
| **System of Record Comparison** | Compare dataset values against a verified source system | Customer master data, financial records |
| **Physical Verification** | Sample records and verify against physical reality (e.g., visit a location, call a phone number) | Asset inventories, location data |
| **External Reference Match** | Cross-reference against authoritative third-party datasets (e.g., postal databases, regulatory filings) | Address data, company registration data |
| **Business Rule Validation** | Check if calculated values are mathematically correct (e.g., revenue = price × quantity) | Financial transactions, derived metrics |
| **Expert Review** | Have domain experts validate a statistically significant sample | Complex domain data (medical, legal, scientific) |

### Common Failure Modes
- **Source system drift:** The upstream system was accurate at one point but has since diverged from reality
- **Transcription errors:** Manual data entry mistakes (typos, misheard values, copy-paste errors)
- **Unit confusion:** Values recorded in wrong units (meters vs. feet, USD vs. local currency)
- **Temporal decay:** Data was accurate when collected but has become outdated (e.g., customer moved, product specs changed)
- **Calculated field errors:** Derived values using incorrect formulas or stale base data

### Scoring Guidance (0-100)

| Score Range | Description | Action |
|-------------|-------------|--------|
| 95-100 | Highly accurate. Error rate < 1% against system of record | Maintain current controls |
| 85-94 | Good accuracy. Error rate 1-5%. Some issues in specific sub-populations | Investigate and remediate specific sub-populations |
| 70-84 | Moderate accuracy. Error rate 5-15%. Patterns suggest systemic issues | Conduct root cause analysis; prioritize high-impact records |
| 50-69 | Poor accuracy. Error rate 15-30%. Significant decision risk | Halt dependent processes; emergency remediation required |
| 0-49 | Critical accuracy failure. Error rate > 30%. Data is not fit for purpose | Do not use for any business decision; full remediation required |

---

## Dimension 2: Completeness

### Definition
Completeness measures whether all required data is present. It is not about whether the dataset is "full" — it is about whether every **required field** for a specific use case has a value.

### Key Insight from DAMA-DMBOK
Completeness must be measured against a **schema or requirement specification**, not a vague sense of "fullness." A dataset with 100 fields may be 100% complete for one use case (needing only 10 fields) and 40% complete for another (needing 40 fields).

### Measurement Approaches

| Approach | Method | Best For |
|----------|--------|----------|
| **Required Field Null Check** | Count records where required fields are NULL, empty, or placeholder values | Structured databases with defined schemas |
| **Schema Coverage Analysis** | Compare actual populated fields against a target schema or data dictionary | Data warehouse tables, API response schemas |
| **Record-Level Completeness** | Calculate % of required fields populated per record; aggregate to dataset level | Customer records, product catalogs |
| **Conditional Completeness** | Check completeness only for records meeting a condition (e.g., "if status = 'Active', then email must be present") | Business-rule-dependent datasets |
| **Temporal Completeness** | Check if expected data arrives for every time period (e.g., daily sensor readings) | Time-series data, scheduled reports |

### Common Failure Modes
- **Optional field confusion:** Fields that were truly optional at design time are now required for a new use case, but the schema was never updated
- **System integration gaps:** Two systems were integrated but not all fields were mapped
- **Conditional logic errors:** Business rules for when a field is required are ambiguous or inconsistently implemented
- **Batch loading failures:** Partial loads leave gaps that are not detected
- **UI/UX issues:** Front-end forms allow submission without validating required fields

### Scoring Guidance (0-100)

| Score Range | Description | Action |
|-------------|-------------|--------|
| 98-100 | Fully complete. All required fields populated for all records | No action needed |
| 90-97 | High completeness. Small gaps in non-critical fields or edge cases | Monitor; address if cost is low |
| 75-89 | Moderate completeness. Gaps in some required fields; may affect specific processes | Identify which processes are affected; prioritize remediation |
| 50-74 | Low completeness. Significant gaps; multiple processes likely impacted | Process-level impact assessment; roadmap required |
| 0-49 | Critical incompleteness. Data is not usable for intended purpose | Do not use; halt dependent processes |

---

## Dimension 3: Consistency

### Definition
Consistency measures whether data is represented the same way across systems and over time. It is about **semantic equivalence**, not syntactic uniformity. Two systems may store the same information differently (e.g., "Active" vs. "1") and still be consistent if the mapping is maintained.

### Key Insight from DAMA-DMBOK
Inconsistency is only a problem when it causes **ambiguity, duplication, or integration failure.** If two systems store dates in different formats but integration handles the conversion correctly, there is no consistency problem.

### Measurement Approaches

| Approach | Method | Best For |
|----------|--------|----------|
| **Cross-System Comparison** | Compare values for the same entity across systems and flag mismatches | Customer data across CRM, ERP, and marketing systems |
| **Reference Data Alignment** | Check whether code values (status codes, country codes, product categories) match the master reference data | Coded fields, classification systems |
| **Temporal Stability Check** | Compare current values against historical snapshots for unexpected changes | Master data that should change slowly (customer name, product SKU) |
| **Format Standardization Check** | Verify whether text, date, and numeric fields follow agreed formats | Phone numbers, addresses, dates, identifiers |
| **Semantic Equivalence Test** | Verify that different representations map to the same meaning (e.g., "US", "USA", "United States" all map to the same country) | Free-text categorical fields |

### Common Failure Modes
- **Reference data drift:** Master code lists are updated in one system but not propagated to others
- **Migration artifacts:** Data was migrated between systems and transformation rules were inconsistent
- **Multiple entry points:** The same entity can be created in different systems with different validation rules
- **Temporal format changes:** A system changed its date format or encoding standard without backward compatibility
- **Case sensitivity issues:** "Active", "active", and "ACTIVE" treated as different values

### Scoring Guidance (0-100)

| Score Range | Description | Action |
|-------------|-------------|--------|
| 95-100 | Highly consistent. All cross-system and temporal checks pass | Maintain reference data governance |
| 85-94 | Good consistency. Minor mismatches in non-critical fields; mapping is maintained | Audit reference data synchronization |
| 70-84 | Moderate consistency. Some cross-system mismatches; integration may be affected | Map all mismatches; assess integration impact |
| 50-69 | Poor consistency. Frequent mismatches; known integration failures | Prioritize critical integration paths; remediation roadmap |
| 0-49 | Critical inconsistency. Data is not interoperable across systems | Halt cross-system processes; full alignment required |

---

## Dimension 4: Timeliness

### Definition
Timeliness measures whether data is available when expected and needed for its intended use. It has two components: **latency** (how long after the event the data is available) and **currency** (how up-to-date the data is when accessed).

### Key Insight from DAMA-DMBOK
Timeliness is **use-case dependent.** Real-time fraud detection requires sub-second latency. Quarterly financial reporting can tolerate days or weeks of latency. Always define the business process and its latency requirement before measuring timeliness.

### Measurement Approaches

| Approach | Method | Best For |
|----------|--------|----------|
| **Latency Measurement** | Calculate time between event occurrence and data availability in the target system | Streaming data, transaction processing |
| **Currency Check** | Compare "last updated" timestamp against current time for a sample of records | Master data, reference data |
| **SLA Compliance** | Check whether data arrival meets documented service-level agreements | Scheduled data feeds, ETL jobs |
| **End-to-End Pipeline Timing** | Measure total time from source event to final consumption | Complex multi-stage pipelines |
| **Business Process Alignment** | Interview stakeholders to verify whether data arrives in time for their decision points | Strategic planning, operational dashboards |

### Common Failure Modes
- **ETL job delays:** Scheduled jobs fail or run late, causing downstream data to be stale
- **Source system latency:** The upstream system itself does not produce data in real time
- **Network/transfer bottlenecks:** Large data transfers between systems cause delays
- **Queue backlogs:** Message queues or streaming platforms accumulate lag
- **Manual process delays:** Human approval or review steps introduce unpredictable delays
- **Clock skew:** Different systems have unsynchronized clocks, making timestamps unreliable

### Scoring Guidance (0-100)

| Score Range | Description | Action |
|-------------|-------------|--------|
| 95-100 | Fully timely. Data meets or exceeds latency requirements for all use cases | Maintain current pipeline performance |
| 85-94 | Good timeliness. Occasional minor delays; no business impact | Monitor SLA compliance; investigate trends |
| 70-84 | Moderate timeliness. Frequent delays affecting some use cases | Identify bottleneck stages; capacity planning |
| 50-69 | Poor timeliness. Significant delays; business decisions made with stale data | Escalate to engineering; interim manual workarounds |
| 0-49 | Critical timeliness failure. Data is effectively unusable for real-time or near-real-time needs | Halt time-sensitive processes; emergency pipeline review |

---

## Dimension 5: Validity

### Definition
Validity measures whether data conforms to defined syntax and business rules. It is about **structural correctness**, not semantic accuracy. A phone number may be structurally valid (correct number of digits) but belong to a non-existent line (accuracy issue).

### Key Insight from DAMA-DMBOK
Validity rules must be **explicitly documented and agreed upon.** What is "valid" is a business decision, not a technical absolute. A "valid" email address format depends on your organization's policy on subdomains, special characters, and length limits.

### Measurement Approaches

| Approach | Method | Best For |
|----------|--------|----------|
| **Syntax Validation** | Check against regex patterns, data type constraints, and length limits | Email addresses, phone numbers, identifiers |
| **Range Validation** | Check numeric values against minimum/maximum bounds | Ages, prices, temperatures, percentages |
| **Enumeration Check** | Verify values are in an allowed list of valid values | Status codes, country codes, product categories |
| **Cross-Field Validation** | Verify relationships between fields (e.g., "end date must be after start date") | Date ranges, financial calculations |
| **Format Validation** | Check adherence to standard formats (ISO 8601, E.164, IBAN, etc.) | Dates, phone numbers, bank account numbers |
| **Referential Integrity** | Check foreign key relationships exist in referenced tables | Relational databases |

### Common Failure Modes
- **Missing validation rules:** Fields accept any input because constraints were never defined
- **Rule evolution without enforcement:** Business rules changed but validation logic was not updated
- **Unicode/encoding issues:** Special characters, non-ASCII text, or encoding mismatches cause validation failures
- **Third-party data violations:** External feeds contain values that violate your business rules
- **Ambiguous rules:** Business rules are contradictory or poorly defined (e.g., "password must be simple but secure")
- **Temporal rule violations:** Values that were valid at one time are no longer valid (e.g., expired product codes)

### Scoring Guidance (0-100)

| Score Range | Description | Action |
|-------------|-------------|--------|
| 98-100 | Fully valid. All records pass all defined validation rules | Maintain rule documentation; review periodically |
| 90-97 | High validity. Small violations in non-critical fields or edge cases | Investigate edge cases; tighten rules if needed |
| 75-89 | Moderate validity. Significant violations in some fields; may indicate rule gaps | Review and update validation rules; assess business impact |
| 50-74 | Low validity. Frequent violations; data integrity at risk | Comprehensive rule review; halt processes that depend on affected fields |
| 0-49 | Critical validity failure. Most records violate rules; data is structurally unreliable | Emergency rule definition and enforcement; do not use for automated processing |

---

## Dimension 6: Uniqueness

### Definition
Uniqueness measures whether there is only one representation of an entity in a dataset. It is about **eliminating unwanted duplication**, not enforcing absolute uniqueness. Some legitimate business scenarios require multiple representations (e.g., a customer with personal and business accounts).

### Key Insight from DAMA-DMBOK
Uniqueness must be defined at the **entity level**, not the record level. Two records for the same customer are a uniqueness problem only if they are unintended duplicates. Two records for two different customers with the same name are not a uniqueness problem.

### Measurement Approaches

| Approach | Method | Best For |
|----------|--------|----------|
| **Exact Duplicate Detection** | Count records that are identical across all fields | Batch-loaded data, imported datasets |
| **Fuzzy Duplicate Detection** | Use string similarity algorithms (Levenshtein, Jaro-Winkler, phonetic matching) to identify near-duplicates | Customer names, company names, addresses |
| **Key-Based Uniqueness** | Verify that declared unique keys (primary keys, composite keys) are truly unique | Database tables with primary keys |
| **Business Entity Resolution** | Apply business rules to determine if two records represent the same entity (e.g., same email + same phone = same person) | Customer databases, contact lists |
| **Golden Record Analysis** | Compare records against a master data management (MDM) golden record | Organizations with MDM systems |

### Common Failure Modes
- **No unique key defined:** The dataset has no primary key or composite key, making duplication inevitable
- **System integration without deduplication:** Multiple systems create the same entity independently
- **Partial matching:** Two records represent the same entity but have slightly different values (e.g., "John Doe" vs. "Jon Doe")
- **Temporal duplicates:** The same entity was created multiple times over time because old records were not archived
- **Legitimate duplicates treated as errors:** Business rules allow multiple accounts, but the audit flags them as duplicates

### Scoring Guidance (0-100)

| Score Range | Description | Action |
|-------------|-------------|--------|
| 98-100 | Fully unique. No unintended duplicates detected | Maintain deduplication processes |
| 90-97 | High uniqueness. Small number of near-duplicates; likely manual entry variation | Review fuzzy match results; consolidate if appropriate |
| 75-89 | Moderate uniqueness. Significant duplication in specific sub-populations | Implement entity resolution for affected sub-populations |
| 50-74 | Low uniqueness. Widespread duplication; data volume inflated | Halt analytics that depend on entity counts; deduplication project required |
| 0-49 | Critical uniqueness failure. Most entities have multiple representations | Full entity resolution initiative; do not use for count-based metrics |

---

## Dimension Selection Matrix

Not all dimensions apply to every dataset. Use this matrix to select dimensions for your audit:

| Dataset Type | Recommended Dimensions | Rationale |
|--------------|----------------------|-----------|
| **Customer Master Data (CRM)** | Accuracy, Completeness, Consistency, Uniqueness | Customer data is shared across systems; accuracy and uniqueness are critical for sales and support |
| **Transaction Data** | Accuracy, Validity, Timeliness | Transactions must be correct, structurally valid, and available in real time for operations |
| **Reference Data (code lists)** | Consistency, Validity, Uniqueness | Reference data must be uniform across systems and strictly valid |
| **IoT/Sensor Data** | Timeliness, Validity, Accuracy | Sensor data is time-critical and must be structurally valid; accuracy depends on calibration |
| **Financial Reports** | Accuracy, Completeness, Consistency | Financial data must be correct, include all required elements, and match across reports |
| **Marketing Lists** | Completeness, Validity, Uniqueness | Marketing needs contactable records (valid emails/phones), no gaps in key fields, and no duplicates |

---

> **Evidence-Gated Note:** All dimension definitions and scoring guidance in this reference are derived from DAMA-DMBOK Second Edition, Chapter 13. Scoring thresholds are calibrated for general business use. Adjust thresholds based on your specific risk tolerance and regulatory environment.
