# Case-Based Artifact Layout Implementation Plan

Goal: move WorkWork from a type-based artifact storage layout toward a case-based and round-based layout without introducing split write authority, validator drift, or heavier-than-necessary workflow artifacts.

Architecture: migrate in phases. First define the case and round storage model and the authority rules. Then update the workflow contract and default path generation for new rounds. Only after canonical paths are stable should validators and compatibility logic be expanded.

Review focus: prevent storage redesign from becoming a cosmetic folder shuffle. Review should specifically check canonical path authority, migration safety, and the separation between required runtime-state artifacts and optional explanatory artifacts.

Tech stack: Markdown workflow contracts, repo-local Python validators, PowerShell, `rg`

---

- [ ] Freeze the target storage model in contract language
Document the target case and round model before changing generators or examples.

Primary targets:
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - supporting design docs under `docs/superpowers/specs/`

Define:
  - the `case` folder
  - the `round` folder
  - `case_slug` and `round_slug` derivation rules
  - `case_root` and `round_root` canonical path formulas
  - required vs optional artifacts inside a round
  - canonical default filenames

- [ ] Define authority rules for migration phases
Write explicit rules for what is canonical during each phase.

The authority rules must answer:
  - where new rounds write in each phase
  - whether legacy type-based directories remain readable
  - whether any dual-write behavior is allowed
  - how validators and operators identify the canonical location
  - how the system determines when a round stays inside an existing case versus when it starts a new case

Guardrail:
  - fallback read compatibility may exist
  - dual active write authority must not exist

- [ ] Introduce case-based path templates for new rounds
Once the contract is explicit, update the path templates used by `$ww` and `$www` for new artifacts.

Primary targets:
  - `SKILL.md`
  - any referenced templates or path examples

The first path shift should cover:
  - `working-brief.md`
  - `dispatch-plan.md`
  - `design-spec.md`
  - `implementation-plan.md`

Do not add optional explanatory artifacts as required outputs in this step.

- [ ] Decide the first compatibility bridge
Choose the smallest safe compatibility model for old artifacts.

Recommended posture:
  - old artifacts remain in place
  - new rounds write only to case-based locations
  - explicit path references continue to work
  - validators gain read awareness only where needed

Avoid:
  - copying historical artifacts into two active hierarchies
  - requiring a bulk migration before new rounds can start

- [ ] Update maintainer and user guidance
Once canonical paths change, update the top-level docs coherently.

Primary targets:
  - `README.md`
  - any maintainer notes or examples that mention `docs/superpowers/working-briefs/`, `dispatch-plans/`, `specs/`, or `plans/`

The docs should explain:
  - what a case is
  - what a round is
  - where to look for the latest round
  - which artifacts are required vs optional

- [ ] Update validators in a later bounded round
Do not mix storage-model design with validator rollout unless a minimal check is absolutely required.

Validator work should come after canonical path rules are stable.

Expected validator phases:
  - phase 1: validate the new path expectations in contract text
  - phase 2: validate generated artifact references if generators change
  - phase 3: optionally validate case-folder structural integrity

Do not add validators for ambiguous transition semantics.

- [ ] Keep optional explanatory artifacts optional
Once case folders make colocated notes easier, explicitly resist turning them into mandatory workflow gates.

Examples that should remain optional unless later approved:
  - `persona-selection-rationale.md`
  - `review-notes.md`
  - similar log-like or audit-supporting files

The required control surfaces should stay minimal:
  - `working-brief.md`
  - `dispatch-plan.md`
  - strict-review targets only when the round requires them

- [ ] Run migration in a narrow first implementation pilot
Do not convert every existing round at once.

Recommended pilot:
  - switch new rounds to case-based paths for one bounded workstream
  - leave legacy artifacts readable in their current locations
  - confirm retrieval, review, and validator behavior before broader rollout

- [ ] Run staged review checkpoints
Use bounded review after each migration phase instead of one large rollout review.

Recommended checkpoints:
  - after contract path model changes
  - after the first new-round path template changes
  - after README and example updates
  - after validator additions
  - after any legacy compatibility bridge is implemented

- [ ] Run final verification for each implementation round
For each round that changes contracts, paths, or validators, verify:
  - targeted `rg` scans for all path references
  - repo validator runs when validator surfaces change
  - `git diff --stat` to confirm the migration stayed scoped

Recommended checks for the first implementation round:

```powershell
rg -n "docs/superpowers/working-briefs|docs/superpowers/dispatch-plans|docs/superpowers/specs|docs/superpowers/plans|docs/cases" `
  "plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md" `
  "README.md" `
  "docs/superpowers/**/*"
```

```powershell
git diff --stat
```

## Recommended Execution Sequence

1. design and authority model
2. workflow-contract path update
3. new-round path generation update
4. README and maintainer guidance update
5. compatibility bridge where needed
6. validator rollout
7. optional historical migration only if still justified

## Success Criteria

This plan succeeds if implementation later produces:

- one canonical case folder per workstream
- one canonical round folder per `$ww` or `$www` cycle
- no dual active write authority during migration
- required and optional artifacts clearly separated
- easier review of historical rounds without reconstructing context from multiple top-level type folders
