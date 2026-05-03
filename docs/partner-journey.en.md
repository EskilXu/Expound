# Anthropic Partner Network — Training & Certification Journey Overview

> **Scope**: This document describes the complete journey of an enterprise (system integrator, consulting firm, ISV, reseller) that wants to join the Anthropic Partner Network — from zero, through becoming a "certified partner", to ongoing operations. **Expound**'s agentic service orchestrates, assists, and accelerates each step along this journey.
>
> **Disclaimer**: What follows is a **reference journey model**. Actual tier names, course catalog, and certification subjects follow the latest description on Anthropic's official Partner Portal. Expound's Eligibility Scout agent fetches the latest requirements from the official pages at runtime and overrides the local knowledge.

---

## 1. The journey at a glance (5 stages)

```
     ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
 ──▶ │ 1.       │──▶│ 2.       │──▶│ 3.       │──▶│ 4.       │──▶│ 5.       │
     │ Discover │   │ Enable   │   │ Certify  │   │ Launch   │   │  Grow    │
     └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
       ~1 week        2–3 weeks      2 weeks         2 weeks       ongoing
```

| Stage | Duration (reference) | Key artifacts | Expound primary agent |
|---|---|---|---|
| **1. Discover** — discovery & application | 3–7 days | Gap report, Business Plan, target tier, signed MSA | Eligibility Scout + Application Packager |
| **2. Enable** — enablement & training | 2–3 weeks | Per-team learning paths, ≥ 90% completion, instructor-led replays | Training Coach |
| **3. Certify** — certification | 1–2 weeks | At least N certified Solutions Architects / Business Associates | Certification Proctor-Prep |
| **4. Launch** — launch & joint GTM | 2 weeks | Demo/POC scaffold, case white paper, Partner Directory listing | Enablement / GTM Agent |
| **5. Grow** — growth & renewal | ongoing | Quarterly Business Review (QBR), tier upgrades, annual recertification | Compliance & Renewal (lightweight daemon) |

---

## 2. Partner tiers (reference 3-tier model)

The actual naming follows Anthropic's official scheme. We use a generic 3-tier model here as an example:

| Tier | Profile | Typical bar | Benefits |
|---|---|---|---|
| **Registered** | Just entering, no revenue yet | 1 Business Associate certification | Tech docs, community, dev credits |
| **Select** | Has Claude implementations live | 2+ Solutions Architects + 2 deals closed | Discounts, joint marketing budget, NFR accounts |
| **Premier** | Strategic partner, industry exemplar | Annual revenue threshold + dedicated industry certification + customer references | Dedicated PAM, co-sell, EBC channel |

The Eligibility Scout reads a company's profile and returns gap reports like **"You currently meet Registered; you are 2 certifications + 1 reference customer away from Select"**.

---

## 3. Curriculum (training matrix)

Expound maps courses by **role**, so each learner gets a personalized learning path rather than "one syllabus shoved at everyone".

### 3.1 Three core learning paths

| Path | Target role | Course modules (examples) | Target certification |
|---|---|---|---|
| **Business Track** | Pre-sales, sales, PM, alliances | Claude value proposition, pricing & packaging, security & compliance basics, competitive comparison, discovery-led selling, case studies | Claude Business Associate |
| **Technical Track** | Solutions Architect, technical pre-sales | Messages API basics, Prompt Engineering, Tool Use, Agent SDK, Evals, Prompt Caching, Extended Thinking | Claude Solutions Architect |
| **Developer / Agent Track** | Application developer | Claude Agent SDK deep-dive, Managed Agents, MCP, Memory, Compaction, Skills, long-horizon agent design patterns | Claude Agent Developer |

### 3.2 Optional industry specializations

- Financial Services (compliance, KYC, RAG on filings)
- Healthcare & Life Sciences (HIPAA, de-identification)
- Public Sector (FedRAMP, data sovereignty)
- Software & Code (coding agents, review, migration)

Reaching Premier typically requires 1–2 industry specializations.

### 3.3 Delivery modes

- **Self-paced**: video + hands-on lab (Academy)
- **Live**: monthly cohort live sessions + Q&A
- **Lab**: real sandbox project (e.g., "Build a compliance Q&A Agent for ACME Bank")
- **Office Hours**: Anthropic Solutions Engineer one-hour open Q&A weekly

The Training Coach packs these heterogeneous resources into each learner's weekly plan, drives weekly progress, and pings on overdue items.

---

## 4. Certification

### 4.1 Subjects and formats

| Certification | Exam format | Passing bar (reference) | Validity |
|---|---|---|---|
| **Claude Business Associate** | 60 multiple-choice + 2 scenario questions, online proctoring | 75% | 12 months |
| **Claude Solutions Architect** | 40 multiple-choice + 1 hands-on Lab (design a Claude solution) | 80% + Lab passing | 12 months |
| **Claude Agent Developer** | Hands-on Lab: build a specified Agent with the Agent SDK and pass a test set | Test set pass rate ≥ 85% | 12 months |

### 4.2 Exam prep flow (Proctor-Prep Agent)

1. **Diagnostic quiz**: after the course, automatically generate 20 questions to locate weak spots
2. **Weak-spot deep-dives**: targeted explanations + extra questions for weak areas
3. **3 mock exams**: Claude provides detailed error analysis after each round
4. When **readiness score ≥ 85**, push the "you can register" notification
5. After failure, automatically generate a remediation plan

### 4.3 Annual recertification

45 days before expiry, automatically trigger a Delta learning path (covering only the past 12 months of product changes), at significantly lower cost than first-time learning.

---

## 5. Detailed timeline (MVP perspective)

The table below shows Expound's typical end-to-end cadence for a single Partner Org:

| Week | Stage | Agent automation | Human checkpoint |
|---|---|---|---|
| W1.D1 | Discover | Eligibility Scout scans the company website + existing AI cases, produces a gap report and tier recommendation | Partner Champion confirms target tier |
| W1.D3 | Discover | Application Packager generates application draft + Business Plan | Legal reviews the MSA, Champion signs |
| W1.D5 | Discover | Submits the application, tracks Anthropic-side review | — |
| W2.D1 | Enable | Training Coach distributes learning paths according to the roster, creates the weekly calendar | Manager approves the path |
| W2–W4 | Enable | Push the weekly plan every Monday, summarize completion rate and risk items every Friday | Overdue > 3 days triggers escalation |
| W4.D5 | Certify | Diagnostic quiz + weak-spot reinforcement | — |
| W5 | Certify | 3 rounds of mock exams | — |
| W6 | Certify | Push "ready, can register" | Learner books the official exam |
| W7 | Launch | Generate the first Demo / POC scaffold based on the Agent SDK | Tech Lead reviews |
| W7.D4 | Launch | Draft joint solution white paper + case 1-pager | Marketing reviews |
| W8 | Launch | Partner Directory listing + co-marketing kit sent | — |
| ongoing | Grow | Monthly QBR data pack, quarterly tier progress | Partner Success Manager hosts QBR |

---

## 6. Human–machine collaboration / HITL principles

The following actions **must** be confirmed by the Champion or the corresponding owner before execution. There is no "default-pass":

1. Submitting the formal application to Anthropic
2. Signing any agreement (MSA, NDA, Co-sell Addendum)
3. Sending external email or Slack messages
4. Listing/de-listing on the Partner Directory
5. Modifying account fields or deal stages in the CRM

Low-risk internal actions (drafting documents, scheduling, internal reminders) are auto-executed by default, with full audit logs.

---

## 7. Metrics for Expound success

| Metric | Baseline (manual) | Expound target |
|---|---|---|
| Application → Registered certification done | 6–8 weeks | **≤ 3 weeks** |
| Partner Success manual effort per learner to complete training | 4 hours / person | **≤ 30 minutes / person** |
| First-attempt certification pass rate | 60–70% | **≥ 85%** |
| Recertification done 30 days before expiry | 40% | **≥ 80%** |
| Champion satisfaction (CSAT) | — | **≥ 4.5 / 5** |

---

## 8. Read next

- `preview/index.en.html` — visual preview of this journey
- `src/expound/` — MVP code skeleton (Orchestrator + Eligibility Scout + Training Coach)
- `README.en.md` — how to run it locally
