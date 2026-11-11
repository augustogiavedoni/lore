"""Command-line interface (argparse, see ADR 0004).

Responsibility:
    Expose subcommands such as ``ingest``, ``ask --role <role> "<question>"``
    and ``eval``, parse arguments, and print answers with their citations.

Must NOT:
    - Contain retrieval or generation logic (delegate to the package).
    - Print secrets or raw configuration.
"""

# TODO(augusto): implement the CLI.
