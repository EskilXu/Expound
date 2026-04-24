"""Seed Partner-Network knowledge.

In production this module would load the full Anthropic Partner Handbook,
course catalog, and certification syllabus (typically tens of KB of stable
text). Because this content is large and stable, it is an ideal candidate
for prompt caching: put it in the system prompt with
``cache_control={"type": "ephemeral"}`` and subsequent requests pay ~0.1x
on the cached portion.

Minimum cacheable prefix:
  * Opus 4.7 / Opus 4.6 / Haiku 4.5 → 4096 tokens
  * Sonnet 4.6                      → 2048 tokens

The seed below is intentionally small (a starting scaffold the Eligibility
Scout can override at runtime by fetching the live Partner Portal). Replace
with the real handbook before shipping.
"""

from __future__ import annotations

PARTNER_HANDBOOK_SEED = """
# Anthropic Partner Network — Reference Handbook (seed)

## Tiers
- Registered: initial tier. Requires 1 Claude Business Associate certification
  and a signed MSA. No revenue commitment.
- Select: proven delivery tier. Requires 2 Claude Solutions Architect
  certifications, 2 closed Claude engagements, and 1 referenceable customer.
- Premier: strategic tier. Requires annual revenue threshold, 1+ industry
  specialization, a named executive sponsor, and 3 referenceable customers.

## Core learning tracks
- Business Track → Claude Business Associate (60 MCQ + 2 scenarios, pass 75%)
- Technical Track → Claude Solutions Architect (40 MCQ + 1 design lab, pass 80%)
- Developer / Agent Track → Claude Agent Developer (hands-on lab, 85% test pass)

## Industry specializations (optional)
- Financial Services, Healthcare & Life Sciences, Public Sector, Software & Code.
- Each requires 1 additional industry-specific exam plus a lighthouse case.

## Certifications — validity
- All three core certifications are valid for 12 months.
- A delta re-certification path is generated 45 days before expiry covering
  only product changes since last certification.

## Required weekly cadence during Enable phase
- Mon: kickoff / syllabus review
- Tue–Thu: self-paced video + labs
- Fri: instructor office hour (optional for Business track, recommended for
  Solutions Architect and Agent Developer tracks)

## HITL checkpoints (must require human approval)
1. Submitting the formal partner application.
2. Signing any legal instrument (MSA, NDA, Co-sell Addendum).
3. Outbound communication to Anthropic or to the partner's customers.
4. Partner Directory listing changes.
5. Any CRM account/stage modification.

## Success metrics
- Time from application to Registered completion: target ≤ 3 weeks.
- First-attempt certification pass rate: target ≥ 85%.
- Re-certification completed before expiry: target ≥ 80%.
"""


def handbook() -> str:
    """Returns the current seed handbook. Replace with live fetch in prod."""
    return PARTNER_HANDBOOK_SEED.strip()
