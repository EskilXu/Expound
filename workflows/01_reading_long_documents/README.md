# Workflow 01: Reading a Long Document with Claude

**Without falling for it.**

---

## When to use this workflow

Use this workflow when you need to extract reliable, verifiable understanding from a document that is too long to read carefully in one sitting — typically 20+ pages. It's designed for situations where being wrong has real consequences: a legal memo, a policy paper, a research report you'll cite, a contract you'll rely on.

Do **not** use this workflow if:
- You just need a rough orientation to a topic (a quick summary is fine for that)
- The document is short enough to read yourself in 30 minutes
- You don't have 60–90 minutes to do it properly

This workflow is slower than asking Claude to summarize. That's intentional.

## Time budget

**60–90 minutes** for a 40–60 page document. Shorter documents take less time, but don't rush the verification steps — they're where the value is.

| Step | Time |
|---|---|
| Setup and section chunking | 10 min |
| Per-section extraction passes | 30–40 min |
| Verification and cross-checking | 15–20 min |
| Synthesis and output | 10 min |

## Required tools

**Claude.ai only.** You do not need the CLI, an API key, or any technical setup. A free Claude account works; Claude.ai Pro or Max is recommended for longer documents (larger context window, no rate limits mid-session).

You will also need:
- The document (PDF, Word, or paste-able text)
- The verification checklist ([`verification_checklist.md`](./verification_checklist.md)) open in a separate window or printed

## The 5 steps

### Step 1: Frame the session

Before uploading the document, open a new Claude conversation and paste this exactly:

> *"I'm going to ask you to help me read a long document carefully. I want you to be conservative about what you claim the document says. If you're uncertain whether a claim is in the document or is your own inference, say so explicitly. I will be checking your work against the source text."*

This sets the operating mode. Claude responds differently when told explicitly that its work will be verified.

**Verification gate 1**: If Claude's response to this framing is something like "Great, I'll do my best!" without acknowledging the verification instruction, re-send the framing and add: *"Please confirm you understand that I will be cross-checking your claims against the source text."*

### Step 2: Upload and section-map

Upload the document (or paste it). Then ask:

> *"Without summarizing the content, list the main sections or chapters of this document and their approximate page numbers or locations."*

Review the section list. Does it match the document's actual table of contents or section headings? If it's significantly wrong or missing sections, the document may not have uploaded correctly, or Claude may be confusing it with a similar document from training.

**Verification gate 2**: Spot-check two section headings against the actual document before continuing.

### Step 3: Extract per section (use prompts.md)

Work through the document one section at a time. For each section, use the prompt sequences in [`prompts.md`](./prompts.md). Do not ask Claude to "summarize the whole document" — work section by section.

For each section, Claude will produce:
- The main claims made in that section
- The evidence offered for each claim
- Anything it flagged as uncertain or inferred rather than stated

**Verification gate 3**: For each section, pick the two most important claims and find them yourself in the source text. Are they actually there? Are they stated as strongly as Claude said, or with more hedging?

### Step 4: Cross-check the synthesis

After completing all sections, ask:

> *"Based on what you've extracted, what is the document's central argument? Give it in one sentence, then list the two or three claims the whole argument depends on most heavily."*

Then ask:

> *"For each of those load-bearing claims: where exactly in the document is it supported? Give me the section and approximate location."*

Go find those locations in the source document.

**Verification gate 4**: If Claude points you to support that doesn't actually support the claim, or gives you a location that doesn't exist, flag it. This is the most common failure point — Claude constructs a plausible central argument and then confabulates support for it.

### Step 5: Document your findings

Write up what you found in your own words — not Claude's words. Claude's extraction is a scaffold, not the output. If you can't re-explain the document's main argument without looking at Claude's summary, you haven't understood it yet.

**Verification gate 5**: Read your own write-up and ask: does this accurately represent what the document actually says, or does it represent what I hoped the document would say? These are different things.

---

## Worked example

See [`examples/EXAMPLE_50page_doc.md`](./examples/EXAMPLE_50page_doc.md) for a full walkthrough using Anthropic's Model Spec as the input document, including one step where Claude produced a wrong answer and how it was caught.

## Known failure modes

The main failure modes for this workflow are documented in [`../../failure_modes/`](../../failure_modes/):
- [Numerical precision](../../failure_modes/numerical_precision.md)
- [Citation fabrication](../../failure_modes/citation_fabrication.md)
- [Time sensitivity](../../failure_modes/time_sensitivity.md)
