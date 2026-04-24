"""Application Packager — prepares submission materials for review.

Stub. Real implementation will render a Business Plan + company 1-pagers
and assemble attachments for DocuSign / email. For v0.1 we return a
placeholder artifact bundle so the orchestrator contract is stable.
"""

from __future__ import annotations

from datetime import date

from ..state import HITLTask


def run_application_packager(partner_name: str, target_tier: str) -> HITLTask:
    return HITLTask(
        id=f"apply-{partner_name.lower().replace(' ', '-')}",
        title=f"Submit Anthropic Partner application for {partner_name}",
        summary=(
            f"Prepared application package targeting {target_tier} tier. "
            "Contains: Business Plan (draft), company 1-pager, existing "
            "case studies. Requires Champion approval before submission."
        ),
        risk="high",
        requires=["champion", "legal"],
        created_on=date.today(),
        attached_artifacts=[
            "business_plan_draft.pdf",
            "company_1pager.pdf",
            "case_studies.zip",
        ],
    )
