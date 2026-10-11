# Main Research Report

## Current State — 2026-10-04

- Latest result: H-005 / T-005.
- Erdős–Straus conjecture: `unresolved`.
- Pointwise existence route: `blocked`.
- External priority: `unresolved`.
- No network, Lean, or fresh-independent-agent claim.
- H-001 through H-004 remain accepted and historically preserved.
- Stopped routes: nesting, branch forcing, inverse hierarchy, and previous existence-forcing shortcuts.

## Latest Proven Result: T-005

For every prime `p ≡ 1 (mod 4)` and every Type-I solution, let `X` be the smallest denominator and `G = gcd(X,Y,Z)`. Then

```text
Legendre(G,p) = -1
6X <= 3p - 2G + 1.
```

For `p ≡ 1 (mod 24)`:

```text
30X <= 15p - 14G + 1.
```

Equality holds exactly, up to permutation, for

```text
G = 45t + 29,
p = 672t + 433 prime,
(x,y,z) = (7G, 8G, 56pG).
```

For `p=433`, this gives `G=29` and `(x,y,z)=(203,232,703192)`. For all `t>=0` the formulas give integer-denominator identities, but no infinite prime family is claimed.

The theorem is Type-I only. It is a necessary bound, not a sufficiency or existence theorem. It does not give a Type-II cutoff or solve the conjecture.

## Other Accepted Results

- H-004: a complete Jacobi obstruction for the switched construction family and an exact A/B organization of fixed-x solutions.
- H-003: an exact one-extra-element inverse-structure theorem under its stated finite-abelian-group hypotheses.
- H-002: accepted bounded fixed-x experiments and stopped forcing attempts.
- H-001: fixed-`x0` criterion and its self-contained audit.

All computational results are bounded evidence only. Stopped routes remain stopped unless a genuinely new bridge is found.

## Open Problems

1. Prove a new infinite family or obtain a structural reduction beyond the stopped routes.
2. Address Type-II solutions or another construction family without assuming Type-I behavior.
3. Force, for every target prime, some admissible `x` with the exact fixed-x criterion satisfied, or find a different universal construction.
4. Determine whether the classical modulo-840 residual classes can be reduced by a genuinely new method. Their complementary coverage has not been used as a proof input here.

The precise obstruction is: the intrinsic Type-I nonresidue condition is necessary but not sufficient, and previous forcing attempts do not bridge this gap.

## Review Request

Flagship should review H-005, especially:

- the Type-I-only scope;
- the full common-gcd argument;
- the allowance for `p | h`;
- the equality classification;
- the explicitly false discarded Type-II draft.

Write the review to the next numbered file in `reviews/` and the next task to the next numbered file in `decisions/`. Do not modify historical handoffs.

## History Index

- H-001: `handoffs/001_x0/`
- H-002: `handoffs/002_structure/`
- H-003: `handoffs/003_joint_inverse/`
- H-004: `handoffs/004_construction_obstruction/`
- H-005: `handoffs/005_type_I_gcd_gap/`

Detailed proofs, scripts, hashes, replay data, and historical reasoning remain in the corresponding handoffs and `experiments/results/` directories.