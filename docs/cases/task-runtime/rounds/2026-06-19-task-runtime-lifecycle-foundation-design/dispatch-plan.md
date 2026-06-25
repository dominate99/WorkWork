# Dispatch Plan: Task Runtime Lifecycle Foundation Design

- Date: 2026-06-19
- Schema Version: 1
- Plan Revision: 2
- Working Brief Version: 1
- Case Slug: task-runtime
- Round Slug: 2026-06-19-task-runtime-lifecycle-foundation-design
- Case Root: `docs/cases/task-runtime/`
- Round Root: `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/`
- Plan State: completed
- Last Approved Revision: 2
- Rollback Baseline Revision: 1
- Task Routing: design/ads/product
- Main Orchestrator: pm-orchestrator

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

> Do not launch any real subagent or draft the lifecycle foundation design until `Plan State: approved`.

## Source Context

- User Request: `$ww round: Task runtime lifecycle foundation design.`
- Working Brief Reference: `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/working-brief.md` version 1
- Artifact Registry Reference: inline mappings in the working brief and this plan

## Dispatch Summary

- Goal: produce an implementation-ready lifecycle foundation design for canonical section phases, existing runtime-state compatibility, transitions, authority, events, rollups, migration, and recovery.
- Relevant Context: the approved umbrella design establishes section-owned `lifecycle_phase`, orthogonal `runtime_state`, orchestrator-only transitions, derived round rollups, and current snapshot plus append-only events.
- Constraints: design only; do not edit active contracts, templates, packet contracts, validators, personas, role bindings, hooks, lane mappings, scoring, or quality gates; do not create an implementation plan.
- Risks: dual state authority, invalid phase/state combinations, snapshot/event disagreement, writable round phase, ambiguous migration, or premature design of later rollout layers.
- Reviewer Rule: the design section returns to the orchestrator after narrow spec review and before human judgment.

## Planned Sections

### Section: Lifecycle Foundation Design

- Section ID: LIFECYCLE-DESIGN-001
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: worker
- Planned Reviewer Persona: spec-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: lifecycle state authority, deterministic transitions, compatibility, migration, and testable acceptance criteria make the built-in spec reviewer the strongest eligible reviewer-only match; built-in fallback is used because no stronger project reviewer covers specification contract fidelity.
- Planned Specialist Personas: technical-writer
- Planned Specialist Persona Sources:
  - Persona ID: technical-writer
  - Source: built-in
  - Runtime Role: worker
  - Selection Rationale: project-first lookup found no eligible documentation/specification worker; `technical-writer` is worker-capable and suited to an implementation-ready durable contract.
- Planned Scope: write only `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/design-spec.md`.
- Planned Scope rule: every writable file listed here appears under `exclusive_write_scope`; shared inputs remain read-only.
- Planning Rationale: a single serial section keeps phase vocabulary, state compatibility, transitions, events, rollups, migration, and recovery internally consistent.
- Planned Workflow Bindings: `superpowers:writing-plans`, `superpowers:requesting-code-review`, `superpowers:verification-before-completion`
- Planned Worker Mode: plan-first
- Worker Mode Rationale: reconcile existing runtime semantics and umbrella decisions before drafting detailed transitions and schemas.
- Goal Tuning: use normative language, transition tables, explicit invariants, invalid-state examples, and implementation acceptance criteria.
- Constraint Interaction Rule: later verifier, hook, lane, model, scoring, validator, and implementation details may be referenced only as deferred integration points, not designed or changed here.
- Planned Review Lanes:
  - Lane ID: LIFECYCLE-SPEC-REVIEW
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: lifecycle state authority, deterministic transitions, compatibility, migration, and testable acceptance criteria make the built-in spec reviewer the strongest eligible reviewer-only match; built-in fallback is used because no stronger project reviewer covers specification contract fidelity.
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `artifact_id`: `LIFECYCLE_FOUNDATION_SPEC`
  - `shared_read_scope`:
    - `artifact_id`: `TASK_RUNTIME_UMBRELLA_DESIGN`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/**/*`
    - `path_glob`: `docs/cases/**/dispatch-plan.md`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: `LIFECYCLE_FOUNDATION_SPEC`
    - `artifact_kind`: design_spec
    - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/design-spec.md`
    - `section_anchors`: `State Ownership`, `Phase Vocabulary`, `Transition Model`, `Lifecycle Event Schema`, `Rollup And Recovery`, `Acceptance Criteria`
- Packet Created: true

## Section Runtime Ledger

### Section: Lifecycle Foundation Design

- Section ID: LIFECYCLE-DESIGN-001
- Runtime State: complete
- Active Execution ID:
- Active Packet ID:
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode:
- Active Persona IDs:
- Active Persona Sources:
- Active Persona Role Bindings:
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
  - Execution ID: exec-lifecycle-spec-review-01
  - Role: reviewer
  - Status: DONE
  - Owned Scope: read-only findings on lifecycle foundation design revisions
  - Started At: 2026-06-19
  - Finished At: 2026-06-20
- Packet Records:
  - Packet ID: packet-lifecycle-spec-review-r3-02
  - Execution ID: exec-lifecycle-spec-review-01
  - Stage: review
  - Template Path: agents/reviewer-prompt.md
  - Review Target Ref: design spec revision 3, `sha256:bc9e48c8f19afd2e989e7456171baedade962de61d78c35f0118ead36cb94f53`
  - Supersedes Attempt ID:
  - Accepts Late Results: false
  - Packet ID: packet-lifecycle-spec-review-r4-03
  - Execution ID: exec-lifecycle-spec-review-01
  - Stage: review
  - Template Path: agents/reviewer-prompt.md
  - Review Target Ref: design spec revision 4, `sha256:39aedc9128711e6d74cb75d4e05a9eec9e872c46061468954e3aef22e96e3060`
  - Supersedes Attempt ID: attempt-lifecycle-spec-review-r3-02
  - Accepts Late Results: false
  - Packet ID: packet-lifecycle-spec-review-r5-04
  - Execution ID: exec-lifecycle-spec-review-01
  - Stage: review
  - Template Path: agents/reviewer-prompt.md
  - Review Target Ref: design spec revision 5, `sha256:f0f820e746517546d872889851e5579454e6d1bbcafed187923e724b83dfb358`
  - Supersedes Attempt ID: attempt-lifecycle-spec-review-r4-03
  - Accepts Late Results: false
  - Packet ID: packet-lifecycle-spec-review-r6-05
  - Execution ID: exec-lifecycle-spec-review-01
  - Stage: review
  - Template Path: agents/reviewer-prompt.md
  - Review Target Ref: design spec revision 6, `sha256:87f60d1ac78b3e90a5c9110dc919add61bacfe3a3eb615f03de2dee0a2b20454`
  - Supersedes Attempt ID: attempt-lifecycle-spec-review-r5-04
  - Accepts Late Results: false
  - Packet ID: packet-lifecycle-spec-review-r7-06
  - Execution ID: exec-lifecycle-spec-review-01
  - Stage: review
  - Template Path: agents/reviewer-prompt.md
  - Review Target Ref: design spec revision 7, `sha256:4382b9948fe543ca305627c04cb8cbfb90e9578fe0a2c20305fbc09d037ba580`
  - Supersedes Attempt ID: attempt-lifecycle-spec-review-r6-05
  - Accepts Late Results: false
  - Packet ID: packet-lifecycle-spec-review-r8-07
  - Execution ID: exec-lifecycle-spec-review-01
  - Stage: review
  - Template Path: agents/reviewer-prompt.md
  - Review Target Ref: design spec revision 8, `sha256:30af50aa94d7b23a951a70ca0bcd384bf866756be0da4990e2a6803895686cfc`
  - Supersedes Attempt ID: attempt-lifecycle-spec-review-r7-06
  - Accepts Late Results: false
  - Packet ID: packet-lifecycle-spec-review-r9-08
  - Execution ID: exec-lifecycle-spec-review-01
  - Stage: review
  - Template Path: agents/reviewer-prompt.md
  - Review Target Ref: design spec revision 9, `sha256:33635b18cb2b5bd9f9f9104bd9820af260ad8a592e5ae25e0c48ac53e805ef0f`
  - Supersedes Attempt ID: attempt-lifecycle-spec-review-r8-07
  - Accepts Late Results: false
  - Packet ID: packet-lifecycle-spec-review-r10-09
  - Execution ID: exec-lifecycle-spec-review-01
  - Stage: review
  - Template Path: agents/reviewer-prompt.md
  - Review Target Ref: design spec revision 10, `sha256:42f1c13babe53291b81efc35e3a1beb1f5a80672645b2f0c9a70931d05098f49`
  - Supersedes Attempt ID: attempt-lifecycle-spec-review-r9-08
  - Accepts Late Results: false
  - Packet ID: packet-lifecycle-spec-review-r11-10
  - Execution ID: exec-lifecycle-spec-review-01
  - Stage: review
  - Template Path: agents/reviewer-prompt.md
  - Review Target Ref: design spec revision 11, `sha256:360ee0d13e3dc705560d3dd7de9e2c3be49251df9e9e32ff2728a1c115b86e6b`
  - Supersedes Attempt ID: attempt-lifecycle-spec-review-r10-09
  - Accepts Late Results: false
- Attempt Records:
  - Attempt ID: attempt-lifecycle-spec-review-r3-02
  - Packet ID: packet-lifecycle-spec-review-r3-02
  - Agent ID: 019ee285-eeb4-78f3-8e5b-0dd300e3682f
  - Return Status: REJECT
  - Runtime State After Return: review-pending
  - Launched At: 2026-06-19
  - Closed At: 2026-06-19
  - Result Summary: four material findings on reviewer return normalization, close transitions, blocked revision persistence, and phase skipping discipline; all patched in design revision 4
  - Result Artifact Location:
  - Attempt ID: attempt-lifecycle-spec-review-r4-03
  - Packet ID: packet-lifecycle-spec-review-r4-03
  - Agent ID: 019ee289-c4ef-77b2-a18e-31848ae7555d
  - Return Status: REJECT
  - Runtime State After Return: review-pending
  - Launched At: 2026-06-19
  - Closed At: 2026-06-19
  - Result Summary: five material findings on migration verification safety, protocol activation readiness, exact failure states, plan recovery, and deterministic next actions; all patched in design revision 5
  - Result Artifact Location:
  - Attempt ID: attempt-lifecycle-spec-review-r5-04
  - Packet ID: packet-lifecycle-spec-review-r5-04
  - Agent ID: 019ee28e-a01d-7242-bbcd-9bcd6e861b36
  - Return Status: REJECT
  - Runtime State After Return: review-pending
  - Launched At: 2026-06-19
  - Closed At: 2026-06-19
  - Result Summary: three material findings on atomic protocol migration, bootstrap transition legality, and exact revision-event phase sets; all patched in design revision 6
  - Result Artifact Location:
  - Attempt ID: attempt-lifecycle-spec-review-r6-05
  - Packet ID: packet-lifecycle-spec-review-r6-05
  - Agent ID: 019ee291-bc72-74d0-9aa2-e03535e7a10f
  - Return Status: REJECT
  - Runtime State After Return: review-pending
  - Launched At: 2026-06-19
  - Closed At: 2026-06-19
  - Result Summary: one material finding that bootstrap destination runtime state conflicted with verification-safe migration normalization; patched in design revision 7
  - Result Artifact Location:
  - Attempt ID: attempt-lifecycle-spec-review-r7-06
  - Packet ID: packet-lifecycle-spec-review-r7-06
  - Agent ID: 019ee294-6b9b-7d50-8f0b-bd47e9327295
  - Return Status: REJECT
  - Runtime State After Return: review-pending
  - Launched At: 2026-06-19
  - Closed At: 2026-06-19
  - Result Summary: four material findings on protocol-specific completion, round-atomic multi-section migration, queued/failed stop recovery, and genesis snapshot consistency; all patched in design revision 8
  - Result Artifact Location:
  - Attempt ID: attempt-lifecycle-spec-review-r8-07
  - Packet ID: packet-lifecycle-spec-review-r8-07
  - Agent ID: 019ee3ca-be86-7232-91ef-889b7e1622a7
  - Return Status: REJECT
  - Runtime State After Return: review-pending
  - Launched At: 2026-06-19
  - Closed At: 2026-06-19
  - Result Summary: two material findings on contradictory legacy running migration and missing multi-lane aggregate progression; all patched in design revision 9
  - Result Artifact Location:
  - Attempt ID: attempt-lifecycle-spec-review-r9-08
  - Packet ID: packet-lifecycle-spec-review-r9-08
  - Agent ID: 019ee3ce-b3cc-79e1-a675-07f3f9999330
  - Return Status: REJECT
  - Runtime State After Return: review-pending
  - Launched At: 2026-06-19
  - Closed At: 2026-06-20
  - Result Summary: three material findings on overlapping bootstrap predicates, partial reviewer coverage migration, and terminal required-section migration; all patched in design revision 10
  - Result Artifact Location:
  - Attempt ID: attempt-lifecycle-spec-review-r10-09
  - Packet ID: packet-lifecycle-spec-review-r10-09
  - Agent ID: 019ee3d8-3113-7ba3-b46d-2545a9a93a49
  - Return Status: REJECT
  - Runtime State After Return: review-pending
  - Launched At: 2026-06-20
  - Closed At: 2026-06-20
  - Result Summary: one material finding that later bootstrap milestones did not cumulatively require matching formal verification and required review evidence; patched in design revision 11
  - Result Artifact Location:
  - Attempt ID: attempt-lifecycle-spec-review-r11-10
  - Packet ID: packet-lifecycle-spec-review-r11-10
  - Agent ID: 019ee3db-8747-75f3-b6f9-1e3ec4e48d50
  - Return Status: PASS
  - Runtime State After Return: review-pending
  - Launched At: 2026-06-20
  - Closed At: 2026-06-20
  - Result Summary: no material findings
  - Result Artifact Location:
- Attempt Count: 10
- Last Update At: 2026-06-19
- Next Action: none; round complete
- Active Write Scope: none
- Result Summary: lifecycle foundation design revision 11 reached canonical spec-review PASS after cumulative bootstrap evidence was made explicit.
- Canonical Result Artifact Location: `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/design-spec.md`
- Concerns: preserve one canonical owner per state surface and defer later rollout layers; revision 11 review is delta-focused on cumulative bootstrap evidence, while new independent subsystem concerns are follow-up only.
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy: non-active attempts may append history only when explicitly accepted and may not advance canonical state.
- Reconciliation Rule: newest active attempt owns the canonical result artifact location.

## Section Review Record

### Section: Lifecycle Foundation Design

- Section ID: LIFECYCLE-DESIGN-001
- Review Target Strategy: review the stable design spec against the working brief, umbrella design, and current WorkWork runtime-state contract.
- Review Lane Records:
  - Lane ID: LIFECYCLE-SPEC-REVIEW
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: lifecycle state authority, deterministic transitions, compatibility, migration, and testable acceptance criteria make the built-in spec reviewer the strongest eligible reviewer-only match; built-in fallback is used because no stronger project reviewer covers specification contract fidelity.
  - Execution ID: exec-lifecycle-spec-review-01
  - Packet ID: packet-lifecycle-spec-review-r11-10
  - Attempt ID: attempt-lifecycle-spec-review-r11-10
  - Review Target Ref:
    - Artifact Path: `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/design-spec.md`
    - Artifact Kind: design_spec
    - Artifact Revision: 11
    - Schema Version: 1
    - Section Anchor: State Ownership
    - Content Hash: `sha256:360ee0d13e3dc705560d3dd7de9e2c3be49251df9e9e32ff2728a1c115b86e6b`
  - Reviewer Findings: no material findings on revision 11; cumulative bootstrap evidence, same-target verification/review requirements, and verify-first fallback are coherent.
  - Orchestrator Synthesis: accept design revision 11 for human judgment; all prior canonical findings are superseded by the current immutable target and no material finding remains.
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes: user approved immutable design artifact revision 11 on 2026-06-20 after canonical packet-bound review returned no material findings; section accepted and closed complete.
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level plan state derives from required-for-goal sections

## Ordering And Parallelism

- Blocking work first: approve the plan, draft the complete foundation spec, stabilize its revision, then run independent spec review.
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
- Approval Time: 2026-06-19
- Notes: revision 2 approved; canonical packet creation and review of design revision 3 are authorized.
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: first bounded lifecycle foundation design round under the approved umbrella architecture
- Supersedes Revision: none
- Revision 2 Created From Brief Version: 1
- Revision Reason: correct reviewer rationale persistence so packet persona provenance can exactly match the approved dispatch selection
- Supersedes Revision: 1

## Dispatch Log

- Agents Launched: one direct reviewer pre-review was launched and closed without a persisted packet; its result is explicitly non-canonical and cannot satisfy the review lane
- Retry Events: none
- Close Events: LIFECYCLE-DESIGN-001 accepted and closed after final human approval
- Review Lane Transitions: non-canonical pre-review informed revisions 2 and 3; canonical revisions 3 through 10 rejected with material findings; canonical revision 11 passed with no material findings and moved to human judgment
- Launch Time: 2026-06-19
- Revisions Since Approval: 1
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
- 2026-06-19: user approved revision 1; plan moved through approved to dispatched and the design section began.
- 2026-06-19: pre-launch packet validation exposed reviewer-rationale drift in approved revision 1; invalid packet was discarded without launch and plan revision 2 was generated for reapproval.
- 2026-06-19: user approved revision 2; plan moved to dispatched for canonical packet-bound review of design revision 3.
- 2026-06-19: canonical revision 3 review returned four material findings; revision 4 patched them, invalidated the prior target hash, and rotated packet and attempt identity for re-review.
- 2026-06-19: canonical revision 4 review returned five material findings; revision 5 patched them, invalidated the prior target hash, and rotated packet and attempt identity for re-review.
- 2026-06-19: canonical revision 5 review returned three material findings; revision 6 patched them, invalidated the prior target hash, and rotated packet and attempt identity for re-review.
- 2026-06-19: canonical revision 6 review returned one material finding; revision 7 patched it, invalidated the prior target hash, and rotated packet and attempt identity for re-review.
- 2026-06-19: canonical revision 7 review returned four material findings; revision 8 patched them, invalidated the prior target hash, and rotated packet and attempt identity for re-review.
- 2026-06-19: canonical revision 8 review returned two material findings; revision 9 patched them, invalidated the prior target hash, and rotated packet and attempt identity for re-review.
- 2026-06-20: canonical revision 9 review returned three material findings; revision 10 patched them under the convergence boundary, invalidated the prior target hash, and rotated packet and attempt identity for bounded re-review.
- 2026-06-20: bounded revision 10 review returned one cumulative-evidence finding; revision 11 patched it and rotated packet and attempt identity for final delta-focused review.
- 2026-06-20: canonical revision 11 review returned no material findings; orchestrator synthesis accepted the artifact for human judgment.
- 2026-06-20: user approved design revision 11; section moved to accepted/complete and plan moved to completed without mutating the reviewed target.
