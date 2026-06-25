# Task Runtime Verification Contract

This reference defines the dormant verification authority layer for the future
`task-runtime-v1` protocol. It extends `task-runtime-lifecycle.md` by defining
formal verifier authority, verification lanes, evidence records, lane selection,
and model capability resolution. It does not activate `task-runtime-v1`.

Legacy rounds must not persist or consult these records as lifecycle authority.
Presence of verification fields, examples, templates, or references is contract
scaffolding only until a later approved activation round implements verifier
bindings, command execution, validator coverage, repair, scoring, close gates,
and end-to-end runtime behavior.

## Authority Boundary

Runtime role, persona, and model capability are separate authorities:

- `runtime_role` determines what the actor may do.
- `persona_id` determines the professional viewpoint used for judgment.
- `model_capability_profile` and `minimum_capability_floor` determine whether
  the selected model and launch environment can perform the lane safely.

Future formal verification uses `runtime_role: verifier`. A verifier may read
the immutable target, run approved verification commands, write bounded evidence
records, and return one lane outcome. A verifier must not mutate the target,
repair failures, create reviewer findings, accept evidence, change
`lifecycle_phase`, change canonical `runtime_state`, score the result, or
approve close.

Workers may run self-checks, but worker self-check output is not formal
verification evidence. Reviewers may cite verification evidence, but reviewer
findings are not verification evidence. The orchestrator selects lanes, freezes
targets, checks isolation and freshness, accepts or rejects evidence, and emits
legal lifecycle events. Human approval may authorize revisions or elevated
commands, but it cannot convert missing, stale, failed, blocked, wrong-target,
identity-conflicted, or below-floor evidence into `PASS`.

## Authority Subject

Every future producer, verifier, and reviewer attempt records an authority
subject:

```yaml
authority_subject:
  runtime_role: worker | verifier | reviewer
  persona_id: <canonical-persona-id>
  persona_source: project | built-in
  agent_id: <runtime-agent-instance-id>
  execution_id: <logical-execution-id>
  packet_id: <execution-payload-id>
  attempt_id: <launch-attempt-id>
```

For one target lineage, worker, verifier, reviewer, and orchestrator runtime
subjects must stay isolated:

- worker, verifier, and reviewer `agent_id` values are pairwise distinct
- worker, verifier, and reviewer `execution_id` values are pairwise distinct
- verifier packets and attempts are distinct from producer packets and attempts
  for the verified target
- reviewer packets and attempts are distinct from producer and verifier packets
  for the reviewed target
- the active orchestrator `agent_id` does not appear as worker, verifier, or
  reviewer in the same target lineage
- one persona may staff multiple lanes only when each lane uses one eligible
  runtime role with distinct execution and attempt identity

Identity is checked before launch when possible and again before evidence
acceptance. Any conflict blocks launch or evidence acceptance and is recorded as
`identity-conflict`.

## Target Identity

Every verifier lane binds to one frozen `verification_target_ref` before packet
creation:

```yaml
verification_target_ref:
  target_id: <stable-id-within-round>
  target_kind: single | aggregate
  artifact_path: <repository-relative-path-or-null>
  artifact_kind: <canonical-kind-or-null>
  artifact_revision: <document-revision-or-full-file-hash-or-null>
  schema_version: <artifact-schema-version-or-null>
  section_anchor: <anchor-or-null>
  content_hash: <sha-256-of-reviewed-bytes-or-exact-slice-or-null>
  target_set_members: []
  target_set_hash: <sha-256-of-canonical-member-list-or-null>
```

A `single` target carries repository-relative artifact identity and has an empty
member list. A schema-bearing artifact must persist its normalized schema
version; schema-less artifacts may use `schema_version: null`. An `aggregate`
target has null single-artifact fields, at least two `target_set_members`, and a
non-null `target_set_hash`.

Each aggregate member uses:

```yaml
target_set_member:
  artifact_path: <normalized-repository-relative-path>
  artifact_kind: <canonical-kind>
  artifact_revision: <revision-or-full-file-hash>
  schema_version: <integer-or-null>
  section_anchor: <anchor-or-null>
  content_hash: <sha-256>
```

Aggregate members are serialized as schema-order UTF-8 JSON, sorted by path,
revision, anchor, and content hash, then hashed. Duplicate member tuples are
invalid. Returned evidence whose target reference differs in any identity field
is wrong-target evidence and can be retained only as history.

## Lane Collections

Future `task-runtime-v1` dispatch artifacts keep authority classes separate:

```yaml
worker_lanes: []
verifier_lanes: []
reviewer_lanes: []
```

Collections are not interchangeable. `lane_type` does not grant authority; the
collection, runtime role, eligible persona binding, and packet binding must all
agree. Moving a lane between authority classes requires a material plan
revision.

## Verifier Lane Schema

```yaml
verifier_lane:
  lane_id: <stable-id-within-section>
  lane_type: test-verification | artifact-verification | deployment-verification | configuration-verification
  runtime_role: verifier
  required: true | false
  selection:
    sources: [task-profile | risk-trigger | user-added]
    task_profile_ids: []
    risk_trigger_ids: []
    rationale: <why-this-lane-applies>
    exclusion_ref: <null-or-material-exclusion-record>
  target_selector:
    artifact_ids: []
    path_globs: []
    environment_ids: []
  verification_target_ref: <complete-frozen-target-ref-or-null-before-freeze>
  verification_commands: []
  evidence_requirements: []
  freshness_policy:
    target_bound: true
    environment_bound: true | false
    max_age_seconds: <positive-integer-or-null>
    environment_change_token_id: <stable-token-type-or-null>
  model_capability_profile: <profile-id>
  model_capability_profile_schema_version: 1
  model_capability_profile_hash: <sha-256>
  minimum_capability_floor: <floor-id>
  minimum_capability_floor_schema_version: 1
  minimum_capability_floor_hash: <sha-256>
  selected_verifier:
    persona_id: <canonical-id>
    persona_source: project | built-in
    selection_rationale: <role-fit-and-source-rationale>
  active_execution_id: <id-or-null>
  active_attempt_id: <id-or-null>
  attempt_history: []
  accepted_outcome_ref: <evidence-bundle-id-or-null>
```

Lane records do not own `runtime_state` or `lifecycle_phase`. They hold lane
attempt pointers and evidence history only. Section `runtime_state` and
`lifecycle_phase` remain canonical under `task-runtime-lifecycle.md`.

`target_selector` is planning input. Before packet creation it resolves to one
complete frozen `verification_target_ref`. After freeze, packets, evidence,
deduplication, freshness, and repair-overlap checks use only the frozen target.
Selector re-expansion is forbidden for old evidence.

Canonical verifier lane types are:

| Lane type | Claim established | Minimum evidence |
|---|---|---|
| `test-verification` | declared automated checks pass for the target revision | command records for every required test command and bounded result evidence |
| `artifact-verification` | expected artifacts exist, are readable, and satisfy declared structural or render checks | target inventory, hashes, inspection commands, and artifact/result references |
| `configuration-verification` | configuration parses, resolves, and matches declared constraints for target and environment | parser/validator command records, normalized configuration identity, and environment fingerprint when applicable |
| `deployment-verification` | an approved deployed-state claim is true in the named environment | approved external-state commands, environment identity, observation time, result references, and side-effect classification |

New lane types require a later approved contract revision.

## Evidence Requirements

Each verifier lane lists closed evidence requirements:

```yaml
evidence_requirement:
  requirement_id: <stable-id-within-lane>
  evidence_kind: command | artifact | environment
  required: true | false
  observation_type: <canonical-artifact-observation-or-null>
  command_ref: <command-spec-id-or-null>
  environment_id: <environment-id-or-null>
  result_artifact_required: true | false
  acceptance_rule: pass | present-and-hash-matched | environment-current
```

Exactly one discriminator is populated:

- `command` uses `command_ref` and `acceptance_rule: pass`
- `artifact` uses `observation_type` and `acceptance_rule: present-and-hash-matched`
- `environment` uses `environment_id`, `acceptance_rule: environment-current`,
  and `result_artifact_required: false`

Every required requirement ID must be satisfied by at least one accepted current
evidence record. Every claimed requirement ID must exist in the owning lane.
Duplicate requirement IDs are invalid.

Any lane with `freshness_policy.environment_bound: true` and either
`max_age_seconds` or `environment_change_token_id` must declare at least one
required environment evidence requirement for every environment in scope.

## Command Specs And Evidence

Each `verification_commands` entry is:

```yaml
verification_command:
  command_ref:
    command_id: <stable-command-id>
    command_spec_hash: <sha-256>
  required: true | false
```

`command_ref` is the schema-order identity tuple
`{command_id, command_spec_hash}`. Every command entry maps to exactly one
command evidence requirement with the same `command_ref` and requiredness, and
every command requirement maps back to exactly one command entry.

Command specs and command evidence are immutable, append-only records. A later
runtime implementation must include command normalization, side-effect
classification, approval boundary, timeout, output bounds, secret redaction, and
result-artifact references before command execution is enabled. This contract
does not implement command execution.

## Evidence Bundles And Outcomes

Each verifier attempt returns exactly one lane disposition:

```text
PASS | FAIL | BLOCKED | SKIPPED
```

- `PASS`: all required evidence and commands completed successfully for the
  exact target, identity checks passed, and the model met the floor.
- `FAIL`: commands ran authoritatively and established one or more required
  verification claims are false.
- `BLOCKED`: the claim could not be evaluated because context, approval, tool
  access, environment certainty, identity isolation, or capability was absent.
- `SKIPPED`: an optional lane or command was intentionally not run with a
  persisted reason and authorizing plan or human decision.

A required lane is accepted only by a current accepted `PASS` bundle for that
lane's frozen target. Required `FAIL`, `BLOCKED`, or `SKIPPED` does not satisfy
verification acceptance. Terminal non-pass bundles are still durable evidence
and may drive blocked review or human recovery decisions.

Evidence applicability is append-only and external to the immutable bundle:

```yaml
evidence_applicability_record:
  applicability: current | stale | wrong-target | identity-conflict | superseded
  reason_code: target-changed | plan-revised | command-spec-changed | environment-changed | ttl-expired | model-resolution-invalid | candidate-facts-invalid | identity-conflict | wrong-target | superseded
  decided_at: <timestamp>
  decided_by:
    runtime_role: orchestrator
    persona_id: <orchestrator-persona-id>
  rationale: <short-explanation>
```

Stale, wrong-target, identity-conflicted, superseded, missing, failed, blocked,
or skipped evidence cannot authorize `VERIFICATION_ACCEPTED`,
`REVERIFICATION_ACCEPTED`, scoring, or close.

## Lane Selection

Required verifier lanes are selected deterministically from:

- approved task-profile baselines
- applicable risk triggers
- explicit user-added lanes

The orchestrator records inclusion and exclusion rationale in each lane's
`selection` block. Baseline and triggered lanes are unioned, then deduplicated
only when target, environment, commands, freshness policy, profile, and floor
are equivalent. Dedupe must not merge lanes whose capability floor or evidence
requirements differ.

A required baseline or risk-triggered lane may be removed only by a material
approved plan revision with a durable exclusion record. Keyword-only lane
selection is invalid; the rationale must point to task profile, risk trigger,
or user-added source.

## Model Capability Profiles

Profiles define required execution ability without naming concrete models:

```yaml
model_capability_profile:
  profile_id: <stable-label>
  profile_schema_version: 1
  profile_hash: <sha-256>
  allowed_runtime_roles: [verifier]
  reasoning_tier: standard | strong | deep
  minimum_context_tier: standard | large
  required_capabilities:
    repository_read: true | false
    structured_output: true | false
    command_execution: true | false
    filesystem_read: true | false
    filesystem_ephemeral_write: true | false
    network_access: true | false
    multimodal_inspection: true | false
  required_tool_classes: []
  prohibited_tool_classes: []
  minimum_floor_id: <stable-floor-id>
  minimum_floor_schema_version: 1
  minimum_floor_hash: <sha-256>
```

Portable initial profile labels are:

- `artifact-inspection`
- `tool-verification`
- `environment-verification`
- `deep-verification`

Capability floors are closed, versioned records:

```yaml
model_capability_floor:
  floor_id: <stable-id>
  floor_schema_version: 1
  floor_hash: <sha-256>
  minimum_reasoning_tier: standard | strong | deep
  minimum_context_tier: standard | large
  required_capabilities: {}
  required_tool_classes: []
  prohibited_tool_classes: []
```

Profile and floor hashes are lowercase SHA-256 digests of schema-order UTF-8
JSON records excluding the hash field itself.

## Model Resolution

Every future verifier launch records model and launch-environment resolution:

```yaml
model_resolution:
  resolution_id: <immutable-id>
  lane_id: <lane-id>
  execution_id: <logical-execution-id>
  packet_id: <execution-payload-id>
  attempt_id: <launch-attempt-id>
  resolution_target_ref: <complete-verification-target-ref>
  requested_profile_id: <profile-id>
  requested_profile_schema_version: 1
  requested_profile_hash: <sha-256>
  minimum_floor_id: <floor-id>
  minimum_floor_schema_version: 1
  minimum_floor_hash: <sha-256>
  candidate_models: [<candidate-id-and-capability-facts-hash>]
  selected_model: <provider-and-model-id>
  selected_model_version: <version-or-null>
  selected_candidate_facts_hash: <sha-256>
  launch_environment_capabilities: <launch-environment-id-and-capability-facts-hash>
  capability_evaluation:
    met: []
    missing: []
    floor_result: met | below-floor | unknown
  fallback_used: true | false
  fallback_from: <model-id-or-null>
  fallback_rationale: <text-or-null>
  approved_plan_revision: <revision>
  resolved_at: <timestamp>
```

Model-owned requirements are reasoning tier, context tier, structured output,
and multimodal inspection. Launch-environment-owned requirements are repository
access, command execution, filesystem access, network access, and required or
prohibited tool classes. The combined resolution meets a floor only when both
owned evaluations meet their requirements. Missing facts, unknown labels, or an
incompatible schema produce `floor_result: unknown`.

Same-floor fallback is allowed without renewed approval when all required
capabilities and the declared floor are met, but every fallback is recorded.
Below-floor or unknown resolution blocks launch under the current plan. Human
approval may revise the plan, floor, lane, command set, or execution route, but
it may not relabel a below-floor run as valid under the old plan.

## Lifecycle Integration

For future active `task-runtime-v1` sections:

1. `EXECUTION_RESULT_ACCEPTED` freezes the producer target and enters
   `verify/queued`.
2. The orchestrator resolves verifier lanes, authority subjects, frozen target
   refs, evidence requirements, and capability profiles before verifier launch.
3. Lane attempts run under aggregate `verify/running` or `re-verify/running`.
4. The orchestrator records each return and applies the lifecycle foundation's
   lane aggregation events.
5. `VERIFICATION_ACCEPTED` or `REVERIFICATION_ACCEPTED` is legal only when every
   required lane has current accepted `PASS` evidence for the correct frozen
   target set.

Required terminal non-pass evidence can contribute to
`REQUIRED_LANES_RETURNED`, but it cannot satisfy verification acceptance. It
drives the blocked review path for later human recovery, repair, or material
revision. This reference does not define repair, scoring, hooks, or close gates.

## Invalid States For Later Validators

Later validator rounds should reject at least:

- verifier fields used as lifecycle authority while protocol is `legacy`
- `runtime_role: verifier` bound to any current worker, reviewer, explorer, or
  orchestrator prompt asset
- worker self-check or reviewer finding referenced as formal verification
- verifier authority subject sharing `agent_id` or `execution_id` with producer,
  reviewer, or orchestrator in the same target lineage
- verifier mutation of a target or repair during verifier execution
- incomplete, mutable, or wrong-target `verification_target_ref`
- required lane satisfied by stale, skipped, failed, blocked, wrong-target,
  conflicted, superseded, or below-floor evidence
- required baseline or risk-triggered lane removed without approved material
  revision
- lane dedupe that ignores target, environment, command, freshness, profile, or
  floor differences
- silent model fallback or fallback without a resolution record
- model launch with `below-floor` or `unknown` capability result
- individual lane record owning section `runtime_state` or `lifecycle_phase`
- `VERIFICATION_ACCEPTED` or `REVERIFICATION_ACCEPTED` without current accepted
  `PASS` evidence for every required verifier lane
- stale pre-fix evidence satisfying re-verification

Dedicated validator rule IDs, fixtures, and enforcement code belong to a later
approved validator-expansion round.
