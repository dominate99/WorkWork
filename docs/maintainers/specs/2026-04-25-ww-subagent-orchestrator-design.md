# WW Subagent Orchestrator Design

**Date:** 2026-04-25

## Goal

Create a local skill triggered by `$ww` that estimates work first, chooses the right top-level orchestrator persona, builds a working brief, writes a tracked dispatch plan file, and then orchestrates persona-bound subagent workflows using Superpowers skills.

## Problem

Baseline behavior without this skill jumps too quickly from task request to ad hoc reviewer dispatch. It tends to:

- skip a formal estimation gate
- skip a working brief
- choose personas from obvious task keywords
- omit a tracked dispatch plan
- omit explicit Superpowers bindings
- blur reviewer findings with final human judgment

## Scope

This skill covers:

- task estimation triggered by `$ww`
- top-level orchestrator selection
- context-driven persona planning
- working brief generation
- subagent packet contracts
- file-backed dispatch planning
- stage-by-stage Superpowers binding
- reviewer and human judgment gates

This skill does not directly replace domain-specific implementation skills. It routes work to the right workflow and personas.

## Top-Level Routing

The skill must map requests into one of three orchestrator categories:

- `code/programming` -> `staff engineer orchestrator`
- `design/ads/product` -> `PM orchestrator`
- `video/creative` -> `creative director orchestrator`

The orchestrator selection is based on context and goal, not raw keywords alone.

## Required Stage Order

Every `$ww` run follows this sequence:

1. `estimation`
2. `working brief`
3. `orchestrator routing`
4. `dispatch approval`
5. `section reviewer`
6. `orchestrator synthesis`
7. `human judgment`

Hard rules:

- no `working brief` before `estimation_complete`
- no persona dispatch before `working_brief_ready`
- no subagent packet creation before `dispatch_decision: approved`
- every section requires a reviewer subagent
- reviewer output must return to the orchestrator before human judgment

## Working Brief

The working brief is the single source of truth for downstream routing and dispatch. It must capture:

- routing category
- orchestrator choice
- goal
- relevant context
- artifact type
- constraints
- risk lenses
- parallelism assessment
- blocking dependencies
- workstreams or sections
- recommended personas
- workflow bindings by stage
- dispatch recommendation
- dispatch decision state

## Persona System

Persona selection is context-driven. The orchestrator may use:

- built-in personas bundled with the skill
- project-defined personas from `docs/superpowers/personas/registry.yaml`

Selection rules:

- project personas override built-in personas when they clearly match
- every chosen persona must include a rationale grounded in the working brief
- reviewer personas and implementer personas must stay distinct
- language specialists are only added when language-specific reasoning materially matters

## Superpowers Binding

Each stage and each subagent packet must bind explicit Superpowers workflows. Typical bindings are:

- estimation and early framing -> `superpowers:brainstorming`
- planning -> `superpowers:writing-plans`
- independent workstreams -> `superpowers:dispatching-parallel-agents`
- implementation -> `superpowers:subagent-driven-development`
- code changes -> `superpowers:test-driven-development`
- debugging -> `superpowers:systematic-debugging`
- review -> `superpowers:requesting-code-review`
- closure -> `superpowers:verification-before-completion`

## Dispatch Plan File

Before any real dispatch begins, the orchestrator writes a tracked file at:

`docs/superpowers/dispatch-plans/YYYY-MM-DD-topic.md`

The file records:

- lifecycle state
- source context
- dispatch summary
- proposed subagents
- ordering and parallelism
- section review chains
- approval state
- dispatch log

The dispatch plan is a gate, not just a note.

## Pre-Dispatch Approval

Real dispatch only begins after the user reviews the dispatch plan and chooses exactly one option:

1. `Approve`
2. `Revise`
3. `Stop`

`Stop` ends the current dispatch round but preserves the working brief and dispatch plan file for later revision.

## Section Review Loop

Every section follows the same review loop:

1. orchestrator draft
2. reviewer findings only
3. orchestrator synthesis
4. human judgment

The orchestrator synthesis must output:

- section draft
- reviewer findings
- recommendation

## Dispatch Plan Format

The dispatch plan template must make gates executable, not merely descriptive. It needs:

- explicit gate checks
- a single approval state aligned with `Approve / Revise / Stop`
- per-section review and judgment loops
- a dispatch log that prevents launches before approval

## Deliverables

The local implementation should produce:

- the skill folder `skills/ww-subagent-orchestrator`
- a finished `SKILL.md`
- `agents/openai.yaml`
- reference files for working brief, persona registry, and subagent packet contracts
- an asset template for dispatch plans
- this design spec
- an implementation plan
