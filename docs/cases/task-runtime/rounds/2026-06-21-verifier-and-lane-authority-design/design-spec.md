# Verifier And Lane Authority Design

- Date: 2026-06-21
- Status: review-pending
- Artifact Revision: 15
- Working Brief Version: 1
- Dispatch Plan Revision: 1
- Lifecycle Protocol During This Round: `legacy`
- Upstream Runtime Design: `docs/superpowers/specs/2026-06-19-workwork-task-runtime-design.md`
- Lifecycle Foundation: `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`

## Goal

Define the dormant authority and persistence contract for formal verification in
`task-runtime-v1`. A later implementation round must be able to add verifier
bindings, lane records, evidence records, lane selection, and model resolution
without re-deciding:

- what a verifier may do
- how worker, verifier, reviewer, orchestrator, and human authority stay separate
- how verification lanes are selected and represented
- what makes verification evidence current, complete, and acceptable
- how model capability requirements are resolved and how fallback is handled
- how interrupted or stale verification is recovered without manufacturing a pass

This design does not activate `task-runtime-v1`. The current round remains
`legacy`, and no lifecycle snapshot or event history is added by this artifact.

## Governing Principles

1. Runtime role determines authority; persona determines judgment; model profile
   determines execution capability. None may substitute for another.
2. The orchestrator is the only actor that changes `lifecycle_phase` or accepts
   lane evidence into the canonical section ledger.
3. Formal verification must be produced by an authority subject isolated from
   the worker that produced the target and from reviewers that judge it.
4. Verification evidence is immutable, target-bound, command-bound, and
   environment-bound where the claim depends on external state.
5. Required lanes come from approved task-profile baselines plus applicable risk
   triggers. Selection is deterministic and its provenance is durable.
6. A required lane cannot pass through omission, an unexplained skip, stale
   evidence, an identity conflict, or model fallback below its capability floor.
7. Lane records are subordinate evidence ledgers. They do not create another
   section phase or another canonical `runtime_state`.

## Compatibility And Activation Boundary

This contract is a design for the future `task-runtime-v1` protocol.

- Schema support may land dormant in a later implementation round.
- New and ordinary rounds continue to use `lifecycle_protocol: legacy`.
- A legacy round must not persist or consult the lane and evidence structures
  defined here as lifecycle authority.
- `task-runtime-v1` remains unselectable until verifier authority, minimum
  required lanes, review progression, repair and re-verification, score
  production, blocker evaluation, close handling, and validator coverage are
  implemented, verified end to end, and approved.
- Presence of verifier fields, profiles, or records never implies activation.
- This design strengthens the `verify` and `re-verify` preconditions from the
  lifecycle foundation. It does not change phase names, legal phase transitions,
  canonical `runtime_state`, or orchestrator-only phase authority.

## Authority Model

### Authority Matrix

| Actor | May mutate target | May execute verification commands | May create formal verification evidence | May create review findings | May accept lane result | May change phase | May approve material or final human gate |
|---|---:|---:|---:|---:|---:|---:|---:|
| worker | yes, within approved write scope | self-checks only | no | no | no | no | no |
| verifier | no while exercising verifier authority | yes, within approved command policy | yes | no | no | no | no |
| reviewer | no | only incidental read-only inspection, not formal verification | no | yes | no | no | no |
| orchestrator | controller records only; not the target | no formal lane execution | no | no | yes | yes | requests gates but does not impersonate the human |
| human | only through a separately authorized work action | may approve elevated commands | no | may supply judgment notes | approves revisions and recovery choices | decision is persisted by orchestrator | yes |

### Worker

A worker produces or repairs artifacts inside approved write scope. Worker
self-checks are execution evidence and may help diagnose a return, but they do
not satisfy a formal verifier lane. A worker may not create, accept, waive, or
approve formal evidence for its own target lineage.

### Verifier

A verifier uses future `runtime_role: verifier`. It may:

- read the immutable target snapshot and declared dependencies
- run approved baseline verification commands
- propose auxiliary supplemental commands under the command policy below
- write command output only to declared evidence locations or approved local
  ephemeral paths
- return a structured lane outcome and immutable evidence records

A verifier may not:

- modify the target or any artifact included in the target set
- repair a failure during the same verifier execution
- create reviewer findings or approve quality
- alter lane selection, capability floors, command approval, or target identity
- advance `lifecycle_phase`, change canonical `runtime_state`, or authorize close

If verification discovers that a target change is required, the verifier returns
`FAIL` or `BLOCKED` with evidence. A later orchestrator-authorized producer
execution performs the change.

### Reviewer

A reviewer returns findings against an immutable review target. Reviewer output
may reference verifier evidence, but it does not become verification evidence.
A reviewer may not rerun or waive a required verifier lane, modify the target,
accept its own findings, or advance phase.

### Orchestrator

The orchestrator owns:

- task-profile and risk-trigger evaluation
- lane selection, deduplication, requiredness, and durable rationale
- verifier persona and capability-profile selection
- command-policy classification and requests for human reapproval
- identity-conflict checks before launch and before evidence acceptance
- target freezing, lane aggregation, evidence acceptance, and staleness marking
- legal lifecycle events and section-state persistence

The orchestrator does not execute a verifier lane or turn its own observations
into formal evidence.

### Human

The human approves the dispatch plan and material revisions, elevated command
authority, below-floor capability changes, blocked recovery, removal of a
required lane, and final close. Human approval changes the plan or authorizes a
controller decision; it does not convert missing, stale, failed, or conflicted
evidence into `PASS`.

## Identity Isolation

### Authority Subject

Every producer, verifier, and reviewer attempt persists this identity tuple:

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

`agent_id` identifies the live runtime subject. `execution_id` remains stable
across retries of one logical lane execution. `packet_id` rotates when the
payload changes. `attempt_id` rotates on every relaunch. Persona identity is not
execution identity and cannot prove isolation by itself.

### Conflict Domain

Isolation is evaluated per target lineage, not merely per file path. A target
lineage begins with one accepted producer result and includes later repaired
revisions until the section closes or a material plan revision creates a new
logical work item.

For one target lineage:

- worker, verifier, and reviewer authority subjects must have pairwise-distinct
  `agent_id` values
- worker, verifier, and reviewer logical executions must have pairwise-distinct
  `execution_id` values
- a verifier packet and attempt must be distinct from every producer packet and
  attempt whose output contributed to the verified target
- a reviewer packet and attempt must be distinct from producer and verifier
  packets and attempts for the reviewed target
- the active orchestrator `agent_id` may not appear as a worker, verifier, or
  reviewer authority subject in the same target lineage
- one persona may staff multiple lanes only when its persona record is eligible
  for that one runtime role and every lane has a separate execution and attempt;
  one persona binding may not cross runtime roles within the lineage
- retries preserve the lane's `execution_id` but rotate `attempt_id`; this does
  not create a conflict because the execution remains isolated from other roles
- a late, stale, or superseded attempt never inherits authority from the active
  attempt and cannot satisfy lane aggregation

Before launch, the orchestrator compares every identity available before agent
allocation: runtime role, persona binding, execution ID, packet ID, and attempt
ID. If the launcher allocates `agent_id` before execution starts, it is included
in that gate. Otherwise, the orchestrator performs an immediate post-allocation
identity gate and cancels or disregards the attempt before accepting any return.
Before evidence acceptance, it repeats the comparison using the returned runtime
identity. Any conflict blocks launch or evidence acceptance and is recorded as
`identity-conflict`; changing display names, personas, packet labels, or lane IDs
does not cure a reused `agent_id` or `execution_id`.

## Target Identity

Every verifier lane binds to one immutable target reference:

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

The variants are mutually exclusive. A `single` target requires every
single-artifact field except nullable `section_anchor` and nullable
`schema_version`, and requires `target_set_members: []` plus
`target_set_hash: null`. `schema_version` is null only for schema-less artifacts;
schema-bearing artifacts must persist the normalized integer schema version. It
uses the same revision rules as reviewer targets: an explicit document revision
when available plus a content hash; otherwise the full-file hash is both
`artifact_revision` and `content_hash`. Excerpt targets hash the exact slice and
carry the source revision. An `aggregate` target requires all six
single-artifact fields from `artifact_path` through `content_hash` to be null,
requires at least two `target_set_members`, and requires non-null
`target_set_hash`. Aggregate targets sort canonical member references by path,
revision, anchor, and hash, then hash that list into `target_set_hash`.

Each aggregate member uses this closed schema:

```yaml
target_set_member:
  artifact_path: <normalized-repository-relative-path>
  artifact_kind: <canonical-kind>
  artifact_revision: <revision-or-full-file-hash>
  schema_version: <integer-or-null>
  section_anchor: <anchor-or-null>
  content_hash: <sha-256>
```

Canonical serialization is UTF-8 JSON with keys in the schema order above, no
insignificant whitespace, lowercase hexadecimal hashes, JSON `null` for a
missing anchor, and `/` path separators. Members are sorted lexicographically by
the tuple `(artifact_path, artifact_revision, section_anchor-or-empty,
content_hash)` before serializing the complete JSON array. `target_set_hash` is
the lowercase SHA-256 digest of those exact array bytes. Duplicate member tuples
are invalid rather than silently deduplicated.
As with single targets, aggregate member `schema_version` is null only for
schema-less artifacts; schema-bearing aggregate members must persist the
normalized integer schema version.

The target is frozen before any verifier packet is created. A return whose
target reference differs in any identity field is wrong-target evidence and may
be retained as history only.

## Lane Model

### Authority-Class Separation

Future dispatch artifacts represent lanes in three separate collections:

```yaml
worker_lanes: []
verifier_lanes: []
reviewer_lanes: []
```

The collections are not interchangeable. `lane_type` does not grant authority;
the collection, `runtime_role`, eligible persona binding, and packet binding must
agree. Moving a record between collections requires a material plan revision.

### Verifier Lane Schema

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

Lane records do not own a second `runtime_state`. Active and historical attempt
pointers describe execution; section `runtime_state` remains canonical. The
aggregate lifecycle events `LANE_RESULT_RECORDED_ACTIVE`,
`LANE_RESULT_RECORDED_PENDING`, and `REQUIRED_LANES_RETURNED` remain exactly as
defined by the lifecycle foundation.

`target_selector` is planning input only. Before packet creation it must resolve
to one complete immutable `verification_target_ref`; after freeze, null is
invalid and all packets, evidence, deduplication, and freshness checks use the
resolved ref rather than re-expanding the selector. Selector re-expansion is
forbidden for staleness or repair-overlap checks. If a repair adds or removes
artifacts that would have matched the old selector but are not part of the
frozen target reference, that is a material target-selection change requiring a
new plan revision and a new frozen lane target, not a reason to reinterpret old
evidence.

Each entry in `evidence_requirements` uses this closed schema:

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

Exactly one discriminator field is populated: `command_ref` for command,
`observation_type` for artifact, or `environment_id` for environment. Command
artifact, and environment evidence records persist `satisfies_requirement_ids`.
Bundle-level environment fingerprint and change-token fields are shorthand
identity fields only; they never satisfy an environment requirement by
themselves. Every required requirement ID must be satisfied by at least one
accepted current record, and every claimed requirement ID must exist in the
owning lane. Duplicate requirement IDs are invalid.

Requirement variants are closed: `command` requires `command_ref`, requires
`acceptance_rule: pass`, and may set `result_artifact_required`; `artifact`
requires `observation_type`, requires `acceptance_rule:
present-and-hash-matched`, and may set `result_artifact_required` only for
`render` or `package`; `environment` requires `environment_id`, requires
`acceptance_rule: environment-current`, and requires
`result_artifact_required: false`. Fields owned by the other variants must be
null. Any other combination is invalid during planning.

Any lane with `freshness_policy.environment_bound: true` and either
`max_age_seconds` or `environment_change_token_id` set must declare at least one
required `environment` evidence requirement for every environment in scope.
Without that required environment evidence, the lane has no freshness anchor and
is invalid during planning.

Each `verification_commands` entry is `{command_ref, required}`. `command_ref`
is the canonical command identity tuple
`{command_id, command_spec_hash}` serialized as schema-order JSON; it is not a
separate free-text ID. Every command entry maps to exactly one
`evidence_requirement` of kind `command` with the same `command_ref` and
`required` value, and every command requirement maps back to exactly one command
entry. Command evidence satisfies a command requirement only when both
`command_id` and `command_spec_hash` match the `command_ref`. Duplicate or
unmapped command refs are invalid. Thus the required command set is the set of
entries where `required: true`; no requiredness is inferred from command order
or exit-code policy.

### Canonical Verifier Lane Types

| Lane type | Claim established | Minimum evidence |
|---|---|---|
| `test-verification` | declared automated checks pass for the target revision | command records for every required test command and bounded result evidence |
| `artifact-verification` | expected artifacts exist, are readable, and satisfy declared structural or render checks | target inventory, hashes, inspection commands, and artifact/result references |
| `configuration-verification` | configuration parses, resolves, and matches declared constraints for the target and environment | parser/validator command records, normalized configuration identity, and environment fingerprint when applicable |
| `deployment-verification` | an approved deployment or deployed-state claim is true in the named environment | approved external-state commands, environment identity, observation time, result references, and side-effect classification |

New lane types require a later approved contract revision. An implementation may
specialize a canonical lane through command and evidence requirements, but may
not invent free-text lane types at runtime.

### Lane Outcome

Each verifier attempt returns exactly one disposition:

```text
PASS | FAIL | BLOCKED | SKIPPED
```

- `PASS`: all required evidence requirements and commands completed successfully
  for the exact target, identity checks pass, and the model met the floor.
- `FAIL`: commands ran authoritatively and established that one or more required
  verification claims are false.
- `BLOCKED`: the claim could not be evaluated because context, approval, tool
  access, environment certainty, identity isolation, or capability was absent.
- `SKIPPED`: the command or optional lane was intentionally not run with a
  persisted reason and authorizing plan or human decision.

A required lane with `SKIPPED` cannot satisfy required PASS aggregation. It must
be replaced by an approved equivalent lane or removed through a material plan
revision before verification can pass. `FAIL`, `BLOCKED`, stale evidence, and
wrong-target evidence also do not satisfy PASS aggregation. Valid terminal
`FAIL`, `BLOCKED`, and required `SKIPPED` results do count as returned terminal
lane results for `REQUIRED_LANES_RETURNED`; when any required terminal result is
not a current `PASS`, the aggregate transition is the blocked review path rather
than verification acceptance.

Attempt disposition is derived with fixed precedence. Any terminal required
record with `BLOCKED` yields `BLOCKED`; otherwise any required `FAIL` yields
`FAIL`; otherwise any required `SKIPPED` yields `SKIPPED`; otherwise the attempt
is `PASS` only when every required command and evidence requirement is satisfied
by current passing evidence. Optional skipped records do not prevent `PASS`.
An explicit attempt disposition that differs from this derivation is invalid.

## Lane Selection

### Selection Inputs

The approved dispatch revision supplies:

1. one or more task profiles for each required section
2. the task profile's baseline verifier lane requirements
3. normalized working-brief risk triggers
4. user-added lanes or approved exclusions
5. resolved artifact and environment targets

Task profiles and risk triggers are declarative selection inputs. They do not
execute commands, accept evidence, change phase, or score quality.

### Baseline Profiles

The first implementation must support these baseline mappings:

| Task profile | Required baseline verifier lanes |
|---|---|
| `document-or-design` | `artifact-verification` |
| `code-change` | `test-verification`, `artifact-verification` |
| `configuration-change` | `configuration-verification`, `artifact-verification` |
| `deployment-change` | `deployment-verification`, `configuration-verification`, `artifact-verification` |

A section that matches more than one profile uses the union. A profile may add
commands or evidence requirements to a lane; it may not weaken another matching
profile's requirements.

### Risk Triggers

The first implementation recognizes these normalized trigger IDs:

| Risk trigger | Lane effect |
|---|---|
| `executable-behavior-changed` | require `test-verification` |
| `generated-or-packaged-artifact` | require `artifact-verification` |
| `configuration-semantics-changed` | require `configuration-verification` |
| `external-environment-claim` | require `deployment-verification` and environment-bound freshness |
| `cross-platform-or-multi-environment` | instantiate the applicable lane once per declared platform or environment target |
| `verification-command-mutates-external-state` | require renewed human approval before launch; it does not remove the applicable lane |

Risk triggers may add lanes or strengthen evidence and freshness requirements.
They may not remove baseline lanes.

### Default Capability Mapping

Lane selection also resolves a default profile and floor deterministically before
deduplication:

| Lane type | Default model capability profile | Default minimum floor |
|---|---|---|
| `artifact-verification` | `artifact-inspection` | `artifact-inspection-floor` |
| `test-verification` | `tool-verification` | `tool-verification-floor` |
| `configuration-verification` | `tool-verification` | `tool-verification-floor` |
| `deployment-verification` | `environment-verification` | `environment-verification-floor` |

Risk triggers may only strengthen the default. `external-environment-claim`
raises the profile and floor to `environment-verification` when the selected
lane is otherwise lower. `verification-command-mutates-external-state` requires
`environment-verification` plus renewed human approval. Any profile or floor
strengthening persists its source trigger in the lane selection record. A lane
may use `deep-verification` only when a risk trigger, user-added lane, or
approved material revision explicitly requires `reasoning_tier: deep`; otherwise
the default table above is authoritative. If two inputs request different
profiles or floors, the strongest combined profile/floor is selected by the
capability union and tier maximum rules in the profile schema. An unresolved
profile or floor blocks planning.

### Deterministic Algorithm

The orchestrator selects lanes in this order:

1. normalize task profiles, risk triggers, artifact mappings, environments, and
   command declarations from the approved plan
2. instantiate every profile-required baseline lane
3. append every risk-triggered lane instance and stronger requirement
4. append user-added lanes
5. resolve each lane's default or strengthened model capability profile and
   minimum floor from the deterministic mapping
6. deduplicate only records with the same `lane_type`, canonical target scope,
   environment scope, command set, evidence requirements, freshness policy,
   model capability profile, and capability floor
7. merge provenance into `selection.sources`, profile IDs, trigger IDs, and one
   rationale; required wins over optional
8. resolve an eligible verifier persona for the already-selected profile/floor
9. persist selected lanes and material exclusions before packet creation

If two candidates differ in target, environment, commands, freshness, model
capability profile, or capability floor, they are not duplicates. Selection that
cannot resolve an artifact or environment target blocks planning rather than
producing a broad or guessed lane.

For step 5, equality is byte equality of normalized components: target scope is
the canonical target JSON defined above; environment scope is a sorted unique
array of normalized environment IDs; command set is a sorted unique array of
`command_spec_hash` values; evidence requirements are schema-order JSON records
sorted by `requirement_id`; freshness is the schema-order tuple
`(target_bound, environment_bound, max_age_seconds,
environment_change_token_id)`; model capability profile is
`(profile_id, profile_schema_version, profile_hash)`; and capability floor is
`(floor_id, floor_schema_version, floor_hash)`. Nulls are explicit JSON `null`,
paths use `/`, IDs are case-sensitive, duplicate IDs or hashes are invalid, and
unresolved components prevent deduplication and block planning.

### Exclusions And Revisions

The dispatch plan records why each selected lane applies. It also records an
exclusion when a plausible lane was considered but omitted and the omission is
material to risk.

- Users may add lanes without weakening existing requirements.
- Removing or weakening a profile-required or triggered lane is a material plan
  revision and requires human approval before new dispatch.
- An exclusion records lane type, source profile or trigger, affected target,
  rationale, compensating evidence, decision actor, and dispatch revision.
- An exclusion cannot turn existing evidence from another authority class into
  formal verification.

## Verification Commands

### Command Specification

Each planned command has an immutable specification:

```yaml
verification_command:
  command_id: <stable-id>
  command_spec_hash: <sha-256-of-canonical-command-spec>
  argv: [<executable>, <arg>]
  normalized_command: <display-form>
  working_directory: <repository-relative-path>
  environment_names: []
  secret_value_persistence: forbidden
  timeout_seconds: <positive-integer>
  output_limit_bytes: <positive-integer>
  expected_exit_codes: [0]
  safety_class: read-only-local | write-local-ephemeral | external-state | destructive
  cleanup_policy: <none-or-approved-policy>
  approval_ref: <dispatch-or-human-decision-ref>
```

`argv` is authoritative where the execution surface supports it. The normalized
display form must round-trip to the same command semantics. Environment records
persist names and non-secret fingerprints only; secret values never enter the
dispatch plan or evidence.

The hash input excludes `command_spec_hash` itself and serializes all remaining
fields in the schema order above as UTF-8 JSON without insignificant whitespace.
Paths use `/`, arrays preserve declared `argv` order, set-like arrays
(`environment_names`, `expected_exit_codes`) are sorted unique, null is explicit,
and safety, cleanup, and approval values are exact case-sensitive IDs. The
lowercase SHA-256 digest of those bytes is `command_spec_hash`; duplicate
`command_id` values or a persisted hash mismatch are invalid.

Command evidence disposition is mechanically derived from the command spec and
recorded facts. `pass` requires `timed_out: false`, non-null `exit_code`, that
`exit_code` is a member of the command spec's `expected_exit_codes`, valid
approval for the safety class, and every required result artifact present and
hash-matched. `fail` requires `timed_out: false`, non-null `exit_code`, and that
`exit_code` is not in `expected_exit_codes`, or a deterministic result-artifact
mismatch for a command that completed. `blocked` is used when the command did
not produce an evaluable exit result because approval, executable access, working
directory, environment, timeout classification, or result-artifact availability
was absent. `skipped` requires no execution and a persisted skip rationale tied
to an optional command or an approved material plan decision. A returned
`disposition` that differs from this derivation is invalid.

### Command Authority

- Baseline commands are approved with the dispatch revision.
- A verifier may propose a supplemental `read-only-local` command when new
  diagnostic evidence would help explain a lane result, but it may not mutate
  `verification_commands`, create or satisfy an `evidence_requirement`, or
  strengthen/weaken the required command set during the same attempt.
- An orchestrator may accept supplemental command output only as auxiliary
  command evidence with `satisfies_requirement_ids: []` after the command spec,
  safety classification, and rationale are persisted in attempt history. If the
  supplemental command should become required evidence, the orchestrator must
  create a material plan revision, rotate the packet, add the command and its
  requirement before launch, and rerun the lane.
- A supplemental `write-local-ephemeral` command is auxiliary only, requires a
  declared output path outside the target set, and requires an approved cleanup
  policy before execution.
- Any command that deploys, migrates, deletes, changes remote state, changes
  credentials, or has uncertain external side effects is `external-state` or
  `destructive` and requires renewed human approval before execution.
- Verifier authority never bypasses filesystem, network, credential, or tool
  permission controls.
- A command whose safety class cannot be determined is treated as
  `external-state` and remains blocked pending human decision.

## Evidence Model

### Environment Fingerprint

Environment-bound lanes resolve this immutable record before launch:

```yaml
environment_fingerprint:
  fingerprint_id: <stable-id>
  environment_id: <approved-environment-id>
  baseline_ref: <approved-plan-environment-record-ref>
  components: {}
  derivation_method: <canonical-inspector-or-registry-method-id>
  source_revision: <revision-or-hash>
  observed_at: <timestamp>
  fingerprint_hash: <sha-256>
```

`components` is a sorted map of approved non-secret identity keys and exact
UTF-8 string values. Required keys come from `baseline_ref`; absent, extra,
secret-bearing, or unknown keys invalidate the record. `fingerprint_hash` is the
lowercase SHA-256 of schema-order UTF-8 JSON containing `environment_id`,
`baseline_ref`, `components`, `derivation_method`, and `source_revision`, with no
insignificant whitespace. Freshness compares those canonical hashes and rejects
records whose baseline reference was not approved by the active plan revision.

### Evidence Bundle

One verifier attempt returns one immutable bundle:

```yaml
verification_evidence_bundle:
  evidence_bundle_id: <immutable-id>
  lane_id: <lane-id>
  lane_type: <canonical-type>
  section_id: <section-id>
  target_ref: <complete-verification-target-ref>
  authority_subject: <complete-authority-subject>
  model_resolution_ref: <resolution-id>
  dispatch_revision: <revision>
  packet_id: <packet-id>
  attempt_id: <attempt-id>
  started_at: <timestamp>
  finished_at: <timestamp>
  command_evidence_refs: []
  artifact_evidence_refs: []
  environment_evidence_refs: []
  environment_fingerprint_ref: <fingerprint-id-or-null>
  environment_change_token_id: <stable-token-type-or-null>
  observed_environment_change_token: <opaque-value-or-null>
  disposition: PASS | FAIL | BLOCKED | SKIPPED
  summary: <bounded-summary>
  blocker_reason: <reason-or-null>
  skip_reason: <reason-or-null>
  supersedes_evidence_bundle_id: <id-or-null>
```

Evidence bundles are append-only. Correction creates a new bundle and
supersedes the erroneous one through an append-only applicability record;
accepted history is never edited in place.

Bundle applicability is tracked outside the immutable bundle body:

```yaml
evidence_applicability_record:
  applicability_record_id: <immutable-id>
  evidence_bundle_id: <owning-bundle-id>
  supersedes_applicability_record_id: <id-or-null>
  applicability: current | stale | wrong-target | identity-conflict | superseded
  reason_code: target-changed | plan-changed | profile-changed | floor-changed | model-resolution-invalid | candidate-facts-invalid | environment-changed | ttl-expired | repair-overlap | wrong-target | identity-conflict | superseded | initial-acceptance
  evaluated_against_target_ref: <complete-verification-target-ref>
  evaluated_against_dispatch_revision: <revision>
  evaluated_against_profile_schema_version: 1
  evaluated_against_profile_hash: <sha-256>
  evaluated_against_floor_schema_version: 1
  evaluated_against_floor_hash: <sha-256>
  evaluated_at: <timestamp>
```

The latest non-superseded applicability record for an evidence bundle is the
only current applicability truth. Staleness, wrong-target classification,
identity conflicts, and supersession append a new applicability record; they
never mutate the original bundle or its earlier applicability records. The
orchestrator, not the verifier, creates the initial applicability record during
acceptance and links it to the immutable bundle by `evidence_bundle_id`; the
returned bundle never references an applicability record that does not exist yet.

Any `result_artifact_ref` or `produced_artifact_ref` resolves to:

```yaml
evidence_result_artifact:
  result_artifact_id: <stable-id>
  repository_relative_path: <path>
  artifact_kind: command-output | render | package | inspection-report
  content_hash: <sha-256>
  size_bytes: <nonnegative-integer>
  producer_evidence_id: <command-or-artifact-evidence-id>
  overlaps_verification_target: false
```

The referenced file must exist, remain repository-contained, match its hash and
size, and be outside the immutable verification target. A verifier-generated
result artifact is evidence only; it cannot replace or mutate the target.

### Artifact Evidence

Each `artifact_evidence_ref` resolves to an append-only record:

```yaml
artifact_evidence:
  artifact_evidence_id: <stable-id>
  evidence_bundle_id: <owning-bundle-id>
  lane_id: <artifact-verification-lane-id>
  target_ref: <complete-verification-target-ref>
  target_set_member_ref: <canonical-member-ref-or-null>
  target_set_member_hash: <sha-256-or-null>
  observation_type: existence | structure | content | render | package
  tool_or_method: <deterministic-tool-command-or-inspection-method>
  observed_at: <timestamp>
  observed_content_hash: <sha-256-or-null>
  satisfies_requirement_ids: []
  result: PASS | FAIL | BLOCKED
  summary: <bounded-factual-summary>
  produced_artifact_refs: []
```

An artifact-verification lane is acceptable only when every referenced record
belongs to the same bundle and lane, matches the complete frozen target identity,
uses the current observed content hash, and collectively covers every artifact
observation required by the lane contract. `observed_content_hash` may be null
only for an `existence` observation whose result is `FAIL` or `BLOCKED` because
the target could not be read; every `PASS` and every non-existence observation
requires the exact observed SHA-256. A `FAIL` or `BLOCKED` record cannot support
a `PASS` bundle. Rendered or packaged outputs are supporting artifacts;
their refs and hashes do not replace the source target identity. Missing,
wrong-target, stale, cross-bundle, or internally contradictory records make the
bundle unacceptable.

For a `single` target, `target_set_member_ref` and `target_set_member_hash` are
null. For an `aggregate` target, each member-level artifact evidence record
must identify exactly one target member by canonical member reference and the
SHA-256 hash of that canonical member reference. Required member coverage is
proved only when every required member has current passing artifact evidence for
the same bundle target. Whole-set render or package observations may set
`target_set_member_ref: null` only when they also bind to the aggregate
`target_set_hash`; they supplement member coverage and do not replace required
per-member evidence unless the lane requirement explicitly accepts whole-set
package evidence.

### Environment Evidence

Each environment requirement resolves to one append-only record:

```yaml
environment_evidence:
  environment_evidence_id: <stable-id>
  evidence_bundle_id: <owning-bundle-id>
  lane_id: <lane-id>
  environment_id: <approved-environment-id>
  environment_fingerprint_ref: <fingerprint-id>
  environment_change_token_id: <stable-token-type-or-null>
  observed_environment_change_token: <opaque-value-or-null>
  satisfies_requirement_ids: []
  observed_at: <timestamp>
  result: PASS | FAIL | BLOCKED
  summary: <bounded-factual-summary>
```

Each claimed requirement must be an environment requirement for the same
environment ID. A requirement is satisfied only by a current `PASS` record with
a fingerprint approved by the active plan and, when configured, a matching
change-token observation. `FAIL` or `BLOCKED` records participate in disposition
precedence but cannot satisfy a requirement. Bundle-level fingerprint and token
fields must equal the environment record when exactly one environment is in
scope; multi-environment lanes require one record per environment and leave the
bundle-level shorthand fields null.

### Command Evidence

Every command evidence record describes either one executed command or one
approved skip:

```yaml
command_evidence:
  command_evidence_id: <immutable-id>
  evidence_bundle_id: <owning-bundle-id>
  lane_id: <lane-id>
  command_id: <command-spec-id>
  normalized_command: <exact-display-form>
  command_spec_hash: <sha-256>
  verifier_execution_id: <execution-id>
  verifier_attempt_id: <attempt-id>
  target_ref: <complete-verification-target-ref>
  working_directory: <repository-relative-path>
  safety_class: <class>
  approval_ref: <decision-ref>
  started_at: <timestamp-or-null>
  finished_at: <timestamp-or-null>
  exit_code: <integer-or-null>
  timed_out: true | false
  bounded_stdout_summary: <text-or-null>
  bounded_stderr_summary: <text-or-null>
  stdout_truncated: true | false
  stderr_truncated: true | false
  stdout_captured_bytes: <nonnegative-integer>
  stderr_captured_bytes: <nonnegative-integer>
  stdout_original_bytes: <nonnegative-integer-or-null>
  stderr_original_bytes: <nonnegative-integer-or-null>
  result_artifact_ref: <path-and-hash-or-null>
  satisfies_requirement_ids: []
  disposition: pass | fail | blocked | skipped
  rationale: <supplemental-or-skip-rationale-or-null>
```

Raw output larger than the declared bound is stored as a result artifact with a
content hash or is truncated with explicit truncation metadata. A summary alone
must not conceal a nonzero exit, timeout, missing output, or skipped command.
When a stream is truncated, its flag is true, captured bytes equal the retained
byte count, and original bytes record the pre-truncation count when knowable;
unknown original size is null. When not truncated, the flag is false and
original bytes equal captured bytes. Truncation without a bounded summary and
either a hashed result artifact or explicit original-size accounting is invalid.
For `skipped` command evidence, `started_at`, `finished_at`, `exit_code`,
bounded output summaries, byte counts, and `result_artifact_ref` are null or zero
as appropriate, and `rationale` plus an optional-command or approved-plan
decision reference are mandatory. Non-skipped command evidence must have non-null
`started_at` and `finished_at`.

### Acceptance Rules

The orchestrator accepts a bundle only when:

- lane, packet, attempt, target, dispatch revision, and active execution match
- authority identity passes both role and conflict checks
- actual model resolution meets the lane's capability floor
- every required command and evidence requirement has one terminal current
  record for the same target
- command safety and approval references are valid
- bundle disposition is mechanically consistent with command records
- target and environment freshness checks pass

`PASS` is rejected when any required command failed, blocked, timed out, or was
skipped, or when a required result artifact is absent. For initial acceptance,
the orchestrator evaluates all acceptance predicates except prior applicability,
then atomically persists the bundle reference plus a new
`evidence_applicability_record` with `applicability: current` and
`reason_code: initial-acceptance`. After that initial record exists, any later
aggregation, resume, phase acceptance, scoring, or close rejects the bundle when
the latest applicability record for the bundle is not `current`.

## Staleness And Invalidation

Evidence applicability is recomputed before lane aggregation, phase acceptance,
score production, resume, and close.

Evidence becomes `stale` when any of these is true:

- target `artifact_revision`, `content_hash`, member identity, or target-set hash
  changes within the lane's declared scope
- the accepted plan changes the lane's commands, evidence requirements,
  environment scope, freshness policy, or capability floor
- the referenced model capability profile or floor content hash changes
- the selected model resolution, selected candidate facts, launch-environment
  facts, or their provenance revisions are invalidated or later discovered not
  to meet the recorded profile/floor
- an environment-bound claim observes a different environment fingerprint
- an environment-bound bundle exceeds its declared `max_age_seconds` for any
  required environment evidence record, measured independently from that
  record's `observed_at` timestamp
- an accepted repair changes any artifact in the frozen target reference: for a
  single target, its path, revision, anchor, or content hash; for an aggregate
  target, any target-set member identity or the target-set hash

Evidence becomes `wrong-target` when the returned immutable target never matched
the packet target. It becomes `identity-conflict` when role isolation fails. It
becomes `superseded` only when a newer accepted bundle explicitly replaces it.
Each transition is persisted as a new `evidence_applicability_record`.

File-content evidence has no time-to-live unless its lane explicitly declares
one. Deployment and other external-state claims must be environment-bound and
must declare either a positive `max_age_seconds` or a durable environment change
token that can prove the observation remains current.

When token-based freshness is used, the lane declares
`environment_change_token_id` and each bundle persists both that ID and the
observed opaque value. Rechecking freshness reads the same token type in the same
environment: equality keeps the observation current, inequality makes it stale,
and an absent, unreadable, or differently typed token blocks initial acceptance.
If a previously accepted bundle cannot re-read the same token type during
aggregation, resume, or close, the orchestrator appends an applicability record
with `applicability: stale` and `reason_code: environment-changed`; the lane
must be rerun to produce new current evidence, or the plan must receive a
material revision that replaces or removes the lane requirement before
aggregation can be satisfied. Human reapproval never revives the stale bundle
under its old requirement. Token values are compared as exact UTF-8 strings and
must not contain secrets.

Stale evidence remains append-only history. It cannot satisfy a required lane,
cannot be revived by changing a label, and cannot authorize
`VERIFICATION_ACCEPTED`, `REVERIFICATION_ACCEPTED`, scoring, or close. After a
repair, every overlapping required verifier lane runs again against the repaired
target; non-overlapping lanes remain current only when their frozen target
references and environment dependencies prove no overlap. Selector coverage that
changes after freeze requires a material plan revision and new target selection.

## Model Capability Profiles

### Separation Of Concerns

- persona answers which professional viewpoint is used
- runtime role answers which actions are authorized
- capability profile answers which execution abilities the model and launch
  environment must provide
- concrete model identity is a launch-time resolution result, not a planning key

### Profile Schema

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

The initial portable labels are:

| Profile | Intended use | Required minimum |
|---|---|---|
| `artifact-inspection` | inspect documents, designs, generated artifacts, and hashes | repository and filesystem read, structured output |
| `tool-verification` | execute local verification commands and capture evidence | artifact-inspection plus command execution and bounded evidence capture |
| `environment-verification` | inspect approved remote or deployed state | tool-verification plus the explicitly approved network/tool classes |
| `deep-verification` | high-ambiguity or high-risk verification requiring stronger reasoning | the underlying tool profile plus `reasoning_tier: deep` |

Profiles declare minimums, not model names. A lane may strengthen a profile but
may not weaken its task-profile or risk-trigger floor.

Capability floors are closed, versioned records rather than opaque labels:

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

Candidate and launch-environment capabilities are normalized to the same keys
as the floor. Tier ordering is `standard < strong < deep` for reasoning and
`standard < large` for context. Floor evaluation is split by fixed capability
ownership. The selected model must meet model-owned requirements: reasoning
tier, context tier, `structured_output`, and `multimodal_inspection`. The launch
environment must meet launch-environment-owned requirements: repository access,
command execution, filesystem access, network access, and required/prohibited
tool classes. The combined resolution meets a floor only when both owned
evaluations meet their required tiers, booleans, required tool classes, and
prohibited tool-class exclusions. Unknown keys, unknown tier labels, missing
capability facts, or incompatible floor schema produce `floor_result: unknown`,
never an inferred pass. `profile_hash` and `floor_hash` are lowercase SHA-256
digests of their respective schema-order UTF-8 JSON records excluding the hash
field itself; arrays are sorted unique and capability maps use the closed key
order. A changed record therefore has a new content identity even when its
human-readable ID is unchanged. Profile requirements and floor requirements are
combined by boolean union, maximum tier, required tool union, and prohibited
tool union; any required/prohibited collision is an invalid plan. The resolution
record persists the exact floor ID and schema version used so comparison is
reproducible.

### Resolution Record

Every launch persists:

```yaml
model_candidate_capability_facts:
  candidate_id: <provider-and-model-id>
  model_version: <version-or-null>
  reasoning_tier: standard | strong | deep
  context_tier: standard | large
  capabilities: {}
  tool_classes: []
  provenance:
    source_type: runtime-registry | provider-metadata | approved-project-record
    source_ref: <stable-reference>
    source_revision: <revision-or-hash>
    observed_at: <timestamp>
```

Candidate IDs are unique within one resolution. Capability keys must be the
closed floor keys; absent facts remain unknown rather than false. Tool classes
are sorted unique canonical IDs. The resolver hashes each schema-order candidate
record and stores that hash in `candidate_models`, making the evaluated facts and
their provenance reproducible. Missing provenance or an unresolvable source
revision yields `floor_result: unknown`.

The launch environment uses the parallel closed record:

```yaml
launch_environment_capability_facts:
  launch_environment_id: <stable-environment-id>
  capabilities: {}
  tool_classes: []
  provenance:
    source_type: runtime-registry | approved-project-record
    source_ref: <stable-reference>
    source_revision: <revision-or-hash>
    observed_at: <timestamp>
  capability_facts_hash: <sha-256>
```

It uses the same closed capability keys, sorted tool IDs, unknown handling, and
provenance requirements as model candidates. Its hash is the lowercase SHA-256
of schema-order UTF-8 JSON excluding `capability_facts_hash`. The selected model
and launch environment must each meet the capabilities they own; the combined
evaluation may not infer one side's missing capability from the other.

Ownership is fixed. Model facts own `reasoning_tier`, `context_tier`,
`structured_output`, and `multimodal_inspection`. Launch-environment facts own
`repository_read`, `command_execution`, `filesystem_read`,
`filesystem_ephemeral_write`, `network_access`, and all required or prohibited
tool classes. A floor capability is evaluated only against its owning record.
If a future capability cannot be assigned by this table, resolution is
`unknown` until a later schema revision assigns it; implementations may not use
cross-record compensation.

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

The resolution record belongs to exactly one launch identity. Its `execution_id`,
`packet_id`, `attempt_id`, `resolution_target_ref`, requested profile hash, and
floor hash must match the accepted evidence bundle and lane record before any
bundle can be considered current.

### Fallback Rules

The resolver evaluates available candidates against required capabilities and
the minimum floor before launch.

- A different concrete model is allowed without renewed approval only when all
  required capabilities and the declared floor are met.
- Every fallback is recorded even when it remains within floor.
- `below-floor` or `unknown` blocks launch under the current plan.
- The human may approve a material plan revision that lowers the floor, changes
  the lane, changes commands, or accepts a different execution route. Human
  approval may not relabel a below-floor run as valid under the old plan.
- Evidence from a model later discovered to have lacked a required capability is
  marked stale with `reason_code: model-resolution-invalid` or
  `candidate-facts-invalid`, and the lane must be rerun with a compliant
  resolution.
- Persona eligibility never compensates for a missing model or tool capability.

## Lifecycle Integration

For an active future `task-runtime-v1` section:

1. `EXECUTION_RESULT_ACCEPTED` freezes the producer target and enters
   `verify/queued`.
2. The orchestrator resolves required verifier lanes, authority subjects, and
   capability profiles before `PHASE_STARTED`.
3. Lane attempts run under the section's aggregate `verify/running` state.
4. Each return is persisted, checked, and followed by exactly one aggregate
   lane event from the lifecycle foundation.
5. Only when every required lane has one accepted current `PASS` bundle for that
   lane's own frozen `verification_target_ref`, and the set of required lane
   target refs equals the section verification target set selected by the
   approved plan, may the orchestrator synthesize verification and emit
   `VERIFICATION_ACCEPTED` from `verify/review-pending`.
6. After `fix`, the same rules apply in `re-verify`; successful current bundles
   permit `REVERIFICATION_ACCEPTED` from `re-verify/review-pending`.

`FAIL` and `BLOCKED` do not advance phase. Their persisted form determines the
event path. A verifier attempt that crashes, loses its execution environment, or
cannot return a valid terminal bundle is an execution failure; while the
aggregate is `running`, it uses `SECTION_FAILED_FROM_RUNNING` and enters
`<lane-phase>/failed`. A verification command's nonzero result or a factual
mismatch is recorded as lane disposition `FAIL`, not as an execution failure.
A verifier-returned valid terminal bundle with derived disposition `FAIL` or
`BLOCKED` is terminal lane evidence, not an immediate controller blocker;
aggregation continues until every required lane is terminal, emits
`REQUIRED_LANES_RETURNED`, then uses `SECTION_BLOCKED_FROM_REVIEW` because no
complete required PASS set exists. The resulting blocked state preserves the
accepted FAIL/BLOCKED evidence for later human recovery, repair, or material
revision decisions, but this design does not define those later policies.
Only blockers that prevent valid lane launch or valid bundle acceptance, such as
missing prerequisite context, missing command approval before execution,
authority identity conflict, wrong target, or below-floor/unknown model
resolution, use the foundation's `SECTION_BLOCKED_FROM_QUEUED`,
`SECTION_BLOCKED_FROM_RUNNING`, or `SECTION_BLOCKED_FROM_REVIEW` event matching
the current state and enter `<lane-phase>/blocked` immediately. The foundation
intentionally has no failed-from-review transition. Detailed repair
authorization, retry limits, scoring, and close policy remain owned by later
rounds.

## Recovery Boundary

Resume uses durable section state, lane records, attempt history, target
identity, evidence bundles, and model resolutions. Chat text is never recovery
authority.

On resume, the orchestrator:

1. validates the lifecycle snapshot and event head under the foundation contract
2. recomputes the selected required lanes from the approved plan and compares
   them with persisted lane records
3. reconciles each active execution and attempt
4. rechecks authority isolation and model floor
5. recomputes target and environment freshness for every accepted bundle
6. rebuilds required-lane aggregation from current accepted bundles only
7. resumes from the persisted section `next_action`

An interrupted attempt with no terminal evidence bundle is
`reconciliation-required`. Partial command evidence remains diagnostic and
cannot produce `PASS`. If the command was local and safely repeatable, an
orchestrator-approved retry preserves `execution_id` and rotates `attempt_id`.
If payload, commands, target, profile, or authority subject changes, `packet_id`
also rotates. If an external-state or destructive command may have partially
executed, automatic replay is forbidden; the section blocks for human
reconciliation and a newly approved recovery action.

This design does not define generic `OnBlocked` hooks, repair loops, retry
budgets, or compaction hooks. It defines only the records and no-false-pass
boundary those later mechanisms must preserve.

## Invalid States

A later validator round must reject at least:

- verifier fields used as lifecycle authority while protocol is `legacy`
- `runtime_role: verifier` bound to a worker, reviewer, explorer, or orchestrator
  prompt or role binding
- verifier authority subject sharing `agent_id` or `execution_id` with a producer,
  reviewer, or orchestrator in the same target lineage
- one persona binding crossing worker, verifier, and reviewer roles in one lineage
- verifier mutation of the target or repair during a verifier attempt
- worker self-check or reviewer finding referenced as formal verification
- evidence bundle with a mutable or incomplete target reference
- `PASS` with missing, failed, blocked, timed-out, skipped, stale, wrong-target,
  conflicted, or superseded required command evidence
- required lane satisfied by `SKIPPED`
- required baseline or triggered lane removed without an approved material plan
  revision
- lane selection with unresolved artifact or environment targets
- deduplication of lanes whose targets, environments, commands, freshness, or
  capability floors differ
- supplemental external-state or destructive command without renewed approval
- persisted secret values in command or evidence records
- model launch with `below-floor` or `unknown` capability result
- silent model fallback or fallback without a resolution record
- individual lane record owning section `runtime_state` or `lifecycle_phase`
- `VERIFICATION_ACCEPTED` or `REVERIFICATION_ACCEPTED` without current accepted
  `PASS` evidence for every required lane and the same immutable target
- stale pre-fix evidence satisfying re-verification
- interrupted or late attempt advancing aggregation without active-attempt
  reconciliation
- automatic replay of an uncertain external-state or destructive command
- evidence edited in place instead of superseded append-only

## Acceptance Criteria

- Worker, verifier, reviewer, orchestrator, and human permissions are explicit
  and non-overlapping.
- Formal verifier authority uses future `runtime_role: verifier` without changing
  current bindings in this round.
- Identity isolation is defined by immutable runtime identities, enforced before
  launch and acceptance, and scoped to a target lineage.
- Single and aggregate target identity is exact and compatible with the existing
  reviewer target revision rules.
- Worker, verifier, and reviewer lanes are separate durable collections.
- The four canonical verifier lane types have exact claims and minimum evidence.
- Lane outcome semantics make required skips, failures, blockers, conflicts, and
  stale results non-passing.
- Baseline task profiles, risk triggers, deterministic union/deduplication, and
  material exclusions are implementation-ready.
- Command records define normalization, safety classes, approval boundaries,
  output bounds, secret handling, and supplemental-command policy.
- Evidence bundles and command evidence are immutable, revision-bound, and
  mechanically acceptable or rejectable.
- Target, plan, command, environment, repair, and time-based staleness rules are
  explicit, while content-only evidence has no accidental time-to-live.
- Persona, runtime role, capability profile, and concrete model resolution remain
  distinct persisted concepts.
- Same-floor fallback is durable and allowed; below-floor or unknown resolution
  blocks until a material approved revision.
- Verify and re-verify integrate with the lifecycle foundation without adding a
  new phase owner or canonical execution state.
- Interrupted attempts cannot manufacture a pass, and uncertain external-state
  commands are never replayed automatically.
- The design contains no activation, bindings, personas, validator code, hooks,
  repair policy, scoring, or quality-gate implementation.

## Out Of Scope

- editing `SKILL.md`, active lifecycle contracts, prompt assets, packet contracts,
  templates, README, registries, or project personas
- adding `verifier` to `agents/openai.yaml` or creating verifier prompts/personas
- implementing lane selection, model resolution, command execution, persistence,
  orchestration, or runtime code
- assigning a concrete next schema version
- activating or migrating any round to `task-runtime-v1`
- defining named transition guards, hook predicates, compact checkpoints, or
  automatic blocked recovery
- defining repair authorization, repair-cycle limits, stagnation policy, or fix
  routing
- defining reviewer findings beyond the authority boundary with verification
- defining quality scores, thresholds, blockers, exception close, or scoring
  weights
- adding validator rule IDs, fixtures, or enforcement code
- changing current approval, strict-review, persona-selection, or legacy runtime
  behavior
- writing an implementation plan
