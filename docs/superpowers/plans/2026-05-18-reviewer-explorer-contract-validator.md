# Reviewer And Explorer Contract Validator Implementation Plan

Goal: add a repo-local validator that automatically checks `reviewer` and `explorer` role contracts, then wire it into the existing WW repository validation entrypoint.

Architecture: add one new Python validator focused on reviewer and explorer role contracts, keep the existing worker validator unchanged in scope, and extend the unified repo validator so CI and maintainers run all three validation layers from one command.

Review focus: verify that this validator protects role boundaries instead of inventing worker-style `mode` logic for reviewer or explorer, and verify that packet role bindings, prompt files, and `SKILL.md` rules stay aligned.

Tech stack: Python, markdown-it-py, Markdown contract files, repo-local validator entrypoint

---

- [ ] Persist this round's design and plan artifacts
Write the approved design and implementation plan before any runtime contract edits or validator implementation changes.

- [ ] Create `tools/validate_ww_role_contracts.py`
Implement a section-aware Markdown validator for reviewer and explorer contract surfaces.

- [ ] Implement reviewer contract rules
Check `SKILL.md`, reviewer packet defaults and example, and `reviewer-prompt.md` for the required findings-only boundaries.

- [ ] Implement explorer contract rules
Check `SKILL.md`, explorer packet defaults, and `explorer-prompt.md` for the required read-only investigation boundaries.

- [ ] Implement cross-role alignment rules
Check that packet role bindings and prompt template paths stay aligned and that reviewer/explorer do not accidentally absorb worker-only contract fields.

- [ ] Extend `tools/validate_ww_repo.py`
Add the new role-contract validator to the unified repo validation flow without breaking the existing frontmatter and worker validator checks.

- [ ] Run local verification
Run the new role validator directly, run the unified repo validator, and confirm failure behavior is still non-zero on rule violations.
