# ADR 0001: Python, swappable provider, Postgres + pgvector, no RAG frameworks

- Status: accepted
- Date: 2026-11-11

## Context

Lore is an open-source knowledge assistant built as a learning project for
AI engineering (RAG, retrieval, evals, agents, MCP). The repository is
public and the corpus is synthetic. We need a language and tooling, a way to
talk to models, a store for embeddings, and a stance on frameworks.

## Decision

1. **Python 3.12+ with uv**, ruff (including bandit `S` rules), mypy strict,
   pytest and pre-commit with gitleaks; same tooling as Hearth.
2. **Chat model behind Lore's own interface, OpenAI-compatible wire format.**
   Same pattern as Hearth (own types, `Protocol`, typed errors), **copied,
   not shared**: no common library between the projects, so each can evolve
   without coordinating releases.
3. **Postgres + pgvector**, run locally with docker compose. One database
   for vectors, metadata, permissions and (later) full-text search.
4. **No RAG frameworks** (LangChain, LlamaIndex): ingestion, chunking,
   retrieval, prompting and evals are written by hand to learn the
   primitives.
5. **CLI only**, no frontend.

## Consequences

- Positive: few dependencies; every step of the pipeline is visible and
  testable; SQL filtering by role and hybrid search live in one engine.
- Negative: more code to write and maintain than with a framework; duplicate
  provider code with Hearth; Postgres needs docker for local development and
  for any test that touches the database.
- Revisit if: the vector store becomes the bottleneck for the corpus size,
  or a framework would remove code that is no longer interesting to learn.
