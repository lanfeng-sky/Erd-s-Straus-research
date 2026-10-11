# Main Research Report

## Current State — 2026-10-05

- Latest submission: [H-006 — signed-character synthesis](handoffs/006_signed_character_synthesis/README.md), executing D-008.
- T-006/T-007/T-008: `proved` by complete separate main rederivations; new H-006 flagship review: `unresolved`.
- H-005 accepted in R-006 within Type I; H-001 through H-005 remain historically unchanged.
- Erdős–Straus: `unresolved`. Pointwise forcing: `blocked`. External priority: `unresolved`.
- This round is proof-only: no interpreter/terminal job, numerical replay, new range, network, installation, Lean, or fresh-independent-agent claim.
- Prior stalled source-parser process state: `unresolved`; no retry or diagnosis.

## Principal Increment: Signed Characters on Clean 4c/n Types

Let c>=1, n>=3 odd, gcd(c,n)=1, and let positive integers solve

```text
4c/n=1/X+1/Y+1/Z, G=gcd(X,Y,Z).
```

Without ordering assumptions, T-008 gives

```text
Clean I:  n|Y, gcd(n,XZ)=1 => Jacobi(-cG,n)=-1.
Clean II: n|Y,Z, gcd(n,X)=1 => Jacobi(-(X/G),n)=-1.
```

For the same-status pair (U,V)=(X,Z) in I or (Y,Z) in II, put H=gcd(U,V), r=U/H, s=V/H. In BOTH types

```text
gcd(r,s)=1, gcd(rs,n)=1, Jacobi(-rs,n)=-1.
```

Thus at n=1 mod 4 the reduced pair has opposite Jacobi signs and U/V cannot be a rational square. This rules out a specified square-ratio construction ansatz, not Erdős–Straus representations. At n=3 mod 4 the signs agree; the square-ratio exclusion is NOT asserted there. The two clean types exhaust odd-prime solutions but not unrestricted composite-denominator solutions.

Main independently checked composite normalization, FULL versus pairwise gcd, numerator c, reciprocity sign, shared n,h factors in I, and nonunit k in II. Exact paper scope checks at (c,n)=(2,5),(1,3),(1,15),(1,93), and non-clean n=9 are in H-006. No executed regression is implied.

The general-numerator/composite intrinsic synthesis extends the inspected local register. Standard normalization, the Jacobi lemma, recovered prime character statements, known odd-square obstruction, and standard nested equality identities are not originality claims. External priority is `unresolved`; significance as a concise combined note is `plausible`.

## Pending Type-II Results Now Independently Audited

For numerator 4, X smallest, G the FULL gcd, s=X/G, and q=q(p) the least positive nonresidue:

**T-006 — proved:**

```text
p=1 mod 24 prime: 7X<=2p+4.
p mod 840 in R={1,121,169,289,361,529} prime: 11X<=3p+9.
```

Both full equality classifications are proved. For the residual bound equality holds exactly, up to permutation, when p=8 mod 11 within the stated domain and

```text
(X,Y,Z)=(3(p+3)/11,3p,p(p+3)/11).
```

It is attained at p=1009 with (276,3027,92828). The global extremal lemma uses the exhaustive split b=m, m<b<2m, b>=2m, not false global monotonicity. Only the assigned m=2,3 cases are applied. Complementary modulo-840 coverage is not a proof input.

**T-007 — proved:**

```text
p=1 mod 4: Legendre(s,p)=-1, 4qG<=p+q+1.
p=1 mod 8, s odd:  8qG<=2p+q+1.
p=1 mod 8, s even: 8qG<=p+2q+1.
```

All equality converses for these UNFLOORED inequalities are proved with q=q(p) and prime-domain hypotheses retained. Equality after flooring is not claimed classified. Odd-case attainment: p=97,q=5,G=5,(25,970,4850), outside R. Even-case attainment: p=4201,q=11,G=48,(1056,201648,4436256), within R. These examples were checked by exact paper arithmetic, not fresh executed tests.

Together with H-005, every solution at p=1 mod 4 has at least one of G,X/G a nonresidue. Both may be nonresidues; the signs do not determine type uniquely or force existence.

## Accepted Type-I Result Retained

H-005 / T-005, accepted R-006, remains `proved` ONLY within Type I:

```text
p=1 mod 4: Legendre(G,p)=-1, 6X<=3p-2G+1.
p=1 mod 24: 30X<=15p-14G+1.
```

Equality in the latter holds exactly, up to permutation, for G=45t+29, p=672t+433 prime, t>=0, with (7G,8G,56pG). The p=433 triple is (203,232,703192). No infinite-prime-family assertion. The old Type-II X<=floor((p+1)/4) claim remains `false` at retained 1009,X=253>252 and is not an input. I-010's abandoned proof formulas remain superseded by I-011, historically unchanged.

## Limitations and Endpoint

All characters and envelopes are NECESSARY conditions on actual solutions. Neither supplies universal existence, a new complete congruence cover, or a counterexample. Clean composite hypotheses cannot be replaced by mere counts of n-multiples; negative Jacobi sign is not a negative Legendre sign at every prime factor.

D-008's ONE task is complete with this rigorous partial structural submission. Old nesting, branch forcing and inverse hierarchy remain `blocked`; no additional optimization level, solution-range expansion, pointwise conjecture, or literature campaign is proposed. Historical finite computations remain bounded evidence only and were not rerun.

## Review Request / Minimal Next Step

Flagship should review the NEW self-contained H-006 in the next numbered review file, concentrating on:

1. composite prime-power allocation and separate FULL/pairwise gcds;
2. numerator twist and signed reciprocity;
3. shared n,h factors and nonunit k, with the 93/15 boundary examples;
4. n=1 mod 4 restriction of the rational-square obstruction;
5. Type-II split-at-2m proof, equality converses and unfloored-equality qualification.

No interpreter execution is needed. New H-006 review remains `unresolved`; do not portray it as already accepted. Keep all historical handoffs, reviews, decisions and ideas unchanged.

## History and Artifacts

- H-001: `handoffs/001_x0/`
- H-002: `handoffs/002_structure/`
- H-003: `handoffs/003_joint_inverse/`
- H-004: `handoffs/004_construction_obstruction/`
- H-005: `handoffs/005_type_I_gcd_gap/`
- H-006: `handoffs/006_signed_character_synthesis/`

New result/evidence-boundary record: `experiments/results/006_signed_character_synthesis/`. The pre-update report and obligations are preserved there; KI-008/KI-009/KI-010 and the dated log section append to the live records. The new handoff is proof-only and self-contained: no external datasets, parser, executable or hash-verification claim.
