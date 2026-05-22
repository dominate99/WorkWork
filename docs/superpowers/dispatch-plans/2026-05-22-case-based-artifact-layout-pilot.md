# Dispatch Plan: Case-Based Artifact Layout Pilot

- Date: 2026-05-22
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Plan State: completed
- Last Approved Revision: 1
- Rollback Baseline Revision: none
- Task Routing: code/programming
- Main Orchestrator: staff-engineer-orchestrator

## Strict Review Runtime State

```yaml
strict_review:
  mode: standard
  target: none
  state: idle
  cycle_count: 0
```

## Preconditions

- Estimation Complete: true
- Working Brief Status: ready

> Do not launch any real subagent until the preconditions are satisfied and `Plan State: approved`.

## Source Context

- User Request: `新的 $ww round 做： case-based artifact layout pilot`
- Working Brief Reference: `docs/superpowers/working-briefs/2026-05-22-case-based-artifact-layout-pilot-v1.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: define a case-based artifact storage model, the default per-round file landing points, and the migration or compatibility posture from the current type-based layout
- Relevant Context: current packaged contract and maintainer guidance still point at type-based directories, but the user wants one case folder to contain the files that belong to that case or round
- Constraints:
  - produce design and planning artifacts first
  - do not widen this round into repo-wide storage migration or validator changes unless the design proves a minimal prerequisite
  - keep optional log-like artifacts separate from required runtime-state artifacts
- Risks:
  - a dual-layout transition could create confusing split authority
  - a case folder without a clean round model could become an unstructured bucket
  - path changes could ripple into `SKILL.md`, README, validators, and future generated artifacts
  - if canonical write authority is not explicitly defined per migration phase, generators and validators will drift apart
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Case-Based Artifact Layout Design

- Section ID: section-case-layout-design
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff-engineer-orchestrator
- Planned Reviewer Persona: staff-engineer-orchestrator
- Planned Specialist Personas: pm-orchestrator
- Planned Scope:
  - `docs/superpowers/specs/2026-05-22-case-based-artifact-layout-design.md`
  - `docs/superpowers/plans/2026-05-22-case-based-artifact-layout.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the highest-leverage next step is to define the case and round storage model before changing the live workflow contract
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: plan-first
- Worker Mode Rationale: the storage model needs a coherent target architecture before migration and compatibility tactics are designed
- Goal Tuning: safety-biased
- Constraint Interaction Rule: prioritize a clear model and migration story over immediate path rewrites
- Planned Review Lanes:
  - Lane ID: lane-case-layout-design-review
  - Lane Type: scope-review
  - Reviewer Persona: staff-engineer-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/superpowers/working-briefs/2026-05-22-case-based-artifact-layout-pilot-v1.md`
    - `path_glob`: `docs/superpowers/dispatch-plans/2026-05-22-case-based-artifact-layout-pilot.md`
    - `path_glob`: `docs/superpowers/specs/2026-05-22-case-based-artifact-layout-design.md`
    - `path_glob`: `docs/superpowers/plans/2026-05-22-case-based-artifact-layout.md`
  - `shared_read_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `README.md`
    - `path_glob`: `docs/superpowers/**/*`
    - `path_glob`: `tools/*.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `ww_skill_contract`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `section_anchors`: `Working Brief`, `Dispatch Plan File`, `Document Summary Contract`
    - `artifact_id`: `readme_guidance`
    - `artifact_kind`: `doc`
    - `artifact_path`: `README.md`
    - `section_anchors`: `How It Works`, `Output Locations`, `For Maintainers`
    - `artifact_id`: `current_superpowers_layout`
    - `artifact_kind`: `dir`
    - `artifact_path`: `docs/superpowers/`
    - `section_anchors`: none
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Case-Based Artifact Layout Design

- Section ID: section-case-layout-design
- Runtime State: complete
- Active Execution ID: execution-case-layout-design
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode: plan-first
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
  - Execution ID: execution-case-layout-design
  - Role: orchestrator-design
  - Status: DONE
  - Owned Scope: `case-based-artifact-layout-design.md`, `case-based-artifact-layout.md`, round documents
  - Started At: 2026-05-22 America/Los_Angeles
  - Finished At: 2026-05-22 America/Los_Angeles
- Packet Records:
  - Packet ID:
  - Execution ID:
  - Stage:
  - Template Path:
  - Review Target Ref:
  - Supersedes Attempt ID:
  - Accepts Late Results:
- Attempt Records:
  - Attempt ID: attempt-case-layout-design-1
  - Packet ID:
  - Agent ID:
  - Return Status: DONE
  - Runtime State After Return: complete
  - Launched At: 2026-05-22 America/Los_Angeles
  - Closed At: 2026-05-22 America/Los_Angeles
  - Result Summary: produced a case-based artifact layout design and staged implementation plan centered on case-first, round-second storage with single-authority migration
  - Result Artifact Location: `docs/superpowers/specs/2026-05-22-case-based-artifact-layout-design.md`, `docs/superpowers/plans/2026-05-22-case-based-artifact-layout.md`
- Attempt Count: 1
- Last Update At: 2026-05-22 America/Los_Angeles
- Next Action: none
- Active Write Scope:
- Result Summary: produced the target case/round storage model plus migration and compatibility plan without changing live workflow path rules
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
  - migration may be underspecified if the design focuses only on the target layout
  - round folders could become too dense if required and optional artifacts are not clearly separated
  - authority could remain ambiguous if the design does not define one canonical path source per artifact class and migration phase
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Case-Based Artifact Layout Design

- Section ID: section-case-layout-design
- Review Target Strategy:
  - validate that the case and round model is clearer than the current type-based split
  - validate that default landing points cover required artifacts and optional log-like artifacts without making the workflow heavier
  - validate that migration and compatibility are explicit enough to avoid split authority
  - validate that the design defines one canonical write path model at every migration phase instead of leaving producer and validator behavior implicit
- Review Lane Records:
  - Lane ID: lane-case-layout-design-review
  - Lane Type: scope-review
  - Reviewer Persona: staff-engineer-orchestrator
  - Execution ID: execution-case-layout-design
  - Packet ID:
  - Attempt ID: attempt-case-layout-design-1
  - Review Target Ref:
    - Artifact Path: `docs/superpowers/specs/2026-05-22-case-based-artifact-layout-design.md`
    - Artifact Kind: doc
    - Artifact Revision: working-tree
    - Schema Version:
    - Section Anchor:
    - Content Hash:
  - Reviewer Findings: no material findings
  - Orchestrator Synthesis: the design now defines a case-first, round-second storage model, keeps optional explanatory artifacts optional, and requires one canonical write-path model at every migration phase
  - Strict Review Outcome: none
  - Persistence rule: pre-approval plans must preserve this review-lane structure and outcome field pattern; `Review Status` must not reappear here, and durable review-lane data must retain `Reviewer Findings`, `Orchestrator Synthesis`, and the `Strict Review Outcome` field pattern.
  - Applicability rule: `Strict Review Outcome` is required when a strict-review target or durable strict-review result applies; otherwise keep the same field pattern without creating a second schema for valid non-strict lanes.
  - Invalid state note: `Review Status` reappears or durable strict-review outcome data is dropped when applicable.

- Human Decision: Approve
- Revision Notes:
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: `section-case-layout-design`
- Parallel sections: none
- Review loop per section: draft -> reviewer findings -> orchestrator synthesis -> human judgment

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
- Current Choice: Approve
- Approved By: user
- Approval Time: 2026-05-22 America/Los_Angeles
- Notes: this pilot round is scoped to case-based artifact layout design and migration planning only
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial pilot round for case-based artifact layout design
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - case-based layout request analyzed against the current type-based storage contract
  - review stance tightened around authority, compatibility, and migration safety
  - working brief persisted
  - dispatch plan drafted
  - design spec completed
  - implementation plan completed
  - scope review completed with no material findings
  - human approval received
- Launch Time: 2026-05-22 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
