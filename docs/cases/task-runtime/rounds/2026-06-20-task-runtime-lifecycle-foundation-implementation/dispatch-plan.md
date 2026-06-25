# Dispatch Plan: Task Runtime Lifecycle Foundation Implementation

- Date: 2026-06-20
- Schema Version: 1
- Plan Revision: 2
- Working Brief Version: 2
- Case Slug: task-runtime
- Round Slug: 2026-06-20-task-runtime-lifecycle-foundation-implementation
- Case Root: `docs/cases/task-runtime/`
- Round Root: `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/`
- Plan State: completed
- Last Approved Revision: 2
- Rollback Baseline Revision: 1
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

- User Request: `下一轮：Lifecycle foundation implementation。`
- Working Brief Reference: `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/working-brief.md`
- Approved Design Reference: `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/design-spec.md`, revision 11
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: implement dormant lifecycle foundation support across the active contract, templates, packet contract, scaffold, tests, and minimal README guidance
- Relevant Context: the approved design fixes lifecycle ownership and transition semantics but requires a coordinated schema bump and compatibility discriminator before later runtime capabilities can build on it
- Constraints:
  - assign schema version 2 as the coordinated current write schema
  - default all new ordinary rounds to `lifecycle_protocol: legacy`
  - do not persist lifecycle snapshots or events for legacy rounds
  - do not activate `task-runtime-v1`
  - do not add verifier roles, hooks, quality scoring, repair policy, routing, personas, or a dedicated lifecycle validator
  - do not rewrite historical artifacts
  - preserve `runtime_state` authority
- Risks:
  - silent activation through scaffold or template defaults
  - mixed schema surfaces
  - lifecycle fields leaking into legacy sections
  - contract drift from approved design revision 11
  - regression tests that do not prove generated defaults
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Lifecycle Foundation Implementation

- Section ID: section-lifecycle-foundation-implementation
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: senior-backend-engineer
- Planned Reviewer Persona: spec-reviewer and code-quality-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: independent contract fidelity and Python regression quality are both required, and no eligible project reviewer covers either lane more strongly
- Planned Specialist Personas:
  - Persona ID: senior-backend-engineer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: the implementation coordinates a Python scaffold with packaged schema and controller contracts; no eligible project worker covers this combination
- Planned Scope:
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `tools/scaffold_ww_case_artifacts.py`
  - `tools/validate_ww_repo.py`
  - `tools/test_scaffold_ww_case_artifacts.py`
  - `README.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: implement one coherent dormant foundation from the approved design while keeping runtime activation and later capability layers separate
- Planned Workflow Bindings:
  - `superpowers:test-driven-development`
  - `superpowers:systematic-debugging`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: test-first
- Worker Mode Rationale: add failing scaffold assertions for schema version 2 and default `legacy` protocol before changing generated output or contract text
- Goal Tuning: compatibility-first and activation-averse
- Constraint Interaction Rule: when a requirement depends on verifier, hook, score, repair, dedicated validation, routing, or persona behavior, document the later-owner boundary instead of implementing it
- Planned Review Lanes:
  - Lane ID: lane-lifecycle-foundation-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: compare every contract and template change with approved design revision 11, especially ownership, dormant activation, schema coordination, migration, and exclusions; built-in fallback is used because no stronger eligible project reviewer covers lifecycle contract fidelity
  - Required: true
  - Lane ID: lane-lifecycle-foundation-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: inspect scaffold defaults, tests, backwards compatibility, and absence of accidental runtime activation; built-in fallback is used because no stronger eligible project reviewer covers Python scaffold quality
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/task-runtime/case.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/working-brief.md`
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/dispatch-plan.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
    - `path_glob`: `tools/scaffold_ww_case_artifacts.py`
    - `path_glob`: `tools/validate_ww_repo.py`
    - `path_glob`: `tools/test_scaffold_ww_case_artifacts.py`
    - `path_glob`: `README.md`
  - `shared_read_scope`:
    - `path_glob`: `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/**/*`
    - `path_glob`: `docs/superpowers/specs/2026-06-19-workwork-task-runtime-design.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
    - `path_glob`: `tools/validate_ww_*.py`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: lifecycle_foundation_contract
      - `artifact_kind`: packaged_skill_contract
      - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
      - `section_anchors`: lifecycle protocol and reference
    - `artifact_id`: lifecycle_foundation_reference
      - `artifact_kind`: normative_reference
      - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
      - `section_anchors`: lifecycle ownership, protocol, transitions, persistence, migration
    - `artifact_id`: lifecycle_foundation_scaffold
      - `artifact_kind`: python_tool
      - `artifact_path`: `tools/scaffold_ww_case_artifacts.py`
      - `section_anchors`: schema and lifecycle protocol generation
- Scope declaration rule: every writable file in `Planned Scope` also appears in `exclusive_write_scope`; round-local controller files are included separately and shared reads remain read-only.
- Packet Created: true

## Section Runtime Ledger

### Section: Lifecycle Foundation Implementation

- Section ID: section-lifecycle-foundation-implementation
- Runtime State: complete
- Active Execution ID:
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode: test-first
- Active Persona IDs: senior-backend-engineer, spec-reviewer, code-quality-reviewer
- Active Persona Sources: senior-backend-engineer=built-in, spec-reviewer=built-in, code-quality-reviewer=built-in
- Active Persona Role Bindings: senior-backend-engineer=worker via `agents/worker-prompt.md`; spec-reviewer=reviewer via `agents/reviewer-prompt.md`; code-quality-reviewer=reviewer via `agents/reviewer-prompt.md`
- Mode Change History:
- Execution Records:
  - Execution ID: execution-lifecycle-foundation-implementation
  - Role: senior-backend-engineer
  - Status: complete
  - Owned Scope: active lifecycle contract, templates, scaffold helper, tests, and README guidance
  - Started At: 2026-06-20
  - Finished At: 2026-06-20
- Packet Records:
  - Packet ID: packet-lifecycle-foundation-code-review-02
  - Execution ID: exec-lifecycle-foundation-code-review-01
  - Stage: review
  - Template Path: agents/reviewer-prompt.md
  - Review Target Ref: sha256:e7f7f5e4f0cb453d520a8790cf9b2bf15489516876ca16d7e975e874dd8f2896
  - Supersedes Attempt ID: attempt-lifecycle-foundation-code-review-01
  - Accepts Late Results: false
  - Packet ID: packet-lifecycle-foundation-spec-review-03
  - Execution ID: exec-lifecycle-foundation-spec-review-01
  - Stage: review
  - Template Path: agents/reviewer-prompt.md
  - Review Target Ref: sha256:c057e90355e92a71f0f4d82d85e936b784c4bcfd964d8a5fde6d18a2b8d2851d
  - Supersedes Attempt ID: attempt-lifecycle-foundation-spec-review-02
  - Accepts Late Results: false
  - Packet ID: packet-lifecycle-foundation-spec-review-r2b
  - Execution ID: exec-lifecycle-foundation-spec-review-r2
  - Stage: review
  - Template Path: agents/reviewer-prompt.md
  - Review Target Ref: sha256:0a89c9565099148e316db25196c9d960cc67c416fd67adb33c98bd3584d7310b
  - Supersedes Attempt ID: attempt-lifecycle-foundation-spec-review-r2
  - Accepts Late Results: false
  - Packet ID: packet-lifecycle-foundation-code-review-r2b
  - Execution ID: exec-lifecycle-foundation-code-review-r2
  - Stage: review
  - Template Path: agents/reviewer-prompt.md
  - Review Target Ref: sha256:70004a3b09698b2546e78deccc282c4c84be1d30a0f58e02d84f2bbfca4ec42e
  - Supersedes Attempt ID: attempt-lifecycle-foundation-code-review-r2
  - Accepts Late Results: false
  - Packet ID: packet-lifecycle-foundation-code-review-r2c
  - Execution ID: exec-lifecycle-foundation-code-review-r2
  - Stage: review
  - Template Path: agents/reviewer-prompt.md
  - Review Target Ref: sha256:6d3b85eca327a216dad7cba79138ff3622817e9b635ccf9a673b1a49de3636b9
  - Supersedes Attempt ID: attempt-lifecycle-foundation-code-review-r2b
  - Accepts Late Results: false
  - Packet ID: packet-lifecycle-foundation-code-review-r2d
  - Execution ID: exec-lifecycle-foundation-code-review-r2
  - Stage: review
  - Template Path: agents/reviewer-prompt.md
  - Review Target Ref: sha256:bff5847ddc7e1171d41baf7820c01e30e45a9c34b2a278a0aee8ba36d424a0d0
  - Supersedes Attempt ID: attempt-lifecycle-foundation-code-review-r2c
  - Accepts Late Results: false
  - Packet ID: packet-lifecycle-foundation-code-review-r2e
  - Execution ID: exec-lifecycle-foundation-code-review-r2
  - Stage: review
  - Template Path: agents/reviewer-prompt.md
  - Review Target Ref: sha256:bff5847ddc7e1171d41baf7820c01e30e45a9c34b2a278a0aee8ba36d424a0d0
  - Supersedes Attempt ID: attempt-lifecycle-foundation-code-review-r2d
  - Accepts Late Results: false
- Attempt Records:
  - Attempt ID: attempt-lifecycle-foundation-spec-review-01
  - Packet ID: packet-lifecycle-foundation-spec-review-01
  - Agent ID: 019ee3ec-c64c-7fd3-a853-ec27705c1847
  - Return Status: FAILED
  - Runtime State After Return: review-pending
  - Result Summary: reviewer initialization failed because the subagent usage limit was reached; no review conclusion was accepted
  - Attempt ID: attempt-lifecycle-foundation-code-review-01
  - Packet ID: packet-lifecycle-foundation-code-review-01
  - Agent ID: 019ee3ec-b25b-7353-80e8-2a23bd70f52e
  - Return Status: FAILED
  - Runtime State After Return: review-pending
  - Result Summary: reviewer initialization failed because the subagent usage limit was reached; no review conclusion was accepted
  - Attempt ID: attempt-lifecycle-foundation-code-review-02
  - Packet ID: packet-lifecycle-foundation-code-review-02
  - Agent ID: 019ee405-1877-7a70-a8e0-9c55acdf816e
  - Return Status: DONE
  - Runtime State After Return: review-pending
  - Result Summary: no material findings
  - Attempt ID: attempt-lifecycle-foundation-spec-review-02
  - Packet ID: packet-lifecycle-foundation-spec-review-02
  - Agent ID: 019ee405-2c66-7de3-93d7-b759092b2b84
  - Return Status: DONE_WITH_CONCERNS
  - Runtime State After Return: review-pending
  - Result Summary: one high and two medium migration/recovery contract omissions
  - Attempt ID: attempt-lifecycle-foundation-spec-review-03
  - Packet ID: packet-lifecycle-foundation-spec-review-03
  - Agent ID: 019ee408-06d4-7df0-a7b7-bb0ab2afc2f3
  - Return Status: DONE
  - Runtime State After Return: review-pending
  - Result Summary: no material findings after the three contract omissions were corrected
  - Attempt ID: attempt-lifecycle-foundation-spec-review-r2
  - Packet ID: packet-lifecycle-foundation-spec-review-r2
  - Agent ID: 019ee41c-5b9f-7d30-92cd-47686b63d822
  - Return Status: DONE_WITH_CONCERNS
  - Runtime State After Return: review-pending
  - Result Summary: one P1 finding for omitted mandatory canonical transition conditions
  - Attempt ID: attempt-lifecycle-foundation-code-review-r2
  - Packet ID: packet-lifecycle-foundation-code-review-r2
  - Agent ID: 019ee41c-6fa9-79d0-bb0a-1a81425f87ae
  - Return Status: DONE_WITH_CONCERNS
  - Runtime State After Return: review-pending
  - Result Summary: one P1 finding for stale revision-2 controller state after reviewer launch
  - Attempt ID: attempt-lifecycle-foundation-spec-review-r2b
  - Packet ID: packet-lifecycle-foundation-spec-review-r2b
  - Agent ID: 019eed6d-53db-77a3-9714-b2c3e26e23bd
  - Return Status: DONE
  - Runtime State After Return: review-pending
  - Result Summary: no material findings after mandatory transition conditions were restored
  - Attempt ID: attempt-lifecycle-foundation-code-review-r2b
  - Packet ID: packet-lifecycle-foundation-code-review-r2b
  - Agent ID: 019eed6f-fc60-71b0-84f2-dde1f7081055
  - Return Status: DONE_WITH_CONCERNS
  - Runtime State After Return: review-pending
  - Result Summary: one P1 controller-history finding and one P2 invalid-child-JSON aggregation finding
  - Attempt ID: attempt-lifecycle-foundation-code-review-r2c
  - Packet ID: packet-lifecycle-foundation-code-review-r2c
  - Agent ID: 019eed74-9a64-7e51-a348-79037dea0197
  - Return Status: DONE_WITH_CONCERNS
  - Runtime State After Return: review-pending
  - Result Summary: one P1 finding for empty or explicit-negative child JSON still producing aggregate success
  - Attempt ID: attempt-lifecycle-foundation-code-review-r2d
  - Packet ID: packet-lifecycle-foundation-code-review-r2d
  - Agent ID: 019eed78-0c8a-7d82-b4b3-885758d2c8c8
  - Return Status: DONE_WITH_CONCERNS
  - Runtime State After Return: review-pending
  - Result Summary: one P1 finding that active r2d packet and attempt records were absent during execution
  - Attempt ID: attempt-lifecycle-foundation-code-review-r2e
  - Packet ID: packet-lifecycle-foundation-code-review-r2e
  - Agent ID: 019eed7a-7360-7d12-8e67-936960066f2c
  - Return Status: DONE
  - Runtime State After Return: review-pending
  - Launched At: 2026-06-21
  - Closed At: 2026-06-21
  - Result Summary: no material findings
- Attempt Count: 12
- Last Update At: 2026-06-21
- Next Action: none
- Active Write Scope: planned scope only
- Result Summary: revision 2 addresses legacy protocol normalization, activation prerequisites, CI execution and JSON aggregation of scaffold regression tests, mandatory transition conditions, and durable controller identity/history; both required reviewer lanes returned no material findings on final targets
- Canonical Result Artifact Location: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
- Concerns:
  - preserve dormant `legacy` default
  - keep later runtime capabilities out of this implementation
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs: attempt-lifecycle-foundation-spec-review-01, attempt-lifecycle-foundation-spec-review-02, attempt-lifecycle-foundation-code-review-01, attempt-lifecycle-foundation-spec-review-r2, attempt-lifecycle-foundation-code-review-r2, attempt-lifecycle-foundation-code-review-r2b, attempt-lifecycle-foundation-code-review-r2c, attempt-lifecycle-foundation-code-review-r2d
- Stale Result Policy: only the active attempt may advance canonical runtime state
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless promoted to active

## Section Review Record

### Section: Lifecycle Foundation Implementation

- Section ID: section-lifecycle-foundation-implementation
- Review Target Strategy:
  - Freeze the implementation diff after focused and repo-wide verification, then create independent immutable reviewer targets for contract fidelity and code quality.
- Review Lane Records:
  - Lane ID: lane-lifecycle-foundation-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: approved design fidelity is an independent gate from implementation quality
  - Execution ID: exec-lifecycle-foundation-spec-review-01
  - Packet ID: packet-lifecycle-foundation-spec-review-r2b
  - Attempt ID: attempt-lifecycle-foundation-spec-review-r2b
  - Review Target Ref:
    - Artifact Path: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
    - Artifact Kind: normative_reference
    - Artifact Revision: sha256:0a89c9565099148e316db25196c9d960cc67c416fd67adb33c98bd3584d7310b
    - Schema Version: 2
    - Section Anchor: full-file revision 2 lifecycle contract
    - Content Hash: sha256:0a89c9565099148e316db25196c9d960cc67c416fd67adb33c98bd3584d7310b
  - Reviewer Findings: revision 2 initially found one P1 for omitted mandatory transition conditions; after restoration, fresh revision 2b review returned no material findings
  - Orchestrator Synthesis: schema-0/1 legacy normalization, implemented-and-verified activation gating, exact mandatory transition conditions, migration, recovery, and authority boundaries now match approved design revision 11
  - Strict Review Outcome: none
  - Lane ID: lane-lifecycle-foundation-code-quality-review
  - Lane Type: code-quality-review
  - Reviewer Persona: code-quality-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: Python scaffold behavior and regression evidence require a separate implementation-quality review
  - Execution ID: exec-lifecycle-foundation-code-review-r2
  - Packet ID: packet-lifecycle-foundation-code-review-r2e
  - Attempt ID: attempt-lifecycle-foundation-code-review-r2e
  - Review Target Ref:
    - Artifact Path: `tools/validate_ww_repo.py`
    - Artifact Kind: python_tool
    - Artifact Revision: sha256:bff5847ddc7e1171d41baf7820c01e30e45a9c34b2a278a0aee8ba36d424a0d0
    - Schema Version: 2
    - Section Anchor: full-file revision 2 repo validation entrypoint
    - Content Hash: sha256:bff5847ddc7e1171d41baf7820c01e30e45a9c34b2a278a0aee8ba36d424a0d0
  - Reviewer Findings: iterative review found stale controller state, incomplete active-attempt history, and incomplete JSON child failure semantics; after fixes and pre-launch durable r2e records, fresh revision 2e review returned no material findings
  - Orchestrator Synthesis: repo validation now executes scaffold regressions in normal and JSON modes, rejects malformed, empty, non-object, and explicit-negative JSON child results, and keeps active and historical controller identities durable
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes: revision 2 resolved all pre-commit and reviewer findings; final spec revision 2b and code-quality revision 2e returned no material findings, and the user approved closure on 2026-06-21
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level plan state follows required-section aggregation

## Ordering And Parallelism

- Blocking work first: section-lifecycle-foundation-implementation
- Parallel sections: none
- Review loop: implementation -> verification -> spec review -> code-quality review -> orchestrator synthesis -> human judgment

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
- Approval Time: 2026-06-20
- Notes: revision 2 approved for regenerated immutable reviewer packets and required re-review
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial lifecycle foundation implementation round
- Supersedes Revision:
- Revision 2 Created From Brief Version: 2
- Revision Reason: address pre-commit findings in legacy normalization, activation safety, CI test integration, and completed controller state
- Supersedes Revision: 1

## Dispatch Log

- Agents Launched:
- Retry Events:
- Close Events:
  - 2026-06-20: final human approval accepted; section runtime state moved to complete and round plan state moved to completed
  - 2026-06-20: pre-commit revision 2 reopened the completed section, invalidated changed reviewer targets, and returned close state to open
  - 2026-06-21: final human approval accepted revision 2; section runtime state moved to complete and round plan state moved to completed
- Review Lane Transitions:
- 2026-06-20: initial reviewer launches failed before review because of temporary subagent usage limits
- 2026-06-20: code-quality revision 2 returned no material findings
- 2026-06-20: spec revision 2 returned one high and two medium findings
- 2026-06-20: the three spec findings were corrected and fresh spec revision 3 returned no material findings
- 2026-06-20: revision 2 approval launched regenerated spec and code-quality reviewer packets; plan moved to dispatched and section moved to review-pending
- 2026-06-21: spec revision 2b returned no material findings after mandatory transition conditions were restored
- 2026-06-21: code-quality revisions iterated on controller history and JSON child semantics; revision 2e returned no material findings
- Launch Time: 2026-06-20
- Revisions Since Approval: 1
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
