# WW Validation CI Implementation Plan

Goal: add a minimal repo-local validation entrypoint and GitHub Actions workflow so WorkWork can automatically validate both packaged skill frontmatter and the worker `work_mode` contract.

Architecture: keep the current worker validator intact, vendor the minimal `quick_validate.py` into `tools/`, and add one thin repo-level wrapper that both maintainers and CI invoke. GitHub Actions installs the two Python dependencies and runs the wrapper on every branch `push` and `pull_request`.

Review focus: verify that the vendored frontmatter validator matches the current local behavior, that the unified entrypoint fails when either child validator fails, and that the workflow depends only on repo-local scripts plus pip-installable Python packages.

Tech stack: Python, PyYAML, markdown-it-py, GitHub Actions, Markdown skill contracts

---

- [ ] Persist this round's design and plan artifacts
Keep the CI addition documented before code changes land.

- [ ] Add `tools/quick_validate.py`
Vendor the minimal frontmatter validator into the repository with the same command-line contract as the current local helper.

- [ ] Add `tools/validate_ww_repo.py`
Implement a thin wrapper that executes both repo-local validators and returns non-zero if either one fails.

- [ ] Add `.github/workflows/validate-ww.yml`
Create a minimal workflow for all-branch `push` and `pull_request` that installs `PyYAML` and `markdown-it-py`, then runs the unified validator command.

- [ ] Update maintainer docs
Replace the single-purpose README validation instructions with the unified repo validation entrypoint while keeping direct worker-validator commands available when useful.

- [ ] Run local verification
Run `quick_validate.py`, `validate_ww_worker_work_mode.py`, `validate_ww_repo.py`, and `py_compile` to confirm the new entrypoint and vendored script work together.
