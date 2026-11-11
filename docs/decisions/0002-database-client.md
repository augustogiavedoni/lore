# ADR 0002: Postgres client

- Status: proposed (decide in M1)
- Date: 2026-11-11

## Context

M1 stores chunks and embeddings in Postgres + pgvector and runs similarity
queries; M3 adds full-text search and M4 filters by role inside the query.
We need a client library and a way to manage the schema. The provider
interface follows Hearth, which is async; whether Lore is async end to end
is part of this decision.

## Options

1. **psycopg 3.** SQL by hand; sync and async APIs; official `pgvector`
   adapter. Most transparent for learning retrieval queries. Schema as plain
   `.sql` files (no migration tool) or a small migration runner.
2. **asyncpg.** Async only, fastest, own API (not DB-API). Fits an async
   provider; more friction for scripts and sync tests.
3. **SQLAlchemy 2 (Core or ORM) + Alembic.** Query builder and versioned
   migrations. More layers between the code and pgvector's SQL; more to
   learn that is not RAG.

## Decision

Pending. To be decided at the start of M1.

## Consequences

To be written with the decision.
