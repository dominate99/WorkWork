# Implementation Plan: Case Contract Validator Pilot

Date: 2026-05-24
Status: Drafted

## Goal

Implement a structural validator that hardens the case-based artifact model and ensures helper output conforms to the same rules.

## Primary Targets

- `plugins/workwork/skills/ww-subagent-orchestrator/references/case-template.md`
- `tools/validate_ww_case_contracts.py`
- `tools/validate_ww_repo.py`
- `tools/scaffold_ww_case_artifacts.py`
- `README.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`

## Steps

1. Add a formal `case.md` template.
2. Implement a validator for:
   - case root presence of `case.md`
   - required `case.md` fields
   - required minimum round artifacts
3. Add helper smoke checks that prove scaffold output conforms to the same contract.
4. Wire the validator into repo-level validation.
5. Document the new template and validator entrypoint.

## Guardrails

- keep the validator structural and deterministic
- avoid prose-quality linting
- avoid introducing new runtime workflow behavior
- treat template-backed contract rules as the source of truth when helper and validator diverge

## Verification

- `python tools/validate_ww_case_contracts.py`
- `python tools/validate_ww_repo.py`
- `python -m py_compile tools/validate_ww_case_contracts.py tools/scaffold_ww_case_artifacts.py`
