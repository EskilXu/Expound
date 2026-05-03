"""CLI entry point — `expound demo` runs a canned end-to-end scenario."""

from __future__ import annotations

import argparse
import os
import sys

from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule

from . import agents as sub
from .client import get_provider, required_env_var
from .orchestrator import orchestrate
from .state import Learner, LearnerRole, PartnerOrg

console = Console()


def _demo_partner() -> PartnerOrg:
    """Canned demo partner — ACME Consulting."""
    return PartnerOrg(
        name="ACME Consulting",
        website="https://acme-consulting.example",
        country="US",
        headcount_ai_practice=18,
        industries=["Financial Services", "Software & Code"],
        existing_case_studies=[
            "LLM-driven KYC triage for mid-market bank (Claude Sonnet, 2025)",
        ],
        learners=[
            Learner(name="Li Wen", role=LearnerRole.SOLUTIONS_ARCHITECT),
            Learner(name="Wang Zhe", role=LearnerRole.DEVELOPER),
            Learner(name="Maria Reyes", role=LearnerRole.SALES),
        ],
    )


def _require_api_key() -> None:
    var = required_env_var()
    if not os.environ.get(var):
        provider = get_provider()
        console.print(
            Panel.fit(
                f"[red]{var} is not set.[/red] (provider={provider})\n\n"
                f"Export it before running the demo:\n"
                f"  [dim]export {var}=...[/dim]",
                border_style="red",
            )
        )
        sys.exit(2)


def cmd_demo(args: argparse.Namespace) -> int:
    _require_api_key()

    partner = _demo_partner()
    console.print(Rule("[bold]Expound demo · ACME Consulting[/bold]"))

    console.print("\n[bold]Step 1[/bold] — Eligibility Scout")
    report = sub.run_eligibility_scout(partner)
    console.print(
        Panel.fit(
            f"Current tier: [bold]{report.current_tier.value}[/bold]\n"
            f"Recommended target: [bold]{report.recommended_target_tier.value}[/bold]\n"
            f"ETA: [bold]{report.estimated_weeks_to_target}[/bold] weeks\n\n"
            f"{report.rationale}",
            title="Eligibility Report",
        )
    )
    for gap in report.gaps:
        console.print(f"  · {gap.requirement}: need [bold]{gap.needed}[/bold] (now {gap.current})")

    console.print("\n[bold]Step 2[/bold] — Training Coach for Li Wen")
    path = sub.run_training_coach(partner.learners[0])
    console.print(
        Panel.fit(
            f"Target: [bold]{path.target_certification}[/bold]\n{path.notes}",
            title=f"Week 1 Plan — {path.learner.name}",
        )
    )
    for item in path.week1:
        console.print(
            f"  {item.day}  [{item.format}]  {item.topic}  [dim]({item.est_minutes}m)[/dim]"
        )

    console.print("\n[bold]Step 3[/bold] — Application Packager (HITL)")
    task = sub.run_application_packager(partner.name, "Select")
    console.print(
        Panel.fit(
            f"[yellow]HITL · {task.title}[/yellow]\n"
            f"Risk: {task.risk} · Requires: {', '.join(task.requires)}\n\n"
            f"{task.summary}\n\n"
            f"Attached: {', '.join(task.attached_artifacts)}",
            title="Awaiting approval",
            border_style="yellow",
        )
    )

    if args.orchestrator:
        console.print("\n[bold]Step 4[/bold] — Orchestrator end-to-end")
        with console.status("[bold cyan]Orchestrator running…[/bold cyan]"):
            summary = orchestrate(
                "A prospective partner 'ACME Consulting' (Financial Services + Software, "
                "18 AI-practice headcount, 1 case study) wants to join at the Select tier. "
                "Run eligibility, design a Week 1 plan for Li Wen (Solutions Architect), "
                "and prepare the application HITL task. Report what you did."
            )
        console.print(Panel(summary, title="Orchestrator summary"))

    console.print(Rule("[green]demo complete[/green]"))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="expound")
    sub_parsers = parser.add_subparsers(dest="command", required=True)

    demo = sub_parsers.add_parser("demo", help="Run the canned demo scenario.")
    demo.add_argument(
        "--orchestrator",
        action="store_true",
        help="Also run the end-to-end Opus 4.7 orchestrator step (costs more).",
    )
    demo.set_defaults(func=cmd_demo)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
