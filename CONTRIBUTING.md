# Contributing to Expound

You don't need to be an engineer to contribute here. In fact, some of the most valuable contributions will come from people who are *not* engineers — lawyers, researchers, operators, educators, and others who've tried to use Claude for serious professional work and have opinions about what works and what doesn't.

## What this project needs most

**1. Failure modes from real use**
If you used a workflow from this collection and Claude gave you wrong, misleading, or confidently incorrect output — that's the highest-value thing you can report. Open an issue with: which workflow, what task you were doing, what Claude got wrong, and (if you caught it) how you caught it.

**2. Verification gaps**
If you found a step in a workflow where Claude's output looked right but wasn't — and there was no verification gate to catch it — open an issue. That's a gap in the workflow design, not a gap in your skills.

**3. Worked examples from your domain**
If you've used a workflow in a professional context — law, medicine, education, finance, policy, journalism — and you're willing to document it (anonymized if needed), open a PR or issue. Real examples from real professionals are more valuable than polished hypotheticals.

**4. Vertical co-authorship**
If you have deep domain expertise (legal, medical, financial, educational) and want to co-author a workflow specific to that domain, please reach out directly: eskilca2024 [at] gmail [dot] com. I want these to be built with domain experts, not written by me speculating about their workflows.

**5. Translations**
The target audience is global. If you can translate a workflow into another language faithfully, including the verification gates, please open a PR.

## What I'm not looking for right now

- Requests to add code components — this collection is intentionally no-installation
- Additions that require CLI or API access as a prerequisite
- Rewrites of the tone toward more technical language

## How to open an issue

Just describe what happened plainly. You don't need to follow a template. If you're not sure whether something is worth reporting, it probably is — open the issue.

## How to open a PR

1. Fork the repo
2. Make your changes in a branch
3. Open a PR with a plain-language description of what you changed and why

For new workflow content: include at least one worked example, and explicitly document at least one failure mode you encountered while developing it.

## On the verification-first philosophy

Everything in this collection is built around explicit verification. If you're contributing a new workflow or modifying an existing one, please maintain this: every workflow should have at least one explicit "stop and check Claude's work here" gate, and the failure_modes/ folder should document the ways the workflow can fail.

A workflow with no failure modes documented is not honest — it means the failure modes haven't been found yet, not that they don't exist.

## License

By contributing, you agree your contributions will be licensed under CC BY 4.0 — the same license as the rest of this collection.

---

Questions? Open an issue or email eskilca2024 [at] gmail [dot] com.
