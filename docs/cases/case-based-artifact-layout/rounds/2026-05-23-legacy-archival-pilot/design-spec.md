# Design Spec: Legacy Archival Pilot

Date: 2026-05-23
Status: Approved for implementation
Scope: archive pre-cutover type-based workflow artifacts into a dedicated legacy surface without changing the active `docs/cases/...` model.

## Goal

Create one explicit home for historical workflow artifacts that used the old type-based layout.

This pilot should:

- preserve the active `docs/cases/<case-slug>/rounds/<round-slug>/` model
- gather old workflow documents into one obvious historical location
- avoid bulk repo cleanup outside the workflow artifact families

## Legacy Surface

Use:

```text
docs/legacy/superpowers/
  working-briefs/
  dispatch-plans/
  specs/
  plans/
```

This keeps the old family names intact while making the archival boundary explicit.

## Decisions

1. Active rounds continue to write only to `docs/cases/...`.
2. Old type-based workflow artifact families move under `docs/legacy/superpowers/`.
3. The pilot moves only those four families:
   - `docs/superpowers/working-briefs/`
   - `docs/superpowers/dispatch-plans/`
   - `docs/superpowers/specs/`
   - `docs/superpowers/plans/`
4. `docs/superpowers/artifact-registry.yaml` and any active references that still point to moved files must be updated.
5. Archived files remain historical references, not active write targets.

## Out Of Scope

- moving `docs/cases/...`
- redesigning validators beyond path/reference updates required by the move
- cleaning every maintainer note or every historical reference in one pass unless it is needed for correctness
