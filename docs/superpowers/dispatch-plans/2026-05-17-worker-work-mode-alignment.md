# Dispatch Plan: Worker Work-Mode Alignment

- Date: 2026-05-17
- Schema Version: 1
- Plan Revision: 2
- Working Brief Version: 2
- Plan State: completed
- Last Approved Revision: none
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

- User Request: `$ww 用$ww 开始修改并且review`
- Working Brief Reference: `docs/superpowers/working-briefs/2026-05-17-worker-work-mode-alignment-v2.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: align the worker work-mode contract across the packaged skill contract, working brief template, dispatch plan template, packet contract, and worker prompt
- Relevant Context: the packaged skill already carries worker `implementation_principles`; this round adds the next execution-order layer and aligns all five runtime surfaces around one authority chain
- Constraints: keep `task_mode` separate from `work_mode`, stay bounded to worker behavior, and avoid duplicate authority across skill contract, brief, plan, packet, and prompt
- Risks:
  - field-name drift could make the propagation chain inconsistent
  - if `SKILL.md` is not updated, the packaged workflow contract will drift away from runtime behavior
  - authority drift could let the worker re-derive behavior outside the packet
  - prompt-order drift could collapse the model back into persona-only execution
  - overly strong goal tuning could silently replace the structure-driven mode
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Worker Work-Mode Contract Alignment

- Section ID: section-worker-mode-contract-alignment
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: senior-backend-engineer
- Planned Reviewer Persona: secure-software-engineer
- Planned Specialist Personas: senior-backend-engineer
- Planned Scope:
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: the round changes one shared execution model across five coupled files, so one bounded worker lane is clearer and safer than parallel editing
- Planned Workflow Bindings:
  - `superpowers:writing-skills`
  - `superpowers:test-driven-development`
  - `superpowers:subagent-driven-development`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: validate-first
- Worker Mode Rationale: the worker should confirm the current contract boundaries before changing field names, rule text, and prompt ordering
- Goal Tuning: validation-biased
- Constraint Interaction Rule: keep user-bounded scope and the `task_mode` versus `work_mode` separation ahead of worker-mode posture
- Planned Review Lanes:
  - Lane ID: lane-worker-mode-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: secure-software-engineer
  - Required: true
  - Lane ID: lane-worker-mode-code-review
  - Lane Type: code-quality-review
  - Reviewer Persona: secure-software-engineer
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md`
    - `path_glob`: `docs/superpowers/working-briefs/2026-05-17-worker-work-mode-alignment-v2.md`
    - `path_glob`: `docs/superpowers/dispatch-plans/2026-05-17-worker-work-mode-alignment.md`
  - `shared_read_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
    - `path_glob`: `docs/superpowers/specs/2026-05-15-worker-persona-enforcement-design.md`
    - `path_glob`: `docs/superpowers/specs/2026-05-17-worker-work-mode-alignment-design.md`
    - `path_glob`: `docs/superpowers/plans/2026-05-17-worker-work-mode-alignment.md`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `ww_skill_contract`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `section_anchors`: `Working Brief`, `Subagent Packet Contract`, `Dispatch Plan File`
    - `artifact_id`: `working_brief_template`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `section_anchors`: `Persona And Workflow Guidance`, `Rules`
    - `artifact_id`: `dispatch_plan_template`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `section_anchors`: `Planned Sections`, `Section Runtime Ledger`
    - `artifact_id`: `subagent_packet_contract`
    - `artifact_kind`: `doc`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `section_anchors`: `Required Fields`, `Packet Rules`, `Worker Packet Defaults`, `Worker Packet Example`
    - `artifact_id`: `worker_prompt`
    - `artifact_kind`: `prompt`
    - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md`
    - `section_anchors`: `Responsibilities`, `Operating rules`
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Invalid state note: `Planned Scope` includes a writable file not mirrored in `exclusive_write_scope`.
- Packet Created: false

## Section Runtime Ledger

### Section: Worker Work-Mode Contract Alignment

- Section ID: section-worker-mode-contract-alignment
- Runtime State: complete
- Active Execution ID:
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
  - Execution ID:
  - Role:
  - Status:
  - Owned Scope:
  - Started At:
  - Finished At:
- Packet Records:
  - Packet ID:
  - Execution ID:
  - Stage:
  - Template Path:
  - Review Target Ref:
  - Supersedes Attempt ID:
  - Accepts Late Results:
- Attempt Records:
  - Attempt ID:
  - Packet ID:
  - Agent ID:
  - Return Status:
  - Runtime State After Return:
  - Launched At:
  - Closed At:
  - Result Summary:
  - Result Artifact Location:
- Attempt Count: 0
- Last Update At: 2026-05-17 America/Los_Angeles
- Next Action: none
- Active Write Scope:
- Result Summary: worker work-mode contract alignment completed across the packaged skill contract, brief template, dispatch plan template, packet contract, and worker prompt
- Canonical Result Artifact Location: derived from the latest active attempt record
- Concerns:
- Blocker Reason:
- Close State: open
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Worker Work-Mode Contract Alignment

- Section ID: section-worker-mode-contract-alignment
- Review Target Strategy:
  - validate field-name alignment across all five files
  - validate that `SKILL.md` describes the same worker-mode authority chain as the lower-level contract surfaces
  - validate authority alignment from brief to plan to packet to prompt
  - validate that the worker packet example demonstrates the new worker-mode fields instead of implying them
  - validate that prompt execution order consumes `work_mode` before persona principles
- Review Lane Records:
  - Lane ID: lane-worker-mode-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: secure-software-engineer
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
    - Artifact Path:
    - Artifact Kind:
    - Artifact Revision:
    - Schema Version:
    - Section Anchor:
    - Content Hash:
  - Reviewer Findings:
    - no material findings; the revised plan covers the required skill-contract surface and the implemented contract changes preserve the intended authority chain
  - Orchestrator Synthesis:
    - the spec-review lane confirms the packaged skill contract and lower-level artifacts describe the same worker-mode model
  - Strict Review Outcome: none
  - Persistence rule: pre-approval plans must preserve this review-lane structure and outcome field pattern; `Review Status` must not reappear here, and durable review-lane data must retain `Reviewer Findings`, `Orchestrator Synthesis`, and the `Strict Review Outcome` field pattern.
  - Applicability rule: `Strict Review Outcome` is required when a strict-review target or durable strict-review result applies; otherwise keep the same field pattern without creating a second schema for valid non-strict lanes.
  - Invalid state note: `Review Status` reappears or durable strict-review outcome data is dropped when applicable.
  - Lane ID: lane-worker-mode-code-review
  - Lane Type: code-quality-review
  - Reviewer Persona: secure-software-engineer
  - Execution ID:
  - Packet ID:
  - Attempt ID:
  - Review Target Ref:
    - Artifact Path:
    - Artifact Kind:
    - Artifact Revision:
    - Schema Version:
    - Section Anchor:
    - Content Hash:
  - Reviewer Findings:
    - no material findings; field names, packet example, and worker prompt ordering all align with the approved worker work-mode model
  - Orchestrator Synthesis:
    - the code-quality-review lane confirms the implemented artifact set is bounded and consistent with the approved plan
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

- Blocking work first: `section-worker-mode-contract-alignment`
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
- Approval Time: 2026-05-17 America/Los_Angeles
- Notes: user approved revision 2 after the staff engineer plan review addressed missing skill-contract coverage and strengthened verification gates
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial round for worker work-mode alignment across the packaged skill surfaces
- Supersedes Revision:
- Revision 2 Created From Brief Version: 2
- Revision Reason: staff engineer review found missing `SKILL.md` contract coverage and insufficiently concrete verification gates
- Supersedes Revision: 1

## Dispatch Log

- Agents Launched: none
- Retry Events:
- Close Events:
- Review Lane Transitions:
  - design clarified in chat
  - design spec persisted
  - implementation plan persisted
  - working brief v1 persisted
  - dispatch plan revision 1 drafted
  - user chose `Revise`
  - staff engineer review found missing skill-contract coverage and weak verification detail
  - design spec revised
  - implementation plan revised
  - working brief v2 persisted
  - dispatch plan revision 2 drafted
  - pre-approval self-audit passed for scope parity, strict-review runtime presence, and review-lane durability surfaces
  - user approved revision 2
- worker work-mode contract updates applied across the five planned files
- alignment scans passed for field naming, packet example coverage, and worker prompt ordering
- bounded review found no material findings
- Launch Time: 2026-05-17 America/Los_Angeles
- Revisions Since Approval:
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
