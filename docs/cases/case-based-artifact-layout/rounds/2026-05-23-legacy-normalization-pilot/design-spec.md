# Design Spec: Legacy Normalization Pilot

Date: 2026-05-23
Status: Approved for implementation
Scope: normalize archived workflow artifact references inside `docs/legacy/superpowers/` without changing the active `docs/cases/...` workflow model.

## Goal

Make the archived workflow surface easier to browse by updating legacy documents that still point at pre-archive type-based paths when those references are acting as navigational links or artifact pointers.

This pilot should:

- preserve `docs/cases/<case-slug>/rounds/<round-slug>/` as the only active workflow root
- keep `docs/legacy/superpowers/` explicitly historical
- improve internal consistency inside the archived surface with bounded, mechanical edits

## Normalization Rule

Normalize a legacy path reference when it is functioning as a current archive-facing pointer, for example:

- `Working Brief Reference`
- `artifact_path`
- `path_glob`
- `Artifact Path`
- `Result Artifact Location`
- similar planned-scope or primary-target path bullets that are clearly identifying a concrete document location

Preserve an old path reference when it is functioning as historical explanation, for example:

- prose describing the pre-archive source families
- design text explaining what the old layout used to be
- command examples or search expressions that intentionally show the old path family as part of the historical migration story

## Decisions

1. The active workflow root remains `docs/cases/...`.
2. The archived workflow root remains `docs/legacy/superpowers/...`.
3. This pilot normalizes only archived workflow documents plus the current round artifacts that describe the normalization.
4. The pilot is allowed to leave intentional historical mentions of `docs/superpowers/...` in place when they describe source-state semantics rather than current archive navigation.
5. No validator or runtime contract changes are required for this round because the active-path model is unchanged.

## Out Of Scope

- moving active artifacts
- rewriting historical reasoning for clarity or style
- turning legacy files into active workflow templates
- exhaustive cleanup of every historical command snippet or migration note
