"""Orchestrator — routes work across specialist sub-agents.

The orchestrator runs Opus 4.7 with adaptive thinking. Each sub-agent is
exposed as a tool via the beta tool runner, so the orchestrator itself
only contains a short system prompt + routing logic; the specialist work
happens inside each tool.

Kept deliberately small: the sub-agents own the domain, the orchestrator
owns sequencing and HITL.
"""

from __future__ import annotations

import json
from typing import Callable

import anthropic
from anthropic import beta_tool

from . import agents as sub
from .state import Learner, LearnerRole, PartnerOrg

ORCHESTRATOR_MODEL = "claude-opus-4-7"

SYSTEM = """\
You are Expound's Orchestrator. You coordinate specialist sub-agents to drive \
an enterprise through the Anthropic Partner Network onboarding journey.

Available specialists (as tools):
  run_eligibility_scout      — gap report + tier recommendation
  run_training_coach         — week-1 learning path for one learner
  run_application_packager   — produces a submission bundle + HITL task
  run_certification_prep     — readiness scoring and targeted review
  run_enablement_gtm         — demo scaffold + GTM deliverables

Rules:
- Delegate domain work; do not answer from memory when a specialist tool applies.
- Any action with external side effects (application submit, signing,
  outbound comms, directory changes, CRM mutations) must be surfaced as a
  HITL task — never executed directly.
- When you have enough results to answer, stop calling tools and produce a
  concise summary for the human operator.
"""


def _make_tools(client: anthropic.Anthropic) -> list[Callable]:
    """Wraps sub-agents in @beta_tool decorators with clear docstrings.

    Each tool returns a JSON string so the orchestrator LLM can read it
    as tool_result content without us having to re-serialize.
    """

    @beta_tool
    def run_eligibility_scout(partner_profile_json: str) -> str:
        """Produce a gap report and tier recommendation for a prospective partner.

        Args:
            partner_profile_json: JSON of a PartnerOrg — name, website,
                country, headcount_ai_practice, industries, existing_case_studies,
                learners. Missing fields are OK — the Scout will treat them as
                unknown rather than fabricate.
        """
        partner = PartnerOrg.model_validate_json(partner_profile_json)
        report = sub.run_eligibility_scout(partner, client=client)
        return report.model_dump_json()

    @beta_tool
    def run_training_coach(learner_name: str, learner_role: str) -> str:
        """Generate a Week 1 learning path for one learner.

        Args:
            learner_name: Full name.
            learner_role: One of 'sales', 'solutions_architect', 'developer'.
        """
        learner = Learner(name=learner_name, role=LearnerRole(learner_role))
        path = sub.run_training_coach(learner, client=client)
        return path.model_dump_json()

    @beta_tool
    def run_application_packager(partner_name: str, target_tier: str) -> str:
        """Bundle application materials and produce a HITL task for the Champion.

        Returns a HITLTask — do NOT submit anything yourself; the HITL gate exists
        precisely so that a human approves before submission.
        """
        task = sub.run_application_packager(partner_name, target_tier)
        return task.model_dump_json()

    @beta_tool
    def run_certification_prep(learner_name: str, certification: str) -> str:
        """Score a learner's current readiness for a given Claude certification."""
        return json.dumps(sub.run_certification_prep(learner_name, certification))

    @beta_tool
    def run_enablement_gtm(partner_name: str, industry: str) -> str:
        """Prepare demo scaffold, joint whitepaper draft, and Partner Directory copy."""
        return json.dumps(sub.run_enablement_gtm(partner_name, industry))

    return [
        run_eligibility_scout,
        run_training_coach,
        run_application_packager,
        run_certification_prep,
        run_enablement_gtm,
    ]


def orchestrate(goal: str, client: anthropic.Anthropic | None = None) -> str:
    """Run the orchestrator to completion against ``goal``.

    Returns the final text response the orchestrator produces for the operator.
    """
    client = client or anthropic.Anthropic()
    tools = _make_tools(client)

    runner = client.beta.messages.tool_runner(
        model=ORCHESTRATOR_MODEL,
        max_tokens=16000,
        thinking={"type": "adaptive"},
        output_config={"effort": "high"},
        system=SYSTEM,
        tools=tools,
        messages=[{"role": "user", "content": goal}],
    )

    final_text = ""
    for message in runner:
        for block in message.content:
            if block.type == "text":
                final_text = block.text
    return final_text
