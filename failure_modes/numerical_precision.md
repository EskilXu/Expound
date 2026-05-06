# Failure Mode: Numerical Precision

**Claude is unreliable for exact numerical work. This is not a bug you can prompt away.**

---

## What the failure looks like

You ask Claude to calculate something — a percentage, a compound growth rate, a unit conversion, a financial projection — and it gives you an answer that looks right. The format is correct, the units are right, it's expressed to two decimal places. It is wrong.

Or: you paste a table of numbers and ask Claude to identify the highest value, compute a sum, or flag an outlier. It produces a confident answer that is approximately right but not exactly right.

Or: you ask Claude to extract numerical data from a document and it gives you numbers that are close to what the document says but subtly off — a year transposed, a decimal shifted, a percentage that's actually a different statistic from the one you asked for.

## Why this happens

Claude is a language model. It was trained on text, not on arithmetic. It does not calculate in the way a spreadsheet or a calculator calculates. When it produces a number, it is producing the token sequence that most plausibly follows from the preceding context. For simple arithmetic on small numbers, this is usually right. For anything involving more than two or three operations, longer numbers, percentages of percentages, or data extraction from complex tables, the error rate is meaningful.

This is a structural property of the architecture, not a calibration issue. Better prompting helps at the margins; it does not solve the underlying problem.

## The specific risks

For professional use, the dangerous scenarios are:
- **Financial models**: any computation involving compounding, ratios, or multi-step arithmetic
- **Legal or regulatory thresholds**: exact numbers matter (statutes of limitations, filing deadlines, penalty thresholds)
- **Statistical results**: percentages, p-values, confidence intervals extracted from research documents
- **Data with units**: converting between currencies, units of measurement, or time zones

## The workaround

**Don't use Claude to calculate. Use Claude to set up the calculation.**

For any numerical task:
1. Ask Claude to identify what numbers need to be computed and what formula or method applies
2. Do the computation yourself in a spreadsheet, calculator, or dedicated tool
3. Return the result to Claude for interpretation or narrative context if needed

For data extraction:
1. Ask Claude to extract numbers and flag where in the source document each number appears
2. Verify every extracted number against the source before using it
3. For tables: extract the structure, then verify each cell independently

**The rule**: if the number matters for a decision, a document, or a communication, verify it from the source or calculate it yourself. Do not use Claude's number as the final answer.
