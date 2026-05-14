# WWW Strict Review Mode Design

**Date:** 2026-05-14

## Goal

Capture the approved maintainer contract for `$www` so the packaged `ww-subagent-orchestrator` docs and future runtime checks use one narrow, consistent strict-review model.

## Approved Decisions

- `$www` is strict mode layered on top of `$ww`, not a separate orchestration system.
- Strict review applies only to persisted `design spec` and `implementation plan` artifacts.
- The strict loop is `self-review -> reviewer-review -> patching -> re-review`.
- A strict-review target passes only when the reviewer reports `no material findings`.
- Each target revision gets exactly one patch cycle.

## State Ownership

- Round-level intent lives in the working brief as `quality_mode: standard | strict`.
- The dispatch plan owns the live per-target gate in `strict_review`, including the active `mode`, `target`, `state`, and `cycle_count`.
- Durable per-target outcomes live in section review lane records keyed by `Review Target Ref`, so later rounds can see which artifact revision passed or blocked.

## Pass And Block Rules

- `passed` means the active strict-review target reached a reviewer result of `no material findings`.
- If material findings remain after the one allowed re-review, the target becomes `blocked`.
- A blocked target does not continue patching in the same target revision.
- A blocked target requires `Revise` or a later approved round or revision before strict review can continue on a new target revision.

## Guardrails

- `$ww` remains the standard path and does not inherit strict-review behavior unless the user invoked `$www`.
- Non-target artifacts do not carry strict-review headers or their own copied strict state.
- The contract does not allow a second patch cycle, subjective pass shortcuts, or artifact-local state that conflicts with the dispatch plan.

## Verification Expectations For The Companion Plan

The maintainer implementation plan should treat `$ww` and `$www` checks as acceptance scenarios only until a later execution round runs them against the active runtime surfaces.
