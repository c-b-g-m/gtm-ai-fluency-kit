#!/usr/bin/env python3
"""
AI Fluency 101 scaffold generator (C-lite).

Generates starter assessment and learning-plan files based on function and role context.
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re


FUNCTION_TO_PLAN = {
    "marketing": "learning-plans/marketing-30-60-90.md",
    "sales-revops": "learning-plans/sales-revops-30-60-90.md",
    "support-success": "learning-plans/support-success-30-60-90.md",
}

GENERIC_OUTCOME_PATTERNS = [
    r"improve productivity",
    r"work faster",
    r"be better",
    r"increase efficiency",
    r"use ai better",
]

GENERIC_JD_PATTERNS = [
    r"responsible for many things",
    r"do various tasks",
    r"support team goals",
    r"help the team",
    r"cross-functional work",
]


def is_generic_outcome(text: str) -> bool:
    normalized = text.strip().lower()
    if len(normalized) < 20:
        return True
    return any(re.search(pattern, normalized) for pattern in GENERIC_OUTCOME_PATTERNS)


def is_generic_jd_summary(text: str) -> bool:
    normalized = text.strip().lower()
    if len(normalized) < 40:
        return True
    return any(re.search(pattern, normalized) for pattern in GENERIC_JD_PATTERNS)


def render_assessment(
    name: str,
    role: str,
    function: str,
    outcome: str,
    maturity: str,
    workflow: str,
    jd_summary: str,
    jd_metrics: str,
    jd_scope: str,
) -> str:
    return f"""# AI Fluency 101 Assessment - {name}

Date: {date.today().isoformat()}
Function: {function}
Role: {role}
Current maturity (self-selected): {maturity}
Primary recurring workflow: {workflow}
Target business outcome: {outcome}

## Job Description Grounding
- JD summary: {jd_summary}
- Scope and ownership boundaries: {jd_scope}
- Role success metrics from JD: {jd_metrics}

## Personalization Constraints (Must Hold)
- The plan must align to listed role responsibilities.
- The plan must align to the stated scope boundaries.
- The plan must improve at least one listed success metric.

## Baseline Self-Rating (1-4)
- Delegation:
- Description:
- Discernment:
- Diligence:
- Slope:

## Evidence To Gather This Month
- Annotated chat logs:
- Before/after output examples:
- Decision logs:
- Diligence statements:

## Priority Gaps
1.
2.
3.

## 30-Day Action Starter
- Week 1:
- Week 2:
- Week 3:
- Week 4:

## Anti-Generic Quality Check
- Is the workflow named clearly (not "general work")?
- Is the business outcome measurable (quality, cycle time, error rate, conversion, etc.)?
- Are accountability checks explicit (review owner, risk checks, disclosure)?
- Does every action map to JD scope and role metrics?
"""


def render_learning_plan(
    name: str,
    role: str,
    function: str,
    outcome: str,
    maturity: str,
    workflow: str,
    jd_summary: str,
    jd_metrics: str,
    jd_scope: str,
) -> str:
    return f"""# AI Fluency 101 Learning Plan - {name}

Date: {date.today().isoformat()}
Function: {function}
Role: {role}
Current maturity (self-selected): {maturity}
Primary recurring workflow: {workflow}
Business outcome target: {outcome}
JD summary: {jd_summary}
JD scope boundaries: {jd_scope}
JD success metrics: {jd_metrics}

## Stop Doing / Start Doing

Stop doing:
- Approaching {workflow} with ad hoc, one-off prompting and no quality criteria.

Start doing:
- Using a repeatable, structured workflow for {workflow} with explicit quality checks and accountability gates tied to: {jd_metrics}.

## 30/60/90 Focus

### 30 Days
- Build one repeatable AI-assisted workflow for: {workflow}
- Define quality criteria and accountability checks.
- Explicitly map this workflow to one JD responsibility and one JD success metric.

### 60 Days
- Standardize workflow and capture before/after metrics.
- Share and test with one teammate.
- Validate that workflow changes remain within JD scope boundaries.

### 90 Days
- Scale or automate one low-risk component with human review points.
- Document governance and ownership.
- Document which JD metrics moved and by how much.

## Evidence Tracker
- Weekly workflow updates:
- Quality improvements observed:
- Risks caught and corrected:
- Team adoption signals:

## Non-Generic Completion Rules
- Every milestone must name a concrete deliverable.
- Every milestone must name one measurable signal.
- Every milestone must name one owner for review/accountability.
- Every milestone must cite one JD responsibility or success metric.
"""


def copy_reference_plan(output_dir: Path, function: str, project_root: Path) -> None:
    source_rel = FUNCTION_TO_PLAN[function]
    source = project_root / source_rel
    target = output_dir / "reference-learning-plan.md"
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate AI Fluency 101 starter assets.")
    parser.add_argument("--name", required=True, help="Participant name")
    parser.add_argument("--role", required=True, help="Role title")
    parser.add_argument(
        "--function",
        required=True,
        choices=sorted(FUNCTION_TO_PLAN.keys()),
        help="Function track",
    )
    parser.add_argument("--outcome", required=True, help="Primary business outcome target")
    parser.add_argument(
        "--maturity",
        required=True,
        choices=["emerging", "developing", "capable"],
        help="Current maturity level",
    )
    parser.add_argument(
        "--workflow",
        required=True,
        help="One concrete recurring workflow to improve",
    )
    parser.add_argument(
        "--jd-summary",
        required=True,
        help="Short role summary from the job description",
    )
    parser.add_argument(
        "--jd-metrics",
        required=True,
        help="Success metrics expected by the role/job description",
    )
    parser.add_argument(
        "--jd-scope",
        required=True,
        help="Scope boundaries and ownership for the role",
    )
    parser.add_argument(
        "--output-dir",
        default="generated",
        help="Directory to write generated files",
    )
    args = parser.parse_args()
    if is_generic_outcome(args.outcome):
        raise SystemExit(
            "Outcome is too generic. Provide a measurable role-specific outcome "
            "(example: 'Reduce support escalation rework by 20% in 60 days')."
        )
    if is_generic_jd_summary(args.jd_summary):
        raise SystemExit(
            "JD summary is too generic. Provide specific responsibilities and scope "
            "(example: 'Own weekly campaign brief development and cross-channel launch QA')."
        )

    project_root = Path(__file__).resolve().parents[1]
    output_dir = (project_root / args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    assessment_path = output_dir / "assessment-starter.md"
    plan_path = output_dir / "learning-plan-starter.md"

    assessment_path.write_text(
        render_assessment(
            args.name,
            args.role,
            args.function,
            args.outcome,
            args.maturity,
            args.workflow,
            args.jd_summary,
            args.jd_metrics,
            args.jd_scope,
        ),
        encoding="utf-8",
    )
    plan_path.write_text(
        render_learning_plan(
            args.name,
            args.role,
            args.function,
            args.outcome,
            args.maturity,
            args.workflow,
            args.jd_summary,
            args.jd_metrics,
            args.jd_scope,
        ),
        encoding="utf-8",
    )
    copy_reference_plan(output_dir, args.function, project_root)

    print(f"Generated files in: {output_dir}")
    print("- assessment-starter.md")
    print("- learning-plan-starter.md")
    print("- reference-learning-plan.md")


if __name__ == "__main__":
    main()
