"""Configuration loading and validation.

Responsibility:
    Read settings from environment variables (optionally a local ``.env``):
    chat provider, embeddings backend and database connection, and validate
    them into typed objects.

Must NOT:
    - Log, print or return raw secret values (API keys, DB password).
    - Fall back to hard-coded credentials or defaults for secrets.
"""

# TODO(augusto): design and implement configuration loading.
