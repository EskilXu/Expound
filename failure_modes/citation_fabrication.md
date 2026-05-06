# Failure Mode: Citation Fabrication

**Claude invents citations. This is the most professionally dangerous failure mode for knowledge workers.**

---

## What the failure looks like

You ask Claude to support a claim with a reference. It gives you an author name, a publication title, a journal, and a year. The citation is formatted correctly. It is not real.

Or: it is partially real — the author exists, the journal exists, but the specific paper doesn't. Or the paper exists, but it doesn't say what Claude claims it says.

Or: Claude extracts citations from a document you've uploaded and produces a list that looks like the document's reference list but contains errors — author names slightly wrong, years transposed, titles paraphrased in a way that doesn't match the actual title.

## Why this happens

Claude does not have access to a database of verified citations. When it produces a citation, it is generating plausible-looking text that matches the pattern of citations in its training data. For well-known papers in high-traffic fields, this often works — the paper exists, and Claude has seen it cited enough times to reproduce the citation accurately. For less prominent work, specialist literature, recent publications, or non-English sources, the error rate is much higher.

The mechanism is the same as fluency-is-not-truth at the sentence level: the citation looks like a citation, is formatted like a citation, and sounds like a citation — because Claude was trained on text that contains citations. Whether it corresponds to a real document is a separate question.

## The specific risks

For professional use, the dangerous scenarios are:
- **Legal briefs and memos**: a fabricated case citation is a professional responsibility violation
- **Academic writing**: a fabricated source is plagiarism by commission (asserting research that doesn't exist)
- **Journalism and policy work**: citing a source that can't be verified undermines credibility
- **Due diligence**: research that relies on non-existent sources is not research

## The workaround

**Treat every citation Claude produces as unverified until you have confirmed it yourself.**

The verification process:
1. For any citation Claude generates: search for the title and author combination in Google Scholar, PubMed, Westlaw, or the relevant field database
2. If the paper exists: verify that the cited claim actually appears in the paper (Claude can correctly identify the paper but misrepresent what it says)
3. If you can't find the paper: do not use the citation, and do not use Claude's summary of what the paper allegedly says

**A better use pattern**: Instead of asking Claude to cite sources, gather your own sources first, then ask Claude to synthesize or analyze the sources you have provided. This inverts the risk: you're asking Claude to work with verified material rather than asking it to retrieve verification.

**Red flag language**: Be especially skeptical when Claude cites: (a) relatively obscure sources, (b) sources from fields where you can't easily verify, (c) sources with suspiciously perfect relevance to your exact question, (d) working papers or conference proceedings (harder to verify than published journals).
