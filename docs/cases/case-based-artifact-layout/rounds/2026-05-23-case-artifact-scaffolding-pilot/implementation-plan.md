# Implementation Plan: Case Artifact Scaffolding Pilot

Date: 2026-05-23
Status: Drafted

## Goal

Add a minimal helper that creates case-based WW artifact skeletons in a deterministic directory structure and updates `case.md` safely.

## Primary Targets

- `tools/scaffold_ww_case_artifacts.py`
- `README.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `docs/cases/case-based-artifact-layout/case.md`
- current round artifacts under `docs/cases/case-based-artifact-layout/rounds/2026-05-23-case-artifact-scaffolding-pilot/`

## Steps

1. Implement a helper that accepts case slug, round slug, title, and user request.
2. Make the helper create `working-brief.md` and `dispatch-plan.md` by default.
3. Add optional flags for `design-spec.md` and `implementation-plan.md`.
4. Update `case.md` so `Current Round` and `Round Index` stay in sync.
5. Document helper usage in maintainer-facing docs.
6. Smoke test the helper against a temporary output root and verify the generated structure.

## Guardrails

- keep helper output placeholder-based rather than authoritative
- refuse to overwrite existing round files without an explicit flag
- preserve existing case metadata in `case.md`
- keep optional artifacts opt-in

## Verification

- `python tools/scaffold_ww_case_artifacts.py --dry-run --case-slug example-case --round-slug 2026-05-23-example-round --title "Example Round" --user-request "example"`
- run the helper against a temporary output root and inspect the generated paths
- `python tools/validate_ww_repo.py`
- `python -m py_compile tools/scaffold_ww_case_artifacts.py`
