# Runtime Persona Packet Validator Dogfood Gap Report

## Status

- Report Status: approved
- Date: 2026-06-01
- Scope: audit and classification only
- Source Commit: `b97f1b3`
- Recommendation: defer canonical slice resolver design

## Audit Question

Does the pushed runtime persona packet validator provide enough artifact and fixture evidence for its current contract, and is there a demonstrated need to open a canonical slice resolver design round?

## Evidence Reviewed

- `tools/validate_ww_persona_packets.py`
- `tools/test_validate_ww_persona_packets.py`
- `tools/validate_ww_repo.py`
- the persisted worker and reviewer packets under the runtime persona packet dogfood pilot round
- the approved dispatch plan that produced those packet artifacts
- the runtime persona packet validator expansion round

## Verification Snapshot

- Focused regression suite: `13` tests passed.
- Persisted packet validator: `PASS: 16 rules checked`.
- Real artifacts scanned: one worker packet and one reviewer packet.
- Aggregate repo suite integration: present under `Runtime persona packet artifact validation`.

## Coverage Classification

| Surface | Classification | Evidence | Notes |
| --- | --- | --- | --- |
| real packet artifacts | covered | repository scan uses `docs/cases/**/packets/*.md`; pilot worker and reviewer packets produce `16` passing rule checks | Current repo evidence is artifact-backed, not fixture-only. |
| negative drift fixtures | covered with a small hardening opportunity | focused suite covers worker-principle drift, role-prompt mismatch, target-hash drift, dispatch-snapshot drift, malformed nested binding, absolute dispatch path, and absolute reviewer target path | The suite is representative. It does not separately pin `..` traversal escape as a named negative fixture. |
| full-file hash fallback | covered | reviewer target validation recomputes the referenced full file SHA-256 when `artifact_revision` begins with `sha256:` and requires both revision and content hash to match | The real reviewer packet dogfoods this path. |
| explicit-revision excerpt identity | bounded coverage by design | focused fixtures accept a non-empty explicit document revision plus a well-formed SHA-256 content hash | The validator preserves excerpt identity but does not recompute a canonical excerpt slice. No real excerpt-backed packet artifact currently proves slice assembly. |
| repo-relative path containment | implemented and representative-fixture covered | path resolution rejects absolute paths and resolved paths outside repo root; focused fixtures reject absolute dispatch and reviewer target paths | A future narrow test-hardening change may add explicit `..` traversal fixtures without changing the contract. |
| multi-section snapshot | covered | focused fixture inserts an earlier misleading section and confirms packet comparison uses `source_section_id` | Section-aware dispatch snapshot selection is exercised. |
| secondary reviewer lane | covered | focused fixture selects a secondary reviewer from a durable lane and confirms the snapshot resolves | Reviewer snapshot extraction is not restricted to the primary planned reviewer. |
| repo suite integration | covered | `tools/validate_ww_repo.py` invokes `tools/validate_ww_persona_packets.py` as an aggregate check | Packet validation participates in standard repository verification. |

## Findings

### PVDA-001: Current packet validator contract is adequately dogfooded

- Severity: none
- Classification: pass

The validator runs against persisted pilot artifacts as well as synthetic fixtures. Its current contract is supported by real full-file packet evidence, focused drift rejection, section-aware snapshot matching, secondary reviewer lane handling, and aggregate repo integration.

### PVDA-002: Path containment has a narrow fixture-hardening opportunity

- Severity: low
- Classification: follow-up optional

The implementation resolves repository-relative paths and rejects values that escape the repository root. Existing fixtures prove rejection of absolute source and target paths. A later narrow test-only hardening change could explicitly cover `../` traversal and, if the supported platform policy requires it, symlink escape behavior. This does not expose a contract gap and does not justify changing the validator in this audit round.

### PVDA-003: Explicit-revision excerpt identity is intentionally not canonical slice verification

- Severity: informational
- Classification: deferred design trigger

For explicit document revisions, the validator requires a non-empty revision token and a SHA-256-shaped content hash. It intentionally does not derive a slice from a section anchor and recompute that excerpt hash. This is an honest boundary: current evidence proves identity persistence, not canonical excerpt assembly.

## Canonical Slice Resolver Decision

Do not open a canonical slice resolver design round yet.

The pushed validator meets its current packet-artifact contract. A resolver design round would be premature because the repository does not yet contain a real excerpt-backed packet artifact, and stable slice semantics have not been demonstrated.

Open that design round only when at least one real workflow needs excerpt-backed review targeting and the following questions can be answered from concrete evidence:

1. Which selector identifies the slice: section anchor, explicit line range, structured node identity, or another durable key?
2. What normalization rules apply before hashing?
3. How should missing, duplicated, renamed, or reordered anchors behave?
4. Which immutable full-artifact revision anchors the slice?
5. Must packet assembly and validator recomputation share one canonical resolver?

## Follow-Up Classification

- Canonical slice resolver design: deferred until real excerpt-backed packet evidence exists.
- Optional packet validator fixture hardening: add explicit traversal-containment cases in a later focused test-only round if desired.
- Validator implementation changes: not required by this audit.
- Packet contract changes: not required by this audit.
- Runtime code changes: not required by this audit.

## Review Checklist

- [x] Current claims stay within persisted artifact and fixture evidence.
- [x] Full-file and explicit-revision excerpt semantics remain distinct.
- [x] Optional fixture hardening is not overstated as a validator gap.
- [x] Canonical slice resolver design is deferred behind concrete entry criteria.
- [x] No validator, packet contract, runtime code, persona, registry, routing, or secondary-tag change is included.
