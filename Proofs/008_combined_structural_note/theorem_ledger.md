# H-008 — Strict theorem and evidence ledger

D-010, 2026-10-06. Every mathematical status below is one of the seven authorized statuses. All evidence is included in structural_note.md; prior reviews identify provenance, not proof dependencies.

## Proved statements

| Claim | Exact scope | Status | Local proof location |
| --- | --- | --- | --- |
| Square-pair numerator lemma | Y/Z rational square; Y=Hr^2,Z=Hs^2 with gcd(r,s)=1; reduced reciprocal-sum numerator S/gcd(S,H), S=r^2+s^2; every odd prime factor is 1 mod 4 | proved | Section 1, first proof paragraph |
| T-009a necessity | Every c>=1, every odd n>=3, every actual representation; any singled-out X and square pair Y/Z | proved | Section 1, second proof paragraph: A,delta,alpha odd; support of delta; alpha=1 mod 4; delta=-n and n*delta=3 mod 4 |
| T-009a all-pairs corollary | All prime factors of n are 1 mod 4; arbitrary c; no clean, gcd(c,n), ordering, or squarefreeness premise | proved | Section 1, permutation argument |
| T-009b iff | c=1 only; odd n>=3; existence of some square-pair representation iff existence of some equal-pair representation iff a prime q=3 mod 4 divides n | proved | Section 1, converse, positivity, integrality and division-free certificate |
| Clean normalization | gcd(c,n)=1; clean I or II; full G and pairwise H are separately identified invariants, not asserted unequal | proved | Section 2, D,E factorization and prime-power allocation; (5) and (6) |
| Specialized Jacobi lemma | b,t>=1; L=4bt-1, including even b and repeated prime factors in L | proved | Section 2, (7), reciprocity and factorization |
| T-008 clean I | n divides Y, gcd(n,XZ)=1, gcd(c,n)=1; J(-cG,n)=-1 | proved | Section 2, M=nh proof; shared n,h factors allowed |
| T-008 clean II | n divides both Y,Z, gcd(n,X)=1, gcd(c,n)=1; J(-(X/G),n)=-1 | proved | Section 2, reciprocity with its sign retained; k is never cancelled mod n |
| T-008 reduced-pair character | In I (U,V)=(X,Z); in II (Y,Z); H=gcd(U,V), r=U/H,s=V/H; gcd(rs,n)=1 and J(-rs,n)=-1 | proved | Section 2, (6) and character transfer |
| T-008 sign consequence | On its clean domain: opposite Jacobi signs and rational nonsquare U/V at n=1 mod 4; equal signs, not square exclusion, at n=3 mod 4 | proved | Section 2, final paragraph |
| Domain complementarity | The unrestricted prime-support result covers non-clean n=25; the signed clean result covers mixed-support n=93 | proved | Section 3, scope table and exact examples |

These claims retain the original identifiers T-008 and T-009. There is no new T-010 theorem. R-009 accepted H-006/T-008 and R-010 accepted H-007/T-009. The compression in H-008 has mathematical status **proved** by its written derivation; review of this NEW presentation is separately **unresolved**.

## False extrapolations and exact witnesses

| Extrapolated claim | Status | Evidence in Section 3 |
| --- | --- | --- |
| Unrestricted n=1 mod 4 alone forbids square pairs | false | n=21,(7,42,42) |
| T-008 square-pair exclusion holds at all odd n | false | Clean II n=3,(1,6,6) |
| delta prime support can be strengthened to delta dividing n | false | n=9,(X,Y,Z)=(36,3,12), delta=27, square ratio 1/4 |
| Every clean-II k is a unit modulo composite n | false | n=15,(4,90,180), k=3 |
| A 3-mod-4 factor suffices for a representation of every 4c/n | false | c=2,n=3: no representation of 8/3 |
| A 3-mod-4 factor forces a square pair in every representation of 4/n | false | n=7,(3,6,14) has no square pair |
| Reduced-numerator prime support suffices for square-pair completion at fixed X | false | n=3,X=4, alpha=13; the only remainder completion is (1,12) |

These failures do not refute Erdős–Straus. Merely counting multiples of n does not establish the clean coprimality hypotheses; n=25 already supplies a non-clean example. A negative Jacobi sign is not negative at every prime divisor: the n=93 example gives J(2,3)=-1 but J(2,31)=1.

## Remaining statuses

- **verified computationally:** no new claim. No executable, numerical range, replay, sample, or timing was run. The exact examples are paper arithmetic, not empirical evidence.
- **conditional:** no theorem in the draft depends on an unproved assumption. Clean hypotheses are theorem hypotheses, not conjectural dependencies.
- **plausible:** usefulness and significance of the combined short note. This is an assessment, not a proof of publishability.
- **blocked:** external-priority certification while network/source work is unauthorized; historical pointwise-forcing routes remain stopped.
- **unresolved:** external priority; standalone publishability; review of H-008's presentation; Erdős–Straus; prior parser process state, which was not investigated.

No heuristic evidence or new conjecture was introduced. Standard sum-of-squares arithmetic, factorization and normalization, Jacobi reciprocity, the repeated-denominator identity and scaling are not novelty claims. The draft consolidates the established local incremental results rather than claiming to discover them again.

## Review checklist and stop rule

1. Verify every statement distinguishes arbitrary c necessity from c=1 existential sufficiency, with repeated denominators allowed.
2. Check the reduced numerator S/gcd(S,H), cancellation of 2 if needed, prime support rather than delta|n, and the modulo-four sign.
3. Check composite clean normalization, gcd(a,n) and gcd(a,X), full G versus pairwise H, and unit reduced pairs.
4. Check c in clean I, multiplicativity with shared n,h, and reciprocity/no k-cancellation in clean II.
5. Confirm the non-clean n=25 and clean mixed-support n=93 examples really separate the scopes.
6. Keep publishability and external priority **unresolved**; no theorem is promoted to a universal solvability claim.

Stop after manuscript review. No new computation or mathematical direction is proposed. Any future external-priority audit requires explicit authorization and is outside D-010.
