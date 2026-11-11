# Corpus

Synthetic knowledge base of a **fictional** fintech. Everything here is made
up: no real companies, people, customers, figures or personal data. It is the
input to ingestion (`src/lore/ingest/`).

> Status: empty. Writing the corpus is milestone M0 (see `docs/roadmap.md`).

## Layout

One markdown file per document, grouped by area:

```
corpus/
  finance/
  engineering/
  operations/
  ...
```

The folder is for humans; the source of truth for metadata is the
frontmatter below.

## File format

Markdown with a YAML frontmatter block. All four fields are **required**;
ingestion rejects a file that is missing any of them.

```markdown
---
id: fin-expense-policy
area: finance
allowed_roles: [finance, executive]
updated_at: 2026-10-01
---

# Expense policy

...
```

| Field | Type | Rules |
|---|---|---|
| `id` | string | Unique across the corpus, stable, lowercase kebab-case. Citations and the eval set refer to it, so never reuse or rename an id. |
| `area` | string | One of the areas defined in M0 (e.g. `finance`, `engineering`, `operations`). |
| `allowed_roles` | list of strings | Roles that may retrieve this document. Never empty. A document visible to everyone lists every role explicitly (or a role defined for that purpose in M0); there is no implicit "public". |
| `updated_at` | date (`YYYY-MM-DD`) | Last meaningful change. Useful when two documents contradict each other. |

## Writing guidelines

- Mix document types: policies, runbooks, postmortems, meeting notes, FAQs.
- Include some contradictions and outdated documents on purpose (an old and
  a new version of a policy), so `updated_at` matters.
- Some facts must exist **only** in restricted documents, so role filtering
  can be tested (M4).
- A few documents should contain text that looks like instructions to the
  assistant (prompt injection), to test that it is treated as data. See
  `docs/threat-model.md`.
- No secrets, not even fake-looking ones (e.g. strings shaped like API
  keys): they trip gitleaks and teach bad habits.
