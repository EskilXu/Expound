"""Training Coach — produces a week-1 learning path for a single learner.

Role-aware: the same course catalog is pruned differently for a Sales vs
a Solutions Architect vs an Agent Developer learner.
"""

from __future__ import annotations

import anthropic

from ..client import get_model, make_client, parse_message, thinking_kwargs
from ..knowledge import handbook
from ..state import Learner, LearningPath

SYSTEM_ROLE = """\
You are the Training Coach, a specialist sub-agent in the Expound onboarding \
system. Given a single learner and their role, output a realistic Week 1 plan \
leading toward the correct certification for their role:

  sales               → Claude Business Associate
  solutions_architect → Claude Solutions Architect
  developer           → Claude Agent Developer

Rules:
- Pull modules from the Partner Handbook course catalog.
- Five days (Mon–Fri), 60–120 total minutes per day.
- Include at least one lab or office_hour across the week.
- Output must conform exactly to the LearningPath schema.
"""


def run_training_coach(
    learner: Learner,
    client: anthropic.Anthropic | None = None,
) -> LearningPath:
    client = client or make_client()

    system = [
        {"type": "text", "text": SYSTEM_ROLE},
        {
            "type": "text",
            "text": f"## Partner Handbook\n\n{handbook()}",
            "cache_control": {"type": "ephemeral"},
        },
    ]

    user_content = (
        f"Generate a Week 1 LearningPath for:\n{learner.model_dump_json(indent=2)}"
    )

    return parse_message(
        client,
        output_format=LearningPath,
        model=get_model("sub_agent"),
        max_tokens=4096,
        system=system,
        messages=[{"role": "user", "content": user_content}],
        **thinking_kwargs(),
    )
