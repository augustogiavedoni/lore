# Architecture

> Draft. Will change as milestones land (see [roadmap](roadmap.md)).

## Components

| Component | Path | Responsibility |
|---|---|---|
| Config | `src/lore/config.py` | Load settings from env; validate with pydantic. |
| Documents | `src/lore/ingest/documents.py` | Read `corpus/` markdown, validate frontmatter. |
| Chunking | `src/lore/ingest/chunking.py` | Split documents into chunks that keep source id and permissions. |
| Ingestion pipeline | `src/lore/ingest/pipeline.py` | Load → chunk → embed → store, idempotently. |
| Vector store | `src/lore/retrieval/store.py` | Postgres + pgvector: persist chunks and run similarity queries. |
| Search | `src/lore/retrieval/search.py` | Top-k chunks for a question and role (vector → hybrid + rerank in M3). |
| Roles | `src/lore/auth/roles.py` | Known roles and the access rule; deny by default. |
| Prompts | `src/lore/generation/prompts.py` | Build messages with retrieved chunks delimited as untrusted data. |
| Answer | `src/lore/generation/answer.py` | Call the chat provider, return answer + cited `source_ids`. |
| Provider interfaces | `src/lore/providers/base.py` | Contracts for chat and embeddings; own types and errors. |
| Chat provider | `src/lore/providers/openai_compat.py` | Any OpenAI-compatible chat endpoint. |
| Embeddings | `src/lore/providers/embeddings.py` | Backend chosen in ADR 0003. |
| CLI | `src/lore/interfaces/cli.py` | `ingest`, `ask`, `eval` subcommands (argparse). |
| Evals | `src/lore/evals/` + `evals/` | Code to run eval sets; datasets as JSONL. |
| Database | `docker-compose.yml`, `db/init/` | Local Postgres + pgvector for development. |

## Dependency direction

```
interfaces/cli
     |
     v
generation  ---->  retrieval  ---->  store (Postgres + pgvector)
     |                 |
     v                 v
providers/chat    providers/embeddings      auth/roles (used by ingest + retrieval)
```

`providers` and `auth` depend on nothing else in the package. Nothing below
`interfaces` knows about the CLI.

## Flow of one question (target design)

1. `lore ask --role engineering "..."` parses arguments; the role comes from
   the caller, never from the model or the documents.
2. `search` embeds the question and queries the store **with the role filter
   inside the query** (M4), returning top-k chunks with source ids.
3. `prompts` builds the messages: instructions, question, and chunks
   delimited as data with their ids.
4. `answer` calls the chat provider and returns the text plus the cited
   `source_ids`, checking they are a subset of the retrieved ones.
5. The CLI prints the answer and its sources. From M5, each step is traced
   (retrieved chunks, tokens, cost, latency).

## Ingestion (target design)

`corpus/**/*.md` → validate frontmatter → chunks (inherit `id`,
`allowed_roles`, `updated_at`) → embeddings (batched) → upsert into the store,
replacing old chunks of the same document.
