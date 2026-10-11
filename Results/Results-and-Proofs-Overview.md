# Results and Complete Proofs Overview

## 0. Global Status

**The Erdos-Straus conjecture remains `unresolved`.** No fixed-denominator result, finite search, restricted-family obstruction, or necessary condition in this compilation is promoted to a universal existence proof.

The common certificate is

`4XYZ = n(XY + XZ + YZ)`, with `X,Y,Z > 0`.

A result marked `proved` is proved under the exact hypotheses and quantifiers stated in its source file. It is not a claim of external priority, Lean formalization, publication, or a solution of the full conjecture.

## 1. KI-001: Fixed Smallest-Denominator Criterion

Let `p` be prime with `p = 1 mod 24` and let `x=(p+3)/4`. A positive integral completion of

`4/p = 1/x + 1/y + 1/z`

at this fixed `x` exists if and only if `x` has a prime divisor `q = 2 mod 3`.

Set `b=px`. Since `4x-p=3`, the remainder is `3/b`, so the equation becomes `3yz=b(y+z)`. Put `d=3y-b` and `e=3z-b`. Then `d,e>0`, `de=b^2`, and `d=e=2 mod 3`. If x has no prime factor congruent to 2 modulo 3, every prime factor of b is 1 modulo 3, contradicting `d=2 mod 3`. Conversely, for `q|x` with `q=2 mod 3`, take `e=b^2/q`, `y=(b+q)/3`, and `z=(b+e)/3`; direct expansion proves the certificate. The factor-pair argument gives completeness at fixed x.

Full proof: `Proofs/001_x0/proof.md`.

Limitations: this is a fixed-x theorem. Failure at this x is not a counterexample. The bounded record contains 273 selected primes through 100000, with 87 successes and 186 fixed-x failures; the computation is `verified computationally`.

## 2. KI-002: Exact Two-Branch Fixed-x Criterion

For prime `p=1 mod 4` and `p/4<x<p`, put `a=4x-p` and `b=px`. A positive integral completion exists if and only if some positive divisor `c|x^2` satisfies either

- Branch A: `c+x = 0 mod a`; or
- Branch B: `4c+1 = 0 mod a`.

With `E=x^2/c`, the reconstructions are

- A: `y=p(x+c)/a`, `z=p(x+E)/a`;
- B: `y=p(x+pc)/a`, `z=(px+E)/a`.

The proof reduces the certificate to `ayz=b(y+z)`, introduces `d=ay-b` and `e=az-b`, and obtains `de=b^2` with `d=e=-b mod a`. Since `v_p(b^2)=2`, the only p-adic allocations are `(1,1)`, `(2,0)`, and `(0,2)`, yielding exactly branches A and B. The converse reconstructs positive integral denominators and verifies the certificate. The divisor-ratio formulation is `R_x` meeting `{-1,-p}`.

Full proof: `Proofs/002_structure/proof.md`.

After sorting a representation, the smallest denominator lies in `(p+3)/4 <= x <= floor(3p/4)`. This is a finite reformulation of existence, not a theorem that every p has a successful x.

## 3. KI-003 and T-003: Binary Growth and the Exact Inverse Layer

For a binary product set in a finite abelian group, quotienting by the actual stabilizer makes every nonidentity binary step increase cardinality. This gives the specialized bound `|S| >= |K|(N+1)` and a fixed-shift sufficient condition. Branch B remains essential.

T-003 states that for odd `m>=3`, a generating list of length `m-2` in `C_(2m)`, with aperiodic subset-sum set `T`, `T` disjoint from `T+m`, and even total sum, has exactly one occurrence in `{2g,-2g}` and all other occurrences in `{g,-g}` for some generator g. The proof uses binary growth, orbit-run counting, and short-cycle analysis.

Full proof: `Proofs/003_joint_inverse/proof.md`.

Limitation: the arithmetic problem does not force any shift to attain the defect level `N=m-2`, so this theorem does not prove existence for every prime.

## 4. KI-004 and KI-006: Switched Parameterization and Jacobi Obstruction

If positive integers satisfy `de=4gk^2p+1` and `d=e=-1 mod 4gk`, define `u=(d+1)/(4gk)` and `v=(e+1)/(4gk)`. Then

`(x,y,z)=(guv,pgku,pgkv)`

is a positive integral solution. In normalized branch A, `x=guv`, `c=gu^2`, and `k=(u+v)/a`; branch B has a different parameter `k=(pu+v)/a` and must not be conflated with A.

For every positive `g,h`, `M=4gh-1` satisfies `gcd(g,M)=1`, `J(g,M)=1`, and `J(-g,M)=-1`, including composite M and even g. If `u+v=k(4guv-n)`, then `n=(4guk-1)a-4gu^2`, which gives `J(n,4guk-1)=-1`. Hence this parameter family cannot produce a positive square n.

Full proof: `Proofs/004_construction_obstruction/proof_audit.md`.

This is an obstruction for a restricted family, not a nonexistence theorem for the unit-fraction equation. The historical false auxiliary identity is corrected in the source proof: the correct expression is `n-x=c(3ak-3)-a`. The nested `u=1` family has no witness at `n=193`, while a non-nested branch-A solution exists: `(50,1930,4825)`.

## 5. KI-007 and T-005: Type-I Gcd Character and Sharp Denominator Bounds

For a Type-I solution with `p=1 mod 4` prime, smallest denominator X, exactly one p-divisible denominator, and full gcd `G=gcd(X,Y,Z)`,

`(G/p)=-1`, and `6X <= 3p-2G+1`.

For `p=1 mod 24`,

`30X <= 15p-14G+1`.

Equality in the latter holds exactly, up to permutation, when `G=45t+29`, `p=672t+433` is prime, and `(X,Z,Y)=(7G,8G,56pG)`.

The proof derives the normalized Type-I form `(X,Y,Z)=(guv,pguk,gvk)`, proves `G=g`, applies Jacobi reciprocity, and obtains the exact gap

`p-2X = v(2gur-1)/(2u+r)`, where `r=k-u`.

Strict monotonicity in u and r, followed by the cases `v>=2`, `r>=2`, and `v=r=1`, yields the bounds and equality classification.

Full proof: `Proofs/005_type_I_gcd_gap/proof_audit.md`.

The retained replay of 2991 pairs, 187 primes, and 955 first B witnesses is `verified computationally`; it is not an enumeration of all Type-I solutions.

## 6. KI-008 and KI-009: Type-II Bounds, Characters, and Equality Cases

For Type-II solutions with X smallest:

- if `p=1 mod 24`, then `7X<=2p+4`;
- if `p mod 840` is in `{1,121,169,289,361,529}`, then `11X<=3p+9`;
- if `G=gcd(X,Y,Z)`, `s=X/G`, and q is the least positive quadratic nonresidue, then `(s/p)=-1` and `4qG<=p+q+1`;
- if `p=1 mod 8`, then odd s gives `8qG<=2p+q+1`, while even s gives `8qG<=p+2q+1`.

The proof uses the Type-II normal form `(Guv,pGku,pGkv)`, an exact extremal lemma, exclusions for `b=1,2`, Jacobi transfer, and parity cases. Equality families and the paper checks at `p=313,1009,97,4201` are preserved in `Proofs/006_signed_character_synthesis/`.

These are necessary conditions only. They do not force a Type-II solution. The former claim `X<=floor((p+1)/4)` is false: `p=1009` has `X=253`.

## 7. KI-010 and T-008: Signed Jacobi Theorems for Clean Types

Assume `gcd(c,n)=1` and

`4c/n=1/X+1/Y+1/Z`.

- Clean I: `n|Y` and `gcd(n,XZ)=1` imply `J(-cG,n)=-1`;
- Clean II: `n|Y,Z` and `gcd(n,X)=1` imply `J(-(X/G),n)=-1`.

For the same-status pair `(X,Z)` in Clean I or `(Y,Z)` in Clean II, if `H=gcd(U,V)`, `r=U/H`, and `s=V/H`, then `J(-rs,n)=-1`. At `n=1 mod 4`, the signs exclude a rational-square ratio for that pair. At `n=3 mod 4`, the sign no longer excludes it, but does not prove that a square pair exists.

The proof handles composite n, the distinction between full and pairwise gcds, shared factors, and nonunit k in Clean II.

## 8. KI-011 and T-009: Unrestricted Rational-Square-Pair Classification

For every odd `n>=3`,

`some representation of 4/n has a rational-square denominator pair`

if and only if

`some representation has two equal denominators`

if and only if

`n has a prime divisor q=3 mod 4`.

The quantifier is existential over representations; repeated denominators are allowed.

More generally, for any `c>=1`, if a representation of `4c/n` has a square pair, put `A=4cX-n`, `delta=gcd(A,nX)`, and `alpha=A/delta`. Then A, delta, and alpha are odd; every prime factor of delta divides n; every prime factor of alpha is `1 mod 4`; `delta=-n mod 4`; and `n*delta=3 mod 4`. Therefore, if all prime factors of n are `1 mod 4`, every representation has all three denominator ratios nonsquare.

The proof writes a square pair as `Hr^2,Hs^2` with `gcd(r,s)=1`, shows that the odd prime factors of the reduced reciprocal numerator are `1 mod 4`, and combines this with the prime support of delta. For sufficiency at numerator 4, choose `q|n`, `q=3 mod 4`, set `m=n/q` and `t=(q+1)/4`, and use `(mt,2mqt,2mqt)`.

Full proof: `Proofs/007_unrestricted_square_ratio/`.

Important corrections: `delta|n` is false; for `n=9`, `(X,Y,Z)=(36,3,12)` gives `delta=27`. Arbitrary-c sufficiency is false; `8/3` has no representation. The non-clean example `n=25,(10,20,100)` shows that unrestricted representations remain possible.

## 9. KI-013 and T-010: Clean-Domain Localization of All Square Pairs

Assume `gcd(c,n)=1` and a positive integral representation of `4c/n` exists.

- In Clean I, cross pairs `(X,Y)` and `(Y,Z)` are never rational squares. A square pair can only be `(X,Z)`, and then `n=3 mod 4`.
- In Clean II, cross pairs `(X,Y)` and `(X,Z)` are never rational squares. A square pair can only be `(Y,Z)`, and then `n=3 mod 4`.

Consequently, at `n=1 mod 4`, every clean representation has all three unordered denominator ratios nonsquare. Any square-pair representation there must be non-clean under every permutation.

The proof starts from `D=aY-nX`, `E=aZ-nX`, and `DE=n^2X^2`, then performs prime-power allocation to obtain

- I: `(X,Y,Z)=(Guv,nGuk,Gvk)`, `ak=nu+v`;
- II: `(X,Y,Z)=(Guv,nGku,nGkv)`, `ak=u+v`.

It reduces all three ratios. In I, a cross-square forces n to be an odd square, contradicting the Jacobi sign. In II, the common squarefree kernel of n and k, together with `k|u+v`, gives the contradictory Jacobi sign. No cancellation of k modulo n is used.

Full proof: `Proofs/009_clean_square_pair_localization/proof.md`.

This is a localization and restricted-construction obstruction, not an existence theorem. The condition `n=3 mod 4` does not imply that every clean representation has a square pair. At `c=1`, however, `(t,2nt,2nt)` with `t=(n+1)/4` gives an equal-denominator representation for every `n=3 mod 4`.

## 10. Computation, Audits, and Endpoint

Fixed-x experiments, structural experiments, switched-parameter tests, gcd and character audits, and Type-II regressions are stored in `Computation/` and `Audits-and-Limitations/`.

The Kneser-based saturation statement is `conditional` when its Kneser inequality is used explicitly. The later specialized binary-growth proof removes that dependency for its local statement, but does not force a successful shift for every prime.

External priority, publication significance, and the old parser state remain `unresolved` or `blocked`. The final mathematical endpoint is a collection of rigorous local structural theorems, necessary conditions, parameterizations, obstructions, and bounded verifications. The full Erdos-Straus conjecture remains unresolved.