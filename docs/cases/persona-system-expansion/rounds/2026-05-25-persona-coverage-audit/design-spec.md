# Design Spec: Persona Coverage Gap Audit

Date: 2026-05-25
Status: Drafted
Scope: Audit and classify the current WorkWork persona-system coverage gaps. This round does not add personas, modify validators, expand routing, or change packet/template contracts.

## Goal

Create a source-grounded coverage gap map for the current `ww-subagent-orchestrator` persona system so later rounds can expand the persona portfolio deliberately instead of adding ad hoc roles.

## Sources Reviewed

- `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
- `docs/superpowers/personas/registry.yaml`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
- `tools/validate_ww_persona_selection_contracts.py`
- recent `docs/cases/case-based-artifact-layout/rounds/*/dispatch-plan.md` usage patterns

## Current Coverage Snapshot

### Built-In Persona Records

The built-in catalog currently contains 6 persona records:

- 3 orchestrators:
  - `staff-engineer-orchestrator`
  - `pm-orchestrator`
  - `creative-director-orchestrator`
- 1 reviewer:
  - `secure-software-engineer`
- 2 worker-capable specialists:
  - `senior-backend-engineer`
  - `java-pro-engineer`

Only the 2 specialist records are worker-capable under the current worker gate because they are not orchestrators, have `review_only: false`, and include `implementation_principles`.

### Project Persona Registry

The project registry currently contains 5 persona records:

- 2 orchestrators:
  - `pm-orchestrator`
  - `creative-director-orchestrator`
- 1 reviewer:
  - `secure-software-engineer`
- 2 worker-capable specialists:
  - `senior-backend-engineer`
  - `java-pro-engineer`

The project registry mostly mirrors the built-in non-staff-engineer subset. It does not materially broaden coverage beyond backend, Java, security review, product orchestration, and creative orchestration.

### Routing Categories

The active skill and working brief template support 3 top-level routing values:

- `code/programming`
- `design/ads/product`
- `video/creative`

The routing model is intentionally simple, but it compresses several common work families into adjacent buckets:

- research and investigation
- documentation and knowledge management
- operations, release, and infrastructure
- data, analytics, and ML
- quality engineering and test strategy
- UX, accessibility, and information architecture

### Review Lanes

The dispatch template supports these lane types:

- `spec-review`
- `code-quality-review`
- `scope-review`
- `editorial-review`
- `other`

The skill review pipeline expects route-specific reviewers:

- code/programming: spec reviewer and code quality reviewer
- design/ads/product: scope reviewer
- video/creative: editorial reviewer

The persona catalog does not currently provide dedicated reviewer personas for most of those lane types. The only built-in reviewer is `secure-software-engineer`, which is appropriate for security-heavy review but is too narrow for general spec, code-quality, scope, editorial, UX, or accessibility review.

Recent case-based workflow rounds show a practical symptom: 8 dispatch plans under `case-based-artifact-layout` use `pm-orchestrator` as the planned reviewer and also set planned specialist personas to `none`. That pattern works for human-understandability review, but it makes reviewer staffing too dependent on a broad orchestrator persona instead of lane-specific reviewer personas.

## Gap Classification

### Gap 1: Worker-Capable Specialist Coverage Is Too Engineering-Narrow

Severity: high

Current worker-capable specialists cover backend/service boundaries and Java-specific correctness. Missing worker families include:

- frontend and product UI implementation
- test and quality engineering
- DevOps, release, and infrastructure operations
- data, analytics, and ML workflows
- technical writing and documentation production
- UX research or information architecture execution

Impact:

- Most non-backend work either falls back to the top-level orchestrator or receives no meaningful specialist persona.
- The worker capability gate is doing its job, but the eligible pool is too small for the breadth of work the workflow claims to coordinate.
- Persona selection can become technically valid while still feeling generic.

### Gap 2: Reviewer Persona Coverage Does Not Match Review Lane Semantics

Severity: high

The review pipeline names several review types, but the catalog only has one reviewer-only persona. Missing reviewer families include:

- spec reviewer
- code quality reviewer
- product scope reviewer
- editorial reviewer
- accessibility or UX reviewer
- documentation clarity reviewer

Impact:

- `pm-orchestrator` is repeatedly used as a reviewer lens even when a narrower reviewer role would be cleaner.
- Reviewer and orchestrator concepts remain distinct in the contract, but the catalog nudges real rounds toward role reuse.
- Review findings may become broad and product-shaped even when the lane needs code quality, editorial clarity, or artifact-contract scrutiny.

### Gap 3: Top-Level Routing Compresses Too Many Work Families

Severity: medium-high

The three current routing buckets are usable but coarse. Several frequent work types do not have a natural primary route:

- repo/process documentation
- data analysis
- infrastructure and release operations
- research-only investigation
- QA/test strategy
- accessibility or UX audit

Impact:

- Mixed tasks are forced to pick the closest route, then patch the mismatch through specialist personas.
- Because specialist coverage is thin, the cross-category mechanism cannot carry much weight yet.
- Later taxonomy work should decide whether these become new top-level routes, secondary route tags, or required specialist lanes.

### Gap 4: Project Registry Does Not Broaden Built-In Coverage

Severity: medium

The project registry is checked first, but it currently does not add a substantially different coverage layer. It duplicates the same core non-staff-engineer persona families:

- security reviewer
- backend specialist
- Java specialist
- PM orchestrator
- creative director orchestrator

Impact:

- The project-first rule is structurally sound but has little practical effect for coverage diversity.
- A strong project match cannot exist for many task families because the project registry does not define them.

### Gap 5: Migration Guidance Suppresses Expansion Without A Coverage Floor

Severity: medium

The registry rules intentionally say to keep the persona catalog small during migration and avoid adding personas merely to express nuances already covered by enrichment fields.

This is a good anti-sprawl rule, but it lacks a paired minimum-coverage rule.

Impact:

- Maintainers get a clear warning against over-expansion but no explicit threshold for when expansion is required.
- Missing role-family coverage can be mistaken for mere nuance.
- Later taxonomy work should distinguish "nuance handled by enrichment" from "missing capability requiring a new persona family."

### Gap 6: Validators Check Selection Semantics, Not Portfolio Coverage

Severity: medium

The persona selection validator checks Markdown contract text in `SKILL.md` and `persona-registry.md`. It does not inspect `built-in-personas.yaml` or `docs/superpowers/personas/registry.yaml` for minimum coverage.

Impact:

- Repo validation can pass while the persona catalog remains too narrow.
- The current validator protects selection order and guardrails, not portfolio completeness.
- Later validator work should be separate from this audit and follow a taxonomy contract first.

## Role Boundary Observations

The current worker gate is healthy:

- orchestrator personas are excluded from worker selection
- reviewer-only personas are excluded from worker selection
- worker-capable personas require exactly two `implementation_principles`

The problem is not that the gate is too strict. The problem is that too few personas are eligible after the gate runs.

The reviewer boundary is less well supported by data:

- reviewer prompts and worker prompts remain distinct
- reviewer-only records exist
- but only one reviewer-only persona exists, so real rounds reuse an orchestrator persona as reviewer

Future expansion should preserve the gate and add eligible records instead of weakening compatibility rules.

## Recommended Follow-Up Round Categories

### 1. Persona Taxonomy Contract

Define a minimum portfolio taxonomy before adding records. The taxonomy should specify:

- supported role families for orchestrators, workers, reviewers, and explorers
- required minimum built-in coverage
- when a missing capability requires a new persona versus optional enrichment
- how project registries may extend or override built-ins without duplicating them

### 2. Worker Persona Expansion

Add worker-capable specialists only after taxonomy approval. Candidate families to evaluate:

- frontend/product engineer
- test quality engineer
- DevOps or release engineer
- data/ML engineer
- technical writer

### 3. Reviewer Persona Expansion

Add reviewer-only personas aligned to existing lane types. Candidate families to evaluate:

- spec reviewer
- code quality reviewer
- product scope reviewer
- editorial reviewer
- accessibility/UX reviewer

### 4. Routing Model Expansion

Decide whether to expand `task_routing` directly or introduce secondary route tags. Candidate coverage:

- research/analysis
- documentation/knowledge
- operations/release
- data/ML
- QA/test
- UX/accessibility

### 5. Persona Coverage Validator

After taxonomy and records exist, add validation for:

- minimum role-family coverage
- worker-capable gate compliance
- reviewer-lane staffing availability
- project registry schema parity
- built-in routing default consistency

## Out Of Scope For This Round

- Adding persona records
- Changing project registry records
- Changing validator behavior
- Changing routing values
- Changing dispatch plan templates
- Changing subagent packet contracts
- Committing or pushing changes

## Acceptance Criteria

- The audit distinguishes missing capability from optional persona nuance.
- The audit separately covers built-in personas, project registry, routing categories, review lanes, and worker capability gates.
- The audit gives later rounds a clear sequence without implementing those later rounds.
- The audit preserves current role-boundary semantics.
