# Worked Example: Reading Anthropic's Model Spec

**Document**: Anthropic Model Spec (["Claude's Character"](https://www.anthropic.com/claude/model-spec))
**Document length**: ~40 pages / ~15,000 words
**Time taken**: 75 minutes
**Date of this run**: May 2026

This is a real walkthrough of Workflow 01 applied to Anthropic's Model Spec — the document that describes how Claude is trained to behave. It's a good test case because: (a) it's substantive and detailed, (b) it covers topics where a reader could easily project their own understanding onto the text, and (c) one section is deliberately ambiguous in a way that Claude consistently misreads.

---

## Step 1: Session framing

I sent Prompt 1 verbatim. Claude's response included:

> *"Understood. I'll distinguish explicitly between claims the document makes directly, inferences I draw from it, and anything I'm drawing from my own knowledge of Anthropic's published work. I'll flag uncertainty rather than smooth it over."*

This was a good response — it restated the instruction in its own words, which suggests it registered.

**Checklist item 1**: ✅ Claude acknowledged the verification instruction explicitly.

---

## Step 2: Section map

After uploading, Claude produced this section map (abbreviated):

> - Being helpful, honest, and avoiding harm (early)
> - Claude's identity and psychological stability (early/mid)
> - Operators and users — how Claude navigates conflicting instructions (mid)
> - Hardcoded vs. softcoded behaviors (mid)
> - Agentic and multi-agent contexts (late)
> - Broader ethics and Anthropic's approach (late)

I checked two headings against the actual document. The section on "Operators and users" matches. The section Claude called "Broader ethics and Anthropic's approach" is real but the heading is slightly different — Claude paraphrased rather than quoting verbatim.

**Checklist item 2**: ✅ Map substantially correct; minor paraphrase of one heading noted.

---

## Step 3: Per-section extraction — "Hardcoded vs. softcoded behaviors"

This is the section I expected to be most important for understanding Claude's actual behavioral constraints.

I used Prompt 3. Claude extracted:

> *1. "The document distinguishes between 'hardcoded' behaviors (things Claude will never do regardless of instructions) and 'softcoded' behaviors (defaults that can be adjusted by operators or users)."*
> *2. "The hardcoded prohibitions include helping create weapons of mass destruction, generating CSAM, and undermining legitimate oversight of AI systems."*
> *3. "Softcoded defaults include how Claude handles sensitive topics, the level of explicitness in content, and whether Claude identifies itself as an AI."*

I verified claim 2 against the source text. The hardcoded prohibitions are listed and accurate.

**Checklist item 4**: ✅ Claims found in source at correct location.

---

## Where Claude was wrong — and I caught it

During the synthesis step (Prompt 5), I asked Claude for the document's central argument. It responded:

> *"The document's central argument is that Claude is trained to prioritize safety above all other considerations, including helpfulness, in all circumstances."*

This sounded plausible — it's what many people assume about AI safety training. But it's not what the document says.

I went back to the source. The Model Spec explicitly states a **priority ordering**: broadly safe first, then broadly ethical, then adherent to Anthropic's principles, then genuinely helpful — but it also states clearly that *in practice, the vast majority of interactions involve everyday tasks where there's no conflict between these properties*, and that being unhelpful is not "safe" from Anthropic's perspective.

The document's actual argument is more nuanced: safety and helpfulness are designed to be complementary, not in tension, and the priority ordering is for conflict resolution in edge cases, not a general statement that safety always overrides helpfulness.

I pushed back:

> *"You said the document argues that safety is prioritized above helpfulness in all circumstances. But I think the document says something more specific — that the priority ordering applies when there's a conflict, and that the document explicitly states unhelpfulness is not 'safe.' Can you re-read the relevant section and revise?"*

Claude's revised response was accurate:

> *"You're right. The document states a priority ordering for conflict cases, but explicitly argues that safety and helpfulness are not fundamentally in tension — and that being unhelpful has real costs that Anthropic takes seriously. I overstated the priority of safety as an absolute rule."*

**What happened here**: Claude's prior training had given it a strong prior that AI safety = safety-above-all. When synthesizing across sections, it defaulted to this prior rather than reporting what the document actually said. The verification step caught it.

**Checklist item 10**: ❌ → ✅ (Caught and corrected via verification gate 4)

---

## Final output quality

After correcting the synthesis error, Claude's plain-language summary was accurate and well-hedged. The summary included this sentence:

> *"The authors argue that genuine helpfulness and safety are complementary goals, and that a model which refuses tasks out of excessive caution is not meaningfully 'safe' — it just shifts the cost onto users."*

This accurately represents the document's position. I verified the relevant passage.

**Checklist item 15**: ✅ Summary accurately represents the document.
**Checklist item 17**: ✅ I can explain the main argument without referring to Claude's summary.

---

## Lessons from this run

1. **The synthesis step is the highest-risk step.** Claude's per-section extractions were accurate, but it introduced an error at synthesis — exactly where prior knowledge is most likely to contaminate the output. Always run verification gate 4.

2. **Plausible errors are the most dangerous.** Claude's wrong synthesis ("safety above helpfulness in all circumstances") was not obviously wrong — it's what many people believe the document says. If I hadn't pushed back, I would have gone away with a confident but inaccurate understanding of a document I'd "read carefully."

3. **Pushing back works.** When given specific feedback ("you said X but the document says Y"), Claude revised accurately. The workflow's value is partly in giving you the tools to push back productively.

---

*Part of the [Expound](https://github.com/EskilXu/Expound) workflow collection.*
