# Design Spec: Case Artifact Scaffolding Pilot

Date: 2026-05-23
Status: Approved for implementation
Scope: add a repo-local helper that scaffolds case-based WW round artifacts under `docs/cases/...` without taking over workflow decisions.

## Goal

Make new case-based rounds easier to start by generating the directory shape and the minimum draft documents that every round already expects.

This pilot should:

- create or update `case.md`
- create `working-brief.md` and `dispatch-plan.md` by default
- create `design-spec.md` and `implementation-plan.md` only when explicitly requested
- avoid deriving approval state, reviewer findings, or dispatch decisions

## Decisions

1. The helper lives in `tools/scaffold_ww_case_artifacts.py`.
2. Default outputs are:
   - `case.md`
   - `working-brief.md`
   - `dispatch-plan.md`
3. Optional outputs behind flags are:
   - `design-spec.md`
   - `implementation-plan.md`
4. Existing round files are not overwritten unless the user passes `--overwrite`.
5. `case.md` updates are navigational only: advance `Current Round` and keep `Round Index` in sync.
6. The helper may write placeholders, but those placeholders do not count as a completed WW round.

## Out Of Scope

- launching subagents
- inferring approval decisions
- generating reviewer findings
- changing validator behavior
- touching the legacy archival surface
