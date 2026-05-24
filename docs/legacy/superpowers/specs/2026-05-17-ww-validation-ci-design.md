# WW Validation CI Design

Date: 2026-05-17
Status: Approved for implementation
Scope: Add a repo-local CI entrypoint that validates both packaged skill frontmatter and the worker `work_mode` contract.

## Goal

Add a minimal GitHub Actions check for WorkWork that runs on every branch `push` and `pull_request`.

The check should:

- validate `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md` frontmatter with a repo-local copy of `quick_validate.py`
- validate the existing worker `work_mode` runtime contract with the current repo-local validator
- expose one repo-local command that maintainers and CI can both run
- fail the workflow on any validation error

## Scope

This round adds:

- `tools/quick_validate.py`
- `tools/validate_ww_repo.py`
- `.github/workflows/validate-ww.yml`
- README maintainer guidance for the unified validation entrypoint

This round does not:

- merge the two validation rule sets into one script
- add a generalized validation framework for every future check
- validate arbitrary plugins or skills in the repository
- add caching, matrix jobs, or release automation

## Design

Keep validation in two focused tools plus one thin orchestration layer.

### 1. Repo-local `quick_validate.py`

Vendor the current minimal `quick_validate.py` behavior into the repo under `tools/`.

Its responsibilities stay narrow:

- accept a skill directory path
- load `SKILL.md`
- validate YAML frontmatter structure
- enforce the allowed frontmatter keys
- enforce existing name and description rules

### 2. Existing worker contract validator

Keep `tools/validate_ww_worker_work_mode.py` unchanged in responsibility. It remains the source of truth for section-aware worker `work_mode` contract checks.

### 3. Unified repo validation entrypoint

Add `tools/validate_ww_repo.py` as a thin wrapper that:

- runs repo-local `quick_validate.py` against `plugins/workwork/skills/ww-subagent-orchestrator/`
- runs `validate_ww_worker_work_mode.py`
- forwards subprocess output
- returns non-zero if either validator fails

This keeps CI and maintainer usage on one stable command without collapsing two unrelated rule sets into one file.

## CI Workflow

Add `.github/workflows/validate-ww.yml` with:

- triggers: all-branch `push` and all-branch `pull_request`
- one job on `ubuntu-latest`
- Python setup
- dependency install for `PyYAML` and `markdown-it-py`
- one validation step that runs `python tools/validate_ww_repo.py`

## Verification

Implementation is complete only if:

- `python tools/quick_validate.py plugins/workwork/skills/ww-subagent-orchestrator` passes locally
- `python tools/validate_ww_worker_work_mode.py` still passes locally
- `python tools/validate_ww_repo.py` passes locally
- the new workflow syntax is valid YAML and points only at repo-local scripts
