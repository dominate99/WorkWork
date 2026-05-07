# WW Subagent Orchestrator Implementation Plan

- Date: 2026-05-06
- Scope: upgrade `ww-subagent-orchestrator` so `$ww` can dispatch and manage subagents with explicit runtime policy
- Depends On: existing `SKILL.md`, `references/`, `assets/`, and `agents/` in this skill

## Objective

Implement the orchestrator upgrade in seven modules:

1. authoritative state model and schema compatibility
2. execution-bound packet contract
3. runtime-aware dispatch plan
4. scope-safe parallel dispatch rules
5. route-specific review pipelines
6. persona-to-runtime prompt binding
7. recovery and closure policy

## Module 0: Authoritative State Model And Schema Compatibility

### Goal

Define one canonical state machine and one compatibility policy before changing any artifact contracts.

### Changes

- update `SKILL.md` first with a normalized vocabulary table
- define the mapping between:
  - global `plan_state`
  - per-section `section_state`
  - per-section canonical `runtime_state`
  - subagent `return_status`
- mark `runtime_status` as deprecated terminology and do not add it as a persisted field
- add `schema_version` to:
  - working brief
  - dispatch plan
  - subagent packet
- define backward-read policy for pre-versioned artifacts
- define whether legacy artifacts are upgraded in place, wrapped, or rejected
- add `attempt_id` semantics and define active-vs-superseded attempt rules

### Done When

- every runtime state name has exactly one meaning
- controller can map a returned subagent status into plan updates without ambiguity
- old artifacts have a documented compatibility path

## Controller Semantics

This section is authoritative for controller behavior. If any later module uses a term inconsistently, this section wins.

### 1. Single Authoritative Runtime State Source

After launch, the single source of truth for orchestration progress is the active section `runtime_state`.

- `plan_state` is an aggregate round-level summary derived from section states
- `section_state` is the human workflow state for drafting, review, and acceptance
- `return_status` is a raw subagent event input, not stored as the canonical long-lived state
- `close_state` is an operational flag derived from `runtime_state`, not an independent progression state

Controller rule:

- controller reads `return_status`
- controller applies the state transition table
- controller writes the resulting canonical `runtime_state`
- controller derives `close_state`, section rollups, and top-level `plan_state` from that canonical state

### 2. Schema Migration Execution Point

Schema migration happens on artifact load, before dispatch decisions.

- pre-versioned artifacts are treated as `schema_version: 0`
- controller normalizes loaded artifacts into the current in-memory schema before any planning or launch logic
- controller writes only the current schema version back to disk
- one orchestration run may read legacy artifacts, but after normalization it may not operate on mixed in-memory schema versions
- if an artifact cannot be normalized, dispatch stops before approval or launch

Compatibility rule:

- working brief, dispatch plan, and packet schema versions must be mutually compatible within one run
- packet creation from a normalized plan always emits the current packet schema version
- plan revision does not silently downgrade artifact schema

### 2A. Working Brief Artifact Contract

Working briefs become first-class persisted artifacts before dispatch-plan creation.

Persistence rules:

- during raw estimation, a working brief may temporarily exist in-chat only
- before a dispatch plan is created, the working brief must be saved to disk
- any artifact participating in schema-version checks, revision comparisons, or reviewer targeting must be the persisted file-backed working brief

Artifact location and naming:

- canonical directory: `docs/superpowers/working-briefs/`
- canonical filename: `YYYY-MM-DD-topic-vN.md`
- `vN` increments only when the brief analysis materially changes

Required persisted fields:

- `schema_version`
- `brief_version`
- `brief_status`
- `topic_slug`
- `created_at`
- `updated_at`
- `derived_from_user_request`

Skill execution rules:

- load-time normalization operates only on persisted working brief artifacts
- if no persisted working brief exists yet, migration does not run and the skill may not advance to dispatch-plan creation
- `not created yet` is valid only in the user-facing document summary before dispatch-plan creation

### 3. Stable Execution Identity

The controller tracks four identity layers:

- `section_id`: stable logical workstream within one dispatch plan
- `execution_id`: stable logical execution record for one section-role pair across resume and retry
- `packet_id`: immutable instruction snapshot for one execution payload revision
- `attempt_id`: one launched agent attempt under one packet

Identity rules:

- resume of the same launched agent keeps the same `attempt_id`
- retry after `NEEDS_CONTEXT`, `BLOCKED`, or failed review rotates `attempt_id`
- regenerating instructions without changing the logical work item keeps `execution_id` and rotates `packet_id`
- changing plan revision or role ownership creates a new `execution_id`
- `active_attempt_id` is the only attempt allowed to advance the active `runtime_state`
- results from older attempts are stale unless `accepts_late_results: true` is explicitly set

### 4. Canonical Scope Normalization And Collision Checks

All scope declarations must normalize into canonical file-backed comparison units before parallel dispatch.

Allowed input scope types:

- `path_glob`
- `doc_section`
- `artifact_id`

Normalization rules:

- `path_glob` resolves to normalized repository-relative file paths
- `doc_section` resolves to `artifact_path + section_anchor`
- `artifact_id` resolves through a registry or declared mapping into exactly one canonical `artifact_path` target
- `artifact_id` registry lives at `docs/superpowers/artifact-registry.yaml` when present
- if no registry exists, the `artifact_id` mapping must be declared inline in the working brief or dispatch plan before launch
- if a scope cannot be expanded into canonical targets, the section is treated as non-parallel-safe

Collision rules:

- any overlap in normalized write targets blocks parallel worker dispatch
- write vs read overlap is allowed only for reviewer and explorer packets marked read-only
- cross-type collisions are checked after normalization, not by original scope label
- when a `doc_section` maps into a file covered by a `path_glob`, the overlap is treated as a collision unless the packet is read-only

Fallback rule:

- non-file-centric work must still resolve to a persisted artifact path plus optional section anchor before it is eligible for parallel safety checks
- aggregate multi-file work must use multiple `artifact_id` entries, explicit `path_glob` scopes, or multiple section records rather than one `artifact_id` with multiple canonical paths

### 4A. Artifact Registry Schema

When present, `docs/superpowers/artifact-registry.yaml` must use this schema shape:

```yaml
schema_version: 1
artifacts:
  <artifact_id>:
    artifact_kind: markdown | plan | brief | spec | code | other
    artifact_path: docs/superpowers/...
    section_anchors:
      default: overview
      <anchor_id>: <anchor_value>
    aliases:
      - <alternate_name>
    notes: optional freeform text
```

Field rules:

- `schema_version` is required at the top level
- `artifacts` is required and maps stable `artifact_id` keys to one artifact record each
- `artifact_id` must be ASCII, lowercase, and underscore-delimited
- `artifact_path` is required and must be repository-relative
- `artifact_kind` is required and is used for review-target and scope heuristics
- `section_anchors` is optional and provides stable anchor names for `doc_section` references
- `aliases` is optional and supports backward-compatible renames
- `notes` is optional and never used for dispatch logic

Resolution rules:

- resolve by exact `artifact_id` first
- if not found, resolve by unique alias
- if alias resolution is ambiguous, fail normalization
- one `artifact_id` maps to exactly one canonical `artifact_path`
- one registry record may expose multiple named `section_anchors`, but not multiple canonical paths

Fallback behavior:

- if `artifact-registry.yaml` is absent, inline mapping in the working brief or dispatch plan must provide the equivalent of `artifact_id`, `artifact_kind`, and `artifact_path`
- if inline mapping omits required fields, the section is non-parallel-safe and may not be used as a reviewer target

### 5. Immutable Review Targets For Spec-Light Tasks

Every reviewer packet must carry an immutable `review_target_ref`.

Required fields:

- `artifact_path`
- `artifact_kind`
- `artifact_revision`
- `schema_version`
- `section_anchor` when applicable
- `content_hash` for excerpt-backed review targets

Spec-light code task precedence remains:

1. implementation plan if present
2. dispatch section contract
3. working brief excerpt

Immutability rules:

- reviewer audits the exact `review_target_ref` captured at packet creation time
- if the underlying artifact changes after packet creation, the reviewer result is stale and must not be used without re-review
- working-brief-excerpt targets must include `content_hash`
- dispatch-section targets must include `section_id + plan revision`

Revision generation rules:

- working brief targets use `brief_version` as `artifact_revision`
- dispatch section targets use `plan_revision + section_id` as `artifact_revision`
- implementation plan or design spec targets use an explicit document version when available, otherwise the full-file `content_hash` becomes the `artifact_revision`
- excerpt-backed targets always use excerpt-level `content_hash` computed from the exact reviewed text slice
- for full-file targets without an explicit document version, set both `artifact_revision` and `content_hash` to the same full-file hash
- registry records do not store `artifact_revision` or `content_hash`; those are generated at packet creation time from the resolved artifact snapshot

## Module 1: Harden Packet Contract

### Goal

Make every approved section convertible into a deterministic subagent launch payload.

### Changes

- update `references/subagent-packet-contract.md`
- add `schema_version`
- add `execution_id`
- add `packet_id`
- add `attempt_id`
- add `execution_binding`
- add `write_scope[]` and `read_scope[]`
- add `expected_return_status[]`
- add `retry_policy`, `close_policy`, and `result_artifact_location`
- add `supersedes_attempt_id` and `accepts_late_results: false|true`
- document defaults for `worker`, `explorer`, and reviewer packets

### Done When

- packet contract can be mapped to `spawn_agent` inputs without controller guesswork
- reviewer packets are read-only by default
- packet identity survives retry, resume, and stale result handling

## Module 2: Add Runtime State To Dispatch Plan

### Goal

Turn the dispatch plan into the canonical runtime ledger after launch, not only a pre-launch approval document.

### Changes

- update `assets/dispatch-plan-template.md`
- add `schema_version`
- add per-section `runtime_state`
- add active pointers:
  - `active_execution_id`
  - `active_packet_id`
  - `active_agent_id`
  - `active_attempt_id`
- add per-section execution history records:
  - `execution_records[]`
  - `packet_records[]`
  - `attempt_records[]`
- keep summary fields:
  - `attempt_count`
  - `last_update_at`
  - `next_action`
- add `active_write_scope`, `result_summary`, `close_state`
- add `superseded_attempt_ids[]` and `stale_result_policy`
- normalize top-level dispatch log for launch, retry, and close events

### Done When

- plan can answer whether a section is queued, running, blocked, review-pending, complete, failed, or stopped
- plan can reconstruct in-flight state after interruption
- plan can distinguish current attempt results from stale retry results
- plan can reconstruct which logical execution and packet revision produced the active runtime state
- plan preserves prior implementer and reviewer packet history for the same section without overwriting lane identity
- `close_state` is stored only as a derived operational flag from canonical `runtime_state`

## Module 3: Enforce Parallelism Boundaries

### Goal

Prevent overlapping write work from being dispatched in parallel.

### Changes

- update `references/working-brief-template.md`
- add `schema_version`
- require `exclusive_write_scope`
- require `shared_read_scope`
- require `depends_on_sections`
- require `parallel_safe_with_sections`
- define canonical scope grammar:
  - `path_glob`
  - `doc_section`
  - `artifact_id`
- define collision rules for each scope type
- update `assets/dispatch-plan-template.md` to persist scope decisions
- update `SKILL.md` with dispatch gating rules

### Done When

- two worker packets can be checked for scope collision before launch
- read-only reviewers and explorers can still run in parallel safely
- collision checks do not depend on free-form scope descriptions

## Module 4: Split Review Pipeline By Route

### Goal

Align review strength with task category instead of using one generic reviewer policy.

### Changes

- update `SKILL.md`
- for `code/programming`, require:
  1. implementer
  2. spec reviewer
  3. code quality reviewer
  4. orchestrator synthesis
  5. human decision
- for spec-light code tasks, define default review target precedence:
  1. implementation plan if present
  2. dispatch section contract
  3. working brief excerpt
- for `design/ads/product`, keep one narrow reviewer lane plus orchestrator synthesis
- for `video/creative`, keep one editorial reviewer lane plus orchestrator synthesis
- update `references/subagent-packet-contract.md` with `review_target_ref`, `review_type`, `pass_condition`, and `reject_condition`
- require reviewer packets to declare which artifact level they are auditing

### Done When

- code routes cannot skip spec review before code quality review
- non-code routes avoid unnecessary code-style review overhead
- spec reviewer always has an explicit artifact contract, even for bugfixes

## Module 5: Bind Personas To Runtime Prompt Assets

### Goal

Make persona selection change actual subagent behavior.

### Changes

- update `references/persona-registry.md`
- add runtime binding fields such as `runtime_role`, `template`, and specialization metadata
- add packet fields for prompt assembly:
  - `persona_binding`
  - `template_path`
  - `prompt_inputs`
- add:
  - `agents/orchestrator-prompt.md`
  - `agents/worker-prompt.md`
  - `agents/reviewer-prompt.md`
  - `agents/explorer-prompt.md`
- update `agents/openai.yaml` so the skill advertises the upgraded execution model

### Done When

- selected persona maps to a concrete runtime template
- reviewer-only personas cannot be used as workers
- packet creation deterministically produces the final subagent prompt payload from persona binding plus template plus prompt inputs

## Module 6: Recovery And Closure Policy

### Goal

Define what the orchestrator does after a subagent returns `DONE`, `DONE_WITH_CONCERNS`, `NEEDS_CONTEXT`, `BLOCKED`, or `FAILED`.

### Changes

- update `SKILL.md`
- update `references/subagent-packet-contract.md`
- update `assets/dispatch-plan-template.md`
- add explicit `return_status -> runtime_state` transition table
- add explicit controller update procedure for launch, return, review, synthesis, human decision, retry, and close
- define retry rules
- define human escalation rules
- define closure timing for workers and reviewers
- define late-result reconciliation rules for superseded attempts

### Done When

- blocked packets have a documented next step
- idle agents are closed deliberately instead of being left ambiguous
- stale results from old attempts are ignored or merged by policy, not guesswork
- controller can deterministically translate every allowed `return_status` into the next canonical `runtime_state`

### Required Transition Table

The implementation must define and document this exact controller transition table:

| Event Type | Input Event | Current `runtime_state` | Next canonical `runtime_state` | Required follow-up |
|---|---|---|---|---|
| subagent return | `DONE` | `running` | `review-pending` or `complete` | send to next required reviewer, or mark complete if no further review applies |
| subagent return | `DONE_WITH_CONCERNS` | `running` | `review-pending` | persist concerns and require orchestrator synthesis before proceeding |
| subagent return | `NEEDS_CONTEXT` | `running` | `blocked` | record missing context, keep `execution_id`, rotate `attempt_id` only on re-launch |
| subagent return | `BLOCKED` | `running` | `blocked` | classify blocker and choose retry, revise, or human escalation |
| subagent return | `FAILED` | `running` | `failed` | close current attempt and require explicit recovery decision before new launch |
| reviewer outcome | `PASS` | `review-pending` | `review-pending` or `complete` | advance to next reviewer or synthesis, then complete if review lane is finished |
| reviewer outcome | `REJECT` | `review-pending` | `blocked` | persist findings, require orchestrator synthesis, and relaunch only through explicit retry or revise path |
| orchestrator event | `SYNTHESIS_COMPLETE` | `review-pending` | `review-pending` or `complete` | wait for human decision when required, otherwise close completed lane |
| human decision | `APPROVE` | `review-pending` | `complete` | persist decision and close when no next action remains |
| human decision | `REVISE` | `review-pending` or `blocked` | `blocked` | create revision task and preserve `execution_id` only if the logical work item is unchanged |
| human decision | `STOP` | `running`, `review-pending`, or `blocked` | `stopped` | record explicit user stop, close active work, and prevent relaunch unless planning is explicitly reopened |
| controller action | `RETRY` | `blocked` or `failed` | `running` | create a new `attempt_id`, preserve or rotate higher identities per Controller Semantics |

Additional rules:

- `review-pending` is the canonical post-worker state when another reviewer or synthesis step is still required
- `complete` is entered only after required review chain and orchestrator synthesis succeed
- `stopped` is a terminal user-directed state and must not be conflated with `failed`
- `close_state` becomes `closed` only after controller has persisted the terminal `runtime_state` and no next action remains

### Plan-State Aggregation Rules

Top-level `plan_state` remains a derived round-level summary and must be computed from section outcomes plus required-section criticality.

Required section metadata:

- each section must declare `required_for_goal: true|false`

Aggregation rules:

- if any `required_for_goal: true` section enters `stopped`, top-level `plan_state` becomes `stopped`
- if a non-required section enters `stopped` while other required sections remain active, top-level `plan_state` remains `dispatched`
- if all required sections are `complete` and only non-required sections are `stopped`, top-level `plan_state` becomes `completed`
- if any section is `running` or `review-pending`, top-level `plan_state` may not be `completed`
- `failed` and `stopped` remain distinct in rollups, logs, and recovery policy

### Controller Update Procedure

The skill implementation must encode the following deterministic procedure.

#### On Launch

1. Load and normalize persisted working brief and dispatch plan artifacts.
2. Verify schema compatibility and approval state.
3. Resolve scope declarations into canonical targets.
4. Build packet with `execution_id`, `packet_id`, `attempt_id`, and `review_target_ref` when applicable.
5. Assemble final prompt payload from:
   - selected persona binding
   - resolved runtime template
   - packet fields
   - workflow bindings
6. Persist `runtime_state: running`, `active_attempt_id`, launch timestamp, and write scope.

#### On Subagent Return

1. Validate that the result belongs to `active_attempt_id` or is explicitly allowed as a late result.
2. Read returned status and apply the transition table.
3. Persist canonical `runtime_state`.
4. Persist result summary, concerns, or blocker reason.
5. Derive `close_state`, section rollups, and top-level `plan_state`.

#### On Reviewer Return

1. Verify immutable `review_target_ref`.
2. Record findings against the reviewed artifact revision.
3. Apply `PASS` or `REJECT` transition.
4. Queue synthesis or revision follow-up as required.

#### On Orchestrator Synthesis

1. Summarize worker or reviewer output.
2. Persist synthesis note into the dispatch plan review record.
3. If human judgment is required, keep `runtime_state: review-pending`.
4. Otherwise advance by transition rule.

#### On Human `Approve`, `Revise`, or `Stop`

1. Record decision and timestamp.
2. Apply transition rule.
3. If `Revise`, create the required revision task and determine whether `execution_id` is preserved.
4. If `Stop`, freeze relaunch until planning is explicitly reopened.

#### On Retry

1. Confirm current state is retry-eligible.
2. Preserve or rotate identity layers according to Controller Semantics.
3. Create new `attempt_id`.
4. Re-assemble prompt payload with updated context.
5. Persist new `runtime_state: running`.

#### On Close

1. Confirm terminal `runtime_state` and no pending next action.
2. Set derived `close_state: closed`.
3. Record closure timestamp and final artifact references.
4. Do not leave dormant open agents without an explicit queued next step.

## Suggested Edit Order

1. `SKILL.md` state-machine and schema rules
2. `references/subagent-packet-contract.md`
3. `references/working-brief-template.md`
4. `assets/dispatch-plan-template.md`
5. `references/persona-registry.md`
6. `agents/openai.yaml`
7. new prompt assets under `agents/`

## Validation Pass

After document and template edits, validate with five dry-run scenarios:

1. code task with one implementer and two reviewers
2. product task with one drafter and one reviewer
3. blocked worker that requires context and one retry
4. stale completion arrives after a retry already became active
5. small bugfix with no formal design spec and dispatch-section-backed spec review

## Risks To Watch

- `SKILL.md` can drift from the contract docs if edited first
- dispatch plan can become too noisy if runtime state is not grouped
- persona binding can become decorative if prompt templates stay generic
- compatibility logic can become hand-wavy if schema versioning is not implemented in every artifact
- scope collision checks can still fail if teams bypass the canonical scope grammar

## Review Questions

The reviewer should specifically check:

1. whether module order is dependency-safe
2. whether any required runtime fields are still missing
3. whether any review lane is under-specified
4. whether the migration and compatibility policy is implementable
5. whether retry and stale-result handling are precise enough to automate
