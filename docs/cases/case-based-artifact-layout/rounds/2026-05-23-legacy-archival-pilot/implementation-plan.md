# Implementation Plan: Legacy Archival Pilot

Goal: move the old type-based workflow artifact families into `docs/legacy/superpowers/` and update the active references that still need to find them.

## Steps

- create `docs/legacy/superpowers/` with preserved family subfolders
- move:
  - `docs/superpowers/working-briefs/`
  - `docs/superpowers/dispatch-plans/`
  - `docs/superpowers/specs/`
  - `docs/superpowers/plans/`
- add a small legacy index note so the archival boundary is obvious
- update active references that still point to the moved files
- update workflow docs to say historical type-based artifacts now live under `docs/legacy/superpowers/`
- verify validators and key path scans still pass

## Guardrails

- do not move `docs/cases/...`
- do not widen into unrelated `docs/maintainers/...` cleanup unless a correctness issue forces it
- preserve the old family names under the legacy root to reduce migration complexity

## Verification

- `python tools/validate_ww_case_path_identity.py`
- `python tools/validate_ww_repo.py`
- `rg -n "docs/superpowers/working-briefs|docs/superpowers/dispatch-plans|docs/superpowers/specs|docs/superpowers/plans|docs/legacy/superpowers" .`
