# Implementation Plan: Legacy Normalization Pilot

Date: 2026-05-23
Status: Drafted

## Goal

Apply a bounded normalization pass to archived workflow artifacts so archive-facing references resolve to `docs/legacy/superpowers/...` wherever they are serving as navigational pointers, while preserving intentional historical context.

## Primary Targets

- `docs/legacy/superpowers/**/*`
- `docs/legacy/superpowers/README.md`
- current round artifacts under `docs/cases/case-based-artifact-layout/rounds/2026-05-23-legacy-normalization-pilot/`

## Steps

1. Define the normalization rule and stop condition.
2. Apply mechanical replacements to archive-facing path-reference fields inside legacy workflow documents.
3. Manually inspect the remaining `docs/superpowers/...` mentions and keep only the ones that still carry historical-source meaning.
4. Update the legacy README to explain the difference between normalized archive pointers and preserved historical prose.
5. Record the completion state in the round dispatch plan.

## Guardrails

- do not edit active `docs/cases/...` artifacts outside the current round
- do not rewrite historical conclusions, rationale, or decisions
- preserve old-path mentions when they are explaining what the source layout used to be
- stop once the remaining old-path references are clearly historical rather than navigational

## Verification

- `rg -n "docs/superpowers/(working-briefs|dispatch-plans|specs|plans)" docs/legacy/superpowers`
- `python tools/validate_ww_repo.py`

The round is done when the remaining old-path references in `docs/legacy/superpowers` are intentional historical mentions rather than stale archive pointers.
