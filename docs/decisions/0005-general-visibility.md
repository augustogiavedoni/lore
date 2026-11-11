# ADR 0005: Company-wide visibility through a base role

- Status: accepted
- Date: 2026-11-11

## Context

Every document declares `allowed_roles`, and a missing or empty list is a
validation error (deny by default, threat model T2). Many documents are
**General** (see `corpus/README.md`): every role may read them. We need a
way to express "every role" that keeps deny-by-default, has no implicit
"public", and keeps the M4 filter inside the search query simple and hard to
get wrong.

## Options considered

1. **List every role explicitly**: the filter has no special case, but the
   rule "everyone sees this" is repeated in every General document. Adding a
   role means editing all of them, and forgetting one fails silently: the
   new role just sees less.
2. **Sentinel value** (e.g. `everyone`) in `allowed_roles`: concise, but the
   search query needs a special case (`ARRAY[$role, 'everyone']`) that every
   search path must remember, and the sentinel must never be accepted as a
   caller's role.
3. **Base role every user has** (`employee`): General documents use
   `allowed_roles: [employee]`. A single function maps the caller's role to
   its effective roles (`engineer → {engineer, employee}`), and the query
   is the generic `allowed_roles && $effective_roles`.
4. **Separate `visibility: public` field**: readable, but two sources of
   truth, and a wrong `public` leaks with nothing to catch it. It is the
   implicit "public" we want to avoid.

## Decision

**Option 3, base role `employee`.** The rule "everyone sees this" lives in
one place, the effective-roles function, which can be tested, instead of
being repeated in every document and maintained by every author. The search
query stays free of special cases, and the model extends to real groups
later without changing the query.

Rules:

- `employee` is a **base role**, not a user role: a caller can never ask
  with `--role employee`; it is rejected at the input boundary. User roles
  are the ones listed in `corpus/README.md`.
- Every user role's effective roles are itself plus `employee`.
- A General document has exactly `allowed_roles: [employee]`. Mixing
  `employee` with other roles is a validation error (it would be redundant
  and hide mistakes).

## Consequences

- Positive: adding a role touches no document; the filter is one generic
  array-overlap condition; the mapping is a small pure function, easy to
  test exhaustively.
- Negative: the effective-roles function is now security surface, so it
  needs its own tests. Every search path (CLI, evals, MCP in M6) must call
  it; a path that passes the raw role fails closed (the user loses General
  documents) rather than leaking.
- `role` in the eval set stays a single user-role string, as a real caller
  would pass it; the eval runner goes through the same effective-roles
  function, so evals exercise the real path.
- The M0 corpus check must enforce: `employee` alone or absent in
  `allowed_roles`, and every `role` in the eval set is a user role.
- Revisit if: users need more than one user role, or groups other than
  `employee` appear (the function grows into a real role hierarchy).
