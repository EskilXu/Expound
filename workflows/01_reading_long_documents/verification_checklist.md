# Verification Checklist — Workflow 01

Print this or open it in a separate window while running the workflow. Check each item as you go. Do not complete the workflow without completing the checklist.

---

## Session setup

- [ ] 1. Did Claude explicitly acknowledge the verification instruction (Prompt 1)? *(If not: resend before continuing.)*
- [ ] 2. Does the section map Claude produced match the document's actual table of contents or headings? *(Spot-check two headings against the source.)*

---

## Per-section extraction (repeat for each section)

- [ ] 3. Did Claude preserve hedged language ("may suggest," "is consistent with," "preliminary") rather than converting it to confident assertions?
- [ ] 4. For the two most important claims in this section: can you find them in the source text at the location Claude indicated?
- [ ] 5. Did Claude distinguish between the document's own claims and claims it is attributing to cited sources?
- [ ] 6. For any claim Claude flagged as "supported by data": can you find that data in the section?

---

## Evidence quality

- [ ] 7. Did Claude correctly identify which evidence is from this document's own analysis vs. cited prior work?
- [ ] 8. Are any of the "supported" claims actually only supported by a single citation to external work — meaning the support lives in someone else's study, not this one?
- [ ] 9. Did Claude note any methodological limitations on the evidence, or did it describe all evidence as equally strong?

---

## Synthesis

- [ ] 10. Is Claude's stated "central argument" actually stated in the document, or is it Claude's inference about what the document is trying to say?
- [ ] 11. For each load-bearing claim: did you find it in the source document at the section Claude named?
- [ ] 12. If Claude said a claim is "well-supported," do you agree after seeing the evidence — or did the evidence turn out to be weaker than that description?

---

## Gaps and uncertainties

- [ ] 13. Do the gaps Claude identified match your own sense of what the document left unanswered?
- [ ] 14. Did Claude identify any claims that need external verification (statistics, citations)? Have you noted which ones you'll verify independently?

---

## Final output

- [ ] 15. Does Claude's plain-language summary accurately represent the document, or does it smooth over hedges and uncertainties the document contains?
- [ ] 16. Are there claims in the summary that didn't appear in your per-section extraction notes? *(If yes: these may be hallucinated or from Claude's prior knowledge — find them in the source or remove them.)*
- [ ] 17. Can you explain the document's main argument in your own words without referring to Claude's summary?

---

## Red flags (stop and re-run if you hit any of these)

- Claude gives a page number or section location for a claim that doesn't exist in the document
- Claude describes a specific data point (percentage, statistic, date) that you can't find in the source
- Claude's section map is missing significant sections of the actual document
- Claude's summary uses language the document doesn't use, without flagging it as inference
- Claude declines to acknowledge uncertainty when you explicitly ask "how confident are you that this is in the document?"

---

*Part of the [Expound](https://github.com/EskilXu/Expound) workflow collection.*
