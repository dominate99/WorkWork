# Design Spec: Case-Based Artifact Generation Pilot

Date: 2026-05-22
Status: Approved for implementation
Scope: adopt `docs/cases/<case-slug>/rounds/<round-slug>/` as the canonical root for new `$ww` and `$www` artifacts.

## Goal

Make the artifact-generation interface simpler and more obvious:

- `docs/cases/<case-slug>/`
- `docs/cases/<case-slug>/rounds/<round-slug>/`

The system should no longer imply that `docs/superpowers/cases/...` is the active destination for new rounds.

## Decisions

1. The canonical root for new rounds becomes `docs/cases/<case-slug>/rounds/<round-slug>/`.
2. `case.md` becomes the lightweight case entrypoint for navigation only.
3. Required round artifacts remain minimal:
   - `working-brief.md`
   - `dispatch-plan.md`
   - `design-spec.md` when needed
   - `implementation-plan.md` when needed
4. Pre-cutover type-based artifacts are legacy history only.
5. No dual-write compatibility path is allowed.

## Interface

```text
docs/cases/<case-slug>/
  case.md
  rounds/
    <round-slug>/
      working-brief.md
      dispatch-plan.md
      design-spec.md
      implementation-plan.md
```

## Out Of Scope

- bulk migration of historical artifacts
- packet or prompt redesign
- validator redesign beyond the minimal root update needed for consistency
