# Implementation Plan: Scaffold Adoption Pilot

Date: 2026-05-24
Status: Drafted

## Goal

Adopt scaffold-first initialization as the active default for new case-based `$ww/$www` rounds.

## Primary Targets

- `README.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `docs/cases/case-based-artifact-layout/case.md`
- `docs/cases/case-based-artifact-layout/rounds/2026-05-24-scaffold-adoption-pilot/*`

## Steps

1. Update maintainer-facing documentation to describe the helper as the default initializer for new rounds.
2. Update the active skill contract to require scaffold-first initialization for new case/round roots while preserving the draft-only boundary.
3. Persist this round's design and implementation artifacts under the current round root.
4. Re-run repo validation to confirm the adoption wording does not drift from the helper and existing case contract.

## Guardrails

- do not imply scaffold output is approval-ready
- do not widen the helper into workflow decision logic
- do not reintroduce old type-based write roots
- keep the change bounded to adoption guidance and current-round artifacts

## Verification

- `python tools/validate_ww_repo.py`
- `python tools/validate_ww_case_contracts.py`
