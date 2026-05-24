# Persona Enrichment Strategy Design

Date: 2026-05-19
Status: Approved for strategy output
Scope: Strengthen the WorkWork persona system so personas materially improve decision quality, execution quality, and taste instead of merely expanding catalog size.

## Goal

Define how to enrich personas so the system becomes meaningfully stronger.

The target is not "more personas." The target is:

- sharper judgment
- better routing
- stronger taste
- cleaner escalation
- more predictable collaboration across orchestrator, worker, reviewer, and explorer roles

## Diagnosis

The current system already does several important things well:

- it separates `persona` from `runtime_role`
- it separates `worker work_mode` from persona
- it keeps `reviewer` and `explorer` behavior constrained by role prompts
- it uses a registry plus packet model instead of ad hoc free-text persona names

But the current persona layer is still relatively shallow.

Most persona records answer:

- what domain this persona covers
- what it is strong at
- when it should be used

That is helpful, but not enough to make personas feel like stronger operators.

What is still under-modeled:

- how the persona decides
- what quality bar it defends
- what tradeoffs it will reject
- what kinds of mistakes it notices first
- when it escalates rather than "powering through"
- what kind of collaboration posture it creates for the rest of the system

Without those layers, personas risk becoming routing labels with slightly different bios.

## Core Principle

The highest-leverage move is:

**make each persona more opinionated in judgment, not more verbose in description**

If a persona sounds richer but does not change what gets noticed, rejected, escalated, simplified, or protected, it is theater.

The system should prefer:

- fewer personas
- clearer differences
- stronger defaults
- explicit tradeoff posture

over:

- many overlapping personas
- prose-heavy bios
- keyword-level routing
- vague "good at everything" specialists

## Design Model

Keep the current 3-layer separation:

1. `runtime_role`
   - worker
   - reviewer
   - explorer
   - orchestrator
2. `persona`
   - the professional viewpoint
3. `role prompt`
   - the behavioral contract for that role

Do not collapse these.

Instead, enrich the `persona` layer so it contributes more meaningful structure to each role.

## What To Add To Personas

The most valuable enrichment is not personality flavor text. It is operational judgment.

Add these concept layers to persona records over time:

### 1. `decision_style`

Examples:

- simplify-first
- risk-first
- speed-first
- systems-first
- customer-empathy-first

This tells the system how the persona resolves ambiguity before detailed instructions arrive.

### 2. `quality_bar`

Examples:

- prototype quality
- production quality
- editorial quality
- platform quality
- security-critical quality

This defines what "good enough" means for that persona.

### 3. `tradeoff_bias`

Examples:

- correctness over speed
- clarity over cleverness
- user trust over feature breadth
- coherence over optionality

This makes persona differences visible in real decisions.

### 4. `failure_modes_to_watch`

Examples:

- over-engineering
- hidden coupling
- weak narrative
- security drift
- scope bloat

This defines what the persona notices early.

### 5. `escalation_triggers`

Examples:

- unclear product intent
- integrity or security ambiguity
- cross-team architectural impact
- irreversible UX complexity

This makes escalation behavior intentional instead of personality-dependent.

### 6. `collaboration_posture`

Examples:

- directive synthesizer
- skeptical reviewer
- exploratory investigator
- hands-on builder
- editorial finisher

This improves how personas work together, not just how they work alone.

### 7. `taste_criteria`

This is the most Jobs-like missing piece.

Examples:

- remove anything the user cannot feel
- prefer one coherent path over many average paths
- reject complexity that exists only to satisfy internal convenience
- make the important thing obvious and the rest disappear

This gives the system a stronger bar for "why this is good," not just "why this is valid."

## What Not To Do

Avoid these anti-patterns:

### 1. Do not equate enrichment with count growth

If every new nuance becomes a new persona, routing quality will collapse.

### 2. Do not write personas like fiction characters

Style can help, but bios are not the product. Judgment is the product.

### 3. Do not duplicate role behavior inside persona records

`reviewer` and `explorer` constraints should stay in role prompts and packet contracts.

### 4. Do not let personas become generic super-experts

A persona that is "excellent at everything" adds no routing value.

### 5. Do not enrich only worker personas

Reviewer, explorer, and orchestrator personas all benefit from stronger decision structure, just in different ways.

## High-Leverage Enrichment Order

If prioritizing impact, enrich personas in this order:

### 1. Orchestrator personas

This is the highest leverage because orchestrators decide:

- decomposition
- routing
- escalation
- synthesis
- when to stop

Stronger orchestrator personas will improve the whole system more than adding niche workers first.

### 2. Reviewer personas

Reviewer personas should become more distinct in what they reject and what they consider material.

Today they already have behavioral constraints. The next gain is sharper judgment criteria.

### 3. Worker personas

Worker personas are already improving through `implementation_principles` and `work_mode`.

The next step is not more worker personas first; it is making existing ones more different in quality bar and tradeoff posture.

### 4. Explorer personas

Explorer personas matter, but they are lower leverage until the system uses them more heavily for evidence-gathering and ambiguity reduction.

## Strategic Recommendation

The strongest move is a 2-step strategy:

### Step 1. Deepen the persona model before adding many new personas

Enrich the schema and selection logic so personas carry stronger judgment structure.

### Step 2. Add only a small number of high-contrast personas

After the model is richer, add personas that create meaningful separation, for example:

- a simplifier/editor persona
- a systems-integrity persona
- a customer-empathy product persona
- a narrative/taste creative persona

The point is contrast, not coverage count.

## Jobs-Like Standard

If evaluating this through a Jobs-style lens, the test is:

- does this make the system more opinionated?
- does it make weak options easier to kill?
- does it make coherence stronger?
- does it make complexity less acceptable?
- does it increase the chance of one excellent answer over five average ones?

If not, it is probably persona decoration, not persona enrichment.

## Recommended Next Implementation Track

If the user wants execution next, the best sequence is:

1. extend persona schema with judgment-oriented fields
2. define enrichment rules separately from current required fields
3. enrich orchestrator personas first
4. enrich reviewer personas second
5. update packet and selection logic only after the model is stable
6. add validator coverage for the new persona fields once the runtime meaning is decided

## Phase 1 Contract Decisions

Phase 1 should convert the strategy into a stable contract without starting registry rollout or runtime adoption.

The phase 1 decisions are:

- keep the current required persona fields unchanged
- add the new judgment-oriented fields as optional enrichment fields
- keep current persona records valid when the new fields are absent
- keep `implementation_principles` as the worker-only execution field
- keep reviewer and explorer constraints in role prompts and packet contracts
- keep worker `work_mode` separate from persona enrichment
- defer packet, prompt, validator, and `SKILL.md` runtime-adoption changes to later approved rounds

The optional enrichment field set is:

- `decision_style`
- `quality_bar`
- `tradeoff_bias`
- `failure_modes_to_watch`
- `escalation_triggers`
- `collaboration_posture`
- `taste_criteria`

These fields should be defined as:

- judgment-oriented
- additive
- optional
- non-theatrical
- distinct from runtime-role behavior

## Phase 1 Migration Rules

Phase 1 should also define a rollout posture before any pilot enrichment begins.

The migration rules should be:

- do not reject current persona records for lacking optional enrichment fields
- during partial adoption, selection still relies on required fields first
- optional enrichment fields may strengthen persona rationale, but they do not become hard eligibility gates yet
- enrich existing personas before adding many new personas
- prioritize rollout in this order:
  - orchestrator personas
  - reviewer personas
  - worker personas
  - explorer personas
- if a field meaning is unclear for a given persona, omit it instead of writing vague filler

## Phase 1 Exit Criteria

Phase 1 is complete only if:

- `persona-registry.md` defines the optional enrichment fields and compatibility boundary clearly
- the design spec records that the fields are additive and non-required
- migration rules are explicit enough to guide later persona pilots
- no runtime contract surface was changed prematurely

## Success Criteria

This strategy is successful if a future enriched persona system produces:

- fewer but sharper persona choices
- clearer disagreement between personas
- better escalation and synthesis
- stronger aesthetic and quality judgment
- less average output
