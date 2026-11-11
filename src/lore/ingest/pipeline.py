"""Ingestion pipeline.

Responsibility:
    Orchestrate load -> chunk -> embed -> store for the whole corpus.
    Re-running it must be safe (idempotent): updated documents replace their
    old chunks instead of duplicating them.

Must NOT:
    - Contain chunking, embedding or SQL logic itself (delegate to modules).
    - Silently skip documents that fail validation (report them).
"""

# TODO(augusto): implement the ingestion pipeline.
