"""Shared state models used across the orchestrator and sub-agents.

These are intentionally small and explicit — they double as the contract
between agents and as the audit surface the Dashboard consumes.
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field


class Tier(str, Enum):
    REGISTERED = "Registered"
    SELECT = "Select"
    PREMIER = "Premier"


class LearnerRole(str, Enum):
    SALES = "sales"
    SOLUTIONS_ARCHITECT = "solutions_architect"
    DEVELOPER = "developer"


class Learner(BaseModel):
    name: str
    role: LearnerRole
    email: str | None = None


class PartnerOrg(BaseModel):
    name: str
    website: str | None = None
    country: str | None = None
    headcount_ai_practice: int | None = Field(
        default=None, description="Headcount already focused on AI / LLM work"
    )
    existing_case_studies: list[str] = Field(default_factory=list)
    industries: list[str] = Field(default_factory=list)
    learners: list[Learner] = Field(default_factory=list)


# ---------- Eligibility Scout output ----------

class GapItem(BaseModel):
    requirement: str
    current: str
    needed: str
    how_to_close: str


class EligibilityReport(BaseModel):
    partner: str
    current_tier: Tier
    recommended_target_tier: Tier
    rationale: str
    gaps: list[GapItem]
    estimated_weeks_to_target: int


# ---------- Training Coach output ----------

class WeeklyPlanItem(BaseModel):
    day: Literal["Mon", "Tue", "Wed", "Thu", "Fri"]
    topic: str
    format: Literal["video", "lab", "live", "office_hour", "reading"]
    est_minutes: int


class LearningPath(BaseModel):
    learner: Learner
    target_certification: str
    weeks: int
    week1: list[WeeklyPlanItem]
    notes: str


# ---------- HITL checkpoints ----------

class HITLTask(BaseModel):
    id: str
    title: str
    summary: str
    risk: Literal["low", "medium", "high"]
    requires: list[str] = Field(
        description="Roles that can approve — e.g. ['champion', 'legal']"
    )
    created_on: date
    attached_artifacts: list[str] = Field(default_factory=list)


# ---------- Run log ----------

class RunLogEntry(BaseModel):
    """One observable step. Dashboard + audit log consume these."""
    ts: str
    agent: str
    action: str
    inputs: dict | None = None
    outputs: dict | None = None
    hitl: HITLTask | None = None
