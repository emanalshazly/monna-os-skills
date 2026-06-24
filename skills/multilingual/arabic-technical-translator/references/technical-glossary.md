# Technical Glossary — Arabic-English Technical Term Mappings

> A living glossary of Arabic-English technical terms commonly used in MENA tech ecosystems. This glossary prioritizes the terms that Egyptian and MENA developers actually use — including code-switched English terms — over literal dictionary translations.

**Last Updated:** 2026-06-24
**Scope:** AI/ML, cloud computing, blockchain/DePIN, infrastructure, DevOps, SaaS, APIs, databases, governance, and agent systems.

---

## How to Use This Glossary

1. **Primary term:** The Arabic term most commonly used in MENA tech.
2. **Alternative:** Other acceptable Arabic terms or regional variants.
3. **English equivalent:** The English term as used in MENA (often kept as-is in code-switching contexts).
4. **Code-switching note:** Guidance on whether to keep the English term, Arabic term, or both.
5. **Market notes:** Any regional preferences (Saudi formal vs. Egyptian colloquial).

---

## Artificial Intelligence & Machine Learning

| English Term | Arabic Primary | Arabic Alternative | Code-Switching Note | Market Notes |
|-------------|----------------|---------------------|---------------------|--------------|
| Artificial Intelligence | الذكاء الاصطناعي | — | Arabic preferred in formal; "AI" acceptable in colloquial | MSA in policies; "AI" common in Egyptian dev communities |
| Machine Learning | تعلم الآلة | تعليم الآلة | "Machine Learning" often kept in English; "ML" ubiquitous | Egyptian devs say "الـ ML" more than "تعلم الآلة" |
| Neural Network | الشبكة العصبية | — | Arabic preferred; "Neural Network" acceptable in English-heavy contexts | Formal: always Arabic. Colloquial: mixed. |
| Deep Learning | التعلم العميق | — | Arabic preferred; "Deep Learning" acceptable | Same as ML |
| Model (ML) | النموذج | — | "Model" or "الـ model" in colloquial; "النموذج" in formal | — |
| Training (data) | التدريب | تدريب النموذج | "Training" commonly kept in English | "الـ training data" very common in Egyptian |
| Inference | الاستدلال | الاستنتاج | "Inference" kept in English in most dev contexts | Formal docs: Arabic preferred |
| Dataset | مجموعة البيانات | — | "Dataset" or "الـ dataset" very common | "الـ dataset" dominates in Egyptian |
| Feature (ML) | السمة | الخاصية | "Feature" often kept in English to avoid ambiguity | "الـ features" in colloquial; "السمات" in formal |
| Label | التصنيف | الوسم | "Label" kept in English; "الـ labels" common | — |
| Agent (AI) | العامل الذكي | الوكيل | **Critical:** "Agent" must NOT be translated as "وكيل" (real estate agent). Always "العامل الذكي" or keep "agent" in English. | This is a common and dangerous error. |
| Prompt Engineering | هندسة التوجيهات | — | "Prompt Engineering" kept in English; "الـ prompt" ubiquitous | Egyptian devs: "الـ prompt engineering" |
| Fine-tuning | الضبط الدقيق | — | "Fine-tuning" kept in English; "الـ fine-tuning" very common | — |
| Token | الرمز | الوسم | "Token" almost always kept in English in LLM contexts | "الـ token limit" — never translate literally |
| Embedding | التضمين | — | "Embedding" kept in English; "الـ embeddings" common | Formal: "التضمين" may be used |
| Hallucination | التوهم | الهلوسة | "Hallucination" kept in English in most dev contexts; "الـ hallucination" common | "الهلوسة" is catching on in Egyptian Arabic |
| RAG (Retrieval-Augmented Generation) | الجيل المعزز بالاسترجاع | — | "RAG" kept as acronym; "نظام RAG" common | Always "RAG" in colloquial |
| LLM (Large Language Model) | النموذج اللغوي الكبير | — | "LLM" ubiquitous; "الـ LLM" most common | Never translate "LLM" literally |
| GPT | GPT | — | "GPT" always kept in English | — |
| Vector Database | قاعدة البيانات المتجهة | — | "Vector DB" or "Vector Database" common | "الـ vector DB" in Egyptian |
| Multi-modal | متعدد الوسائط | — | "Multi-modal" kept in English | "الـ multimodal" common |

---

## Cloud Computing & Infrastructure

| English Term | Arabic Primary | Arabic Alternative | Code-Switching Note | Market Notes |
|-------------|----------------|---------------------|---------------------|--------------|
| Cloud Computing | الحوسبة السحابية | — | **Code-switching standard:** "الـ cloud computing" or "الـ cloud" are the most common forms in Egyptian Arabic. | Saudi formal: "الحوسبة السحابية" may be preferred. Egyptian: "الـ cloud" dominates. |
| Cloud | السحابة | — | "الـ cloud" is ubiquitous. | Never force "السحابة" if the audience says "الـ cloud." |
| Server | الخادم | السيرفر | "السيرفر" extremely common in Egyptian; "الخادم" in formal | Saudi formal: "الخادم" preferred. Egyptian: "السيرفر" dominates. |
| Virtual Machine | الجهاز الافتراضي | الـ VM | "الـ VM" or "الـ Virtual Machine" very common | "الـ VM" is standard shorthand |
| Container | الحاوية | الـ Container | "الـ container" or "الكونتينر" (Egyptian pronunciation) | "الحاوية" in formal; "الـ container" in dev contexts |
| Kubernetes | Kubernetes | كوبيرنيتيس | Always "Kubernetes" or "الـ Kubernetes" | Never translate |
| Docker | Docker | دوكر | "Docker" or "الـ Docker" | "دوكر" is Egyptian pronunciation |
| API | واجهة برمجة التطبيقات | الـ API | "الـ API" dominates in all contexts; full Arabic form rarely used except in formal docs | Always "الـ API" in Egyptian; formal docs may use full Arabic |
| Endpoint | نقطة النهاية | الـ Endpoint | "الـ endpoint" common in dev contexts | "الـ endpoint" more common than Arabic equivalent |
| Microservices | الخدمات المصغرة | الـ Microservices | "الـ microservices" very common | Formal: "الخدمات المصغرة" |
| Load Balancer | موزع الحمل | الـ Load Balancer | "الـ load balancer" common | "موزع الحمل" in formal architecture docs |
| CDN | شبكة توصيل المحتوى | الـ CDN | "الـ CDN" ubiquitous | "الـ CDN" always |
| Latency | زمن الاستجابة | الـ Latency | "الـ latency" common in performance contexts | "الـ latency" or "الـ delay" |
| Throughput | الإنتاجية | الـ Throughput | "الـ throughput" common | "الـ throughput" in dev; "الإنتاجية" in formal |
| Scalability | قابلية التوسع | الـ Scalability | "الـ scalability" common | "الـ scalability" or "التوسع" |
| High Availability | التوفر العالي | الـ High Availability | "الـ high availability" or "الـ HA" | "الـ HA" in ops contexts |
| Disaster Recovery | التعافي من الكوارث | الـ DR | "الـ DR" or "الـ disaster recovery" | "الـ DR" in ops |
| On-premise | محلي | الـ On-prem | "الـ on-prem" or "محلي" | "الـ on-prem" in dev; "محلي" in formal |
| Hybrid Cloud | السحابة الهجينة | — | "الـ hybrid cloud" or "السحابة الهجينة" | Mixed usage |
| Serverless | بلا خادم | الـ Serverless | "الـ serverless" dominates | "الـ serverless" almost always |

---

## Blockchain, DePIN & Web3

| English Term | Arabic Primary | Arabic Alternative | Code-Switching Note | Market Notes |
|-------------|----------------|---------------------|---------------------|--------------|
| Blockchain | سلسلة الكتل | الـ Blockchain | "الـ blockchain" dominates in all contexts | "الـ blockchain" is standard; "سلسلة الكتل" in formal whitepapers |
| Decentralized | لامركزي | الـ Decentralized | "الـ decentralized" or "لامركزي" | "لامركزي" in formal docs |
| Smart Contract | العقد الذكي | الـ Smart Contract | "الـ smart contract" or "العقد الذكي" | Mixed; "العقد الذكي" common in formal |
| Token | الرمز | الـ Token | "الـ token" ubiquitous in crypto | Same as ML token — context determines meaning |
| Cryptocurrency | العملة المشفرة | الـ Cryptocurrency | "الـ crypto" or "العملات المشفرة" | "الـ crypto" very common in Egyptian |
| Wallet | المحفظة | الـ Wallet | "الـ wallet" or "المحفظة" | "المحفظة" in formal; "الـ wallet" in community |
| Node | العقدة | الـ Node | "الـ node" or "العقدة" | "العقدة" in formal; "الـ node" in dev |
| Validator | المدقق | الـ Validator | "الـ validator" or "المدقق" | "المدقق" in formal staking docs |
| Staking | التحصيص | الـ Staking | "الـ staking" dominates; "التحصيص" rare | Always "الـ staking" in Egyptian |
| DePIN (Decentralized Physical Infrastructure Networks) | شبكات البنية التحتية الفيزيائية اللامركزية | الـ DePIN | "الـ DePIN" dominates — term is too new for Arabic equivalent | Always "الـ DePIN" |
| NFT | الرمز غير القابل للاستبدال | الـ NFT | "الـ NFT" ubiquitous | "الـ NFT" always; full Arabic in formal legal |
| DAO | المنظمة المستقلة اللامركزية | الـ DAO | "الـ DAO" common | "الـ DAO" in dev; full Arabic in formal |
| Gas (fees) | رسوم الغاز | الـ Gas | "الـ gas fees" or "رسوم الـ gas" | "الـ gas" always; "رسوم الغاز" in formal |
| Mining | التعدين | — | "الـ mining" or "التعدين" | "التعدين" common |
| Layer 1 / Layer 2 | الطبقة الأولى / الطبقة الثانية | الـ L1 / الـ L2 | "الـ L1 / الـ L2" dominates | Always "الـ L1/L2" |
| Bridge (cross-chain) | الجسر | الـ Bridge | "الـ bridge" or "الجسر" | "الجسر" in formal; "الـ bridge" in dev |
| Airdrop | — | الـ Airdrop | "الـ airdrop" dominates — no common Arabic equivalent | Always "الـ airdrop" |

---

## Databases & Data Engineering

| English Term | Arabic Primary | Arabic Alternative | Code-Switching Note | Market Notes |
|-------------|----------------|---------------------|---------------------|--------------|
| Database | قاعدة البيانات | الـ Database | "الـ database" or "الداتابيز" (Egyptian pronunciation) | "الداتابيز" very common in Egyptian |
| SQL | SQL | — | "SQL" always kept | — |
| NoSQL | NoSQL | — | "NoSQL" always kept | — |
| Relational Database | قاعدة البيانات العلائقية | — | "الـ relational DB" or "الـ RDBMS" | "الـ RDBMS" in formal |
| Schema | المخطط | الـ Schema | "الـ schema" common | "الـ schema" in dev; "المخطط" in formal |
| Table | الجدول | الـ Table | "الـ table" or "الجدول" | Mixed; "الجدول" common in formal |
| Query | الاستعلام | الـ Query | "الـ query" very common; "الاستعلام" in formal | "الـ query" dominates in Egyptian |
| Index | الفهرس | الـ Index | "الـ index" or "الفهرس" | "الفهرس" in formal; "الـ index" in dev |
| Migration | الترحيل | الـ Migration | "الـ migration" or "الترحيل" | "الـ migration" in dev contexts (Alembic, etc.) |
| Backup | النسخ الاحتياطي | الـ Backup | "الـ backup" or "النسخة الاحتياطية" | "الـ backup" common |
| Replication | النسخ المتماثل | الـ Replication | "الـ replication" or "النسخ المتماثل" | "النسخ المتماثل" in formal |
| Sharding | التجزئة | الـ Sharding | "الـ sharding" dominates | "الـ sharding" always |
| Data Pipeline | خط أنابيب البيانات | الـ Data Pipeline | "الـ pipeline" or "الـ data pipeline" | "الـ pipeline" very common |
| ETL | ETL | — | "ETL" always kept | — |
| Data Warehouse | مستودع البيانات | الـ Data Warehouse | "الـ data warehouse" or "الـ DWH" | "الـ DWH" in enterprise |
| Data Lake | بحيرة البيانات | الـ Data Lake | "الـ data lake" or "بحيرة البيانات" | Mixed |
| OLAP / OLTP | OLAP / OLTP | — | Acronyms always kept | — |
| ACID | ACID | — | "ACID" always kept | — |
| CRUD | CRUD | — | "CRUD" always kept | — |
| ORM | ORM | — | "ORM" always kept | — |

---

## APIs, Development & DevOps

| English Term | Arabic Primary | Arabic Alternative | Code-Switching Note | Market Notes |
|-------------|----------------|---------------------|---------------------|--------------|
| REST API | REST API | — | Always kept in English | — |
| GraphQL | GraphQL | — | Always kept in English | — |
| JSON | JSON | — | Always kept in English | — |
| XML | XML | — | Always kept in English | — |
| HTTP / HTTPS | HTTP / HTTPS | — | Always kept | — |
| Webhook | Webhook | — | "الـ webhook" common | — |
| SDK | SDK | — | "SDK" always kept | — |
| CLI | واجهة سطر الأوامر | الـ CLI | "الـ CLI" or "سطر الأوامر" | "الـ CLI" very common |
| Git | Git | — | Always kept | — |
| Repository | المستودع | الـ Repo | "الـ repo" or "المستودع" | "الـ repo" dominates in Egyptian |
| Commit | الالتزام | الـ Commit | "الـ commit" ubiquitous; "الالتزام" rare | Always "الـ commit" |
| Pull Request | طلب السحب | الـ PR | "الـ PR" dominates; "طلب السحب" in formal docs | "الـ PR" always in Egyptian |
| Merge | الدمج | الـ Merge | "الـ merge" or "الدمج" | "الـ merge" common |
| Branch | الفرع | الـ Branch | "الـ branch" or "الفرع" | "الفرع" in formal; "الـ branch" in dev |
| CI/CD | CI/CD | — | Always kept | — |
| Pipeline | خط الأنابيب | الـ Pipeline | "الـ pipeline" dominates | "الـ pipeline" always in dev |
| Deployment | النشر | الـ Deployment | "الـ deployment" or "النشر" | "النشر" in formal; "الـ deployment" in dev |
| Rollback | التراجع | الـ Rollback | "الـ rollback" or "التراجع" | "الـ rollback" in ops |
| Environment | البيئة | الـ Environment | "الـ environment" or "البيئة" | "البيئة" in formal; "الـ env" in dev |
| Production | الإنتاج | الـ Production | "الـ production" or "الـ prod" | "الـ prod" in ops shorthand |
| Staging | التجهيز | الـ Staging | "الـ staging" dominates | "الـ staging" always |
| Log | السجل | الـ Log | "الـ log" or "السجل" | "الـ log" or "الـ logs" common |
| Debugging | التصحيح | الـ Debugging | "الـ debugging" or "التصحيح" | "الـ debugging" common |
| Refactoring | إعادة الهيكلة | الـ Refactoring | "الـ refactoring" or "إعادة الهيكلة" | Mixed |
| Tech Debt | الدين التقني | الـ Tech Debt | "الـ tech debt" or "الدين التقني" | "الدين التقني" in formal |
| Sprint | السبرينت | — | "الـ sprint" dominates | Always "الـ sprint" |
| Agile | أجايل | الـ Agile | "الـ agile" or "أجايل" | "الـ agile" very common |
| Scrum | سكروم | الـ Scrum | "الـ scrum" or "سكروم" | Mixed |
| Kanban | كانبان | — | "الـ kanban" or "كانبان" | — |

---

## SaaS, Product & Business

| English Term | Arabic Primary | Arabic Alternative | Code-Switching Note | Market Notes |
|-------------|----------------|---------------------|---------------------|--------------|
| SaaS | SaaS | البرمجيات كخدمة | "SaaS" always kept in English | — |
| Subscription | الاشتراك | الـ Subscription | "الاشتراك" or "الـ subscription" | "الاشتراك" common |
| Freemium | فريميوم | الـ Freemium | "الـ freemium" or "فريميوم" | Mixed |
| Onboarding | التأهيل | الـ Onboarding | "الـ onboarding" or "التأهيل" | "الـ onboarding" dominates in Egyptian startups |
| Churn | معدل الانسحاب | الـ Churn | "الـ churn" or "معدل الانسحاب" | "الـ churn" common in SaaS |
| MRR | MRR | — | Always kept | — |
| ARR | ARR | — | Always kept | — |
| LTV | LTV | القيمة الد lifetime | "LTV" or "القيمة الد lifetime" | "LTV" always |
| CAC | CAC | تكلفة اكتساب العميل | "CAC" or "تكلفة الاكتساب" | "CAC" always |
| KPI | مؤشر الأداء الرئيسي | الـ KPI | "الـ KPI" very common | "الـ KPI" in business; "مؤشر الأداء" in formal |
| Dashboard | لوحة التحكم | الـ Dashboard | "الـ dashboard" or "لوحة التحكم" | "لوحة التحكم" common in formal |
| Feature (product) | الميزة | الـ Feature | "الـ feature" or "الميزة" | "الـ feature" common in product |
| Roadmap | خارطة الطريق | الـ Roadmap | "الـ roadmap" or "خارطة الطريق" | "الـ roadmap" common in startups |
| User Story | قصة المستخدم | الـ User Story | "الـ user story" or "قصة المستخدم" | "الـ user story" dominates |
| Feedback | التغذية الراجعة | الـ Feedback | "الـ feedback" or "الفيدباك" (Egyptian) | "الفيدباك" very common in Egyptian |
| A/B Testing | اختبار أ/ب | الـ A/B Testing | "الـ A/B testing" or "اختبار أ/ب" | "الـ A/B test" common |
| Conversion Rate | معدل التحويل | الـ Conversion Rate | "الـ conversion rate" or "معدل التحويل" | Mixed |
| Funnel | القمع | الـ Funnel | "الـ funnel" or "القمع" | "الـ funnel" common in growth |
| Landing Page | صفحة الهبوط | الـ Landing Page | "الـ landing page" or "صفحة الهبوط" | "الـ landing page" dominates |
| CTA | CTA | دعوة للعمل | "CTA" or "الـ call to action" | "CTA" in marketing |
| UX / UI | UX / UI | تجربة المستخدم / واجهة المستخدم | "UX/UI" always kept; full Arabic in formal docs | "الـ UX" ubiquitous |

---

## Governance, Security & Compliance

| English Term | Arabic Primary | Arabic Alternative | Code-Switching Note | Market Notes |
|-------------|----------------|---------------------|---------------------|--------------|
| Governance | الحوكمة | — | Arabic preferred in formal; "الـ governance" acceptable | "الحوكمة" in Saudi formal docs; "الـ governance" in Egyptian |
| AI Governance | حوكمة الذكاء الاصطناعي | الـ AI Governance | "الـ AI governance" or "حوكمة الـ AI" | Mixed |
| Risk Management | إدارة المخاطر | — | Arabic preferred in formal | "إدارة المخاطر" in formal policies |
| Compliance | الالتزام | الـ Compliance | "الـ compliance" or "الالتزام" | "الالتزام" in formal; "الـ compliance" in business |
| Audit | التدقيق | الـ Audit | "الـ audit" or "التدقيق" | "التدقيق" in formal; "الـ audit" in business |
| Policy | السياسة | الـ Policy | "السياسة" or "الـ policy" | "السياسة" in formal; "الـ policy" in SaaS |
| Framework | الإطار | الـ Framework | "الإطار" or "الـ framework" | "الـ framework" common in tech |
| GDPR | GDPR | — | "GDPR" always kept; note: not applicable in MENA, use local equivalents | Reference PDPL (Saudi) or NPDP (UAE) |
| PDPL (Saudi) | نظام حماية البيانات الشخصية | — | Use Arabic for Saudi context | Saudi-specific |
| NPDP (UAE) | سياسة حماية البيانات | — | Use Arabic for UAE context | UAE-specific |
| Encryption | التشفير | — | Arabic preferred | "التشفير" standard |
| Authentication | المصادقة | الـ Authentication | "الـ authentication" or "المصادقة" | "المصادقة" in formal security |
| Authorization | التفويض | الـ Authorization | "الـ authorization" or "التفويض" | "التفويض" in formal |
| Vulnerability | الثغرة | الـ Vulnerability | "الثغرة" or "الـ vulnerability" | "الثغرة" in security |
| Penetration Test | اختبار الاختراق | — | Arabic preferred | "اختبار الاختراق" standard |
| Zero Trust | عدم الثقة | الـ Zero Trust | "الـ zero trust" or "عدم الثقة" | "الـ zero trust" common |
| Incident | الحادث | الـ Incident | "الـ incident" or "الحادث" | "الحادث" in formal IR |
| SLA | SLA | اتفاقية مستوى الخدمة | "SLA" always kept; full Arabic in formal contracts | "SLA" ubiquitous |
| DORA (Digital Operational Resilience Act) | DORA | — | "DORA" kept; explain in Arabic for EU context | EU-specific |
| NIST RMF | NIST RMF | — | "NIST RMF" kept; explain in Arabic | International standard |
| ISO 42001 | ISO 42001 | — | "ISO 42001" kept | — |
| EU AI Act | قانون الاتحاد الأوروبي للذكاء الاصطناعي | الـ EU AI Act | "الـ EU AI Act" or full Arabic | Use full Arabic in formal Saudi/UAE compliance docs |

---

## Agent Systems & Skills (MONNA Framework Domain)

| English Term | Arabic Primary | Arabic Alternative | Code-Switching Note | Market Notes |
|-------------|----------------|---------------------|---------------------|--------------|
| Agent (system) | العامل | الوكيل | "الـ agent" or "العامل" — **never "وكيل"** | "العامل الذكي" in formal AI governance |
| Skill | المهارة | الـ Skill | "الـ skill" or "المهارة" | "الـ skill" common in MONNA framework |
| Prompt | التوجيه | الـ Prompt | "الـ prompt" ubiquitous; "التوجيه" in formal | "الـ prompt" always in Egyptian |
| System Prompt | توجيه النظام | الـ System Prompt | "الـ system prompt" or "توجيه النظام" | Mixed |
| Workflow | سير العمل | الـ Workflow | "الـ workflow" or "سير العمل" | "الـ workflow" common |
| Orchestrator | المنسق | الـ Orchestrator | "الـ orchestrator" or "المنسق" | "الـ orchestrator" in tech |
| Sub-agent | العامل الفرعي | الـ Sub-agent | "الـ sub-agent" or "العامل الفرعي" | "الـ sub-agent" in dev |
| Tool (LLM) | الأداة | الـ Tool | "الـ tool" or "الأداة" | "الأداة" in formal; "الـ tool" in dev |
| Memory (AI) | الذاكرة | الـ Memory | "الـ memory" or "الذاكرة" | "الـ memory" in agent contexts |
| Context Window | نافذة السياق | الـ Context Window | "الـ context window" or "نافذة السياق" | "الـ context window" common |
| Function Calling | استدعاء الوظيفة | الـ Function Calling | "الـ function calling" or "استدعاء الوظيفة" | "الـ function calling" in dev |
| RAG (see ML) | — | — | — | — |
| Hallucination (see ML) | — | — | — | — |
| Guardrails | حواجز الحماية | الـ Guardrails | "الـ guardrails" or "حواجز الحماية" | "الـ guardrails" common |
| Evaluation | التقييم | الـ Evaluation | "الـ evaluation" or "التقييم" | "التقييم" in formal |
| Benchmark | المعيار | الـ Benchmark | "الـ benchmark" or "المعيار" | "الـ benchmark" common |
| Fine-tuning (see ML) | — | — | — | — |
| Temperature (LLM) | درجة الحرارة | الـ Temperature | "الـ temperature" or "درجة الحرارة" | "الـ temperature" common |
| Token (see ML) | — | — | — | — |
| Embedding (see ML) | — | — | — | — |
| Vector Store (see ML) | — | — | — | — |

---

## General Computing

| English Term | Arabic Primary | Arabic Alternative | Code-Switching Note | Market Notes |
|-------------|----------------|---------------------|---------------------|--------------|
| Algorithm | الخوارزمية | — | Arabic preferred | "الخوارزمية" standard |
| Variable | المتغير | الـ Variable | "الـ variable" or "المتغير" | "المتغير" in education; "الـ variable" in dev |
| Function | الدالة | الـ Function | "الـ function" or "الدالة" | "الدالة" in education; "الـ function" in dev |
| Class | الصنف | الـ Class | "الـ class" or "الصنف" | "الصنف" in formal; "الـ class" in dev |
| Object | الكائن | الـ Object | "الـ object" or "الكائن" | "الكائن" in formal; "الـ object" in dev |
| Interface | الواجهة | الـ Interface | "الـ interface" or "الواجهة" | "الواجهة" in formal |
| Library | المكتبة | الـ Library | "الـ library" or "المكتبة" | "المكتبة" in formal; "الـ lib" in dev |
| Package | الحزمة | الـ Package | "الـ package" or "الحزمة" | "الـ package" common |
| Dependency | التبعية | الـ Dependency | "الـ dependency" or "التبعية" | "الـ dependency" common |
| Version | الإصدار | الـ Version | "الـ version" or "الإصدار" | "الإصدار" in formal; "الـ version" in dev |
| Release | الإصدار | الـ Release | "الـ release" or "الإصدار" | "الـ release" common |
| Tag | الوسم | الـ Tag | "الـ tag" or "الوسم" | "الـ tag" common in Git |
| Cache | ذاكرة التخزين المؤقت | الـ Cache | "الـ cache" or "الكاش" (Egyptian) | "الكاش" very common in Egyptian |
| Buffer | المخزن المؤقت | الـ Buffer | "الـ buffer" or "المخزن المؤقت" | "الـ buffer" common |
| Thread | الخيط | الـ Thread | "الـ thread" or "الخيط" | "الـ thread" common |
| Process | العملية | الـ Process | "الـ process" or "العملية" | "الـ process" common |
| Memory (RAM) | الذاكرة | الـ Memory | "الـ memory" or "الذاكرة" | "الذاكرة" in hardware; "الـ memory" in software |
| CPU | المعالج | الـ CPU | "الـ CPU" or "المعالج" | "المعالج" common |
| GPU | GPU | — | "GPU" always kept | — |
| Kernel | النواة | الـ Kernel | "الـ kernel" or "النواة" | "النواة" in formal; "الـ kernel" in dev |
| Boot | الإقلاع | الـ Boot | "الـ boot" or "الإقلاع" | "الإقلاع" in formal |
| Driver | التعريف | الـ Driver | "الـ driver" or "التعريف" | "التعريف" in formal Windows contexts |
| Plugin | الملحق | الـ Plugin | "الـ plugin" or "الملحق" | "الـ plugin" common |
| Extension | الامتداد | الـ Extension | "الـ extension" or "الامتداد" | "الـ extension" common |
| Configuration | الإعدادات | الـ Config | "الـ config" or "الإعدادات" | "الإعدادات" in formal; "الـ config" in dev |
| Parameter | المعامل | الـ Parameter | "الـ parameter" or "المعامل" | "المعامل" in formal; "الـ param" in dev |
| Argument | المعامل | الـ Argument | "الـ argument" or "المعامل" | "الـ argument" common |
| Return Value | قيمة الإرجاع | الـ Return Value | "الـ return value" or "قيمة الإرجاع" | "الـ return" common |
| Callback | رد النداء | الـ Callback | "الـ callback" or "رد النداء" | "الـ callback" common |
| Event | الحدث | الـ Event | "الـ event" or "الحدث" | "الـ event" common in programming |
| Listener | المستمع | الـ Listener | "الـ listener" or "المستمع" | "الـ listener" common |
| Handler | المعالج | الـ Handler | "الـ handler" or "المعالج" | "الـ handler" common |
| Exception | الاستثناء | الـ Exception | "الـ exception" or "الاستثناء" | "الاستثناء" in formal; "الـ exception" in dev |
| Error | الخطأ | الـ Error | "الـ error" or "الخطأ" | "الـ error" very common |
| Stack | المكدس | الـ Stack | "الـ stack" or "المكدس" | "المكدس" in formal CS; "الـ stack" in dev |
| Queue | الطابور | الـ Queue | "الـ queue" or "الطابور" | "الـ queue" common |
| Heap | الكومة | الـ Heap | "الـ heap" or "الكومة" | "الكومة" in formal CS |
| Recursion | التكرار | الـ Recursion | "الـ recursion" or "التكرار" | "الـ recursion" common |
| Iteration | التكرار | الـ Iteration | "الـ iteration" or "التكرار" | "الـ iteration" in agile |

---

## Contributing

This glossary is a living document. To add a term:
1. Ensure it is commonly used in MENA tech contexts.
2. Prefer code-switched English terms where they are standard in the ecosystem.
3. Include market notes for regional variations.
4. Submit with a usage example from real MENA tech content.

---

*This glossary was built for the MENA tech ecosystem by someone who lives in it. It prioritizes how developers actually communicate over dictionary correctness.*
