# Corpus

Synthetic knowledge base of a **fictional** fintech. Everything here is made
up: no real companies, people, customers, figures or personal data. It is the
input to ingestion (`src/lore/ingest/`).

> Status: empty. Writing the corpus is milestone M0 (see `docs/roadmap.md`).

## The company

**Corvalia** is a fictional digital bank for small and medium businesses in
Latin America: business accounts, corporate cards, QR and payment-link
collections, and short-term working-capital advances. It has about 400
employees and is regulated, so it runs KYC/AML controls, reports to a
financial regulator and is audited. The name and everything about it are
invented.

## Areas

`area` says what a document is **about**, not who may read it. Each document
has exactly one area.

| `area` | Covers | Examples |
|---|---|---|
| `engineering` | Platform, infrastructure, architecture, technical incidents. | Architecture notes, deploy runbooks, postmortems, on-call guide. |
| `operations` | Day-to-day customer operations. | Support macros, chargeback and dispute handling, business onboarding steps, service hours and SLAs. |
| `risk` | Corvalia's own risk decisions: fraud and credit. | Fraud rules and thresholds, credit scoring for advances, card limits. |
| `compliance` | Regulatory obligations: KYC, AML, regulator and audits. | How to report a suspicious operation, KYC requirements, audit reports, regulator correspondence, AML case files. |
| `finance` | Corvalia's own money. | Expense policy, budget, treasury, monthly results. |
| `people` | Employees and how the company works for them. | Vacation and leave, benefits, code of conduct, salary bands, performance reviews. |

Tie-breakers: fraud is `risk`, money laundering is `compliance`. A document
about *handling* a customer case is `operations` even if it mentions fraud;
the rules and thresholds behind it are `risk`.

## Roles

A role is an **access profile** (what a person may read), not an area. Role
names are deliberately different from area names so the two are never
confused. Every user of Lore has exactly one role.

| `role` | Who | Access in one line |
|---|---|---|
| `executive` | C-level and directors. | Almost everything, except AML case files. |
| `engineer` | Software, infrastructure and data engineers. | General documents, all of engineering, plus the technical side of risk and operations. |
| `finance-analyst` | Accounting, treasury and FP&A. | General documents plus all of finance. |
| `people-partner` | HR. | General documents plus all of people. |
| `compliance-officer` | Risk and compliance team (one team at this size). | General documents plus all of compliance and risk. |
| `support-agent` | Customer support agents. | General documents plus operations only. The most limited role. |

There is also one **base role**, `employee`, that every user has on top of
their own role. It is used only to mark General documents and can never be
passed as a caller's role (ADR 0005).

## Access model

Every document is one of two levels:

- **General**: visible to **every role**. For company-wide policies and
  information everyone needs to do their job. A General document contains
  no customer data, no data about individual employees, no internal
  figures (amounts, budgets, results) and no thresholds or rules that could
  be gamed.
- **Restricted**: visible only to the area's default roles, adjusted by the
  exceptions below.

A General document has exactly `allowed_roles: [employee]`, never
`employee` mixed with other roles (ADR 0005).

### Role × area matrix

What each role sees by default. **G** = only General documents of that area;
**R** = also the area's Restricted documents; **—** = nothing beyond
General (same as G, spelled out where it matters).

| | `engineering` | `operations` | `risk` | `compliance` | `finance` | `people` |
|---|---|---|---|---|---|---|
| `executive` | R | R | R | R (except AML case files) | R | R |
| `engineer` | R | G + escalation runbooks | G + fraud engine implementation | G | G | G |
| `finance-analyst` | G | G | G | G | R | G |
| `people-partner` | G | G | G | G | G | R |
| `compliance-officer` | G | R | R | R | G | G |
| `support-agent` | G | R | G | G | G | G |

Default `allowed_roles` for a **Restricted** document, by area:

| `area` | Default `allowed_roles` |
|---|---|
| `engineering` | `[engineer, executive]` |
| `operations` | `[support-agent, compliance-officer, executive]` |
| `risk` | `[compliance-officer, executive]` |
| `compliance` | `[compliance-officer, executive]` |
| `finance` | `[finance-analyst, executive]` |
| `people` | `[people-partner, executive]` |

### Exceptions

| Documents | `allowed_roles` | Why |
|---|---|---|
| AML case files (`compliance`): investigations of specific customers. | `[compliance-officer]` | Need-to-know and the legal duty not to tip off the customer; not even executives read individual cases. |
| Fraud engine implementation (`risk`): how rules are deployed and evaluated, not the thresholds themselves. | `[compliance-officer, engineer, executive]` | Engineers build and run the engine. Threshold values stay in separate risk documents. |
| Escalation runbooks (`operations`): what support does when a technical issue blocks customers. | `[support-agent, compliance-officer, engineer, executive]` | On-call engineers receive those escalations. |

`support-agent` never sees Restricted `risk` documents: knowing fraud
thresholds would let a compromised or social-engineered agent help a
fraudster stay below them.

### Deciding `allowed_roles` for a new document

1. Pick the `area` by topic (see tie-breakers above).
2. If the document meets every condition for **General**, it is General:
   `allowed_roles: [employee]`.
3. Otherwise use the area's default `allowed_roles`.
4. If it matches a row in Exceptions, use that row instead.
5. If in doubt, choose the more restrictive option. Missing access is a bad
   answer; extra access is a leak.

## Layout

One markdown file per document, grouped by area:

```
corpus/
  engineering/
  operations/
  risk/
  compliance/
  finance/
  people/
```

The folder is for humans; the source of truth for metadata is the
frontmatter below.

## File format

Markdown with a YAML frontmatter block. All four fields are **required**;
ingestion rejects a file that is missing any of them.

```markdown
---
id: fin-treasury-policy
area: finance
allowed_roles: [finance-analyst, executive]
updated_at: 2026-10-01
---

# Treasury policy

...
```

| Field | Type | Rules |
|---|---|---|
| `id` | string | Unique across the corpus, stable, lowercase kebab-case. Citations and the eval set refer to it, so never reuse or rename an id. |
| `area` | string | One of the values in [Areas](#areas). |
| `allowed_roles` | list of strings | Roles that may retrieve this document, chosen with [Access model](#access-model). Never empty; there is no implicit "public". General documents use exactly `[employee]` (ADR 0005). |
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
