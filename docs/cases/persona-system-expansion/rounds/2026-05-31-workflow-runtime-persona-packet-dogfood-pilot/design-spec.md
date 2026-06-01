# Runtime Persona Packet Dogfood Gap Report

Date: 2026-05-31
Status: Approved
Scope: Create and review one minimal real worker packet and one minimal real
reviewer packet derived from an approved dispatch plan. This report classifies
packet assembly evidence only. It does not implement runtime code, change the
packet contract, edit validators, add personas, modify the project registry,
expand routing, or add secondary tags.

## Goal

Close the packet-artifact evidence portion of DG-004 by checking whether a
minimal worker packet and reviewer packet can preserve runtime persona
selection provenance from an approved dispatch plan.

## Pilot Artifacts

- Approved source plan:
  `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/dispatch-plan.md`
- Worker packet:
  `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/packets/worker-packet.md`
- Reviewer packet:
  `docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/packets/reviewer-packet.md`
- Worker packet SHA-256:
  `537c6b31ffc0b288a7aef7c81a2c5ed5ba8994ddafec46519fe1f3c6d0a35bac`
- Reviewer packet SHA-256:
  `28aeb32e4f6c67db669bf3ad44b80a3907da0731480bd75ebd748343ece75ad0`

## Lifecycle Evidence

- The working brief recorded `estimation_complete: true` and
  `brief_status: ready`.
- The dispatch plan was approved before either packet artifact was created.
- The approved dispatch section records reviewer and specialist persona ids,
  sources, runtime roles, rationales, prompt template paths, and the worker
  implementation-principle snapshot used by this pilot.
- The reviewer packet binds an immutable full-file worker-packet snapshot by
  SHA-256.
- No subagent was launched. This is an artifact-level dogfood pilot.

## Field-Copy Audit

### Worker Packet

| Field | Approved Dispatch Snapshot | Worker Packet | Result |
| --- | --- | --- | --- |
| `subagent_persona` | `technical-writer` | `technical-writer` | pass |
| `persona_source` | `built-in` | `built-in` | pass |
| `persona_rationale` | built-in fallback because no stronger eligible project worker covers packet evidence documentation | exact approved rationale copied | pass |
| `persona_binding.runtime_role` | `worker` | `worker` | pass |
| `persona_binding.template_path` | `agents/worker-prompt.md` | `agents/worker-prompt.md` | pass |
| `implementation_principles[0]` | task-oriented documentation hard rule | exact persona-definition and approved-snapshot string copied | pass |
| `implementation_principles[1]` | stable-structure soft principle | exact persona-definition and approved-snapshot string copied | pass |

### Reviewer Packet

| Field | Approved Dispatch Snapshot | Reviewer Packet | Result |
| --- | --- | --- | --- |
| `subagent_persona` | `spec-reviewer` | `spec-reviewer` | pass |
| `persona_source` | `built-in` | `built-in` | pass |
| `persona_rationale` | built-in fallback because no stronger eligible project reviewer covers packet contract fidelity | exact approved rationale copied | pass |
| `persona_binding.runtime_role` | `reviewer` | `reviewer` | pass |
| `persona_binding.template_path` | `agents/reviewer-prompt.md` | `agents/reviewer-prompt.md` | pass |
| `write_scope` | reviewer-only read authority | `[]` | pass |
| `review_target_ref` | stable worker packet artifact | immutable SHA-256 full-file snapshot | pass |

## Capability-Gate Audit

### Worker Gate

Status: pass.

Evidence:

- `technical-writer` is a built-in persona with `role_type: specialist`.
- `technical-writer` records `review_only: false`.
- Its persona definition contains exactly two ordered
  `implementation_principles`.
- The worker packet copies those two strings directly and in order.
- The worker packet uses `runtime_role: worker` and
  `agents/worker-prompt.md`.

### Reviewer Gate

Status: pass.

Evidence:

- `spec-reviewer` is a built-in persona with `role_type: reviewer`.
- `spec-reviewer` records `review_only: true`.
- The reviewer packet has `write_scope: []`.
- The reviewer packet uses `runtime_role: reviewer` and
  `agents/reviewer-prompt.md`.
- Its immutable target is the worker packet SHA-256 snapshot.

## Findings

### PKT-001: DG-004 Is Resolved At The Packet-Artifact Layer

Status: pass.

The pilot now supplies one persisted worker packet and one persisted reviewer
packet. Both preserve the selected persona id, source, rationale, runtime role,
and prompt template path. The worker packet additionally preserves the
technical writer's two canonical implementation principles in order.

Classification: packet artifact evidence gained.

### PKT-002: Generic Dispatch Template Does Not Yet Require Launch Snapshots

Status: non-blocking follow-up design question.

The active dispatch plan template requires planned reviewer and specialist
persona source, runtime role, and rationale. It does not require a planned
prompt-template-path snapshot or a planned worker-principles snapshot.

This pilot persisted both as round-local approved launch snapshot fields so the
copy audit could be direct and inspectable. The current packet contract is
still coherent: it separately requires role-specific prompt bindings and
direct sourcing of worker principles from the selected persona definition.

Classification: validator-design input, not a packet-contract failure.

Recommended follow-up:

- In the later validator round, decide whether dispatch plans must always
  persist these launch snapshots or whether validators should cross-check
  packet prompt bindings against runtime role and worker principles against
  the selected persona definition.

### PKT-003: Artifact Evidence Is Not Runtime-Code Evidence

Status: expected limitation.

The repository now demonstrates that contract-complete packets can be
assembled and reviewed as persisted artifacts. No runtime assembly code was
implemented or executed, and no subagent was launched.

Classification: explicit evidence boundary.

## Validator-Round Readiness

Decision: enough evidence exists to open a focused packet validator design or
validator expansion round.

A later validator round can use this pilot to design checks for:

- packet required fields
- approved source dispatch plan and plan revision
- exact persona id, source, rationale, and runtime-role copying
- role-specific prompt template path
- worker capability gate
- exact ordered worker implementation principles
- reviewer-only gate and empty reviewer write scope
- immutable reviewer target hash
- separation between packet-artifact validation and runtime-code claims

The later round should resolve PKT-002 explicitly before treating
dispatch-to-packet copying as a generic repository invariant.

## Acceptance Criteria Check

- One worker packet artifact exists.
- One reviewer packet artifact exists.
- Both packets derive from an approved dispatch plan.
- Required persona provenance and role-binding fields were checked.
- Worker implementation principles were checked against the approved snapshot
  and built-in persona definition.
- Reviewer-only authority was checked.
- Evidence is classified without implementing runtime code or changing active
  contract surfaces.
- Validator-round readiness is stated with an explicit boundary.

## Conclusion

The packet dogfood pilot passes. WorkWork now has enough persisted artifact
evidence to open a focused packet validator follow-up round. The next round
should stay narrow: design or add packet-level validation while deciding how
generic dispatch plans should expose prompt-path and worker-principle launch
snapshots.
