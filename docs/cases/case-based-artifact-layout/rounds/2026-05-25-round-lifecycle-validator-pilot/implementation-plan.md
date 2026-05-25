# Implementation Plan: Round Lifecycle Validator Pilot

Date: 2026-05-25
Status: Drafted

## Goal

Implement a validator that enforces the round lifecycle ownership rules.

## Primary Targets

- `plugins/workwork/skills/ww-subagent-orchestrator/references/case-template.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `README.md`
- `tools/validate_ww_round_lifecycle.py`
- `tools/validate_ww_repo.py`
- `docs/cases/case-based-artifact-layout/rounds/2026-05-25-round-lifecycle-validator-pilot/*`

## Steps

1. Add lifecycle ownership language to the active contract surfaces.
2. Implement a dedicated validator for `Current Round`, `Round Index`, `case.md` authority boundaries, and round dispatch authority signals.
3. Wire the validator into the repo-level validator.
4. Persist this round's design and implementation artifacts.
5. Re-run repo validation to confirm the new checks stay bounded.

## Guardrails

- do not require `case.md` to mirror runtime state
- keep checks deterministic and structural
- do not widen helper responsibilities
- do not duplicate existing case-path or case-structure checks unnecessarily

## Verification

- `python tools/validate_ww_round_lifecycle.py`
- `python tools/validate_ww_repo.py`
