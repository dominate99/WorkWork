# Case-Based Artifact Layout Design

Date: 2026-05-22
Status: Approved for design output
Scope: Define a case-based artifact storage model for `$ww` and `$www` that groups one case's related artifacts together without creating split authority during migration.

## Goal

Replace the current "document type first" mental model with a "case first, round second" model.

The target is not just cleaner folders. The target is:

- one coherent home for all artifacts that belong to the same case
- clearer round-level auditability
- less context scattering across `working-briefs/`, `dispatch-plans/`, `specs/`, and `plans/`
- a migration story that preserves one canonical path model at every phase

## Diagnosis

The current structure is type-oriented:

- `docs/superpowers/working-briefs/`
- `docs/superpowers/dispatch-plans/`
- `docs/superpowers/specs/`
- `docs/superpowers/plans/`

That works for simple persistence, but it weakens case continuity.

For one real `$ww` effort, the operator must reconstruct context across multiple directories:

- the working brief lives in one folder
- the dispatch plan lives in another
- the design spec and implementation plan live elsewhere
- optional artifacts such as rationale notes or review notes want to live somewhere too

As the number of rounds grows, this becomes an information-retrieval problem rather than just a naming problem.

## Core Principle

**The canonical storage unit should be the case, not the artifact type.**

Within a case, the next unit should be the round.

That yields a two-level model:

1. `case`
   - the long-lived workstream or problem area
2. `round`
   - one bounded `$ww` or `$www` execution cycle inside that case

Artifact types should become files inside a round, not top-level directory drivers.

## Target Model

Use this layout:

```text
docs/superpowers/cases/<case-slug>/
  case.md
  rounds/
    <round-slug>/
      working-brief.md
      dispatch-plan.md
      design-spec.md
      implementation-plan.md
      persona-selection-rationale.md
      review-notes.md
```

## Case And Round Identity

The storage model needs deterministic identity rules, not just folders.

### `case_slug`

`case_slug` identifies the long-lived workstream.

Rules:

- derive it from the enduring topic, not the momentary round action
- keep it stable across related rounds
- create a new case only when the underlying workstream materially changes

Examples:

- `persona-enrichment`
- `case-based-artifact-layout`

### `round_slug`

`round_slug` identifies one bounded `$ww` or `$www` cycle inside a case.

Rules:

- derive it from the current round purpose
- include the date prefix to preserve chronology
- revisions within the same round update the same round folder instead of creating a new case

Examples:

- `2026-05-22-layout-pilot`
- `2026-05-22-runtime-selection-validator`

### Derived roots

The canonical path roots should be:

- `case_root = docs/superpowers/cases/<case-slug>/`
- `round_root = docs/superpowers/cases/<case-slug>/rounds/<round-slug>/`

These roots should be carried explicitly by generated round artifacts so producers, validators, and operators do not have to re-derive them ad hoc.

### `case` level

The case folder is the durable home for one workstream.

Its job is to answer:

- what this case is
- why it exists
- which rounds belong to it
- what the current status is

Recommended required file:

- `case.md`

Recommended content:

- case goal
- current status
- active or latest round
- important cross-round references

### `round` level

A round folder is the execution unit for one `$ww` or `$www` cycle.

Its job is to contain the artifacts needed to understand that cycle without leaving the folder.

Recommended required files by round type:

- `working-brief.md`
- `dispatch-plan.md`

Conditionally required:

- `design-spec.md`
- `implementation-plan.md`

Optional explanatory artifacts:

- `persona-selection-rationale.md`
- `review-notes.md`
- other narrow log-like artifacts

## Required vs Optional Artifacts

This distinction must stay explicit.

### Required runtime-state or control artifacts

These remain the authoritative workflow artifacts for a round:

- `working-brief.md`
- `dispatch-plan.md`

For strict design/planning rounds, these may also be required:

- `design-spec.md`
- `implementation-plan.md`

### Optional explanatory artifacts

These may exist to improve auditability or user visibility, but they are not dispatch gates by default:

- `persona-selection-rationale.md`
- `review-notes.md`
- similar explanatory or log-like artifacts

This preserves a key boundary:

**better observability should not automatically become more workflow weight**

## Authority Model

This is the most important design requirement.

During every migration phase, there must be one canonical write-path model for each artifact class.

Not:

- old paths for some producers
- case paths for some producers
- validators guessing both

Instead:

- one canonical model per phase
- one documented compatibility rule
- one resolver story

### Authority rule

At any given phase:

- producers, validators, and human operators must all agree on the same canonical location model
- fallback lookup may exist temporarily
- fallback lookup must not imply dual write authority

## Migration Strategy

Migrate in phases.

### Phase A: Design-only

Define the target case/round model and compatibility posture.

No runtime contract path changes yet.

### Phase B: Introduce case-based canonical paths for new rounds

New `$ww` and `$www` rounds write to case-based paths.

During this phase:

- new writes use case-based paths only
- old type-based artifacts remain readable as legacy history
- any resolver or validator compatibility support is read-only for legacy artifacts

This is the preferred migration shape because it preserves single write authority.

The default write rule in this phase should be:

- new working briefs write to `<round_root>/working-brief.md`
- new dispatch plans write to `<round_root>/dispatch-plan.md`
- new design specs write to `<round_root>/design-spec.md`
- new implementation plans write to `<round_root>/implementation-plan.md`

### Phase C: Bridge references and tooling

Update:

- `SKILL.md`
- `README.md`
- artifact resolution rules
- validators
- any path examples or generated references

This phase aligns all producers and checkers with the new canonical model.

### Phase D: Legacy directory retirement

Once new rounds no longer write to the old type-based structure:

- keep legacy directories for historical reads only, or
- replace them with clear index or migration notes

Do not keep both as active write targets.

## Compatibility Rules

The design should adopt these compatibility rules:

1. new rounds should not dual-write to both path models
2. validators should tolerate legacy history only through explicit compatibility logic
3. examples in docs must switch in one coherent round, not piecemeal
4. optional explanatory artifacts should not be required just because the case folder makes them easy to add

## Naming Model

Use stable slugs.

### Case slug

Represents the long-lived workstream.

Examples:

- `persona-enrichment`
- `case-based-artifact-layout`

### Round slug

Represents one bounded cycle inside the case.

Examples:

- `2026-05-22-runtime-selection-validator`
- `2026-05-22-layout-pilot`

This keeps chronology visible while preserving case continuity.

## Artifact Resolution Implications

The current artifact model already uses:

- explicit `artifact_path`
- optional `section_anchor`

That is compatible with case-based storage because explicit paths still work.

The bigger change is not resolution syntax. The bigger change is default write location and canonical path expectation.

So the migration should prefer:

- keeping explicit path references valid
- changing where new artifacts are created
- then updating default examples and generator behavior

## What Not To Do

### 1. Do not keep dual active write locations indefinitely

That creates split authority and guarantees drift.

### 2. Do not collapse case and round into one folder

A case should survive multiple rounds. A round should stay bounded.

### 3. Do not treat optional logs as mandatory control surfaces

That would turn observability into process inflation.

### 4. Do not migrate every artifact class in one unbounded round

Path, tooling, validator, and doc changes should move in staged phases.

## Recommended Next Move

The next implementation round should not migrate the repo all at once.

It should:

1. define the canonical case and round path templates in the workflow contract
2. define the compatibility rule for legacy type-based artifacts
3. update one narrow set of generated artifact defaults first
4. only then update validators and examples

## Success Criteria

This design succeeds if a future implementation yields:

- one obvious folder for one case
- one obvious folder for each round inside that case
- required artifacts and optional artifacts clearly separated by role, not by top-level directory
- no dual-authority write model during migration
- a simpler recovery path for users reviewing historical `$ww` and `$www` work
