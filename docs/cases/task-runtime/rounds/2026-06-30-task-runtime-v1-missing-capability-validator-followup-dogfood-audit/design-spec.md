# Design Spec: Task Runtime V1 Missing Capability Validator Dogfood Audit

## Artifact Metadata

- `schema_version`: 1
- `design_status`: review-pending
- `case_slug`: task-runtime
- `round_slug`: 2026-06-30-task-runtime-v1-missing-capability-validator-followup-dogfood-audit
- `created_at`: 2026-06-30
- `updated_at`: 2026-06-30
- `artifact_type`: dogfood_audit_gap_report

## Scope

This audit reviews the existing missing-capability validator expansion for
coverage, fixture strength, JSON output, repo-suite integration, and
overbroad or underbroad checks.

The audit does not change validator behavior, fixtures, contract docs,
personas, project registry, runtime binding, command execution, routing,
packet assembly, repair/scoring/hooks, or `task-runtime-v1` activation.

## Evidence Commands

```text
python tools\validate_ww_missing_capability_contracts.py
PASS: 7 rules checked

python tools\validate_ww_missing_capability_contracts.py --json
ok: true
rule_failures: 0
results: WWMC001-WWMC007 passed

python -m unittest tools.test_validate_ww_missing_capability_contracts -v
Ran 9 tests
OK

python tools\validate_ww_repo.py --json
repo_ok: true
Missing-capability contract validation: ok true
payload.rule_failures: 0
```

## Coverage Matrix

| Audit Surface | Current Coverage | Dogfood Assessment |
| --- | --- | --- |
| `task-runtime-missing-capabilities.md` reference linkage | WWMC001 checks the reference file and required record family names. | Covered. The rule catches deleted reference content, but does not validate deeper prose semantics. That is acceptable for the dormant contract layer. |
| SKILL guidance | WWMC002 checks the packaged `SKILL.md` linkage and legacy non-authority language. | Covered. The linkage is represented in both validator and negative fixtures. |
| README guidance | WWMC003 checks README linkage and dormant guidance. | Covered. The CLI JSON failure fixture also exercises this rule. |
| Dispatch template record families | WWMC004 checks the task-runtime-v1 missing capability block, all ten record family names, and the legacy omission rule. | Covered for template presence. Fixture coverage is broad enough for the current scaffold, but not per-family exhaustive. |
| Working brief `missing_capability_preparation` | WWMC006 checks the preparation field and dormant non-authority note. | Covered. The fixture mutates required wording and proves the guard fires. |
| Packet source-context dormant fields | WWMC005 checks packet contract source-context fields and dormant/non-authorizing language. | Covered. The validator correctly treats packet fields as dormant source context, not runtime authority. |
| Legacy non-authority guard | WWMC007 scans legacy dispatch plans for active missing-capability authority. | Partially covered. The guard catches full active blocks, but likely misses a legacy dispatch that contains only one active record family without the canonical heading. |
| Negative fixtures | The unittest suite has one valid fixture, rule-specific negative fixtures, a legacy guard fixture, and CLI JSON failure coverage. | Partially covered. Fixtures prove major breakage paths, but the legacy guard fixture does not isolate record-family fallback behavior. |
| JSON output | Standalone validator JSON includes `ok`, `rule_failures`, and per-rule `results`; tests cover a failure payload. | Covered. Standalone and repo-suite JSON both preserve the missing-capability result payload. |
| Repo-suite integration | `validate_ww_repo.py` includes `Missing-capability contract validation`; repo-suite JSON returns it as ok. | Covered. The new validator participates in the aggregate suite and JSON mode. |

## Findings

### P2: Single record-family legacy authority drift can pass

`legacy_dispatch_authority_violations()` flags legacy dispatch plans when the
canonical "Section Missing Capability Records" heading appears, or when at
least two missing-capability record family field names appear.

That means a legacy dispatch plan could likely contain a single active field
such as `internal_hook_records: []` without the heading and still pass WWMC007.
The user-requested contract says legacy rounds must not treat any of
`internal_hook_records`, `quality_gate_records`, `score_records`,
`repair_records`, `review_synthesis_records`,
`reverification_requirements`, `close_gate_records`,
`final_judgment_records`, `recovery_requirement_records`, or
`checkpoint_records` as active lifecycle authority. The current heuristic is
therefore underbroad for single-family drift.

Recommended hardening: add a fixture that inserts one YAML-like active record
family into a legacy dispatch plan without the heading, then tighten WWMC007 to
reject active record-family assignments while still allowing dormant prose.

### P2: Legacy guard fixture does not isolate record-family fallback

`test_rejects_legacy_dispatch_with_active_missing_capability_block` appends the
canonical heading plus record family fields. Because the heading alone is
sufficient to trigger WWMC007, the test does not prove the `matched_records`
fallback detects record-family authority drift.

Recommended hardening: split the legacy fixtures into at least:

- heading-only active block fixture
- single record-family assignment without heading
- multiple record-family assignments without heading
- dormant/prose-only mention that must remain accepted

### P3: Record-name prose can become a false positive

The current fallback counts record family names in normalized text. A legacy
dispatch plan that mentions two raw field names in explanatory prose could be
flagged even when it does not create an authority block. Existing safe-prose
coverage uses ordinary phrases such as "internal hooks" and "close gates", not
raw field names.

Recommended hardening: scope record-family detection to YAML-like assignments,
template blocks, or a bounded "Section Missing Capability Records" region
instead of matching raw field names anywhere in the file.

## Activation Readiness Implication

The missing-capability validator is good enough as a dormant contract scaffold:
it proves reference linkage, template presence, packet source-context language,
working brief preparation, JSON output, and repo-suite integration.

It is not yet activation-grade for legacy non-authority enforcement. Before
`task-runtime-v1` activation or any runtime pilot that depends on these guards,
WorkWork should run a focused validator hardening round for WWMC007 fixture
isolation and single-record-family detection.

## Recommendation

Open a follow-up validator hardening round.

Suggested scope:

- harden `legacy_dispatch_authority_violations()` so any YAML-like active
  missing-capability record family in a legacy dispatch plan fails WWMC007
- preserve dormant prose examples that mention missing-capability concepts
- add isolated negative fixtures for heading-only, single-family, and
  multi-family legacy drift
- keep the change limited to validator/tests and necessary test notes
- do not alter dormant contracts, personas, routing, packet assembly, runtime
  command execution, repair/scoring/hooks, or `task-runtime-v1` activation
