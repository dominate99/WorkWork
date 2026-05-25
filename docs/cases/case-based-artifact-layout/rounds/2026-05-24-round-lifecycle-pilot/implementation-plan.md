# Implementation Plan: Round Lifecycle Pilot

Date: 2026-05-24
Status: Drafted

## Goal

Define the minimal lifecycle contract between `case.md` and round artifacts.

## Primary Targets

- `docs/cases/case-based-artifact-layout/case.md`
- `docs/cases/case-based-artifact-layout/rounds/2026-05-24-round-lifecycle-pilot/*`

## Steps

1. Document the current ambiguity between case-level navigation and round-level execution state.
2. Define ownership boundaries for `Current Round`, `Round Index`, and terminal round state.
3. Capture a deterministic rule set for:
   - when `Current Round` changes
   - what `Round Index` means
   - where `completed` and `stopped` state belongs
4. Keep the pilot bounded to planning/contract surfaces only.
5. Use this pilot as the basis for a later lifecycle validator round if the repo needs automatic stale-pointer checks.

## Guardrails

- do not turn `case.md` into a runtime ledger
- do not duplicate round state in two active places
- do not widen helper responsibilities in this round
- keep active root and case contract intact

## Verification

- `python tools/validate_ww_case_contracts.py`
- `python tools/validate_ww_repo.py`
