# Dispatch Plan: Scaffold Adoption Pilot

- Date: 2026-05-24
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: case-based-artifact-layout
- Round Slug: 2026-05-24-scaffold-adoption-pilot
- Case Root: `docs/cases/case-based-artifact-layout/`
- Round Root: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-scaffold-adoption-pilot/`
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

Path identity rules:

- `Case Root` must resolve to `docs/cases/<case_slug>/`
- `Round Root` must resolve to `docs/cases/<case_slug>/rounds/<round_slug>/`
- new dispatch-round artifacts are canonically written under `Round Root`
- legacy type-based paths are legacy history only; they are not canonical targets or ongoing generation defaults

## Source Context

- User Request: `scaffold adoption pilot`
- Working Brief Reference: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-scaffold-adoption-pilot/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: make the scaffold helper the default initialization path for new `$ww/$www` case rounds
- Relevant Context: the helper and case contract validator already exist; this round is about adoption guidance and default usage, not redesigning the helper
- Constraints:
  - keep scope on active contract and maintainer guidance
  - do not add new packet/runtime behavior
  - do not re-open legacy path policy
- Risks:
  - helper output could be misread as approval-ready if adoption language is sloppy
  - contract and helper behavior could drift if defaults are documented in only one place
  - over-prescriptive wording could force helper use where manual repair is still appropriate
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Scaffold Draft

- Section ID: section-scaffold-adoption
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: staff-engineer-orchestrator
- Planned Reviewer Persona: pm-orchestrator
- Planned Specialist Personas: none
- Planned Scope:
  - `README.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `docs/cases/case-based-artifact-layout/case.md`
  - `docs/cases/case-based-artifact-layout/rounds/2026-05-24-scaffold-adoption-pilot/**/*`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the helper and contract validator are already in place, so the highest-leverage next step is to make scaffold-first startup explicit in the active workflow guidance
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: confirm helper behavior, case contract, and maintainer docs stay aligned before making scaffold-first the default
- Goal Tuning: validation-biased
- Constraint Interaction Rule: adoption wording may tighten defaults, but it must not imply helper output is sufficient for approval by itself
- Planned Review Lanes:
  - Lane ID: lane-scaffold-adoption-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `README.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/case.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-scaffold-adoption-pilot/working-brief.md`
    - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-24-scaffold-adoption-pilot/dispatch-plan.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/**/*`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/case-template.md`
    - `path_glob`: `tools/scaffold_ww_case_artifacts.py`
    - `path_glob`: `tools/validate_ww_case_contracts.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `scaffold_helper`
    - `artifact_kind`: `tool`
    - `artifact_path`: `tools/scaffold_ww_case_artifacts.py`
    - `section_anchors`: `default outputs`, `optional outputs`
    - `artifact_id`: `case_contract_validator`
    - `artifact_kind`: `tool`
    - `artifact_path`: `tools/validate_ww_case_contracts.py`
    - `section_anchors`: `case contract`, `helper conformance`
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: false

## Section Runtime Ledger

### Section: Scaffold Draft

- Section ID: section-scaffold-adoption
- Runtime State: complete
- Active Execution ID: execution-scaffold-adoption-pilot
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
  - Execution ID: execution-scaffold-adoption-pilot
  - Role: orchestrator-implementation
  - Status: DONE
  - Owned Scope: `README.md`, `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`, current round documents
  - Started At: 2026-05-24 America/Los_Angeles
  - Finished At: 2026-05-24 America/Los_Angeles
- Packet Records:
- Attempt Records:
  - Attempt ID: attempt-scaffold-adoption-pilot-1
  - Packet ID:
  - Agent ID:
  - Return Status: DONE
  - Runtime State After Return: complete
  - Launched At: 2026-05-24 America/Los_Angeles
  - Closed At: 2026-05-24 America/Los_Angeles
  - Result Summary: scaffold-first initialization is now the documented default for new case-based rounds while helper output remains explicitly draft-only
  - Result Artifact Location: `README.md`, `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`, `docs/cases/case-based-artifact-layout/rounds/2026-05-24-scaffold-adoption-pilot/`
- Attempt Count: 1
- Last Update At: 2026-05-24
- Next Action: none
- Active Write Scope:
- Result Summary:
- Canonical Result Artifact Location:
- Concerns:
  - validator coverage already proves helper output structure; this round changes only adoption guidance
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Scaffold Draft

- Section ID: section-scaffold-adoption
- Review Target Strategy:
  - verify scaffold-first language is explicit
  - verify helper remains a draft initializer, not an approval substitute
  - verify active contract and maintainer docs describe the same default behavior
- Review Lane Records:
  - Lane ID: lane-scaffold-adoption-review
  - Lane Type: scope-review
  - Reviewer Persona: pm-orchestrator
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
  - Reviewer Findings: no material findings
  - Orchestrator Synthesis: active guidance now points maintainers to scaffold-first startup while preserving the rule that helper output remains a draft initializer only
  - Strict Review Outcome: none
- Human Decision: Approve
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
- Current Choice: Approve
- Approved By: user
- Approval Time: 2026-05-24 America/Los_Angeles
- Notes: scaffold-first adoption approved after contract and maintainer docs were tightened
