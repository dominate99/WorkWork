# Dispatch Plan: Runtime Persona Packet Dogfood Pilot

- Date: 2026-05-31
- Schema Version: 1
- Plan Revision: 1
- Working Brief Version: 1
- Case Slug: persona-system-expansion
- Round Slug: 2026-05-31-workflow-runtime-persona-packet-dogfood-pilot
- Case Root: `docs/cases/persona-system-expansion/`
- Round Root: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/`
- Plan State: completed
- Last Approved Revision: 1
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

> Do not create packet artifacts or launch any real subagent until the preconditions are satisfied and `Plan State: approved`.

## Source Context

- User Request: `new $ww round: runtime persona packet dogfood pilot. Based on completed persona runtime selection adoption and durable review lane rationale cleanup, create and review a minimal set of real packet artifacts: one worker packet and one reviewer packet. Verify that they copy subagent_persona, persona_source, persona_rationale, persona_binding.runtime_role, template_path, and worker implementation_principles correctly from an approved dispatch plan. Only do packet dogfood pilot and evidence classification; do not implement runtime code, change packet contract, change validators, add personas, change project registry, expand routing, or add secondary tags. Produce design-spec.md or gap report and judge whether packet assembly has enough evidence to enter a later validator round.`
- Working Brief Reference: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/working-brief.md`
- Artifact Registry Reference: `docs/superpowers/artifact-registry.yaml`

## Dispatch Summary

- Goal: create and audit one worker packet plus one reviewer packet as round-local packet dogfood evidence
- Relevant Context: DG-004 remains open because packet contract text exists but recent rounds did not persist live packet artifacts
- Constraints:
  - create exactly one worker packet and one reviewer packet after approval
  - create one `design-spec.md` gap report
  - do not implement runtime code
  - do not edit packet contract, validators, personas, project registry, routing, or secondary tags
- Risks:
  - packet creation before approval
  - incorrect field-copy source
  - worker principle order drift
  - reviewer write authority leakage
  - overclaiming artifact evidence as runtime-code evidence
- Reviewer Rule: Every section returns to the orchestrator before human judgment.

## Planned Sections

### Section: Runtime Persona Packet Dogfood Pilot

- Section ID: section-runtime-persona-packet-dogfood-pilot
- Section State: accepted
- Runtime State: complete
- Required For Goal: true
- Draft Author Role: technical-writer
- Planned Reviewer Persona: spec-reviewer
- Planned Reviewer Persona Source: built-in
- Planned Reviewer Runtime Role: reviewer
- Planned Reviewer Selection Rationale: packet contract fidelity, immutable review targeting, and evidence classification make the built-in spec reviewer the strongest eligible reviewer-only match; built-in fallback is used because no stronger eligible project reviewer covers packet contract fidelity
- Planned Reviewer Template Path: agents/reviewer-prompt.md
- Planned Specialist Personas:
  - Persona ID: technical-writer
    - Source: built-in
    - Runtime Role: worker
    - Selection Rationale: the primary work is persisted packet evidence and a maintainer-facing dogfood report; built-in fallback is used because no stronger eligible project worker persona covers packet evidence documentation
    - Template Path: agents/worker-prompt.md
    - Implementation Principles:
      - prefer task-oriented documentation that helps the reader act correctly over exhaustive explanation
      - when tradeoffs are close, bias toward stable structure, clear source of truth, and maintainable wording
- Planned Scope:
  - `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/packets/worker-packet.md`
  - `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/packets/reviewer-packet.md`
  - `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/design-spec.md`
- Planned Scope rule: every writable file listed here must also appear under `exclusive_write_scope`; `shared_read_scope` is for read-only dependencies only and must not hide writable ownership.
- Planning Rationale: generate minimal inspectable packet artifacts before considering a packet-level validator round
- Planned Workflow Bindings:
  - `superpowers:writing-plans`
  - `superpowers:requesting-code-review`
  - `superpowers:verification-before-completion`
- Planned Worker Mode: conservative-first
- Worker Mode Rationale: keep the pilot to one contract-complete worker packet, one read-only reviewer packet, and one evidence report
- Goal Tuning: validation-biased
- Constraint Interaction Rule: runtime code, packet contract, validators, personas, project registry, routing, and secondary tags remain read-only
- Planned Review Lanes:
  - Lane ID: lane-runtime-persona-packet-dogfood-pilot-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: review approved-dispatch derivation, required persona field copying, ordered worker principles, read-only reviewer authority, and evidence classification boundaries
  - Required: true
- Scope Declarations:
  - `exclusive_write_scope`:
    - `path_glob`: `docs/cases/persona-system-expansion/case.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/working-brief.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/dispatch-plan.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/packets/worker-packet.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/packets/reviewer-packet.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/design-spec.md`
  - `shared_read_scope`:
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
    - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
    - `path_glob`: `docs/superpowers/personas/registry.yaml`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/design-spec.md`
    - `path_glob`: `docs/cases/persona-system-expansion/rounds/2026-05-30-workflow-durable-review-lane-persona-rationale-cleanup/dispatch-plan.md`
  - `depends_on_sections`: none
  - `parallel_safe_with_sections`: none
  - `artifact_mappings`:
    - `artifact_id`: runtime_persona_packet_worker_evidence
      - `artifact_kind`: worker_packet
      - `artifact_path`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/packets/worker-packet.md`
      - `section_anchors`: worker packet evidence
    - `artifact_id`: runtime_persona_packet_reviewer_evidence
      - `artifact_kind`: reviewer_packet
      - `artifact_path`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/packets/reviewer-packet.md`
      - `section_anchors`: reviewer packet evidence
    - `artifact_id`: runtime_persona_packet_dogfood_gap_report
      - `artifact_kind`: dogfood_gap_report
      - `artifact_path`: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/design-spec.md`
      - `section_anchors`: packet dogfood findings
- Scope declaration rule: every writable file in `Planned Scope` must also appear in `exclusive_write_scope`; `shared_read_scope` must not hide writable ownership.
- Packet Created: true

## Section Runtime Ledger

### Section: Runtime Persona Packet Dogfood Pilot

- Section ID: section-runtime-persona-packet-dogfood-pilot
- Runtime State: complete
- Active Execution ID: exec-runtime-persona-packet-dogfood-reviewer-01
- Active Packet ID: packet-runtime-persona-packet-dogfood-reviewer-01
- Active Agent ID:
- Active Attempt ID:
- Active Worker Mode: conservative-first
- Active Persona IDs: technical-writer, spec-reviewer
- Active Persona Sources: technical-writer=built-in, spec-reviewer=built-in
- Active Persona Role Bindings: technical-writer=worker via `agents/worker-prompt.md`; spec-reviewer=reviewer via `agents/reviewer-prompt.md`
- Mode Change History:
  - Previous Mode:
  - New Mode:
  - Trigger Evidence:
  - Approved By:
  - Changed At:
- Execution Records:
  - Execution ID: exec-runtime-persona-packet-dogfood-worker-01
    - Role: worker packet artifact
    - Status: assembled
    - Owned Scope: `design-spec.md`
    - Started At: 2026-05-31
    - Finished At: 2026-05-31
  - Execution ID: exec-runtime-persona-packet-dogfood-reviewer-01
    - Role: reviewer packet artifact
    - Status: reviewed
    - Owned Scope: findings only; read-only review of `packets/worker-packet.md`
    - Started At: 2026-05-31
    - Finished At: 2026-05-31
- Packet Records:
  - Packet ID: packet-runtime-persona-packet-dogfood-worker-01
    - Execution ID: exec-runtime-persona-packet-dogfood-worker-01
    - Stage: implement
    - Template Path: `agents/worker-prompt.md`
    - Review Target Ref: `design-spec.md`
    - Supersedes Attempt ID:
    - Accepts Late Results: false
  - Packet ID: packet-runtime-persona-packet-dogfood-reviewer-01
    - Execution ID: exec-runtime-persona-packet-dogfood-reviewer-01
    - Stage: review
    - Template Path: `agents/reviewer-prompt.md`
    - Review Target Ref: `packets/worker-packet.md` SHA-256 `537c6b31ffc0b288a7aef7c81a2c5ed5ba8994ddafec46519fe1f3c6d0a35bac`
    - Supersedes Attempt ID:
    - Accepts Late Results: false
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
- Last Update At: 2026-05-31
- Next Action: round complete
- Active Write Scope: round-local packet artifacts and `design-spec.md` only
- Result Summary: assembled and reviewed one worker packet plus one reviewer packet; field-copy audit passes; DG-004 is resolved at the packet-artifact layer; generic launch-snapshot persistence remains a validator-design question
- Canonical Result Artifact Location: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/design-spec.md`
- Concerns:
  - packet artifact creation is forbidden before approval
  - keep evidence classification distinct from runtime-code proof
  - generic dispatch template does not yet require prompt-path or worker-principles launch snapshots
- Blocker Reason:
- Close State: closed
- Superseded Attempt IDs:
- Stale Result Policy:
- Reconciliation Rule:
  - newest active attempt owns `result_artifact_location`
  - late results may append attempt history when accepted, but they do not replace the canonical location unless the controller promotes that attempt to active

## Section Review Record

### Section: Runtime Persona Packet Dogfood Pilot

- Section ID: section-runtime-persona-packet-dogfood-pilot
- Review Target Strategy:
  - Review round-local packet artifacts and the final report for approved-dispatch derivation, source/rationale/binding field copying, worker principle ordering, reviewer read-only authority, and evidence classification accuracy.
- Review Lane Records:
  - Lane ID: lane-runtime-persona-packet-dogfood-pilot-spec-review
  - Lane Type: spec-review
  - Reviewer Persona: spec-reviewer
  - Reviewer Source: built-in
  - Reviewer Runtime Role: reviewer
  - Reviewer Selection Rationale: review packet-contract fidelity and evidence-bound conclusions
  - Execution ID: exec-runtime-persona-packet-dogfood-reviewer-01
  - Packet ID: packet-runtime-persona-packet-dogfood-reviewer-01
  - Attempt ID: local-artifact-spec-review-2026-05-31
  - Review Target Ref:
    - Artifact Path: `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/packets/worker-packet.md`
    - Artifact Kind: worker_packet
    - Artifact Revision: sha256:537c6b31ffc0b288a7aef7c81a2c5ed5ba8994ddafec46519fe1f3c6d0a35bac
    - Schema Version: 1
    - Section Anchor: worker packet evidence
    - Content Hash: sha256:537c6b31ffc0b288a7aef7c81a2c5ed5ba8994ddafec46519fe1f3c6d0a35bac
  - Reviewer Findings: no material field-copy drift; worker principles are canonical and ordered; reviewer authority remains read-only; residual non-blocking design question is whether generic dispatch plans must persist prompt-path and worker-principles launch snapshots
  - Orchestrator Synthesis: packet artifact dogfood passes and DG-004 is resolved at the artifact layer; the report correctly keeps runtime-code proof out of scope and records PKT-002 for the focused validator follow-up
  - Strict Review Outcome: none
- Human Decision: Approve
- Revision Notes: user approved the reviewed packet dogfood gap report on 2026-05-31; packet artifact evidence is accepted, section state is accepted, runtime state is complete, and plan state is completed
- Rollup Rule:
  - Approve -> section state becomes `accepted`
  - Revise -> section state becomes `revision-requested` and plan state becomes `revising`
  - Stop -> section state becomes `stopped`; top-level `plan_state` is derived from `required_for_goal`

## Ordering And Parallelism

- Blocking work first: section-runtime-persona-packet-dogfood-pilot
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
- Approved By: human
- Approval Time: 2026-05-31
- Notes: approval authorizes round-local worker packet, reviewer packet, and evidence report creation only; runtime code, packet contract, validators, personas, project registry, routing, and secondary tags remain out of scope
- Choice Mapping:
  - Approve -> `Plan State: approved`
  - Revise -> `Plan State: revising`
  - Stop -> `Plan State: stopped`

## Revision History

- Revision 1 Created From Brief Version: 1
- Revision Reason: initial runtime persona packet dogfood pilot round
- Supersedes Revision:

## Dispatch Log

- Agents Launched: none; artifact-only dogfood pilot
- Retry Events:
- Close Events:
  - 2026-05-31: user approved the reviewed packet dogfood gap report; section closed complete
- Review Lane Transitions:
  - 2026-05-31: round-local reviewer packet assembled against immutable worker packet SHA-256 snapshot; local spec review returned no material findings
- Launch Time: none; no subagent launch in this artifact-only pilot
- 2026-05-31: approval recorded; plan moved from `approved` to `dispatched` for packet artifact assembly and review
- Revisions Since Approval: 0
- Stop State Preserves Files: true
- No Launch Before Approval: true
- Result Artifact Location Source: latest active attempt record
