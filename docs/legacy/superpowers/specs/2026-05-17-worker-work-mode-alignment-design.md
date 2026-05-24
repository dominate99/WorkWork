# Worker Work-Mode Alignment Design

Date: 2026-05-17
Status: Drafted for `$ww` approval
Scope: Second-layer improvement for `ww-subagent-orchestrator` worker behavior

## Problem

The current worker persona layer now carries `implementation_principles`, but worker behavior is still missing a stable execution-order contract. A specialist persona can influence tradeoffs inside an implementation path, yet the orchestrator still lacks a first-class way to decide whether a worker should validate first, plan first, iterate first, or stay conservative.

That gap creates two failures:

- worker behavior still degrades toward a generic implementer when task shape changes
- the working brief, dispatch plan, packet, and worker prompt do not share one aligned execution-order contract

## Goal

Make worker execution behavior depend on both:

1. the selected specialist persona
2. an automatically chosen `work_mode` that reflects task structure first and goal tuning second

## Non-Goals

- do not redesign top-level orchestrator routing
- do not make `goal_tuning` a replacement for `work_mode`
- do not introduce a second task-type field that overlaps with `task_mode`
- do not extend this layer to reviewer or explorer execution behavior yet

## Design

### 1. Split worker behavior into four ordered control layers

Worker execution should follow this fixed order:

1. `user_constraints`
2. `work_mode`
3. `persona`
4. `goal_tuning`

Interpretation:

- user constraints define hard boundaries, prohibitions, and delivery expectations
- `work_mode` determines default execution sequence
- persona `implementation_principles` shape professional judgment inside that sequence
- `goal_tuning` only softens or sharpens emphasis

### 2. Add four canonical worker work modes

The worker layer should recognize these modes:

- `plan-first`
- `validate-first`
- `iterate-first`
- `conservative-first`

Behavioral intent:

- `plan-first`: break down the work and confirm execution shape before implementation
- `validate-first`: verify the current state, intended change, or risk before implementation
- `iterate-first`: establish a minimal working path first, then expand safely
- `conservative-first`: prefer the smallest closed-scope change and avoid spread

### 3. Route work mode from task structure before goal tuning

Default routing should be structure-driven:

- single-file coding -> `conservative-first`
- multi-file coding -> `iterate-first`
- feature-level coding -> `plan-first`
- code modification or plan modification -> `validate-first`

When a task spans multiple shapes:

- choose from the primary artifact first
- break ties by the highest-risk decision area
- let `goal_tuning` adjust posture only after the structure default is chosen

`goal_tuning` may bias execution toward speed, safety, or validation, but it must not replace the structure-driven default.

### 4. Align the contract surfaces around one worker-mode chain

The active runtime surfaces must align as one chain:

- the packaged `SKILL.md` records the canonical workflow contract at the skill level
- working brief recommends worker mode
- dispatch plan decides and records the effective worker mode
- packet freezes one execution snapshot of that mode
- worker prompt consumes packet state and must not re-derive worker mode from the brief

This is the key anti-drift rule. `work_mode` is only useful if every later layer consumes the earlier layer instead of reinterpreting it. `SKILL.md` does not need to duplicate every field name from the lower-level templates, but it must describe the worker-mode layering and the authority chain so the packaged skill contract stays truthful.

### 5. Add mode-change auditability

If execution reveals that the original `work_mode` no longer fits, the controller may change it only after recording the new evidence in the dispatch plan. A packet must never silently mutate in place.

Required change chain:

1. update dispatch-plan section state
2. record the old mode, new mode, evidence, and approval source
3. issue a new packet snapshot
4. relaunch with a new attempt when needed

## Required Contract Changes

### Working Brief

Add section-level recommendation fields:

- `recommended_worker_mode_by_section`
- `worker_mode_reasoning_by_section`
- `goal_tuning_by_section`
- `constraint_override_notes_by_section`

The working brief remains a recommendation layer only.

### Dispatch Plan

Add section-level decision and runtime-tracking fields:

- `Planned Worker Mode`
- `Worker Mode Rationale`
- `Goal Tuning`
- `Constraint Interaction Rule`
- `Active Worker Mode`
- `Mode Change History`

The dispatch plan becomes the section-level authority for the effective mode before packet creation.

### Subagent Packet Contract

For worker packets, require:

- `work_mode`
- `work_mode_rationale`
- `goal_tuning`
- `constraint_precedence_note`

This keeps the launch payload explicit and prevents worker-mode drift from being hidden inside free-text prompts.

### Worker Prompt

The worker prompt must consume packet state in this order:

1. constraints, scope, and non-goals
2. `work_mode`
3. persona `implementation_principles`
4. `goal_tuning`

### Packaged Skill Contract

Update `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md` so the canonical skill contract reflects:

- the worker execution order: `user constraints -> work_mode -> persona -> goal_tuning`
- the authority chain: working brief recommends, dispatch plan decides, packet freezes, worker prompt consumes
- the separation between `task_mode` and `work_mode`

## Validation Rules

This layer is complete only if:

1. the working brief can recommend worker mode per section without acting as final authority
2. the dispatch plan records one effective worker mode per section and logs mode changes
3. worker packets carry one explicit `work_mode` snapshot
4. the worker prompt applies `work_mode` before persona principles
5. `task_mode` remains separate from `work_mode`
6. `goal_tuning` can adjust emphasis but cannot replace the chosen `work_mode`
7. the packaged `SKILL.md` reflects the new worker-mode chain without drifting away from the lower-level contract surfaces

## Open Follow-Up

Later work may extend this model to:

- reviewer review modes
- explorer investigation modes
- stronger project-persona registries for non-engineering worker lanes
