# WW Worker Work-Mode Validator Implementation Plan

Goal: add a repo-local Python validator that structurally checks the `ww-subagent-orchestrator` worker `work_mode` contract across the five approved Markdown contract surfaces.

Architecture: keep the first version single-purpose. The validator lives at the repo level under `tools/`, uses one Markdown AST dependency, loads a fixed file list, runs section-aware structural rules, prints human-readable output by default, supports `--json`, and exits non-zero on any failure.

Review focus: verify that the validator is section-aware instead of using whole-file text matches, that the machine-readable schema is stable, and that the script catches worker packet example drift in addition to top-level contract drift.

Tech stack: Python, Markdown AST parsing, standard-library JSON, Markdown contract files, PowerShell

---

- [ ] Add the validator design and dispatch artifacts for this round
Persist the approved design, implementation plan, working brief, and dispatch plan before adding the tool implementation.

- [ ] Provision the Markdown AST dependency
Choose one Python Markdown AST parser and make the install path explicit enough that maintainers can run the script. The script must also fail clearly when the dependency is missing.

- [ ] Create `tools/validate_ww_worker_work_mode.py`
Implement a single-purpose validator with a fixed file map for the five approved targets.

- [ ] Implement section-aware structural parsing
Parse headings and list content so rules can validate the correct section rather than accepting whole-file text matches.

- [ ] Implement the first rule set
Cover the approved `SKILL.md`, working-brief template, dispatch-plan template, packet contract, worker packet example, and worker prompt checks.

- [ ] Implement dual output modes
Default output should be human-readable. `--json` should emit the approved stable machine-readable schema.

- [ ] Add matching maintainer docs
Document how to run the validator and what it checks. Keep docs aligned with the actual dependency and command path used by the script.

- [ ] Run validation and review
Run the validator in default mode and `--json` mode. Review the implementation for section-awareness, correct exit behavior, and bounded scope.

- [ ] Run final verification
Confirm the validator passes against the current five-file contract set and that the repo diff stays bounded to the intended implementation artifacts.
