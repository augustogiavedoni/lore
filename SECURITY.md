# Security policy

lore is a learning project, but it is designed around role-based access to
company knowledge and handles model provider API keys, so security reports
are taken seriously.

## Reporting a vulnerability

**Do not open a public issue.** Report it privately through
[GitHub private vulnerability reporting](https://github.com/augustogiavedoni/lore/security/advisories/new).

Please include what you found, how to reproduce it, and its impact. Use
placeholders instead of real emails, tokens, hostnames, IP addresses or
company documents.

## Supported versions

There are no releases yet. Only the `main` branch is supported.

## Scope

In scope: code and configuration in this repository, for example:

- a role retrieving, or getting an answer or citation from, a document its
  role may not read, including side channels such as error messages,
  refusals that confirm a document exists, or scores and counts in traces;
- prompt injection through document content that changes behaviour beyond
  a bad answer, for example leaking restricted content or, once agent mode
  exists, driving tool calls;
- leakage of API keys, database credentials or other secrets in logs,
  traces, error messages or the repository;
- MCP tools (planned) that do not enforce the caller's role, or that accept
  unvalidated input;
- weaknesses in the local setup (`docker-compose.yml`, `db/`), such as the
  database being reachable beyond `127.0.0.1`.

Out of scope:

- vulnerabilities in third-party services and libraries (model and
  embeddings providers, Postgres, pgvector) unless lore uses them in an
  unsafe way; report those to their maintainers;
- data sent to providers and runaway cost, which are design concerns for
  real deployments; open a regular issue for those.

The threats this project is designed against are described in
[docs/threat-model.md](docs/threat-model.md).

## What to expect

This is maintained by one person in their spare time, so there is no
guaranteed response time. Reports will be acknowledged, and fixes will be
credited in the advisory if you wish.
