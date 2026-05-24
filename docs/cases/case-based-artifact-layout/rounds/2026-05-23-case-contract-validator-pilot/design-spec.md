# Design Spec: Case Contract Validator Pilot

Date: 2026-05-24
Status: Approved for implementation
Scope: define a formal `case.md` template and add a repo-local validator that enforces case and round artifact structure.

## Goal

Turn the case-based artifact layout from a clear convention into a machine-checkable contract.

This pilot should:

- define a dedicated `case.md` template
- require every case root under `docs/cases/` to contain a `case.md`
- require every round directory to contain `working-brief.md` and `dispatch-plan.md`
- verify that scaffold-helper output satisfies the same structural rules

## Decisions

1. `plugins/workwork/skills/ww-subagent-orchestrator/references/case-template.md` becomes the canonical template for `case.md`.
2. A new validator script checks case-root and round-root structure.
3. The validator stays structural; it does not judge planning quality or prose quality.
4. Repo-level validation includes the new case contract validator.
5. Helper conformance is tested by generating temporary scaffold output and checking it against the same contract.

## Out Of Scope

- changing runtime packet semantics
- changing approval flow semantics
- linting case or round prose quality
- redesigning the legacy surface
