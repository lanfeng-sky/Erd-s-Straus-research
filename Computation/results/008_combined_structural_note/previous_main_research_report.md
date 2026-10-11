# Main Research Report

## Current State — 2026-10-05, after D-009

- Latest submission: [H-007 — unrestricted square-ratio classification](handoffs/007_unrestricted_square_ratio/README.md), executing D-009.
- T-009a/b: `proved` by a complete separate main rederivation of I-014 Sections 2–4. Flagship review of NEW H-007: `unresolved`.
- R-009 accepts H-006 / T-006–T-008 within their exact hypotheses; O-013 is now `proved`. H-005 remains accepted R-006. H-001 through H-006 are unchanged.
- Erdős–Straus: `unresolved`. Pointwise forcing: `blocked`. External priority and standalone publishability: `unresolved`.
- This round is proof-only: exact symbolic and paper integer arithmetic, no interpreter/terminal job, numerical replay, range, network, installation, Lean or fresh-independent-agent claim.
- Prior stalled source-parser process state: `unresolved`; no retry or diagnosis.

## Principal Increment: Exact Unrestricted Square-Pair Classification

For every odd n>=3, T-009b proves the equivalence

```text
some positive integral representation of 4/n has a rational-square denominator pair
  iff some representation has two equal denominators
  iff n has a prime divisor congruent to 3 modulo 4.
```

Repeated denominators are allowed. This is existential over representations, not a property of every representation at such n. The converse is for numerator 4 only.

T-009a gives the stronger necessity for EVERY c>=1 and odd n>=3, without clean-type, ordering, squarefreeness, primality, or gcd(c,n)=1 assumptions. In any representation of 4c/n, if Y/Z is a rational square, put

```text
A=4cX-n>0, delta=gcd(A,nX), alpha=A/delta.
```

Then A,delta,alpha are odd; every prime divisor of delta divides n; every prime divisor of alpha is 1 modulo 4 (alpha=1 allowed); and delta=-n modulo 4, n*delta=3 modulo 4. Consequently, if n is supported only on primes 1 modulo 4, EVERY actual representation of 4c/n has ALL THREE denominator ratios nonsquare in the rationals. This includes non-clean composite solutions.

Proof mechanism: a square pair is Hr^2,Hs^2 with coprime r,s. Its reduced reciprocal-sum numerator is (r^2+s^2)/gcd(r^2+s^2,H); odd primes in it are 1 modulo 4 by the order-four argument. Combining this with the prime support of delta gives the modulo-four contradiction. No clean normalization or Jacobi theorem is a proof dependency. For sufficiency at c=1, q|n, q=3 modulo 4 gives m=n/q,t=(q+1)/4 and (mt,2mqt,2mqt); positivity, integrality and 4XYZ=n(XY+XZ+YZ) are explicitly proved.

All D-009 scope cases pass exact PAPER checks: non-clean n=25; square pairs at n=21 and n=9; square-pair-free (3,6,14) at n=7; nonexistence of 8/3; and n=3,X=4 where reduced numerator 13 does not suffice for a square-pair completion. Within the prescribed n=9 witness, (X,Y,Z)=(36,3,12) gives delta=27 not dividing n=9, alpha=5 and Y/Z=1/4. Thus delta|n is `false` even under the actual square-pair hypothesis; only prime support is used. These false extrapolations are not Erdős–Straus counterexamples.

The unrestricted all-pairs domain and exact existential iff extend the inspected local register. The primitive-sum-of-two-squares input, standard repeated-denominator identity and scaling are NOT novelty claims. External priority remains `unresolved`; value of a combined structural note is `plausible`. No new congruence-coverage result is claimed.

## Accepted Complement: Signed Characters on Clean 4c/n Types

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

## Accepted Type-II Results — R-009

The following H-006 results and equality classifications are accepted within their stated hypotheses. For numerator 4, X smallest, G the FULL gcd, s=X/G, and q=q(p) the least positive nonresidue:

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

T-009 is a classification of a restricted construction target, not of Erdős–Straus solvability. At n supported on primes 1 modulo 4, all square-pair constructions are excluded but unrestricted representations remain possible; n=25,(10,20,100) is an explicit example. Necessity for arbitrary c is distinct from sufficiency at c=1. Reduced-numerator support is not fixed-X sufficiency, and a prime factor 3 modulo 4 does not force a square pair in every solution. Repeated denominators are allowed.

H-006's characters and envelopes remain necessary conditions within their stated domains. Clean composite hypotheses cannot be replaced by mere counts of n-multiples; negative Jacobi sign is not a negative Legendre sign at every prime factor. Neither the old nor the new theorem forces universal existence.

D-009's ONE task is complete with this rigorous partial structural submission. Old nesting, branch forcing and inverse hierarchy remain `blocked`; no distinct-pair construction hunt, squareclass hierarchy, additional optimization level, solution-range expansion, pointwise conjecture, or literature campaign is proposed. Historical finite computations remain bounded evidence only and were not rerun. No new claim is `verified computationally`.

## Review Request / Minimal Next Step

Flagship should review the NEW self-contained H-007 in a new numbered review file, concentrating on:

1. coprime-square normalization and the reduced reciprocal-sum numerator;
2. prime support of delta, not delta|n (with the explicit n=9,delta=27 check);
3. oddness and the sign delta=-n, n*delta=3 modulo 4;
4. permutation covering all pairs without clean-type hypotheses;
5. c=1 and existential scope, repeated denominators, and the constructive certificate.

H-006 review is already discharged by R-009; new H-007 review O-016 remains `unresolved`. No interpreter execution is needed. Keep all historical handoffs, reviews, decisions and ideas unchanged.

## History and Artifacts

- H-001: `handoffs/001_x0/`
- H-002: `handoffs/002_structure/`
- H-003: `handoffs/003_joint_inverse/`
- H-004: `handoffs/004_construction_obstruction/`
- H-005: `handoffs/005_type_I_gcd_gap/`
- H-006: `handoffs/006_signed_character_synthesis/`
- H-007: `handoffs/007_unrestricted_square_ratio/`

New result/evidence-boundary record: `experiments/results/007_unrestricted_square_ratio/`. It preserves the pre-D-009 report and obligations. KI-011 and the dated research-log section append to the live records, with an explicit acceptance reconciliation for the earlier H-006 submission-time notes. H-007 contains its entire proof and scope checks; no external dataset, parser, executable or hash-verification claim.
