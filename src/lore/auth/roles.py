"""Roles and access policy.

Responsibility:
    Define the known roles and the rule that decides whether a role may see
    a document (from its ``allowed_roles``). Single source of truth used by
    ingestion (validation) and retrieval (filtering).

Must NOT:
    - Allow access by default when roles are unknown or missing (deny).
    - Trust a role coming from model output or document content.
"""

# TODO(augusto): define roles and the access rule.
