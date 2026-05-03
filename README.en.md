# Expound

> Agentic service that helps enterprises join the **Anthropic Partner Network** and complete the training & certification journey.

Expound is a multi-agent orchestrated onboarding service. It compresses what is normally a 6–8 week, cross-role, cross-department partner application and training process into an agent-driven, human-in-the-loop (HITL) approved pipeline.

> 🌐 Other languages: [简体中文](./README.md) · [日本語](./README.ja.md)

## Quick tour

| What I want to see | Open |
|---|---|
| Overall journey (5 stages / tiers / training matrix / certification) | [`docs/partner-journey.en.md`](./docs/partner-journey.en.md) |
| Training matrix & individual exam prep (enterprise + individual) | [`docs/training-guide.en.md`](./docs/training-guide.en.md) |
| Visual preview page | [`preview/index.en.html`](./preview/index.en.html) — open locally in a browser |
| Code skeleton | [`src/expound/`](./src/expound/) |

The preview page works as a static file (no build step):

```bash
open preview/index.en.html        # macOS
xdg-open preview/index.en.html    # Linux
```

## Architecture at a glance

```
             ┌───────────────────────────────┐
Slack/Web ─▶ │   Orchestrator (Opus 4.7)     │ ◀── HITL approval
             └──────────────┬────────────────┘
                            │  delegate · aggregate
  ┌────────────┬────────────┼────────────┬────────────┐
  ▼            ▼            ▼            ▼            ▼
Eligibility Application  Training   Certification Enablement
  Scout     Packager      Coach    Proctor-Prep     / GTM
```

- **Orchestrator**: Claude Opus 4.7 — routing, aggregation, HITL orchestration.
- **Sub-agents**: Claude Sonnet 4.6 — each owns one stage of the work.
- **High-frequency small tasks**: Claude Haiku 4.5 (tagging, classification, progress write-back).
- **Long-horizon state**: structured state + Memory, persisted across weeks.
- **Cost optimization**: large stable knowledge (Partner Handbook, certification outline) uses Prompt Caching.

## MVP scope

v0.1 (the current state of this repo) focuses on a CLI demo of **Orchestrator + Eligibility Scout + Training Coach**, demonstrating multi-agent delegation and the HITL flow. The other sub-agents have stub interfaces and will be wired in incrementally.

| Agent | Status | Notes |
|---|---|---|
| Orchestrator | ✅ MVP | Multi-agent orchestration via tool use |
| Eligibility Scout | ✅ MVP | Given a company profile, produces a gap report and tier recommendation |
| Training Coach | ✅ MVP | Generates a 4-week learning path per role |
| Application Packager | 🚧 stub | Interface defined, returns template |
| Certification Prep | 🚧 stub | Interface defined, returns template |
| Enablement / GTM | 🚧 stub | Interface defined, returns template |

## Run locally

```bash
# 1. Clone and enter the directory
cd Expound

# 2. Recommended: uv or venv
python -m venv .venv && source .venv/bin/activate
pip install -e .

# 3. Configure your API key
export ANTHROPIC_API_KEY=sk-ant-...

# 4. Run the demo
expound demo
```

The demo uses a fictional company "ACME Consulting" as the Partner Org and triggers, in order:
1. Eligibility Scout scans the company and produces a gap report
2. Training Coach generates a learning path for a sample learner
3. A simulated HITL approval card (before submitting the application)

## Provider switching (Anthropic / DeepSeek)

Expound switches between two providers via the `EXPOUND_PROVIDER` env var:

| Provider | Default models (orchestrator / sub-agent / fast) | Required env | Orchestrator available? |
|---|---|---|---|
| `anthropic` (default) | `claude-opus-4-7` / `claude-sonnet-4-6` / `claude-haiku-4-5` | `ANTHROPIC_API_KEY` | ✅ |
| `deepseek` | `deepseek-reasoner` / `deepseek-chat` / `deepseek-chat` | `DEEPSEEK_API_KEY` | ❌ sub-agents only |

```bash
# Default: Anthropic
export ANTHROPIC_API_KEY=sk-ant-...
expound demo

# Switch to DeepSeek (note: the orchestrator depends on Anthropic beta
# features — tool_runner, adaptive thinking — which DeepSeek's
# Anthropic-compat shim doesn't implement; that path will fail loudly)
export EXPOUND_PROVIDER=deepseek
export DEEPSEEK_API_KEY=sk-...
expound demo  # sub-agents still run; the orchestrator step raises a clear error
```

To override model names per role, set:

- `EXPOUND_MODEL_ORCHESTRATOR`
- `EXPOUND_MODEL_SUB_AGENT`
- `EXPOUND_MODEL_FAST`

## Design principles

- **Human-in-the-loop is the default**: external communications, signatures, and submissions all require human confirmation. No silent auto-approve.
- **Prompt Caching first**: stable, large content like the Partner Handbook is placed in `cache_control`.
- **Structured output**: sub-agents return Pydantic models, so the orchestration layer can aggregate and audit them easily.
- **Observability**: every agent call writes a run log, ready for downstream Dashboard consumption.

## Roadmap

- Extend the single-tenant CLI MVP into multi-tenant + Slack Bot
- Integrate with Anthropic Academy / the official Partner Portal (mock interfaces are stubbed)
- Introduce persistent storage (Postgres + object storage)
- Dashboard (Next.js) consuming run logs

## License

TBD. The repo is in design phase.
