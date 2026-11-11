"""Vector store (Postgres + pgvector).

Responsibility:
    Persist chunks with their embeddings and metadata, and run similarity
    queries. Owns all SQL that touches chunks.

Must NOT:
    - Build SQL by string formatting with user input (use parameters).
    - Return rows without their source id and permissions.
"""

# TODO(augusto): implement once ADR 0002 (database client) is accepted.
