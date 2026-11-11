<!--
PR title must follow Conventional Commits; it becomes the squash commit on main.
Example: feat(retrieval): add vector search
-->

## What and why

<!-- One or two sentences. What changes and why it is needed. -->

- Milestone: <!-- e.g. M1, or "none" -->
- ADR: <!-- e.g. docs/decisions/0002-database-client.md, or "none" -->

## How it was tested

<!-- Commands run locally and anything checked by hand. -->

- [ ] `uv run pytest`
- [ ] `uv run mypy`
- [ ] `uv run pre-commit run --all-files`
- [ ] Eval score before / after (if retrieval or generation changed):

## Security checklist

- [ ] No secrets, tokens or credentials in code, tests, docs, corpus or examples.
- [ ] No real company data and no personal data; the corpus stays fictional.
- [ ] Role filtering still happens inside retrieval, not in the prompt.
- [ ] Document content is still passed to the model as delimited data.
- [ ] If this PR closes a milestone: `docs/threat-model.md` was reviewed.

## Notes for reviewers

<!-- Trade-offs, open questions, follow-ups. Delete if empty. -->
