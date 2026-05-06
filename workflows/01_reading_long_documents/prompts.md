# Workflow 01 — Prompt Sequences

Ready-to-paste prompts for each step of the long-document reading workflow. Use these in order, one section at a time. Do not skip the verification asks — they are part of the prompt, not optional add-ons.

---

## Prompt 1: Session framing (send this first, before uploading)

```
I'm going to ask you to help me read a long document carefully. I want you to be conservative about what you claim the document says. Specifically:

- If something is stated explicitly in the document, say so.
- If something is implied but not stated, flag it as an inference.
- If you're uncertain whether something is in the document or is your own prior knowledge, say so explicitly.

I will be checking your claims against the source text. Please confirm you understand this operating mode before we continue.
```

**What to look for in the response**: Claude should acknowledge the verification instruction explicitly, not just say "sure." If it doesn't, resend with: *"Please confirm specifically that you will flag inferences separately from direct claims."*

---

## Prompt 2: Section map (send after uploading the document)

```
Without summarizing any content yet, please list the main sections or chapters of this document. For each section, give:
- The section heading or title
- Its approximate location (page number, or early/middle/late if no page numbers)
- One sentence describing what kind of content it contains (e.g. "methodology description," "data tables," "policy recommendations")

Do not summarize the content of any section yet.
```

**Verification ask**: Before continuing, check two of the section headings against the actual document.

---

## Prompt 3: Per-section claim extraction

```
Now let's work through [SECTION NAME] carefully.

For this section only, please extract:
1. The main claims the document makes (not background, not citations of others — claims this document is asserting)
2. For each claim: is it supported by evidence in this section, or is it asserted without support here?
3. Any language that hedges or qualifies the claim (words like "may," "suggests," "is consistent with," "preliminary evidence indicates") — preserve these exactly, don't smooth them out

Format as a numbered list. One claim per item.
```

**Verification ask**: Pick the two most important claims. Find them in the source text. Are they there? Are the hedges preserved?

---

## Prompt 4: Evidence quality check

```
For the claims you just extracted from [SECTION NAME]:

For each claim that has supporting evidence, tell me:
- Is the evidence from this document's own data/analysis, or is it citing someone else's work?
- How strong is it? (Direct measurement / logical argument / analogy / single citation)
- Is there anything about the methodology or data that would make a skeptical reader question this evidence?

Be specific. Don't just say "the evidence is strong" — tell me what kind of evidence it is.
```

**Verification ask**: If Claude says a claim is supported by "the study's own data," verify you can find that data in the section.

---

## Prompt 5: Cross-section synthesis

```
We've now worked through [list the sections covered]. 

Based only on what we've extracted — not on your prior knowledge of this topic — what is the document's central argument? Give it in:
1. One sentence (the thesis)
2. The two or three claims the whole argument depends on most heavily (the load-bearing claims)
3. For each load-bearing claim: which section does it appear in, and is it well-supported or asserted?

If you're drawing on prior knowledge to fill gaps in the document, say so explicitly.
```

**Verification ask**: Find the load-bearing claims in the source document. Are they where Claude says they are?

---

## Prompt 6: Gap and uncertainty map

```
Now I want to understand what this document does NOT address or leaves uncertain.

Please identify:
1. Questions that a careful reader would want answered that the document doesn't address
2. Claims the document makes that would need external verification (e.g. statistical claims, citations you'd want to check)
3. Areas where the document's own hedged language suggests the authors are less confident

This is not a criticism of the document — I want to know where to focus my own verification effort.
```

**Verification ask**: The gaps and uncertainties Claude lists should feel right to you as someone who's now read the section extractions. If a gap surprises you, check whether it's genuinely missing or whether Claude missed content.

---

## Prompt 7: Plain-language output

```
Finally, write a plain-language summary of this document as I would explain it to a colleague who hasn't read it. This summary should:
- Reflect only what the document actually says (not what you know about the topic)
- Use hedged language where the document itself hedges
- Include the two or three things a reader should verify before acting on this document

Write in the first person plural: "The document argues..." or "The authors claim..."
```

**Verification ask**: Read this summary against your own notes from the extraction passes. Does it match? Any claims that appeared in the summary that didn't appear in your extraction notes?

---

*Part of the [Expound](https://github.com/EskilXu/Expound) workflow collection.*
