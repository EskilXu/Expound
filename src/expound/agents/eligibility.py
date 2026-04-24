"""Eligibility Scout — assesses a PartnerOrg against tier requirements.

Uses Claude Sonnet 4.6 with structured outputs to guarantee a well-formed
``EligibilityReport`` the orchestrator can consume without fragile parsing.
Large stable context (the Partner Handbook) goes into ``system`` with
``cache_control`` so repeated Scout runs during a demo are cheap.
"""

from __future__ import annotations

import anthropic

from ..knowledge import handbook
from ..state import EligibilityReport, PartnerOrg

MODEL = "claude-sonnet-4-6"

SYSTEM_ROLE = """\
You are the Eligibility Scout, a specialist sub-agent in the Expound onboarding \
system. Your job: given a prospective partner org, determine the current tier \
they satisfy, recommend a realistic target tier, and enumerate the gaps between.

Rules:
- Ground tier requirements in the Partner Handbook provided below.
- If required data is missing from the org profile, do NOT fabricate it —
  list it as an unmet requirement with 'unknown' as the current value.
- Weeks-to-target is a realistic calendar estimate assuming the standard
  Enable + Certify + Launch pace (8 weeks end-to-end).
- Output must conform exactly to the EligibilityReport schema.
"""


def run_eligibility_scout(
    partner: PartnerOrg,
    client: anthropic.Anthropic | None = None,
) -> EligibilityReport:
    client = client or anthropic.Anthropic()

    system = [
        {
            "type": "text",
            "text": SYSTEM_ROLE,
        },
        {
            "type": "text",
            "text": f"## Partner Handbook\n\n{handbook()}",
            "cache_control": {"type": "ephemeral"},
        },
    ]

    user_content = (
        "Produce an EligibilityReport for the partner below.\n\n"
        f"## Partner profile (JSON)\n{partner.model_dump_json(indent=2)}"
    )

    response = client.messages.parse(
        model=MODEL,
        max_tokens=4096,
        thinking={"type": "adaptive"},
        system=system,
        messages=[{"role": "user", "content": user_content}],
        output_format=EligibilityReport,
    )
    if response.parsed_output is None:
        raise RuntimeError(
            f"Eligibility Scout failed to parse output (stop_reason={response.stop_reason})"
        )
    return response.parsed_output
