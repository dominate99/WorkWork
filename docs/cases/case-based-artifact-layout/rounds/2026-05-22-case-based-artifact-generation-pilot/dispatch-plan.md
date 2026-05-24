# Dispatch Plan: Case-Based Artifact Generation Pilot

- Date: 2026-05-22
- Schema Version: 1
- Plan Revision: 2
- Working Brief Version: 2
- Case Slug: case-based-artifact-layout
- Round Slug: 2026-05-22-case-based-artifact-generation-pilot
- Case Root: `docs/cases/case-based-artifact-layout/`
- Round Root: `docs/cases/case-based-artifact-layout/rounds/2026-05-22-case-based-artifact-generation-pilot/`
- Plan State: completed
- Last Approved Revision: 2
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

Path identity rules:

- `Case Root` must resolve to `docs/cases/<case_slug>/`
- `Round Root` must resolve to `docs/cases/<case_slug>/rounds/<round_slug>/`
- new dispatch-round artifacts are canonically written under `Round Root`
- legacy type-based paths are legacy history only; they are not canonical targets or ongoing generation defaults

## Source Context

- User Request: `case-based artifact generation pilot`
- Working Brief Reference: `docs/cases/case-based-artifact-layout/rounds/2026-05-22-case-based-artifact-generation-pilot/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: adopt case-based artifact generation for new `$ww` and `$www` rounds so required artifacts are generated under `round_root` by default and pre-cutover type-based paths are treated as legacy history only
- Relevant Context: the contract, README, and validators now use case-based path identity; this round completes the cutover by making actual new-round generation follow the simpler `docs/cases/...` root consistently
- Constraints:
  - do not widen into repo-wide historical migration
  - keep required round artifacts minimal
  - avoid optional explanatory artifacts becoming mandatory control surfaces
  - only add a bounded case-level entrypoint if it materially improves case navigation without creating a new gate
  - prefer explicit legacy classification or a dedicated legacy surface over open-ended path compatibility rules
  - historical pre-cutover artifacts remain out of scope for bulk movement in this pilot
- Risks:
  - partial adoption could leave operators manually creating new files in old type-based directories
  - a soft compatibility story could recreate split write authority by implication even without formal dual-write
  - over-designing the case folder could add weight without improving execution clarity
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Case-Based Artifact Generation Adoption

- Section ID: section-case-based-artifact-generation-adoption
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff-engineer-orchestrator
- Planned Reviewer Persona: pm-orchestrator
- Planned Specialist Personas: none
- Planned Scope:
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `README.md`
  - `docs/cases/case-based-artifact-layout/case.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: canonical path identity is already defined and validated; the next bounded move is to make actual new-round artifact generation behavior follow a simpler case-based root while sharply separating historical legacy artifacts from current generation behavior
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: this round should first validate which surfaces still control new-round artifact creation, then implement the narrowest changes that make generation behavior and migration posture align
- Goal Tuning: validation-biased
- Constraint Interaction Rule: change the active generation root and hard legacy classification rules only; do not broaden into legacy bulk movement or new mandatory artifact classes
- Planned Review Lanes:
  - Lane ID: lane-case-based-artifact-generation-adoption-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-22-case-based-artifact-generation-pilot/working-brief.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-22-case-based-artifact-generation-pilot/dispatch-plan.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `README.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/case.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/case-based-artifact-layout/**/*`
    - `path_glob`: `docs/legacy/superpowers/specs/2026-05-22-case-based-artifact-layout-design.md`
    - `path_glob`: `docs/legacy/superpowers/plans/2026-05-22-case-based-artifact-layout.md`
    - `path_glob`: `tools/validate_ww_case_path_identity.py`
    - `path_glob`: `tools/validate_ww_repo.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `ww_skill_contract`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `section_anchors`: `Working Brief`, `Dispatch Plan File`, `Document Summary Contract`
    - `artifact_id`: `working_brief_template`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `section_anchors`: `Artifact Metadata`, `Rules`
    - `artifact_id`: `dispatch_plan_template`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `section_anchors`: `Path identity rules`, `Preconditions`
    - `artifact_id`: `case_layout_design`
    - `artifact_kind`: `doc`
    - `artifact_path`: `docs/legacy/superpowers/specs/2026-05-22-case-based-artifact-layout-design.md`
    - `section_anchors`: `Target Model`, `Migration Strategy`
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Case-Based Artifact Generation Adoption

- Section ID: section-case-based-artifact-generation-adoption
- Runtime State: complete
- Active Execution ID: execution-case-based-artifact-generation-adoption
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode: validate-first
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
  - Execution ID: execution-case-based-artifact-generation-adoption
  - Role: orchestrator-implementation
  - Status: DONE
  - Owned Scope: `SKILL.md`, `working-brief-template.md`, `dispatch-plan-template.md`, `README.md`, `tools/validate_ww_case_path_identity.py`, case-based round artifacts
  - Started At: 2026-05-22 America/Los_Angeles
  - Finished At: 2026-05-22 America/Los_Angeles
- Packet Records:
- Attempt Records:
  - Attempt ID: attempt-case-based-artifact-generation-adoption-1
  - Packet ID:
  - Agent ID:
  - Return Status: DONE
  - Runtime State After Return: complete
  - Launched At: 2026-05-22 America/Los_Angeles
  - Closed At: 2026-05-22 America/Los_Angeles
  - Result Summary: switched new-round artifact generation to `docs/cases/...`, created a `case.md` entrypoint, and aligned the case-path validator with the new root
  - Result Artifact Location: `docs/cases/case-based-artifact-layout/`, `plugins/workwork/skills/ww-subagent-orchestrator/*`, `README.md`, `tools/validate_ww_case_path_identity.py`
- Attempt Count: 1
- Last Update At: 2026-05-22 America/Los_Angeles
- Next Action: none
- Active Write Scope:
- Result Summary:
- Canonical Result Artifact Location:
- Concerns:
  - historical type-based artifacts still exist and should be handled in a separate legacy-archival round if desired
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Case-Based Artifact Generation Adoption

- Section ID: section-case-based-artifact-generation-adoption
- Review Target Strategy:
  - validate that new round artifact generation is explicitly case-based by default, with `docs/cases/...` as the canonical root
  - validate that legacy type-based paths are treated as legacy history only
  - validate that optional explanatory artifacts remain optional
  - validate that any `case.md` addition is informational rather than a control gate
- Review Lane Records:
  - Lane ID: lane-case-based-artifact-generation-adoption-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
  - Reviewer Findings: no material findings
  - Orchestrator Synthesis: the root cutover is now explicit in contract, docs, validator, and the pilot round itself; `case.md` improves navigation without becoming a gate
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

- Blocking work first: `section-case-based-artifact-generation-adoption`
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
- Notes: this pilot is scoped to new-round artifact generation and hard legacy classification posture only
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 2 Created From Brief Version: 2
- Revision Reason: cut over the canonical root from `docs/superpowers/cases/...` to `docs/cases/...` and persist this round under the new active path
- Supersedes Revision: 1

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - prior case-based layout design and path-identity validator rounds reviewed
  - generation adoption identified as the next bounded migration step
  - working brief persisted
  - dispatch plan drafted
  - canonical root cut over to `docs/cases/...`
  - `case.md` entrypoint created
  - validator updated to enforce the new root
  - verification completed
- Launch Time: 2026-05-22 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
