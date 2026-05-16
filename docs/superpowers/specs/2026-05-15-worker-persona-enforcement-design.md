# Worker Persona Enforcement Design

Date: 2026-05-15
Status: Approved for spec review
Scope: First-layer improvement for `ww-subagent-orchestrator` worker persona behavior

## Problem

The current `ww-subagent-orchestrator` flow can select a project or built-in persona, record it in the working brief and dispatch plan, and carry it into the packet contract. But for `worker` launches, persona is still too descriptive and not sufficiently behavioral.

Today the system records:

- persona identity
- persona rationale
- role binding

But it does not strongly encode what that persona must prioritize during implementation. As a result, a selected worker persona can behave like a generic implementer with a label attached, instead of a constrained implementation specialist.

## Goal

Make worker persona selection materially affect implementation behavior.

The first-layer goal is:

1. persona must strongly shape worker thinking and risk ordering
2. persona may softly influence workflow and tool choices
3. persona may softly influence output style and delivery emphasis

This layer applies only to `worker` behavior. It does not yet change `reviewer` or `explorer` behavior.

## Non-Goals

- do not redesign persona selection itself
- do not expand strict runtime controls to `reviewer` or `explorer`
- do not introduce a large new execution-rules schema
- do not convert persona guidance into a long checklist or output template

## Design

### 1. Add implementation principles to worker-capable personas

Both persona sources must define executable implementation guidance for any persona that may be used as a `worker`:

- project registry: `docs/superpowers/personas/registry.yaml`
- built-in registry: `references/persona-registry.md`

Add a new field:

- `implementation_principles`

Rules:

- exactly 2 entries
- entry 1 is a hard implementation rule
- entry 2 is a soft implementation principle
- the entries are decision principles, not strengths, not checklists, and not writing-style tips

Examples of the intended shape:

- hard rule: prefer boundary safety and correctness over implementation speed
- soft rule: when tradeoffs are close, bias toward explicitness and maintainability

### 2. Treat missing principles as a worker-launch contract failure

If a persona can be selected for `worker` use but lacks valid `implementation_principles`, the orchestrator must not launch that persona as a worker packet.

Allowed outcomes:

- choose a different valid worker persona
- treat the persona as descriptive only and do not bind it to worker execution
- revise the persona registry before dispatch

This prevents worker persona behavior from degrading back into decorative metadata.

### 3. Carry implementation principles into the packet contract

The subagent packet contract must preserve the selected persona's executable principles for worker launches.

This can be done either by:

- adding `implementation_principles` as an explicit packet field
- or requiring it inside the packet's persona binding structure

The key requirement is behavioral fidelity: the worker launch payload must contain the selected persona's two implementation principles in a form the runtime prompt can consume directly.

For this first layer, explicit carriage is required for worker packets only.

### 4. Make worker prompt consume principles before implementation choices

The worker runtime prompt must not treat persona as context flavor. It must direct the worker to apply the persona's implementation principles before choosing an approach.

Expected behavioral ordering:

1. apply the hard implementation rule first when making implementation decisions
2. use the soft principle to break close tradeoffs
3. only then choose workflows, tools, and output emphasis

This preserves the desired hierarchy:

- strong effect on thinking and risk ordering
- softer effect on workflow and tools
- softest effect on output style

## Required Contract Changes

### Persona registries

For worker-capable personas:

- require `implementation_principles`
- require exactly 2 entries
- require the first to be treated as hard and the second as soft

For reviewer-only personas:

- `implementation_principles` are not required in this first layer

### Packet contract

For worker packets:

- require carriage of persona implementation principles
- require those principles to be sourced from the selected persona definition

For reviewer and explorer packets:

- no new requirement in this layer

### Worker prompt

Require the prompt to instruct the worker that:

- persona principles are implementation constraints, not optional flavor
- the hard rule governs primary implementation choices
- the soft rule governs default tradeoff posture when the hard rule does not fully decide the choice

## Validation Rules

The first layer should be considered complete only if all of the following are true:

1. every worker-capable persona in both registries has exactly 2 `implementation_principles`
2. worker packet assembly cannot silently omit those principles
3. worker prompt language explicitly consumes the principles before workflow or output decisions
4. reviewer and explorer contracts remain unchanged in this layer

## Open Follow-Up

Second-layer expansion may later extend persona enforcement to:

- reviewer personas
- explorer personas
- richer persona-specific workflow shaping

That future work is intentionally deferred so the current change can establish one clean path first: project persona definition -> packet contract -> worker runtime behavior.
