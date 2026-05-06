# Failure Mode: Time Sensitivity

**Claude's knowledge has a training cutoff. For anything that changes over time, it may be confidently out of date.**

---

## What the failure looks like

You ask Claude about a regulation, a market rate, a company's current leadership, a law that was recently amended, a policy that changed last year. Claude answers in the present tense, confidently, with specific details. The answer reflects the state of the world as of its training cutoff — which may be a year or more before the current date.

Or: you ask about a pending situation — a bill that was being debated, a company that was in acquisition talks, a court case that was under appeal. Claude tells you the outcome. The outcome it tells you is wrong, or it tells you the case is still pending when it has long since been decided.

Or: Claude correctly tells you that X was true as of its training data, but doesn't flag that X is the type of thing that changes frequently and that you should verify the current state.

## Why this happens

Claude's training data has a cutoff date. It does not have access to the internet during a conversation (unless you are using a version with web search enabled, in which case this failure mode is partially mitigated but not eliminated). When it answers questions about current facts, it is reporting the state of its training data, not the current state of the world.

What makes this particularly dangerous is that Claude often doesn't know what it doesn't know. It can't tell you "this regulation was amended after my training cutoff" if the amendment occurred after its training cutoff and it has no knowledge of it. It simply answers based on what it knows — which may be outdated.

## The specific risks

- **Law and regulation**: statutes are amended, regulations are updated, enforcement priorities change
- **Market and financial data**: prices, rates, valuations, and competitive landscapes shift
- **Organizational facts**: leadership, corporate structure, subsidiary relationships, ownership
- **Technology**: software versions, API capabilities, platform policies, product availability
- **Policy and geopolitics**: government positions, international agreements, sanctions, trade rules

## The workaround

**Apply the recency test to every factual claim before acting on it.**

The recency test: for any specific fact Claude gives you, ask: "Could this have changed in the last 12–24 months?" If yes, verify before using.

**Practical steps**:
1. When asking about any fact in the categories above, add: *"Please note if this is the kind of information that changes over time and that I should verify for current accuracy."* This prompt nudges Claude to self-flag, though it's not a substitute for your own judgment.
2. For regulatory and legal facts: always verify against the primary source (the official text of the regulation, the court docket, the agency website) rather than relying on any secondary synthesis, including Claude's.
3. For market and competitive facts: treat Claude's knowledge as historical background, not current intelligence. Use it to understand the landscape as of 12–24 months ago; verify the current state through primary sources.

**When web search helps**: If you're using Claude with web search enabled (Claude.ai with search, or equivalent), time-sensitive facts are more reliable — but the citation fabrication failure mode still applies. Verify that the search results Claude is summarizing actually say what Claude claims.
