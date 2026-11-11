"""Search.

Responsibility:
    Given a question and a role, return the top-k relevant chunks with
    scores and source ids. Starts as vector search (M1); hybrid search and
    reranking come in M3; role filtering is enforced here in M4.

Must NOT:
    - Filter by role after ranking only (filter inside the query, so a
      restricted chunk can never reach the model).
    - Call the chat model.
"""

# TODO(augusto): implement search.
