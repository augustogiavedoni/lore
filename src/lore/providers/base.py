"""Provider interfaces.

Responsibility:
    Define the contracts for the chat model and the embeddings backend, with
    Lore's own message/response types and error hierarchy, so the rest of
    the code does not depend on a vendor SDK.

Must NOT:
    - Contain vendor-specific code or HTTP calls.
    - Hold or load credentials.
"""

# TODO(augusto): define the chat and embeddings interfaces.
