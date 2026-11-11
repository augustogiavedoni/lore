"""Chunking.

Responsibility:
    Split a document into chunks suitable for embedding and retrieval. Every
    chunk keeps a reference to its source document (``id``) and inherits its
    ``allowed_roles``, so citations and permission filtering stay possible.

Must NOT:
    - Produce chunks without source id or permissions.
    - Depend on a specific embeddings backend or database.
"""

# TODO(augusto): choose a chunking strategy and implement it.
