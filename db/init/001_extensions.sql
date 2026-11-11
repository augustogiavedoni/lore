-- Enables pgvector. Runs once when the container starts with an empty volume.
-- Tables and indexes are NOT defined here: the schema is part of M1
-- (TODO(augusto)) and depends on ADR 0002 (database client / migrations).
CREATE EXTENSION IF NOT EXISTS vector;
