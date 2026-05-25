# Design Spec: Scaffold Adoption Pilot

Date: 2026-05-24
Status: Approved for implementation
Scope: make the case-artifact scaffold helper the default initializer for new `$ww/$www` case rounds without expanding it into workflow decision logic.

## Goal

Turn scaffold usage from an optional maintainer convenience into the documented default startup path for new case-based rounds.

This pilot should:

- make scaffold-first initialization explicit in active workflow guidance
- preserve the distinction between scaffold output and approval-ready planning artifacts
- keep `docs/cases/...` as the only active write root
- avoid re-opening legacy handling or packet/runtime semantics

## Decisions

1. `tools/scaffold_ww_case_artifacts.py` becomes the default initializer for new case-based `$ww/$www` rounds.
2. The helper remains a structure generator only; it does not satisfy approval or dispatch requirements by itself.
3. Adoption language belongs in the active skill contract and maintainer README, not only in helper-specific notes.
4. Manual repair or exceptional edits remain allowed, but scaffold-first is the standard path for new rounds.

## Out Of Scope

- redesigning the helper interface
- adding new validator rules beyond the existing case contract
- changing packet contracts or runtime dispatch semantics
- changing legacy archival policy
