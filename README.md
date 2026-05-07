# Expound

> **Anthropic + agentic AI, made navigable for non-technical users.**
> The d/acc *accessibility* pillar, in practice.

[![Status](https://img.shields.io/badge/status-launching-yellow)]() [![License](https://img.shields.io/badge/license-CC%20BY%204.0-blue)]() [![Audience](https://img.shields.io/badge/for-non--engineers-green)]()

---

## The problem

Most of the people who would benefit most from agentic AI tools — operators, lawyers, researchers, journalists, school administrators, mid-career knowledge workers — bounce off the documentation. The official docs assume Python, the YouTube tutorials assume you can read a stack trace, and the "AI for everyone" courses are usually thin.

Meanwhile the people who *do* navigate the tools (developers, ML researchers, indie hackers) often build the wrong thing because they've never had to defend a cell phone bill, run a school board meeting, or sit across from a regulator. The two populations rarely meet.

That gap is the d/acc accessibility problem. It's also a strategic problem: a frontier safety methodology — like Constitutional AI — only delivers safety in proportion to how widely it's actually used in practice. Tools used by 1% of the people who could use them well are not safe. They're concentrated.

## What this is

`Expound` is a curated, opinionated guide collection for non-technical users to **actually use** Anthropic's Claude (and adjacent agentic AI tools) for serious work — research, drafting, decision support, knowledge management, contract review, market analysis. It's not "10 cool ChatGPT tricks." It's:

- **Workflows that mirror how a thoughtful professional already works** — adapted to incorporate Claude as a collaborator, not as a replacement.
- **Verification practices baked in** — every workflow has an explicit "where does Claude lie to you, and how do you catch it" section.
- **No installation gates** — almost everything works in [Claude.ai](https://claude.ai) or the desktop app; CLI only when it's worth the cost.
- **Honest about what doesn't work yet** — areas where current LLMs are not ready (numerical precision, citation accuracy on obscure topics, anything time-sensitive without web search) get explicit boundary maps.

## Who it's for

- 🏛️ **Lawyers and policy professionals** — drafting, comparative analysis, contract review with verification practices
- 🔬 **Researchers (any field)** — long-form reading, literature exploration, hypothesis surfacing
- 📰 **Journalists and analysts** — interview prep, source synthesis, claim auditing
- 🎓 **Educators and administrators** — curriculum design, parent communication, decision documentation
- 💼 **Mid-career operators** — strategic memos, market research, customer communication
- 👤 **You, if you've felt the gap** between "everyone says AI will change my work" and "I cannot make this thing useful for my actual work"

## What it's NOT

- ❌ A "use AI to replace your job" promise — agentic AI doesn't replace knowledge work, it changes the verification budget for knowledge work
- ❌ Anthropic-affiliated, official, or endorsed — I'm a heavy Claude user and I respect Anthropic's published methodology, but this is independent
- ❌ A code course — this assumes zero programming and stays there
- ❌ Hype — every workflow is boring and works, or it's not in the collection

## Status

**Launching.** Initial collection is being built one workflow at a time, in public. First three workflows in flight:

- [ ] *Reading a 50-page document with Claude without falling for it* — see [`workflows/01_reading_long_documents/`](./workflows/01_reading_long_documents/)
- [ ] *Drafting a legal-adjacent memo when you're not a lawyer* — see [`workflows/02_legal_adjacent_memo/`](./workflows/02_legal_adjacent_memo/) *(in development)*
- [ ] *Doing market research that actually replicates next quarter* — see [`workflows/03_market_research/`](./workflows/03_market_research/) *(in development)*

Each workflow ships with: (a) the prompt sequences, (b) the verification checks, (c) the failure modes documented from real use, (d) at least one worked example including one that intentionally went wrong.

## Why I'm building this

Two reasons, both honest:

**(1) Mission**: The most concrete way I know to operationalize accessibility is to give the people who don't write code real instructions for using safety-aligned AI well. Constitutional AI is published and serious; if it doesn't reach the people whose work would benefit from it, that's a distribution failure, not a methodology failure. I want to fix the distribution side.

**(2) Apprenticeship**: I came to deep agentic AI use late, as an operator without an engineering background. I had to learn this from scratch in 2025–2026 by daily practice. The notes I made for myself are useful to others in the same boat. Sharing them is cheap; the cost of *not* sharing them is that the gap between agentic-AI-fluent and agentic-AI-illiterate professionals will widen and concentrate further.

## How to use this collection

Each workflow lives in its own folder. Browse, fork, adapt. Workflows are CC BY 4.0 licensed — use them anywhere, attribution appreciated, no permission needed.

If you've used a workflow and found a failure mode I haven't documented, **please open an issue or PR**. Failure modes from actual use are the highest-value contribution.

## Contributing

Particularly looking for contributions from:
- Non-engineers who've made Claude useful in a specific professional context
- People who've found a workflow break in production (not theory)
- Domain experts willing to co-author a vertical workflow (legal, medical, education, finance)

See [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

## License

CC BY 4.0. Use, adapt, redistribute, including commercially. Attribution required.

## Connect

- 📧 eskilca2024 [at] gmail [dot] com
- 💼 [LinkedIn](https://www.linkedin.com/in/yufeng-xu-9856a716/)
- 🐦 [@infinitegardenX](https://x.com/infinitegardenX)

---

*Maintained by [Eskil (Yufeng Xu)](https://github.com/EskilXu).*
