# Design Spec: Round Lifecycle Validator Pilot

Date: 2026-05-25
Status: Approved for implementation
Scope: add repo-local validation for the lifecycle ownership rules defined in the prior round.

## Goal

Make stale `Current Round` drift and lifecycle-authority duplication machine-detectable without changing the lifecycle model itself.

This pilot should:

- validate that `Current Round` points to the newest active round
- validate that `Current Round` appears in `Round Index`
- validate that `case.md` does not own runtime approval/execution state
- validate that round `dispatch-plan.md` remains the state authority surface

## Decisions

1. Add a dedicated round lifecycle validator instead of overloading the existing case contract validator.
2. Keep lifecycle checks structural and deterministic.
3. Validate state authority by checking for the presence of state fields in round `dispatch-plan.md` and the absence of forbidden authority fields in `case.md`.
4. Wire the validator into the repo-level validator and maintainer docs.

## Out Of Scope

- changing scaffold helper behavior
- changing lifecycle ownership semantics
- prose-quality linting
- packet/runtime controller changes
