# Example 1: Auditing Customer Data Quality in a CRM System

> **Domain:** Customer Relationship Management (CRM)  
> **Dataset:** Customer accounts, contacts, and opportunity records  
> **Systems:** Salesforce CRM (primary), HubSpot (marketing), ERP (billing), support ticketing system  
> **Dimensions Audited:** Accuracy, Completeness, Consistency, Uniqueness  
> **Difficulty:** Intermediate  
> **Time to Complete:** 3-5 days

---

## Phase 1: Scope Definition & Dimension Selection

### Dataset Boundary

| Attribute | Definition |
|-----------|------------|
| **Tables included** | `Account`, `Contact`, `Opportunity` |
| **Fields included** | All standard fields + 12 custom fields used by sales and support |
| **Time range** | Accounts created or updated in the last 24 months |
| **Records included** | 16,482 active accounts, 34,105 contacts, 8,920 open opportunities |
| **Records excluded** | Archived accounts, leads (not yet converted), test records |
| **Systems in scope** | Salesforce (primary), HubSpot (sync), ERP (billing sync), support system (sync) |

### Dimension Selection Rationale

| Dimension | Selected? | Rationale |
|-----------|-----------|-----------|
| **Accuracy** | ✅ Yes | Customer data directly affects revenue forecasting, support routing, and billing |
| **Completeness** | ✅ Yes | Missing fields cause sales reps to waste time on incomplete records |
| **Consistency** | ✅ Yes | Four systems sync customer data; mismatches cause operational confusion |
| **Timeliness** | ❌ No | Data is batch-synced nightly; latency is acceptable for all use cases |
| **Validity** | ❌ No | Salesforce enforces strict validation; historical audit shows 99%+ validity |
| **Uniqueness** | ✅ Yes | Duplicate customer records are a known problem; sales team reports frequent duplicates |

### Severity Thresholds

| Dimension | Critical (0-49) | Warning (50-74) | Acceptable (75-89) | Good (90-97) | Excellent (98-100) |
|-----------|-----------------|-----------------|-------------------|--------------|-------------------|
| Accuracy | >15% error | 5-15% error | 2-5% error | 0.5-2% error | <0.5% error |
| Completeness | >30% missing | 15-30% missing | 5-15% missing | 1-5% missing | <1% missing |
| Consistency | >20% mismatch | 10-20% mismatch | 5-10% mismatch | 1-5% mismatch | <1% mismatch |
| Uniqueness | >10% duplicates | 5-10% duplicates | 2-5% duplicates | 0.5-2% duplicates | <0.5% duplicates |

### Stakeholders

| Role | Name | Responsibility |
|------|------|--------------|
| Business Owner | VP of Sales | Owns CRM data strategy; approves remediation budget |
| Technical Owner | Salesforce Admin | Manages CRM configuration, validation rules, integrations |
| Data Consumer | Sales Operations | Uses data for forecasting, territory planning, commission calculation |
| Data Consumer | Customer Support | Uses data for ticket routing, account history, SLA tracking |
| Data Engineer | Integration Team | Maintains HubSpot, ERP, and support system syncs |

---

## Phase 2: Baseline Assessment

### Accuracy Assessment

**Measurement Method:** System of Record Comparison + Business Rule Validation

| Test | Sample Size | Errors | Error Rate | Score |
|------|-------------|--------|------------|-------|
| Phone number vs. external validation API (Twilio Lookup) | 500 | 23 | 4.6% | 95.4 |
| Billing address vs. ERP system | 500 | 31 | 6.2% | 93.8 |
| Email format validation (regex) | 34,105 | 412 | 1.2% | 98.8 |
| Opportunity close date vs. actual closed won date (ERP) | 200 closed opps | 18 | 9.0% | 91.0 |
| Account industry classification vs. business website (manual check) | 100 | 12 | 12.0% | 88.0 |

**Accuracy Score: 92/100 (Good)**

**Key Finding:** Industry classification is the weakest accuracy area. Sales reps select industries from a dropdown that is outdated and overly broad, leading to 12% misclassification. This affects marketing segmentation and industry-specific sales plays.

### Completeness Assessment

**Measurement Method:** Required Field Null Check + Record-Level Completeness

| Field | Required For | Total Records | Null/Empty | Completeness Rate |
|-------|-------------|---------------|------------|-------------------|
| `Account.Name` | All use cases | 16,482 | 0 | 100.0% |
| `Account.BillingAddress` | Billing, shipping | 16,482 | 1,247 | 92.4% |
| `Account.Industry` | Marketing segmentation | 16,482 | 3,847 | 76.7% |
| `Contact.Email` | Marketing, support | 34,105 | 2,105 | 93.8% |
| `Contact.Phone` | Sales outreach | 34,105 | 8,420 | 75.3% |
| `Contact.Title` | Account planning | 34,105 | 14,952 | 56.2% |
| `Opportunity.Amount` | Forecasting | 8,920 | 892 | 90.0% |
| `Opportunity.CloseDate` | Forecasting | 8,920 | 0 | 100.0% |
| `Opportunity.StageName` | Pipeline management | 8,920 | 0 | 100.0% |
| `Account.Custom_Last_Contact_Date__c` | Account health scoring | 16,482 | 9,235 | 44.0% |

**Completeness Score: 78/100 (Acceptable)**

**Key Finding:** Two fields are severely incomplete:
1. `Contact.Title` (56.2%) — Not required in the UI, so reps skip it. Impacts account-based selling and executive outreach.
2. `Account.Custom_Last_Contact_Date__c` (44.0%) — Requires manual entry after calls. Reps forget. Impacts account health scoring and churn risk models.

### Consistency Assessment

**Measurement Method:** Cross-System Comparison + Semantic Equivalence Test

| Field | Salesforce Value | HubSpot Value | ERP Value | Match Rate |
|-------|----------------|---------------|-----------|------------|
| Account Name | "Acme Corp" | "Acme Corp" | "Acme Corporation" | 67% (semantic mismatch) |
| Account Industry | "Technology" | "Software" | "Information Technology" | 45% (semantic mismatch) |
| Contact Email | "john@acme.com" | "john@acme.com" | N/A | 98% (exact match) |
| Account Status | "Active" | "Active" | "1" | 100% (mapped correctly) |
| Billing Address | "123 Main St" | "123 Main Street" | "123 Main St, Suite 100" | 52% (partial match) |
| Opportunity Amount | $50,000 | $50,000 | $50,000 | 96% (exact match) |

**Consistency Score: 74/100 (Warning)**

**Key Finding:** Industry and billing address have severe consistency issues across systems. The industry field uses different code lists in each system. Billing addresses differ because each system has its own address standardization rules.

### Uniqueness Assessment

**Measurement Method:** Fuzzy Duplicate Detection + Business Entity Resolution

| Algorithm | Duplicates Found | Duplication Rate |
|-----------|-----------------|------------------|
| Exact match on email | 342 | 1.0% |
| Exact match on phone | 891 | 2.6% |
| Fuzzy match on name + company (Jaro-Winkler > 0.85) | 1,247 | 3.7% |
| Business entity resolution (email + phone + name similarity) | 1,584 | 4.6% |

**Uniqueness Score: 71/100 (Warning)**

**Key Finding:** 4.6% of contacts represent duplicate individuals. Root cause: HubSpot web form submissions create new contacts even when an existing contact with the same email exists. The deduplication rule was disabled after a false-positive incident six months ago and never re-enabled.

---

## Phase 3: Root Cause Analysis

### Issue Mapping

| Issue ID | Dimension | Description | Root Cause | Category | Impact |
|----------|-----------|-------------|------------|----------|--------|
| CRM-001 | Accuracy | 12% industry misclassification | Industry dropdown is outdated and overly broad | Business Rule | Marketing segmentation; industry-specific sales plays |
| CRM-002 | Completeness | 56% missing contact titles | Field is optional in UI; no enforcement | Business Rule | Account-based selling; executive outreach |
| CRM-003 | Completeness | 56% missing last contact date | Manual entry; reps forget | Human Process | Account health scoring; churn risk models |
| CRM-004 | Consistency | 55% industry mismatch across systems | Each system uses different reference code list | Business Rule | Cross-system reporting; lead routing |
| CRM-005 | Consistency | 48% billing address mismatch | No shared address standardization service | Pipeline/ETL | Billing accuracy; tax calculation |
| CRM-006 | Uniqueness | 4.6% duplicate contacts | HubSpot deduplication disabled after false-positive | Pipeline/ETL | Inflated contact counts; skewed engagement metrics |

### Lineage Tracing (Selected: CRM-004 — Industry Inconsistency)

```
[Origin: Salesforce CRM]
  ↓ Industry field: dropdown values from Salesforce custom list
    ↓ Values: "Technology", "Healthcare", "Finance", "Manufacturing", "Other"
  ↓ [HubSpot sync — MuleSoft]
    ↓ Industry field mapped to HubSpot property "industry"
    ↓ Values: "Software", "Health Care", "Financial Services", "Manufacturing", "Technology"
    ↓ Mapping is manual spreadsheet maintained by Marketing Ops; last updated 18 months ago
  ↓ [ERP sync — nightly batch]
    ↓ Industry field mapped to ERP "customer_segment"
    ↓ Values: "Information Technology", "Life Sciences", "Banking", "Industrial", "Technology"
    ↓ Mapping is hardcoded in Python script; last updated 3 years ago
  ↓ [Consumption: Tableau Executive Dashboard]
    ↓ Industry filter shows 5 different values for the same customer
```

**Point of Degradation:** The mapping spreadsheets and hardcoded scripts are stale and unmaintained. Each system added new industry values over time, but mappings were never updated.

**Root Cause:** No governance process for reference data changes. Marketing Ops, Sales Ops, and Finance each maintain their own mapping without coordination.

---

## Phase 4: Remediation Roadmap

| Priority | Issue | Action | Owner | Effort | Dependencies | Milestone |
|----------|-------|--------|-------|--------|--------------|-----------|
| P1 | CRM-006 (Duplicates) | Re-enable HubSpot deduplication with improved matching rules; merge 1,584 duplicates | Salesforce Admin | M | Marketing Ops approval | Day 30 |
| P1 | CRM-003 (Last Contact Date) | Automate last contact date via call/meeting sync; remove manual entry | Salesforce Admin | M | Integration Team | Day 45 |
| P2 | CRM-004 (Industry Ref Data) | Implement master reference data management for industry codes; align all 3 systems | Data Governance Lead | L | P1 complete, stakeholder alignment | Day 60 |
| P2 | CRM-005 (Billing Address) | Deploy shared address validation service (Loqate or similar) | Integration Team | L | Budget approval | Day 75 |
| P3 | CRM-002 (Contact Titles) | Make title field required in UI for new contacts; backfill via LinkedIn enrichment API | Salesforce Admin | S | API subscription | Day 30 |
| P3 | CRM-001 (Industry Misclassification) | Update industry dropdown to NAICS-based taxonomy; reclassify existing accounts | Marketing Ops | M | CRM-004 complete | Day 90 |

---

## Phase 5: Continuous Monitoring & KPI Dashboard

### Monitoring KPIs

| KPI | Target | Warning Threshold | Critical Threshold | Measurement Method | Owner |
|-----|--------|-------------------|-------------------|-------------------|-------|
| % Contacts with complete required fields | >95% | 90% | 85% | Weekly Salesforce report | Salesforce Admin |
| Duplicate contact rate | <1% | 2% | 5% | Weekly fuzzy duplicate scan | Salesforce Admin |
| Cross-system industry match rate | >95% | 90% | 85% | Monthly reconciliation report | Data Governance Lead |
| Data quality issue mean time to resolution | <5 days | 10 days | 15 days | Ticketing system tracking | Data Governance Lead |

### Alerting
- **Weekly:** Salesforce Admin reviews contact completeness report
- **Monthly:** Data Governance Lead reviews cross-system consistency report
- **Quarterly:** Full re-audit using this scorecard

---

## Executive Summary

The CRM data quality audit revealed a dataset in **acceptable to good condition** overall, with four specific warning areas requiring attention. The most critical finding is a **4.6% duplicate contact rate** caused by disabled HubSpot deduplication, which inflates marketing metrics and wastes sales effort. The highest priority action is to re-enable deduplication with improved matching rules (P1, Day 30). 

The second priority is fixing the **manual last contact date process**, which leaves 56% of accounts without health scoring data. Automating this via calendar integration will have immediate impact on churn prediction.

Reference data governance (industry codes, address standardization) is the underlying systemic weakness. Without a master reference data process, consistency issues will recur. The roadmap includes a master reference data initiative (P2, Day 60) and shared address validation (P2, Day 75).

---

> **Example Version:** 1.0.0 | **Aligned with:** DAMA-DMBOK Second Edition, Chapter 13 | **License:** MIT
