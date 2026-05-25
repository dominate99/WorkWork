# Case Template

Use this template for every active case root under `docs/cases/<case-slug>/`.

## Purpose

`case.md` is the navigational entrypoint for one long-lived case. It is not a dispatch gate, a runtime state machine, or a replacement for round artifacts.

## Required Layout

```md
# Case: <case-slug>

- Status: active | paused | archived
- Canonical Root: `docs/cases/<case-slug>/`
- Current Round: `<round-slug>`
- Goal: <short case goal>
- Legacy Status: <legacy posture note>

## Round Index

- `<round-slug>`

## Notes

- New `$ww` and `$www` rounds for this case should write under `docs/cases/<case-slug>/rounds/<round-slug>/`.
- Older artifacts that predate the `docs/cases/...` cutover are historical references under `docs/legacy/superpowers/`, not active write targets.
- `case.md` is navigational only. It is not a dispatch gate.
```

## Required Fields

- `# Case: <case-slug>`
- `Status`
- `Canonical Root`
- `Current Round`
- `Goal`
- `Legacy Status`
- `## Round Index`
- `## Notes`

## Rules

- Every case directory under `docs/cases/` must contain exactly one top-level `case.md`.
- `Canonical Root` must resolve to `docs/cases/<case-slug>/`.
- `Current Round` must point to the newest active round for the case.
- `Current Round` must also appear in `## Round Index`.
- `Round Index` is navigational history, not an approval or runtime ledger.
- `case.md` must not duplicate round approval, execution, or closure state; those remain owned by each round's `dispatch-plan.md`.
- `case.md` may be updated by repo-local scaffold helpers, but those helpers must preserve this layout.
