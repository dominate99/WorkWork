# Implementation Plan: Case-Based Artifact Generation Pilot

Goal: switch new `$ww` and `$www` artifact generation to `docs/cases/...` with a hard legacy boundary and no dual-write bridge.

## Steps

- update workflow contract references from `docs/superpowers/cases/...` to `docs/cases/...`
- update path-identity validation to enforce the new root
- create a lightweight `case.md` entrypoint under the new case root
- persist this pilot round under the new canonical round root
- verify the repo validators still pass

## Guardrails

- do not bulk-migrate historical artifacts
- do not turn optional explanatory artifacts into required control surfaces
- keep legacy semantics explicit: historical only, not active compatibility

## Verification

- `python tools/quick_validate.py plugins/workwork/skills/ww-subagent-orchestrator`
- `python tools/validate_ww_case_path_identity.py`
- `python tools/validate_ww_repo.py`
- `python -m py_compile tools/validate_ww_case_path_identity.py tools/validate_ww_repo.py tools/quick_validate.py`
