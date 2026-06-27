# Design Spec: Verifier Lane Authority Validator Dogfood Audit

## Artifact Metadata

- `schema_version`: 1
- `spec_status`: approved
- `case_slug`: task-runtime
- `round_slug`: 2026-06-27-verifier-lane-authority-validator-dogfood-audit
- `created_at`: 2026-06-27
- `updated_at`: 2026-06-27
- `source_dispatch_plan`: `docs/cases/task-runtime/rounds/2026-06-27-verifier-lane-authority-validator-dogfood-audit/dispatch-plan.md`
- `validator_under_audit`: `tools/validate_ww_verifier_authority_contracts.py`
- `validator_expansion_commit`: `6b6eaf2 Add verifier authority contract validation`

## Summary

The verifier/lane authority validator is sufficient as a dormant-contract sentinel for the current WorkWork stage. It confirms that the new verifier authority reference exists, that active docs/templates point to it, that the key dormant verifier fields remain present, that the active legacy packet role gate has not been widened, and that legacy dispatch plans do not render obvious active verifier authority blocks.

The validator is not a schema validator. Its coverage is mostly normalized fragment checks plus a legacy dispatch denylist. That is acceptable for the current dormant phase, but it leaves several realistic drift classes for a later hardening round if WorkWork moves closer to `task-runtime-v1` activation.

Recommendation: open a later validator hardening round only after one more contract expansion or before activating `task-runtime-v1`. The highest-value future work is targeted hardening for dispatch verifier lane schema shape, per-field negative fixtures, and safer legacy prose handling.

## Audit Scope

This audit reviewed whether the validator covers:

- `task-runtime-verification.md` reference existence and baseline contract vocabulary
- SKILL/README/template/packet contract linkage to dormant verifier authority
- legacy non-authority guard
- dispatch template verifier lane block
- packet dormant verifier gate and active legacy role gate
- working brief verification preparation
- negative fixtures
- repo-suite integration
- over-broad and under-broad behavior

Out of scope:

- editing validator code or tests
- adding verifier personas
- adding verifier runtime binding
- implementing verifier command execution
- implementing repair, scoring, hooks, routing expansion, secondary tags, or `task-runtime-v1` activation

## Coverage Matrix

| Surface | Rule/Test Evidence | Current Coverage | Classification |
|---|---|---|---|
| Dormant verifier reference exists | `WWVA001`, `test_rejects_missing_reference_file` | Requires `task-runtime-verification.md` and core vocabulary for dormant verifier authority, lanes, evidence, lane selection, model capability resolution, and legacy non-authority. | Sufficient for dormant stage |
| SKILL reference linkage | `WWVA002`, `test_rejects_skill_without_reference_link` | Requires link to `task-runtime-verification.md` and text saying dormant verifier fields are not consumed as legacy lifecycle authority. | Sufficient for dormant stage |
| README reference and guidance | `WWVA003`, `test_rejects_readme_without_legacy_non_authority_note`, CLI JSON test | Requires maintainer-visible validation/guidance and legacy non-authority boundary. | Sufficient for dormant stage |
| Dispatch verifier lane block | `WWVA004`, `test_rejects_dispatch_template_missing_model_resolutions` | Requires the template to contain the future verifier-lane block and key fields such as verifier lanes, target refs, evidence requirements, freshness policy, model profile, minimum floor, and model resolutions. | Partially sufficient |
| Packet dormant verifier gate | `WWVA005`, `test_rejects_packet_contract_without_active_legacy_role_gate` | Preserves the active legacy role set and requires future verifier packet fields to remain dormant/non-authorizing. | Sufficient for dormant stage |
| Working brief verification preparation | `WWVA006`, `test_rejects_working_brief_without_verification_preparation` | Requires planning fields for verifier authority notes, lane preparation, baseline/risk-triggered lane candidates, evidence kinds, model capability, and legacy non-authority note. | Sufficient for dormant stage |
| Legacy dispatch non-authority | `WWVA007`, `test_rejects_legacy_dispatch_with_active_verifier_lanes` | Scans legacy dispatch plans for active-looking verifier authority blocks or field names. | Useful but over-broad risk |
| Repo-suite integration | `validate_ww_repo.py` check plus full suite execution | The repo-level validator runs the new verifier/lane authority validator. | Sufficient operationally |

## Findings

### Finding 1: Dispatch Template Coverage Is Presence-Based

Severity: medium

The validator proves the dispatch template contains the expected verifier-lane fields, but it does not verify YAML shape, nesting, or field relationships. For example, a future edit could keep all required field names while moving `model_resolutions` outside the intended section or removing structural context that matters for `task-runtime-v1`.

Current impact is low because the verifier lane block is dormant and not consumed as runtime authority.

Future hardening candidate:

- parse or structurally slice the `Section Verification Lanes` example
- verify required keys under the expected block
- add negative fixtures for several individual fields, not only one representative field

### Finding 2: Negative Fixtures Are Representative, Not Exhaustive

Severity: medium

The test suite has one negative fixture per major rule, which is enough to prove the rule surfaces are wired and fail. It does not exhaustively test every required fragment or every realistic drift class. In particular, `WWVA004`, `WWVA005`, and `WWVA006` each validate multiple required fragments but have only one targeted removal/mutation test.

Current impact is acceptable because this validator is a lightweight sentinel, and full repo validation also exercises current real files.

Future hardening candidate:

- add parameterized negative fixtures for every required dispatch block key
- add packet contract fixtures for missing dormant fields and missing non-authorizing text
- add working brief fixtures for missing evidence/model capability/legacy note clauses

### Finding 3: Legacy Dispatch Denylist May Catch Legitimate Audit Prose

Severity: medium

`WWVA007` scans every legacy `dispatch-plan.md` for active-looking verifier authority markers. This is useful, but the denylist can become over-broad if a legacy audit dispatch plan intentionally quotes future field names with colon syntax while discussing why they are dormant.

Current impact is contained because the active dogfood dispatch plan avoids rendering active verifier field syntax and keeps detailed field analysis in `design-spec.md`, which `WWVA007` does not scan.

Future hardening candidate:

- restrict the legacy guard to fenced YAML blocks under active verifier-lane headings
- distinguish quoted prose from rendered authority blocks
- keep a negative fixture for active block rendering and a positive fixture for harmless explanatory prose

### Finding 4: Repo-Suite Integration Is Operational But Not Unit-Protected

Severity: low

The repo-level suite includes the new validator, and full validation passes. The verifier validator test suite does not include a direct unit test that mutates `validate_ww_repo.py` to prove the integration line itself is protected.

Current impact is low because full repo validation output explicitly shows the verifier/lane authority check, and README documents the standalone validator.

Future hardening candidate:

- add a lightweight repo-suite integration regression test only if this pattern becomes common across multiple contract validators

### Finding 5: Dormant Stage Does Not Yet Need Full Semantic Validation

Severity: low

The validator intentionally does not enforce runtime verifier behavior, command evidence, verifier packet generation, model floor compatibility, freshness, repair overlap, or close-gate semantics. That is correct for this stage because these fields are dormant and `task-runtime-v1` is not active.

Current impact is positive: the validator avoids prematurely activating runtime behavior.

Future hardening candidate:

- defer semantic validation until a later activation design explicitly selects `task-runtime-v1`

## Over-Broad Risk

The main over-broad risk is `WWVA007`. It treats exact active-looking strings in legacy dispatch plans as violations regardless of surrounding context. This is appropriate for preventing accidental authority rendering, but it can block a future legacy audit dispatch plan that quotes field syntax directly.

Mitigation for now:

- keep detailed field examples in design specs or references, not legacy dispatch plans
- avoid colon-suffixed active verifier field syntax in legacy dispatch plan prose

Later hardening may make this rule more precise.

## Under-Broad Risk

The main under-broad risk is that normalized fragment checks can pass even when schema shape or intended section ownership is damaged. The validator checks that important words exist, not that they are arranged as a parseable contract.

Mitigation for now:

- treat the validator as a sentinel, not as a task-runtime verifier schema compiler
- require dogfood/audit rounds before activating any future runtime protocol

Later hardening should target structural parsing for the dispatch verifier-lane block first.

## Hardening Decision

Do not open an immediate hardening implementation round solely from this audit.

Open a later validator hardening round when either condition becomes true:

- WorkWork starts a concrete `task-runtime-v1` activation path.
- A future contract change adds more verifier-lane fields or changes the dispatch verifier lane schema.

Recommended future hardening round, when triggered:

`verifier lane authority validator hardening`: add structural dispatch verifier-lane block checks, parameterized negative fixtures for required verifier packet/working brief fields, and a positive legacy prose fixture so `WWVA007` blocks active authority rendering without blocking harmless audit prose.

## Acceptance Criteria

- Every requested dogfood surface is explicitly classified.
- No validator, contract, template, README, SKILL, packet contract, persona, project registry, or runtime code is modified by this round.
- The report distinguishes current sufficiency from future hardening candidates.
- The final recommendation says whether a hardening round is needed now.

## Conclusion

The validator is good enough for the current dormant verifier authority stage. It should remain as-is for now. The next hardening should wait until `task-runtime-v1` activation becomes concrete or the verifier lane schema changes again.
