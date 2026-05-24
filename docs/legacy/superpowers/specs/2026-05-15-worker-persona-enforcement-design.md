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
- built-in persona data file: `references/built-in-personas.yaml`

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

`references/persona-registry.md` remains the rules layer. It should continue to define:

- required persona fields
- selection rules
- prompt-binding rules

It should not become the storage location for concrete built-in persona records. Built-in persona records must live in the new dedicated data file so the design stays cleanly split between:

- rules layer
- data-record layer

The built-in persona data file must use the same top-level schema shape as the project registry:

```yaml
personas:
  - id: ...
```

This keeps project personas and built-in personas structurally compatible and avoids two parallel data formats for the same concept.

### 2. Filter worker candidates before selection

A persona must pass implementation-principles completeness checks before it can enter the `worker` selection set.

This first layer should not model the problem as:

- selected first, then rejected later
- kept as descriptive-only metadata after worker selection

Instead, the contract should require pre-selection filtering:

- any persona intended for `worker` use must already have valid `implementation_principles`
- a persona that fails this check must not enter the `worker` candidate set
- the orchestrator must choose from valid worker candidates only

This prevents worker persona behavior from degrading back into decorative metadata and keeps the contract failure at the correct stage: before worker selection, not after packet assembly.

### 3. Carry implementation principles into the packet contract

The subagent packet contract must preserve the selected persona's executable principles for worker launches.

For this first layer, the carriage location must be fixed and canonical:

- add `implementation_principles` as an explicit top-level packet field
- place it alongside:
  - `subagent_persona`
  - `persona_rationale`
  - `persona_binding`
- do not store it only inside `persona_binding`

Rationale:

- `persona_binding` is runtime binding metadata
- `implementation_principles` are execution-contract content
- mixing them would blur binding structure and behavioral constraints

The key requirement is behavioral fidelity: the worker launch payload must contain the selected persona's two implementation principles in a direct, canonical form the runtime prompt can consume.

For this first layer, explicit top-level carriage is required for worker packets only.

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
- require completeness before the persona may enter the `worker` selection set

For reviewer-only personas:

- `implementation_principles` are not required in this first layer

### Worker-capable persona definition

For this first layer, `worker-capable persona` means:

- a persona with `review_only: false`
- and `role_type` not equal to `orchestrator`

Implementation-level exclusions:

- `review_only: true` personas must not enter the `worker` selection set
- `role_type: orchestrator` personas are not worker-capable
- this first layer primarily targets specialist or other implementation-facing personas that may legitimately execute owned write work

### Packet contract

For worker packets:

- require carriage of persona implementation principles
- require those principles to be sourced from the selected persona definition
- require the carriage location to be one canonical top-level field: `implementation_principles`

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
2. worker candidate filtering blocks any persona that lacks valid `implementation_principles`
3. worker packet assembly cannot silently omit those principles and always stores them in the canonical top-level field
4. worker prompt language explicitly consumes the principles before workflow or output decisions
5. reviewer and explorer contracts remain unchanged in this layer

## Open Follow-Up

Second-layer expansion may later extend persona enforcement to:

- reviewer personas
- explorer personas
- richer persona-specific workflow shaping

That future work is intentionally deferred so the current change can establish one clean path first: project persona definition -> packet contract -> worker runtime behavior.
