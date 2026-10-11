# Erdos-Straus Results Compilation

This directory consolidates the mathematical results, complete proofs, computational evidence, and audit records from the two source workspaces `10 7` and `8d246dcb-19b9-452f-8489-d2a40936e5dd`. The source workspaces substantially overlap. The newer workspace is used as the baseline for the complete proof collection, while both source copies are preserved.

## Directory

- `Results/Results-and-Proofs-Overview.md`: an English index of the main results, proof mechanisms, exact scopes, and limitations, organized by KI/T identifier.
- `Proofs/`: complete mathematical proof packages, including proof files, audits, scope notes, and counterexamples.
- `Computation/`: exact-arithmetic scripts, experiment outputs, verification records, and environment data.
- `Audits-and-Limitations/`: review reports, decisions, corrections, blocked routes, and unresolved obligations.
- `Original-Research-Copies/`: research files copied from both source workspaces. Platform metadata `.backup/` and `.operit/`, as well as raw HTML literature snapshots, are excluded from the compilation.

## Overall Status

The full Erdos-Straus conjecture has not been proved in this workspace. The strict status ledger is:

- local structural theorems and necessary conditions: `proved`;
- bounded exact computations: `verified computationally`;
- arguments depending on an explicitly stated Kneser input: `conditional`;
- abandoned or unsupported construction routes: `blocked` or `false`;
- external priority, publication status, and the conjecture itself: `unresolved`.

The main equation is

`4/n = 1/X + 1/Y + 1/Z`,

and, more generally,

`4c/n = 1/X + 1/Y + 1/Z`,

with positive integer denominators. Every finite computation is restricted to its stated range and is not a substitute for a universal proof.

## Integrity Rules

- Proofs use exact integer arithmetic, factorization, gcd arguments, Jacobi and Legendre symbols, and quadratic reciprocity.
- A fixed-denominator failure, a finite no-hit search, a restricted-family obstruction, or a necessary condition must not be presented as a counterexample to the conjecture.
- The raw HTML literature snapshots are source materials rather than proof records. Their local conclusions and comparison notes remain available in the copied Markdown research files.