# Manifesto

*Why Expound exists, and what it's trying to do.*

---

## The accessibility problem in d/acc

Vitalik Buterin's d/acc framework — differential acceleration of the defensive, decentralized, and accessible — is the most coherent framework I've found for thinking about how to build technology in an era of powerful AI. The third term, accessible, is usually the one that gets the least attention. Defensive is exciting. Decentralized is ideologically satisfying. Accessible sounds like a nice-to-have.

It isn't. It's structural.

Here's why: a safety methodology that only benefits the people who can already navigate the technical infrastructure is not a safety methodology — it's a capability concentrator. If Constitutional AI produces genuinely safer, more honest AI assistants, and those assistants are effectively only usable by developers and ML researchers, then Constitutional AI's safety properties accrue to a very small fraction of the people whose decisions shape the world. The lawyer doing contract review, the school administrator managing a crisis, the mid-career operator making a hiring decision — they are either not using AI at all, or they're using it badly, without the verification practices that make it trustworthy.

That gap is not a personal failing. It's a distribution failure. The documentation assumes Python. The tutorials assume familiarity with APIs. The "AI for everyone" courses are thin enough to be useless for serious work. The people who need these tools most are the ones most likely to bounce off the on-ramp.

## Distribution is safety

This is the thesis Expound is built on: **distribution is safety**.

A frontier safety methodology only delivers safety in proportion to how widely it's actually used in practice. An AI assistant trained to be honest and harmless, used by someone with no framework for catching its failure modes, is not a net safety gain — it's a confident hallucination machine with good manners. The safety properties are only activated by a user who knows where to push back.

That means the work of making AI safe is not finished when the model ships. It continues in the hands of every person who uses it. And most of those people have never read a paper on Constitutional AI, don't know what RLHF means, and don't have time to learn. They need a different kind of on-ramp: one that starts with their work, not with the technology.

## What Expound is and isn't

Expound is a collection of practical workflows for using Claude well — not code courses, not introductions to AI concepts, not hype about productivity gains. Workflows for real professional tasks: reading a long document without being fooled by fluency, drafting a memo with appropriate uncertainty markers, doing market research that can be reproduced.

Each workflow includes explicit verification gates — places where you are instructed to check Claude's work before using it. This is not optional, and it's not paternalism. It reflects an honest assessment of where current LLMs fail: numerical calculations, obscure citations, time-sensitive information, domain-specific judgment calls. A workflow without verification is just a faster way to produce confident errors.

**What Expound is not**: Anthropic-affiliated, official, or endorsed. I'm an independent user who respects Anthropic's published methodology and uses their tools daily. Nothing in this collection represents Anthropic's views, and nothing should be taken as Anthropic's guidance. If there's a conflict between something here and Anthropic's official documentation, trust the official documentation.

## Why I'm the one building this

I came to serious agentic AI use late — in 2025, after fifteen years operating at the intersection of infrastructure, regulatory environments, and emerging technology. I am not an engineer. I had to learn these tools from scratch, by daily practice, making all the mistakes that come from not having a CS background.

That turned out to be useful. Because I had to build my own on-ramp, I know where the on-ramp is hard. The notes I made for myself — the verification steps, the failure modes I hit, the workarounds that actually work — are the raw material for this collection.

Sharing them is the cheapest thing I can do to address the distribution problem. If they help one lawyer catch a hallucinated citation before it lands in a brief, or one school administrator understand why Claude's confident summary of a policy document might be wrong, that's one more person using AI with their eyes open.

That's d/acc accessibility, in practice.

---

*— Eskil (Yufeng Xu), Tokyo, 2026*
*[github.com/EskilXu](https://github.com/EskilXu) · eskilca2024 [at] gmail [dot] com*
