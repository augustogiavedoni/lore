# Roadmap

Each milestone is done only when its acceptance criteria pass and the
threat model has been reviewed for it.

This file is the source of truth. Each milestone has a matching
[GitHub milestone](https://github.com/augustogiavedoni/lore/milestones)
that shows its progress; issues assigned to it are the concrete work toward
these criteria, and pull requests close them. If a criterion changes, update
it here first.

## M0 — Corpus + eval set
- [ ] Roles and areas of the fictional fintech are defined and documented in
      `corpus/README.md`.
- [ ] 30–50 synthetic documents in `corpus/`, covering at least three areas,
      each with valid `id`, `area`, `allowed_roles` and `updated_at`.
- [ ] `evals/dataset.jsonl` has 30 questions in the format of
      `evals/README.md`; at least 5 are unanswerable and at least 5 are
      restricted by role (same question, different `role` and `answerable`).
- [ ] An automated check (test or script run in CI) validates the corpus and
      the dataset: required fields, unique ids, every `source_id` exists,
      every `role` is known, and the source of an answerable question is
      visible to that role.
- [ ] No real company, person or personal data anywhere in the corpus.

## M1 — Basic RAG with citations
- [ ] ADR 0002 (database client) and ADR 0003 (embeddings) are accepted.
- [ ] `lore ingest` loads the corpus into Postgres + pgvector; running it
      twice does not duplicate chunks (covered by a test).
- [ ] `lore ask --role <role> "<question>"` prints an answer and the
      `source_ids` it cites; cited ids are a subset of the retrieved ones.
- [ ] `lore eval` runs the dataset and prints a single number (e.g. recall@k
      of `source_ids`) plus per-question results to `evals/runs/`.
- [ ] Unit tests use fake providers, no network.

## M2 — Evals in CI
- [ ] Retrieval metrics (recall@k, MRR) computed per run.
- [ ] LLM-as-judge scores answers against `expected_answer`, and checks that
      unanswerable questions get a refusal; the judge prompt is versioned.
- [ ] CI runs the evals (subset or cheap model) and fails if the score drops
      below a threshold stored in the repo.
- [ ] Eval cost per run is reported and bounded.

## M3 — Hybrid search + reranking
- [ ] Keyword search (e.g. Postgres full-text) combined with vector search.
- [ ] A reranking step over the combined candidates.
- [ ] The eval report compares M3 against the M1 baseline on the same
      dataset; the change is kept only if it improves the main metric (or
      the trade-off is written down in an ADR).

## M4 — Role-based permissions
- [ ] Role filter is applied inside the search query.
- [ ] A test proves a role does not retrieve restricted documents, for every
      restricted document in the corpus.
- [ ] Restricted eval questions pass: no restricted content in answers or
      citations.
- [ ] Threat model T2 reviewed, including side channels.

## M5 — Observability
- [ ] Every query produces a trace: question, role, retrieved chunk ids and
      scores, prompt size, tokens, cost and latency per step.
- [ ] Traces contain no secrets (covered by a test).
- [ ] `lore eval` aggregates cost and latency per run.

## M6 — Agent mode (MCP)
- [ ] Search and document-fetch tools exposed as an MCP server.
- [ ] Tools enforce the caller's role; a test proves an MCP call cannot
      fetch a restricted document.
- [ ] An agent run answers multi-step questions from the eval set, with a
      step limit.
- [ ] Threat model T1 and T6 reviewed for tool use.
