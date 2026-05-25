# Design Spec: Round Lifecycle Pilot

Date: 2026-05-24
Status: Approved for implementation
Scope: define how `case.md` and per-round artifacts should stay synchronized as rounds are created, approved, completed, or stopped.

## Goal

Make case/round lifecycle ownership deterministic without turning `case.md` into a second runtime state machine.

This pilot should:

- define which lifecycle facts belong in `case.md`
- define which lifecycle facts remain owned by round artifacts
- clarify when `Current Round` and `Round Index` should change
- establish the future validation direction for stale round pointers

## Decisions

1. `case.md` remains navigational only. It must not mirror per-round runtime state such as execution status, reviewer outcomes, or packet-level progress.
2. `dispatch-plan.md` remains the source of truth for round approval, execution, and closure state.
3. `Current Round` in `case.md` points to the newest active round for the case. Creating a new round advances it immediately, even before that round completes.
4. `Round Index` is append-only navigational history for created rounds. It is not an approval ledger and does not encode completion semantics by itself.
5. Terminal lifecycle facts such as `completed` or `stopped` stay in the round's `dispatch-plan.md`; `case.md` only needs enough information to help humans find the current round and prior rounds.
6. A future validator may compare `Current Round` to actual round creation state, but this pilot does not add a second lifecycle state surface to `case.md`.

## Ownership Model

- `case.md`
  - owns case-level navigation
  - owns `Current Round`
  - owns `Round Index`
  - may summarize legacy posture
- `working-brief.md`
  - owns round framing and planning recommendations
- `dispatch-plan.md`
  - owns round approval/execution/closure state
  - owns section review and runtime ledger state

## Lifecycle Rules

- creating a new round:
  - adds that round to `Round Index`
  - updates `Current Round` to the new round slug
- completing or stopping a round:
  - updates only the round's `dispatch-plan.md`
  - does not require adding a second completion field to `case.md`
- opening a later round:
  - supersedes the earlier round as `Current Round`
  - leaves prior round artifacts intact in `Round Index`

## Out Of Scope

- packet/runtime controller changes
- redesigning scaffold helper output
- changing the legacy archive model
- adding new lifecycle fields to `case.md` in this pilot
