# Claude Training & Certification Guide

> **This guide is for two audiences**:
> - **Enterprises / teams** that want their organization to systematically master Claude — whether or not they join the Anthropic Partner Network
> - **Individuals** — engineers, pre-sales, PMs — who want to self-study Claude, pass the official certifications, and turn it into career capital
>
> If you only care about the **end-to-end Partner Network flow** (apply → train → certify → launch → renew), see [`partner-journey.en.md`](./partner-journey.en.md). This guide focuses more on **training mix and exam prep strategy**.
>
> **Disclaimer**: This document reflects the publicly visible Anthropic course structure and certification framework as of May 2026. Actual course catalog, exam format, and validity follow the latest description on the official Partner Portal / Anthropic Academy.

---

## Part 1: Enterprise Training Guide (Enterprise Track)

### 1.1 Who this is for

| Org type | Typical motivation | Goal |
|---|---|---|
| Systems integrator / consultancy | Join Partner Network, get NFR + discounts, run Claude implementation business | Reach Registered in 1–3 months, Select in 3–6 months |
| ISV / SaaS | Integrate Claude into the product, need internal capability to support it | Engineering team 80% completes Tech Track, 1–2 Agent Developers |
| Internal AI department in a large enterprise | Promote internal Claude use cases, train cross-team staff | Build an internal Center of Excellence, continuously produce certified people |
| Training providers / universities | Run Claude-related courses or lab classes | All instructors complete Tech Track; learners split into Business / Dev paths |

### 1.2 Role matrix and training allocation

Don't "train everyone the same way". Inventory roles first, then assign learning paths by responsibility.

| Internal role | Recommended path | Target certification | Investment (per person) | Time to complete |
|---|---|---|---|---|
| Pre-sales / solution consultant | Business + Technical | Business Associate + Solutions Architect | ~80h | 6–8 weeks |
| Sales / Alliance | Business | Business Associate | ~30h | 2–3 weeks |
| PM / Product | Business + selective Tech | Business Associate (+ 1 Tech module) | ~40h | 3–4 weeks |
| Backend / application developer | Developer / Agent | Agent Developer | ~120h | 8–12 weeks |
| Solutions Engineer | Technical + Developer | Solutions Architect + Agent Developer | ~150h | 10–14 weeks |
| Data / ML engineer | Technical (deep) | Solutions Architect | ~80h | 6–8 weeks |
| Legal / compliance | "Security & compliance" module of Business | None required | ~8h | 1 week |
| Marketing / Content | Business overview | None required | ~6h | 1 week |

### 1.3 Team certification target (reference tier mix)

Example: a 30-person consulting firm targeting Select tier:

```
        Business Associate × 5 ─────────────────────  covers pre-sales / PM / Alliance
        Solutions Architect × 3 ────────────────────  covers SE / pre-sales leads
        Agent Developer × 2 ────────────────────────  covers core delivery engineers
        + 1 industry specialization (e.g., Financial / Healthcare) ── supports your target vertical
```

Redundancy: at least 2 people per critical certification — avoid single points of failure.

### 1.4 Quarterly cadence (reference)

| Quarter | Theme | Key outputs |
|---|---|---|
| Q1 | **Inventory + Business literacy** | Everyone completes Business overview; 3–5 people start Business Associate |
| Q2 | **Tech core training** | SA / Dev candidates finish core Tech modules; 2 internal hackathons |
| Q3 | **Certification sprint** | Mock exams + Office Hours Q&A; target headcount certified |
| Q4 | **Retrospective + GTM landing** | Case white papers, customer references, next year's learning roadmap |

### 1.5 Internal capability building: the four pillars

"Sending people to take exams" alone is not enough — enterprises also need a long-term internal ecosystem:

1. **Center of Excellence (CoE)**
   A 2–3 person team owning the prompt library, best-practice sediment, and onboarding for new hires. Monthly demo day.
2. **Internal Prompt / Skill Library**
   Sediment production-grade prompts, agent skills, and Claude Code subagents into an internal git repo, reviewed before reuse.
3. **Weekly "Claude Hour"**
   1 hour of internal sharing: Anthropic release notes recap, internal pitfalls, customer cases.
4. **Anthropic Office Hours connection**
   Premier / Select tiers usually get 1 hour of Office Hours per week. Set up a rotation; bring questions back.

### 1.6 Governance and compliance essentials

| Dimension | Recommended practice |
|---|---|
| **API key management** | Per-project keys; production / staging / training labs separated; lab keys have monthly budget caps |
| **HITL boundaries** | External comms, signatures, production deployments require human approval; internal drafts can flow freely |
| **Data compliance** | Customer data goes through PII redaction before entering prompts; sensitive industries (healthcare, finance) use a dedicated channel |
| **Cost governance** | Partner Handbook, stable system prompts must use Prompt Caching; monthly review of top 10 token-consuming use cases |
| **Audit** | Every agent call writes a run log; production has trace IDs back to prompt + model version |
| **Model version** | Lock model IDs in production (e.g., `claude-opus-4-7`); upgrades go through staged rollout in staging |

### 1.7 Mapping to official Anthropic resources

| Resource | Use for | Who should use it |
|---|---|---|
| Anthropic Academy | Main self-study entry | Everyone |
| Partner Portal | Application, tier status, official course catalog | Champion / Alliance |
| Solutions Engineer Office Hours | Real-question Q&A | SA / Dev leads |
| Anthropic Cookbook (GitHub) | Code samples | Dev / SE |
| Claude Docs (docs.claude.com) | API, tools, Skills reference | Anyone doing dev work |
| Anthropic Blog / Release Notes | Product updates | CoE scans weekly |

### 1.8 Relationship to Expound

`partner-journey.en.md` describes the "end-to-end 6–8 week flow" that Expound automates. This guide adds **"long-term training mix + internal ecosystem"**. Expound's role:

- Eligibility Scout produces a gap report for **current role matrix vs. target tier**
- Training Coach maps this guide's "role → learning path" into a concrete weekly plan
- Certification Prep handles exam prep (see Part 2, §2.4)
- Compliance & Renewal triggers a Delta learning path 45 days before certification expiry

### 1.9 Three enterprise case studies

#### Case A: BlueRiver Consulting — 30-person boutique consultancy, zero to Select tier

**Background**: 30-person strategy consultancy, only one founding partner is interested in Claude; the rest of the team has never used it.

**6-month cadence**:
- M1–M2: All-hands Business overview (1 lunch session/week); 5 people start BA
- M3–M4: 5 finish BA; 3 commit to SA, 1 starts Agent Dev
- M5: Anthropic application + Lab work + mock-exam sprint
- M6: 3 SA + 1 Agent Dev pass, Partner Directory listed

**Result**: Reach Select in 6 months; sign 2 Claude implementation deals totaling RMB 800k.

**Key decision**: Don't rush into certifications in Q1 — first make sure everyone understands "what we're selling". Champion spends 30% of their time on internal evangelism.

#### Case B: NorthPole AI — 200-person SaaS, no Partner status, but builds an internal CoE

**Background**: Need to integrate Claude into the product. 8-person AI team + 60 other engineers who haven't touched LLMs.

**Path**:
- All 8 AI engineers take Agent Developer (4 months)
- After passing, each mentors 5 "apprentices": weekly 1-on-1 + monthly demo day
- Don't apply to Partner Network — business model doesn't need it

**Governance**: Lab key monthly cap of USD 2000; production keys centrally managed by CoE; all prompts reviewed before commit.

**Result**: Within 6 months, 40% of engineers can independently ship Claude integrations; product NPS up 12 points.

**Pitfall hit**: 3 of the first batch of "apprentices" only watched videos and didn't build anything — no growth in 3 months. Later policy: every apprentice must ship 1 PR per month.

#### Case C: GlobalBank EMEA — compliance-first internal deployment

**Background**: Large bank. Data cannot leave SaaS. Claude deployed via Bedrock. Training is for 50 internal engineers only — no external partner activity.

**Path**:
- All-hands Business overview (8h) — understand what's possible and what isn't
- 25 take the SA path (10 certified)
- 10 advance to Agent Developer (5 certified)

**Governance**: Every prompt goes through a PII redaction pipeline; model version locked to `claude-opus-4-7` with 6-week staged rollouts; audit logs retained 7 years.

**Result**: 4 production agents shipped (KYC assist, compliance Q&A, report drafting, knowledge retrieval). Monthly token spend USD 1500, cache hit rate 92%.

---

## Part 2: Individual Training Guide (Individual Track)

### 2.1 Self-positioning: which type are you?

| You are / want to become | Recommended main path | Target certification |
|---|---|---|
| Pre-sales / sales / PM / industry consultant | Business Track | Claude Business Associate |
| Solutions Architect / senior front-end / tech pre-sales | Technical Track | Claude Solutions Architect |
| Backend / Agent / application developer | Developer / Agent Track | Claude Agent Developer |
| Want to be well-rounded (independent consulting, freelance) | Business + Technical (in two phases) | BA → SA |
| Student / total beginner | Business intro, then decide | Business Associate |

**How to judge**: look at what you spend 80% of your time on. If you write code, pick Developer; if you design solutions, pick Technical; if you talk to customers about needs, pick Business.

### 2.2 Trade-offs among three learning modes

| Mode | Pros | Cons | Best for |
|---|---|---|---|
| Pure self-study (Academy + docs) | Free / flexible | No one to ask, easy to drop out | Self-driven people with a project pulling them along |
| Self-study + Office Hours | Get key questions answered | Have to fit the schedule | Most SA / Dev candidates |
| Joining an enterprise / Partner training | Peers, momentum | Bound to company pace | Already at a Partner Org |
| Paid bootcamp | Tight pace, high density | Expensive, variable quality | People who need to ramp up in 4–6 weeks |

### 2.3 Recommended time investment (reference)

> All estimated based on "studying part-time, 5–8 hours/week". Full-time can compress by 60%.

| Target certification | Total hours | Weeks (part-time) | Notes |
|---|---|---|---|
| Business Associate | 30–40h | 4–5 weeks | People with sales / commercial background can compress to 3 weeks |
| Solutions Architect | 80–120h | 10–14 weeks | The Lab portion may iterate multiple times |
| Agent Developer | 120–180h | 14–20 weeks | Need at least 1 end-to-end agent project |

### 2.4 Exam prep strategies for each of the three certifications

#### 2.4.1 Claude Business Associate

**Format**: 60 multiple-choice + 2 scenario questions, online-proctored. Pass at 75%.

**Cadence**:
- Weeks 1–2: Pass through the Business modules in Anthropic Academy
- Week 3: Official sample questions + 1 case study
- Week 4: 2 full mock exams; review wrong answers carefully

**Top 3 traps**:
1. **Value proposition phrasing**: Claude isn't "just another LLM" — emphasize safety, long context, agentic. Answer from "customer scenario → Claude's differentiated value".
2. **Pricing & packaging**: questions on tiers, tokens, caching discounts; memorize the official tables.
3. **Compliance boundaries**: "Which deployment shape for which scenario" (HIPAA, FedRAMP) — memorize the basic frameworks.

#### 2.4.2 Claude Solutions Architect

**Format**: 40 multiple-choice + 1 Lab (design a Claude solution). Pass at 80% + Lab pass.

**Cadence**:
- Weeks 1–3: Messages API, Prompt Engineering, Tool Use (type code, don't just watch)
- Weeks 4–6: Agent SDK, Memory, Compaction (build 1 small agent demo)
- Weeks 7–8: Prompt Caching, Extended Thinking, Evals
- Weeks 9–10: Pick 2 real customer scenarios; draft your own solution designs
- Weeks 11–12: Mock exam + Lab practice (4-hour timed solution design)

**Keys to passing the Lab**:
- Don't pile up features — first state the **business problem + success criteria**
- Must include: architecture diagram, prompt design, HITL boundaries, cost estimate, risks & mitigations
- Provide an evaluation design (how do you measure if the solution is good?)

**Top 3 traps**:
1. **Tool Use error handling**: tool call failures, timeouts, malformed responses — frequently tested.
2. **Long-horizon agent state management**: when to use Memory tool, when to use structured state, when to compact — heavily weighted.
3. **Cost vs. latency trade-offs**: cache hit rate, choosing among Haiku / Sonnet / Opus — be ready to give numbers.

#### 2.4.3 Claude Agent Developer

**Format**: Hands-on Lab — build a specified agent with the Agent SDK and pass a test set. Pass rate ≥ 85%.

**Cadence**:
- Weeks 1–4: Agent SDK basics; run through every official quickstart
- Weeks 5–8: Deep-dive into subagents, MCP, Skills, Hooks
- Weeks 9–12: Build 2 end-to-end projects (one coding-agent, one business-agent)
- Weeks 13–16: Mock exam + refactor projects to production-grade (evals, error handling, observability)

**Keys to passing the Lab**:
- Clean project structure, README, evals
- High error-handling coverage (tool failures, model timeouts, context overflow)
- Observability (every agent call logged)
- Cost awareness (caching, sensible model layering)

**Top 3 traps**:
1. **Context management**: not using compaction / Memory / subagent isolation — context overflows fast.
2. **Tool design**: vague tool descriptions cause the agent to misroute calls.
3. **Eval design**: shipping to "production" without evals — it almost certainly fails.

### 2.5 Hands-on project recommendations

The exam only verifies basics. To actually be useful, build 1–2 end-to-end projects:

| Difficulty | Project | What you learn |
|---|---|---|
| ★ | Personal PDF Q&A agent | Messages API, Tool Use basics |
| ★★ | Email auto-classify + draft-reply agent | Tool use, external API integration, HITL |
| ★★ | Slack internal knowledge Q&A bot | RAG, prompt caching, long context |
| ★★★ | Code review assistant (GitHub Action) | Agent SDK, subagent, structured output |
| ★★★ | Multi-step research agent (Deep Research-style) | Subagent orchestration, long-horizon, context engineering |
| ★★★★ | A vertical agent for your industry (legal / medical / finance) | Real data, compliance, HITL design |

Pick one you can sustain for 4–8 weeks; open-source it / blog about it. Hugely useful for jobs and consulting leads.

### 2.6 Common pitfalls

| Pitfall | Consequence | Correct approach |
|---|---|---|
| Skipping Business straight to Tech | Don't understand customer scenarios; can't design well | Spend at least 1 week skimming Business modules |
| Watching videos without doing | Lab will fail | Pair every video with 1 hands-on exercise |
| Only learning the latest model, not the fundamentals | Obsolete after one release | Messages API, prompt design — these never go stale |
| Trying for all 3 certs at once | Front spread thin, easy to drop | Start with BA (quick win), then SA / Dev (long investment) |
| Ignoring evals | Project "looks like it runs", explodes in production | Every agent needs its own eval set |
| Studying alone in a hole | Easy to stall | Find 1–2 study buddies; weekly progress review |
| Not budgeting cost | Learning-period API bill spikes | Use Haiku in labs, enable caching; review monthly spend |

### 2.7 What if you don't pass?

Failing the first time is very common; don't be discouraged.

1. Get the wrong-answer report (the cert system gives weak-area feedback)
2. Targeted reinforcement on weak areas for 1–2 weeks (don't re-learn the whole course)
3. 2 mock exams, readiness ≥ 85, then book again
4. Failing the Solutions Architect / Agent Developer Lab usually means "not enough engineering practice" — recommend doing 1 real project before retaking

### 2.8 After you pass

Certification is just the start. Recommended next steps:

| Path | How |
|---|---|
| Technical depth | Track Anthropic release notes, write a teardown for each new feature; contribute to the Cookbook |
| Job search / switch | Put projects on GitHub + write a tech blog; watch Partner Network hiring |
| Independent consulting | Publish cases on LinkedIn / X; take small PoC engagements to build reputation |
| Internal Champion | Lead your company's CoE or Claude Hour |
| Community contribution | Anthropic Discord, MCP ecosystem, open-source agent projects |

### 2.9 Continuous learning rhythm

Models and tools iterate fast. Make learning a routine:

- **Weekly**: 30 min skimming Anthropic Blog + Release Notes
- **Monthly**: 1 hands-on demo of a new feature (e.g., new Skills, new MCP server)
- **Quarterly**: 1 full project / 1 deep technical post
- **45 days before cert expiry**: Delta learning path (only the past 12 months of changes)

### 2.10 Three individual case studies

#### Case A: Tao Zhang — 8-year Java backend engineer → Agent Developer

**Starting point**: Knew nothing about LLMs; company didn't use Claude. Pure spare-time effort.

**Path (8 months)**:
- M1: Business overview, understand what Claude can do
- M2–M3: Messages API + Tool Use, type through every official cookbook
- M4–M7: 2 open-source GitHub projects (code review bot + email agent), iterating
- M8: Lab mocks + Agent Developer certification

**Pitfall hit**: In M4 jumped straight to subagent + Memory and blew through tokens. Went back to context engineering basics.

**Result**: Switched to an AI startup with a 40% raise. The two open-source projects together earned 800+ stars.

#### Case B: Jia Lin — 5-year PM → Solutions Engineer

**Starting point**: No coding experience. Target role required both BA + SA.

**Path (5 months)**:
- BA (6h/week) + SA (6h/week) in parallel
- M3: signed up for a 2-week hands-on bootcamp to break the code-fear
- M4: BA passed; SA Lab failed first time (architecture diagram missed cost estimate)
- M5: targeted reinforcement on wrong-area; SA passed on second attempt

**Result**: Joined a Partner SE team, paired initially with a senior SA.

**Reflection**: Don't skip the Lab just because you're a PM — the Lab is the actual differentiator.

#### Case C: Ya Wang — senior enterprise consultant → independent consulting + Claude services

**Starting point**: 5 years in enterprise consulting (financial + retail clients), wants to add an AI service line.

**Path (3 months, full-time)**:
- M1: BA full curriculum (passed in 15 days)
- M2: SA full curriculum; mid-month took a customer PoC project as Lab practice
- M3: Agent Dev intro; built 1 demo (didn't take the cert)

**Result**: 1 month after updating LinkedIn with the certifications, received 3 PoC inquiries; 4 months later landed a first RMB 300k contract.

**Key insight**: Certification + real cases — both required. A cert without a demo doesn't close customers.

---

## Part 3: Individual ↔ Enterprise Synergy

### 3.1 Being a Champion inside a company as an individual

If you're an IC but the company wants to push Claude, you can step up as the internal Champion:

- Help HR / managers design the role matrix (see §1.2)
- Run the weekly Claude Hour
- Maintain the internal Prompt / Skill Library
- Liaise with the Anthropic Partner Account Manager

This usually becomes major capital for internal promotion.

### 3.2 How enterprises identify and support high-potential individuals

| Signal | Meaning |
|---|---|
| Asks API questions, files issues | Has the curiosity to dig |
| Side projects on the side | Strong engineering ability |
| Can explain Claude clearly to non-technical colleagues | Understands tech AND business — rare |
| Tracks release notes consistently | Strong long-term commitment signal |

For these people: provide lab budget, Office Hour priority, conference attendance, and route them into SA / Agent Dev certifications.

### 3.3 Three individual ↔ enterprise synergy cases

#### Case A: Engineer Li (NorthPole AI internal Champion → Tech Lead)

Started as a regular engineer; took initiative to lead the internal Claude Hour. Within 1 year:
- Got the company from no Partner relationship to Registered
- Promoted to Tech Lead, 35% pay raise
- Open-sourced the internal Prompt Library, gained industry attention

**Lesson**: When the company doesn't have a clear direction yet, the people willing to fill the gap get noticed.

#### Case B: Dr. Chen (company-funded certifications → startup → reverse partnership)

Funded by a multinational SaaS company to take BA + SA + Agent Dev. Left after 1 year to start a 5-person AI consultancy.
- Former employer became his first client (they actually needed this kind of service)
- He became a Sub-Partner of the former employer, sharing referrals
- The two reference each other on the Partner Directory and run joint GTM

**Lesson**: "Losing" trained talent isn't necessarily a loss — it can convert into long-term ecosystem assets.

#### Case C: Liang Zhou (open-source contributor → multiple Partners reach out)

In spare time, contributed 3 open-source servers to the MCP ecosystem (GitHub, Notion, internal wiki integrations).
- Projects accumulated 1500+ stars, included in Anthropic's official awesome list
- 3 Partner Orgs reached out for collaboration
- Eventually joined one as contractor + equity, retaining independence

**Lesson**: Sustained contribution in a new ecosystem (MCP / Skills / Subagents) is a natural connector between an individual and enterprises.

---

## Appendix

### A. Certification cheat sheet

| Cert | Format | Pass | Validity | Recommended hours |
|---|---|---|---|---|
| Business Associate | 60 MC + 2 scenarios | 75% | 12 months | 30–40h |
| Solutions Architect | 40 MC + Lab | 80% + Lab | 12 months | 80–120h |
| Agent Developer | Hands-on Lab | Test set ≥ 85% | 12 months | 120–180h |

### B. Learning resource checklist (mostly English)

- Anthropic Academy — main entry
- docs.claude.com — API / tools / Skills reference
- Anthropic Cookbook (GitHub) — code samples
- Anthropic Blog / Release Notes — product updates
- Claude Code docs — must-read if you build coding agents
- MCP protocol docs (modelcontextprotocol.io) — agent ecosystem extensions

### C. Recommended "30-day MVP study plan" (individual, Tech Track)

| Day | Goal | Output |
|---|---|---|
| D1–D3 | Run the Messages API quickstart | A working chat script |
| D4–D7 | Learn Prompt Engineering | 3 prompt versions for one real task, comparing results |
| D8–D14 | Tool Use deep-dive | A small agent calling an external API |
| D15–D21 | Agent SDK + Memory | A multi-turn research / organize agent |
| D22–D26 | Prompt Caching + Evals | Add caching and evals to the above agent |
| D27–D30 | Retrospective + 1 mock exam | Self-assessment, decide next month's pace |

### D. Hooking into Expound

If your company uses Expound:
- Individual learning progress auto-syncs to the Training Coach dashboard
- Mock exam scores feed into the Certification Prep readiness score
- The enterprise dashboard shows "team overall readiness"

If you're an independent learner:
- Expound's open-source code itself is a multi-agent case study — recommend reading through `src/expound/`
- The preview page (`preview/index.en.html`) is a nice visual reference for "what does an agentic service look like"

---

## Next

- For the end-to-end Partner flow, see [`partner-journey.en.md`](./partner-journey.en.md)
- For the code, see [`../src/expound/`](../src/expound/)
- To run the demo, see [`../README.en.md`](../README.en.md)
