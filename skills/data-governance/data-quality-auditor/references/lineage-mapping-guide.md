# Data Lineage Mapping Guide

> **Purpose:** A step-by-step guide for tracing data quality issues through upstream systems, pipelines, and external sources. Use this guide during Phase 3 (Root Cause Analysis) of the data quality audit process.
>
> **Prerequisite:** Before using this guide, you should have completed Phase 2 (Baseline Assessment) and identified at least one dimension scoring below threshold.

---

## What Is Data Lineage?

Data lineage is the **complete lifecycle of data** — from its origin, through all transformations, to its final consumption. For data quality auditing, lineage answers the question: **"Where did this bad data come from, and how did it get here?"**

Lineage mapping is not about drawing pretty diagrams. It is about **documenting the path of data** so you can identify the exact point where quality degraded.

---

## Lineage Mapping Principles

### Principle 1: Trace to the Source, Not Just the Previous Step

A quality issue in a data warehouse may trace back through an ETL job, a staging database, an API integration, and finally to a third-party vendor. If you stop at the ETL job, you will fix the symptom, not the cause. Always trace to the **origin system** or the **point of first quality degradation**.

### Principle 2: Document Transformations, Not Just Connections

Knowing that "System A feeds System B" is not enough. You must document:
- What fields are mapped?
- What filters are applied?
- What aggregations or calculations occur?
- What business rules are enforced (or not enforced)?
- What data is dropped, split, or merged?

A transformation that drops 15% of records may explain a completeness issue. A calculation that uses a deprecated formula may explain an accuracy issue.

### Principle 3: Lineage Is Temporal

Data lineage changes over time. A field that was sourced from System A last year may now come from System B. A pipeline that used to validate email formats may have lost that validation in a recent deployment. Always capture the **time period** for which lineage is valid and check for recent changes.

### Principle 4: Not All Lineage Is Technical

Some data quality issues originate in **human processes**, not code:
- A business analyst manually uploaded a spreadsheet with incorrect mappings
- A data steward approved a reference data change without impact analysis
- A customer service representative entered data into a free-text field that should have been a dropdown

Document these human-in-the-loop steps as part of lineage.

---

## Step-by-Step Lineage Mapping Process

### Step 1: Identify the Quality Issue to Trace

From your scorecard, select one specific issue with a clear example. Do not trace "Accuracy is low." Trace "Customer phone number +1-555-0199 in record ID 48291 is incorrect."

| Field | Entry |
|-------|-------|
| **Issue ID** | |
| **Dimension** | |
| **Affected Field(s)** | |
| **Example Record ID(s)** | |
| **Observed Value** | |
| **Expected Value (if known)** | |
| **First Detected Date** | |

### Step 2: Map the Downstream Consumption Path

Start from the dataset where the issue was detected and work backward. Document every system, job, or process that touches this data.

| Stage | System/Process | Role | Timestamp/Version |
|-------|---------------|------|-------------------|
| **Detected Here** | [Target system] | Final consumption / reporting | |
| **Stage N** | [Previous system] | [Transformation / storage / integration] | |
| **Stage N-1** | [Previous system] | [Transformation / storage / integration] | |
| **...** | ... | ... | |
| **Origin** | [Source system] | Original creation / capture | |

### Step 3: Document Transformations at Each Stage

For each stage, fill in the transformation log:

| Stage | Input Fields | Output Fields | Transformation Type | Validation Applied | Records In | Records Out | Notes |
|-------|-------------|---------------|---------------------|-------------------|------------|-------------|-------|
| | | | ☐ Pass-through ☐ Filter ☐ Aggregate ☐ Calculate ☐ Join ☐ Split ☐ Merge ☐ Manual | | | | |

### Step 4: Compare Values Across Stages

Follow the example record through each stage and capture the value at each point.

| Stage | Field Value | Match to Expected? | Notes |
|-------|-------------|-------------------|-------|
| **Origin (System A)** | | ☐ Yes ☐ No | |
| **Stage 2 (ETL Job)** | | ☐ Yes ☐ No | |
| **Stage 3 (Staging DB)** | | ☐ Yes ☐ No | |
| **Stage 4 (Data Warehouse)** | | ☐ Yes ☐ No | |
| **Detected (Target System)** | | ☐ Yes ☐ No | |

### Step 5: Identify the Point of Degradation

The point of degradation is the **first stage where the value deviates from expected** or where a required transformation was not applied.

| Finding | Entry |
|---------|-------|
| **Point of Degradation** | [Stage name / system] |
| **Root Cause Category** | ☐ Source System ☐ Pipeline/ETL ☐ Business Rule ☐ Human Process ☐ External ☐ Temporal |
| **Specific Cause** | |
| **When Did It Start?** | |
| **Scope of Impact** | [Number of records / percentage of dataset] |
| **Is This Fixable at Source?** | ☐ Yes ☐ No ☐ Partially |
| **Recommended Fix Location** | |

### Step 6: Document Secondary Effects

Quality issues often cascade. A completeness problem in an upstream system may cause a validity problem downstream. An accuracy problem in a reference table may cause consistency problems across ten downstream systems. Document these ripple effects.

| Downstream System | Effect Type | Description | Severity |
|-------------------|-------------|-------------|----------|
| | ☐ Completeness ☐ Accuracy ☐ Consistency ☐ Timeliness ☐ Validity ☐ Uniqueness | | |

---

## Lineage Mapping Techniques

### Technique 1: Automated Lineage Tools

If your organization uses a data catalog or lineage tool (e.g., Apache Atlas, Collibra, Alation, DataHub, Monte Carlo, Bigeye), use it to:
- Auto-generate lineage graphs
- Track field-level lineage (not just table-level)
- Identify upstream dependencies
- Alert on schema changes that affect downstream systems

**Limitation:** Automated tools often miss:
- ETL logic inside stored procedures or custom scripts
- Manual data entry or spreadsheet uploads
- External API transformations
- Human approval workflows

### Technique 2: Code Review

For pipeline stages without automated lineage, review the source code:
- SQL scripts (look for JOINs, WHERE clauses, CASE statements, CASTs)
- ETL tool configurations (Informatica, Talend, dbt, Airflow DAGs)
- API integration code (payload mappings, error handling, retry logic)
- Custom scripts (Python, Spark, shell scripts)

**What to look for:**
- Hardcoded values or business rules that may be outdated
- Missing or incomplete error handling
- Implicit type conversions
- Filters that drop records without logging
- Joins that produce duplicates or lose records

### Technique 3: Interview-Based Mapping

When automated tools and code review are insufficient, interview the people who built or maintain the pipeline:

| Role | Questions to Ask |
|------|-----------------|
| **Data Engineer** | "Walk me through the ETL job that loads this table. What validations run? What gets dropped?" |
| **Business Analyst** | "Where does this field come from? Who enters it? Is it ever calculated or derived?" |
| **Data Steward** | "When was the last time the reference data for this field changed? Who approved it?" |
| **Source System Owner** | "Does your system validate this field before sending it? What happens if validation fails?" |
| **External Vendor** | "What is your data quality SLA? How do you handle anomalies or missing values in the feed?" |

### Technique 4: Temporal Comparison

If the issue is recent, compare the lineage before and after the issue started:
- Check code version history (Git commits, deployment logs)
- Check schema change logs
- Check reference data change history
- Check ETL job schedule or configuration changes

---

## Common Lineage Patterns and Their Quality Implications

| Pattern | Description | Typical Quality Impact |
|---------|-------------|----------------------|
| **The Long Chain** | Data passes through 5+ systems before consumption | Errors compound; timeliness degrades; root cause is hard to trace |
| **The Spider Web** | One source feeds 10+ downstream systems | A single source issue creates widespread, inconsistent problems |
| **The Black Box** | A system or process has no documentation or code access | Root cause analysis is blocked; must rely on interviews and inference |
| **The Human Bridge** | Data is manually transferred between systems (e.g., spreadsheet upload) | High accuracy and completeness risk; no audit trail; temporal gaps |
| **The API Roulette** | Third-party API changes without notice | Validity and accuracy issues appear suddenly; no internal control |
| **The Stale Copy** | A downstream system maintains its own copy of reference data | Consistency issues when reference data updates are not propagated |
| **The Silent Drop** | ETL job drops invalid records without logging | Completeness issues are hidden; no trace of what was lost |

---

## Lineage Documentation Standards

At minimum, your lineage documentation should include:

1. **System inventory** — Every system that touches the data, with owner and contact
2. **Field-level mapping** — Which fields map to which fields at each stage
3. **Transformation logic** — What happens to the data at each stage
4. **Validation rules** — What checks are applied and what happens on failure
5. **Change history** — When the lineage last changed and why
6. **Known gaps** — What you could not trace and what you assumed

---

## Example Lineage Map (Text Format)

```
[Origin: Salesforce CRM]
  ↓ API daily sync (MuleSoft)
  ↓ Filter: only Active accounts
  ↓ Validation: email format checked, invalid emails set to NULL
  ↓ [Staging: AWS S3 raw/]
    ↓ dbt transformation (staging → warehouse)
    ↓ JOIN with HubSpot contacts on email
    ↓ Deduplication: keep most recent updated record
    ↓ [Warehouse: Snowflake analytics.customers]
      ↓ Tableau extract (nightly)
      ↓ [Consumption: Tableau Customer Dashboard]

Point of Degradation: dbt deduplication stage
  - JOIN with HubSpot created duplicate customer records
  - Deduplication logic "keep most recent" is incorrect for merged accounts
  - Result: Some merged accounts show outdated Salesforce data instead of current HubSpot data
Root Cause: Business rule ambiguity — "most recent" was not defined for merged accounts
Scope: 347 records (2.1% of customer base)
```

---

> **Scope Note:** Lineage mapping requires access to systems, code, and people. If you lack access to a critical stage, document it as a **lineage gap** and add "improve lineage visibility" to the remediation roadmap. Do not guess or assume transformations you cannot verify.
