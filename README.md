# lore

An open-source knowledge assistant: a CLI chat that answers questions about
a company's internal knowledge (finance, engineering, operations), cites its
sources, and respects role-based permissions.

> **Status: early.** This repository is a scaffold. Most modules are
> intentionally empty and will be written by hand as a learning project.
> Nothing here is usable yet.

## Goal

Learn AI engineering by building the primitives instead of using a
framework: ingestion, chunking, embeddings, retrieval (vector, hybrid,
reranking), grounded generation with citations, evals, observability and,
finally, an agent mode exposed over MCP.

The knowledge base is a **synthetic corpus of a fictional fintech**. It
contains no real company data and no personal data.

## Architecture

```
  lore ask --role <role> "question"
            |
            v
   +-----------------+     +---------------------+     +-------------------+
   | interfaces/cli  |---->|     retrieval/      |---->| Postgres +        |
   +-----------------+     | search (role filter |     | pgvector          |
            |              | inside the query)   |     +-------------------+
            |              +---------------------+              ^
            v                        |                          |
   +-----------------+               v                   +-------------+
   |   generation/   |<---- chunks + source ids          |   ingest/   |<-- corpus/*.md
   | prompt + answer |                                   | load, chunk,|
   +-----------------+                                   | embed, store|
            |                                            +-------------+
            v
   providers/ (chat, embeddings)  --->  model APIs
            |
            v
   answer + cited source_ids
```

See [docs/architecture.md](docs/architecture.md) and the
[roadmap](docs/roadmap.md).

## Roadmap and tracking

- **[Roadmap](docs/roadmap.md)** is the source of truth: milestones M0–M6
  and their acceptance criteria. If something changes, it changes there
  first.
- **[Milestones](https://github.com/augustogiavedoni/lore/milestones)**
  mirror the roadmap, one per milestone, and show progress.
- **[Issues](https://github.com/augustogiavedoni/lore/issues)** are concrete
  work toward a milestone, labelled with `task` and an `area:`. Pull
  requests close them.
- **[ADRs](docs/decisions/)** record why each decision was made and which
  alternatives were rejected.

## Security notice

- Role permissions are enforced **in retrieval**, not in the prompt: a role
  never gets restricted chunks in the model context.
- Document content is treated as **untrusted input** (prompt injection).
- Secrets live only in a local `.env` (git-ignored); see `.env.example`.
- The local database listens on `127.0.0.1` only.

Read [docs/threat-model.md](docs/threat-model.md). If you find a security
issue, please open a private security advisory instead of a public issue.

## Development

Requires Python 3.12+, [uv](https://docs.astral.sh/uv/) and Docker.

```bash
uv sync
uv run pre-commit install
cp .env.example .env   # then fill in the values
docker compose up -d
uv run pytest
```

## License

MIT. See [LICENSE](LICENSE).
