from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CASES_ROOT = REPO_ROOT / "docs" / "cases"
LEGACY_STATUS = "pre-cutover artifacts are archived under `docs/legacy/superpowers/`"


@dataclass(frozen=True)
class RenderContext:
    case_slug: str
    round_slug: str
    title: str
    user_request: str
    case_goal: str
    task_routing: str
    orchestrator: str
    quality_mode: str
    cases_root: Path
    case_root: Path
    round_root: Path
    topic_slug: str
    current_date: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scaffold WW case and round artifacts under docs/cases/."
    )
    parser.add_argument("--case-slug", required=True, help="Case slug, for example case-based-artifact-layout.")
    parser.add_argument("--round-slug", required=True, help="Round slug, for example 2026-05-23-topic.")
    parser.add_argument("--title", required=True, help="Human-readable round title.")
    parser.add_argument("--user-request", required=True, help="Original user request for the round.")
    parser.add_argument(
        "--case-goal",
        help="Optional case goal used when creating a new case.md. Defaults to a TODO placeholder.",
    )
    parser.add_argument(
        "--task-routing",
        default="code/programming",
        choices=["code/programming", "design/ads/product", "video/creative"],
        help="Initial task routing placeholder for the generated brief and dispatch plan.",
    )
    parser.add_argument(
        "--orchestrator",
        default="staff-engineer-orchestrator",
        help="Initial orchestrator placeholder for the generated brief and dispatch plan.",
    )
    parser.add_argument(
        "--quality-mode",
        default="standard",
        choices=["standard", "strict"],
        help="Initial quality mode placeholder for the generated working brief.",
    )
    parser.add_argument(
        "--with-design-spec",
        action="store_true",
        help="Create a design-spec.md scaffold in the round directory.",
    )
    parser.add_argument(
        "--with-implementation-plan",
        action="store_true",
        help="Create an implementation-plan.md scaffold in the round directory.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_CASES_ROOT,
        help="Root directory for case artifacts. Defaults to docs/cases/.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing round files if they already exist.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned actions without writing files.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Emit machine-readable JSON output.",
    )
    return parser.parse_args()


def derive_topic_slug(round_slug: str) -> str:
    match = re.match(r"^\d{4}-\d{2}-\d{2}-(.+)$", round_slug)
    if match:
        return match.group(1)
    return round_slug


def relative_markdown_path(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def build_context(args: argparse.Namespace) -> RenderContext:
    cases_root = args.output_root.resolve()
    case_root = cases_root / args.case_slug
    round_root = case_root / "rounds" / args.round_slug
    case_goal = args.case_goal or f"TODO: describe the long-lived goal for `{args.case_slug}`"
    return RenderContext(
        case_slug=args.case_slug,
        round_slug=args.round_slug,
        title=args.title,
        user_request=args.user_request,
        case_goal=case_goal,
        task_routing=args.task_routing,
        orchestrator=args.orchestrator,
        quality_mode=args.quality_mode,
        cases_root=cases_root,
        case_root=case_root,
        round_root=round_root,
        topic_slug=derive_topic_slug(args.round_slug),
        current_date=date.today().isoformat(),
    )


def render_case_md(context: RenderContext, existing_text: str | None) -> str:
    case_root_markdown = f"{relative_markdown_path(context.case_root)}/"
    if existing_text is None:
        return "\n".join(
            [
                f"# Case: {context.case_slug}",
                "",
                "- Status: active",
                f"- Canonical Root: `{case_root_markdown}`",
                f"- Current Round: `{context.round_slug}`",
                f"- Goal: {context.case_goal}",
                f"- Legacy Status: {LEGACY_STATUS}",
                "",
                "## Round Index",
                "",
                f"- `{context.round_slug}`",
                "",
                "## Notes",
                "",
                f"- New `$ww` and `$www` rounds for this case should write under `{case_root_markdown}rounds/<round-slug>/`.",
                "- Older artifacts that predate the `docs/cases/...` cutover are historical references under `docs/legacy/superpowers/`, not active write targets.",
                "- `case.md` is navigational only. It is not a dispatch gate.",
                "",
            ]
        )

    lines = existing_text.splitlines()
    current_round_line = f"- Current Round: `{context.round_slug}`"
    updated = []
    current_round_set = False
    in_round_index = False
    round_present = False
    inserted = False

    for index, line in enumerate(lines):
        if line.startswith("- Current Round:"):
            updated.append(current_round_line)
            current_round_set = True
            continue

        if line.strip() == "## Round Index":
            in_round_index = True
            updated.append(line)
            continue

        if in_round_index:
            if line.startswith("## "):
                if not round_present:
                    if updated and updated[-1] != "":
                        updated.append("")
                    updated.append(f"- `{context.round_slug}`")
                    round_present = True
                    inserted = True
                in_round_index = False
            elif line.strip().startswith(f"- `{context.round_slug}`"):
                round_present = True

        updated.append(line)

        if in_round_index and index == len(lines) - 1 and not round_present:
            updated.append(f"- `{context.round_slug}`")
            inserted = True
            round_present = True

    if not current_round_set:
        insertion_index = 4 if len(updated) >= 4 else len(updated)
        updated.insert(insertion_index, current_round_line)

    if "## Round Index" not in existing_text:
        if updated and updated[-1] != "":
            updated.append("")
        updated.extend(["## Round Index", "", f"- `{context.round_slug}`"])
        inserted = True

    if not inserted and not round_present:
        updated.append(f"- `{context.round_slug}`")

    return "\n".join(updated) + "\n"


def render_working_brief(context: RenderContext) -> str:
    round_root_markdown = f"{relative_markdown_path(context.round_root)}/"
    case_root_markdown = f"{relative_markdown_path(context.case_root)}/"
    return f"""# Working Brief: {context.title}

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: draft
- `topic_slug`: {context.topic_slug}
- `case_slug`: {context.case_slug}
- `round_slug`: {context.round_slug}
- `case_root`: `{case_root_markdown}`
- `round_root`: `{round_root_markdown}`
- `created_at`: {context.current_date}
- `updated_at`: {context.current_date}
- `derived_from_user_request`: `{context.user_request}`

## Round Intent

- `quality_mode`: {context.quality_mode}

## Gate State

- `estimation_complete`: false
- `brief_status`: draft
- `brief_version`: 1

## Routing

- `task_routing`: `{context.task_routing}`
- `orchestrator_choice`: `{context.orchestrator}`

## Core Intent

- `goal`: TODO
- `artifact_type`: scaffolded round artifact
- `relevant_context`:
  - TODO
- `constraints`:
  - TODO

## Risk And Structure

- `risk_lenses`:
  - TODO
- `parallelism_assessment`:
  - TODO
- `blocking_dependencies`:
  - TODO
- `section_or_workstream_map`:
  - section 1: TODO

## Scope Preparation

- `artifact_mappings`:
  - TODO
- `exclusive_write_scope`:
  - `path_glob`: `{relative_markdown_path(context.case_root / "case.md")}`
  - `path_glob`: `{relative_markdown_path(context.round_root / "working-brief.md")}`
  - `path_glob`: `{relative_markdown_path(context.round_root / "dispatch-plan.md")}`
- `shared_read_scope`:
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/**/*`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - TODO
- `persona_selection_notes`:
  - TODO
- `recommended_worker_mode_by_section`:
  - section 1: TODO
- `worker_mode_reasoning_by_section`:
  - section 1: TODO
- `goal_tuning_by_section`:
  - section 1: TODO
- `constraint_override_notes_by_section`:
  - section 1: TODO
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - TODO

## Grill-Me Decision Log

The orchestrator owns this log. The `grill-me` explorer remains read-only and is applied inline during planning.

Use one entry per decision:

- Decision ID:
- State: open | confirmed | deferred
- Question:
- User-Confirmed Answer:
- Recommendation Offered:
- Rationale Or Repository Evidence:
- Dependencies Resolved:
- Dependent Branches Unblocked:

Rules:

- create or update an entry only when `grill-me` is explicitly active
- keep `State: open` until the user explicitly confirms an answer
- do not treat the recommended answer as confirmation
- record repository-resolved facts as evidence without asking the user to decide them
- use confirmed entries as inputs to later design specs and implementation plans
- keep round approval and runtime lifecycle state in `dispatch-plan.md`
- when the user stops grilling, mark the current unresolved branch `deferred`

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-1: true
- `review_target_strategy`:
  - TODO
- `controller_semantics_notes`:
  - TODO

## Rules

- This file is a scaffold and must be completed before dispatch-plan approval.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
"""


def render_dispatch_plan(context: RenderContext) -> str:
    round_root_markdown = f"{relative_markdown_path(context.round_root)}/"
    case_root_markdown = f"{relative_markdown_path(context.case_root)}/"
    brief_path = relative_markdown_path(context.round_root / "working-brief.md")
    case_md_path = relative_markdown_path(context.case_root / "case.md")
    return f"""# Dispatch Plan: {context.title}

- Date: {context.current_date}
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: {context.case_slug}
- Round Slug: {context.round_slug}
- Case Root: `{case_root_markdown}`
- Round Root: `{round_root_markdown}`
- Plan State: awaiting-approval
- Last Approved Revision: none
- Rollback Baseline Revision: none
- Task Routing: {context.task_routing}
- Main Orchestrator: {context.orchestrator}

## Strict Review Runtime State

```yaml
strict_review:
  mode: {context.quality_mode}
  target: none
  state: idle
  cycle_count: 0
```

## Preconditions

- Estimation Complete: false
- Working Brief Status: draft

> Do not launch any real subagent until the preconditions are satisfied and `Plan State: approved`.

Path identity rules:

- `Case Root` must resolve to `docs/cases/<case_slug>/`
- `Round Root` must resolve to `docs/cases/<case_slug>/rounds/<round_slug>/`
- new dispatch-round artifacts are canonically written under `Round Root`
- legacy type-based paths are legacy history only; they are not canonical targets or ongoing generation defaults

## Source Context

- User Request: `{context.user_request}`
- Working Brief Reference: `{brief_path}`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: TODO
- Relevant Context: TODO
- Constraints:
  - TODO
- Risks:
  - TODO
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Scaffold Draft

- Section ID: section-scaffold-draft
- Section State: drafted
- Runtime State: queued
- Required For Goal: true
- Draft Author Role: {context.orchestrator}
- Planned Reviewer Persona: TODO
- Planned Specialist Personas: none
- Planned Scope:
  - `TODO`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: TODO
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: TODO
- Worker Mode Rationale: TODO
- Goal Tuning: TODO
- Constraint Interaction Rule: TODO
- Planned Review Lanes:
  - Lane ID: lane-scaffold-review
  - Lane Type: scope-review
  - Reviewer Persona: TODO
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `{case_md_path}`
    - `path_glob`: `{relative_markdown_path(context.round_root / "working-brief.md")}`
    - `path_glob`: `{relative_markdown_path(context.round_root / "dispatch-plan.md")}`
  - `shared_read_scope`:
    - `path_glob`: `README.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/**/*`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: TODO
    - `artifact_kind`: TODO
    - `artifact_path`: TODO
    - `section_anchors`: TODO
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Scaffold Draft

- Section ID: section-scaffold-draft
- Runtime State: queued
- Active Execution ID:
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode:
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
- Packet Records:
- Attempt Records:
- Attempt Count: 0
- Last Update At: {context.current_date}
- Next Action: await human approval
- Active Write Scope:
- Result Summary:
- Canonical Result Artifact Location:
- Concerns:
  - TODO
- Blocker Reason:
- Close State: open
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Scaffold Draft

- Section ID: section-scaffold-draft
- Review Target Strategy:
  - TODO
- Review Lane Records:
  - Lane ID: lane-scaffold-review
  - Lane Type: scope-review
  - Reviewer Persona: TODO
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
  - Reviewer Findings:
  - Orchestrator Synthesis:
  - Strict Review Outcome: none
- Human Decision: none
- Revision Notes:

## Approval Block

- Required Human Choice (rendered labels):
  - `1. Approve`
  - `2. Revise`
  - `3. Stop`
- Numeric Reply Mapping:
  - `1` -> `Approve`
  - `2` -> `Revise`
  - `3` -> `Stop`
- Canonical Decision Values: `Approve` | `Revise` | `Stop`
- Accepted Word Replies: `Approve` | `Revise` | `Stop`
- Current Choice: none
- Approved By:
- Approval Time:
- Notes: scaffolded draft; complete the planning fields before approval
"""


def render_design_spec(context: RenderContext) -> str:
    return f"""# Design Spec: {context.title}

Date: {context.current_date}
Status: Drafted
Scope: TODO

## Goal

TODO

## Decisions

1. TODO

## Out Of Scope

- TODO
"""


def render_implementation_plan(context: RenderContext) -> str:
    return f"""# Implementation Plan: {context.title}

Date: {context.current_date}
Status: Drafted

## Goal

TODO

## Primary Targets

- TODO

## Steps

1. TODO

## Guardrails

- TODO

## Verification

- TODO
"""


def write_text(path: Path, content: str, overwrite: bool) -> str:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Refusing to overwrite existing file without --overwrite: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return "updated" if path.exists() else "created"


def plan_actions(context: RenderContext, args: argparse.Namespace) -> list[tuple[str, Path, str]]:
    case_md_path = context.case_root / "case.md"
    existing_case_text = case_md_path.read_text(encoding="utf-8") if case_md_path.exists() else None
    actions = [
        ("case.md", case_md_path, render_case_md(context, existing_case_text)),
        ("working-brief.md", context.round_root / "working-brief.md", render_working_brief(context)),
        ("dispatch-plan.md", context.round_root / "dispatch-plan.md", render_dispatch_plan(context)),
    ]
    if args.with_design_spec:
        actions.append(("design-spec.md", context.round_root / "design-spec.md", render_design_spec(context)))
    if args.with_implementation_plan:
        actions.append(
            (
                "implementation-plan.md",
                context.round_root / "implementation-plan.md",
                render_implementation_plan(context),
            )
        )
    return actions


def emit_output(ok: bool, message: str, actions: list[dict], as_json: bool) -> int:
    if as_json:
        print(json.dumps({"ok": ok, "message": message, "actions": actions}, indent=2))
    else:
        print(message)
        for action in actions:
            print(f"- {action['status']}: {action['path']}")
    return 0 if ok else 1


def main() -> int:
    args = parse_args()
    context = build_context(args)
    actions = plan_actions(context, args)

    if args.dry_run:
        return emit_output(
            True,
            "Dry run: the following scaffold actions would be performed.",
            [{"status": "would-write", "path": relative_markdown_path(path)} for _, path, _ in actions],
            args.as_json,
        )

    for _, path, _ in actions:
        if path.exists() and not args.overwrite and path.name != "case.md":
            return emit_output(
                False,
                f"Refusing to overwrite existing round file without --overwrite: {relative_markdown_path(path)}",
                [{"status": "blocked", "path": relative_markdown_path(path)}],
                args.as_json,
            )

    written_actions: list[dict] = []
    for _, path, content in actions:
        existed = path.exists()
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.name == "case.md":
            path.write_text(content, encoding="utf-8")
            status = "updated" if existed else "created"
        else:
            if existed and not args.overwrite:
                return emit_output(
                    False,
                    f"Refusing to overwrite existing round file without --overwrite: {relative_markdown_path(path)}",
                    [{"status": "blocked", "path": relative_markdown_path(path)}],
                    args.as_json,
                )
            path.write_text(content, encoding="utf-8")
            status = "updated" if existed else "created"
        written_actions.append({"status": status, "path": relative_markdown_path(path)})

    return emit_output(True, "WW case artifact scaffold created.", written_actions, args.as_json)


if __name__ == "__main__":
    raise SystemExit(main())
