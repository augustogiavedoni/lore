"""Document loading.

Responsibility:
    Read markdown files from ``corpus/``, parse their frontmatter (``id``,
    ``area``, ``allowed_roles``, ``updated_at``) and return typed documents.
    Reject files with missing or invalid metadata instead of guessing.

Must NOT:
    - Default ``allowed_roles`` to "everyone" when it is missing or empty.
    - Read files outside the configured corpus directory.
    - Interpret document text as instructions (it is untrusted data).
"""

# TODO(augusto): define the document type and implement loading/validation.
