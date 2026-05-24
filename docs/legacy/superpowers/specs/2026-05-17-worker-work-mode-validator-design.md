# WW Worker Work-Mode Validator Design

Date: 2026-05-17
Status: Approved for `$ww` implementation
Scope: Repo-local validator for the `ww-subagent-orchestrator` worker `work_mode` contract

## Goal

Add a repo-local automated validator for the `ww-subagent-orchestrator` worker `work_mode` contract.

The first version should:

- validate only the current `worker work-mode` contract surface
- use Python
- parse Markdown structurally with a Markdown AST parser
- fail with a non-zero exit code on any rule violation
- print human-readable results by default
- print machine-readable results with `--json`

## Scope

This validator checks only these five files:

- `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md`

It does not yet validate:

- reviewer or explorer mode contracts
- persona registry YAML
- live dispatch-plan instance files
- arbitrary repo-wide skills

## Non-Goals

- do not build a generic validator framework for every skill in the repo
- do not validate wording exactness across the whole documents
- do not introduce CI wiring in this first round
- do not require external configuration for file discovery

## Tool Shape

Recommended path:

- `tools/validate_ww_worker_work_mode.py`

Recommended commands:

```powershell
python tools/validate_ww_worker_work_mode.py
python tools/validate_ww_worker_work_mode.py --json
```

## Dependencies

Use:

- Python
- one Markdown AST library
- no YAML dependency in v1

Dependency rule:

- if the Markdown parser dependency is missing, the script must fail clearly with a non-zero exit code and a message explaining what to install

## Validation Model

The validator should use section-aware structural checks, not plain text grep.

That means:

- parse headings and section boundaries
- inspect list items inside the expected section
- treat matches in the wrong section as failures
- allow nearby prose differences as long as the required structural contract exists

## First Rule Set

### `SKILL.md`

Must structurally declare:

- worker execution order includes `user constraints -> work_mode -> persona -> goal_tuning`
- `task_mode` is separate from `work_mode`
- working brief recommends worker mode
- packet carries worker `work_mode` fields
- dispatch plan records effective worker mode and mode history
- worker prompt consumes packet state only

### `working-brief-template.md`

Must structurally contain under persona/workflow guidance:

- `recommended_worker_mode_by_section`
- `worker_mode_reasoning_by_section`
- `goal_tuning_by_section`
- `constraint_override_notes_by_section`

Must also contain rules stating:

- working brief recommends, not decides
- recommendations come from structure, scope, or risk
- constraints come before worker-mode recommendation

### `dispatch-plan-template.md`

Must structurally contain under planned section fields:

- `Planned Worker Mode`
- `Worker Mode Rationale`
- `Goal Tuning`
- `Constraint Interaction Rule`

Must structurally contain under runtime ledger:

- `Active Worker Mode`
- `Mode Change History`

Must also contain a rule that `task_mode` is not reused as `worker mode`.

### `subagent-packet-contract.md`

Must structurally require for worker packets:

- `work_mode`
- `work_mode_rationale`
- `goal_tuning`
- `constraint_precedence_note`

Must also contain rules stating:

- packet inherits one effective `work_mode`
- `work_mode` is an execution snapshot
- `task_mode` stays separate from `work_mode`

Must validate the worker packet example includes the new fields.

### `worker-prompt.md`

Must structurally state:

- constraints or non-goals first
- `work_mode` before persona principles
- `goal_tuning` only as a light modifier

Must also define all four modes:

- `plan-first`
- `validate-first`
- `iterate-first`
- `conservative-first`

## Output Contract

### Default output

Human-readable summary:

- overall pass or fail
- failed rule count
- one line per violation with file and rule id

Example shape:

```text
FAIL: 2 rule violations

[WWWM001] plugins/.../SKILL.md
Missing worker execution order contract in the expected section.

[WWWM007] plugins/.../worker-prompt.md
Missing `validate-first` mode definition.
```

### `--json` output

Stable machine-readable schema:

```json
{
  "ok": false,
  "rule_failures": 2,
  "results": [
    {
      "rule_id": "WWWM001",
      "passed": false,
      "file": "plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md",
      "section": "Core Rules",
      "message": "Missing worker execution order contract."
    }
  ]
}
```

Required fields per result:

- `rule_id`
- `passed`
- `file`
- `section`
- `message`

## Exit Behavior

- all rules pass -> exit `0`
- any rule fails -> non-zero exit
- parser, dependency, or runtime error -> non-zero exit

## Verification Plan

Implementation is complete only if:

- default run checks all five fixed files
- failures are section-aware, not whole-file text matches
- `--json` emits the stable schema above
- worker packet example failures are caught
- missing dependency path fails clearly
