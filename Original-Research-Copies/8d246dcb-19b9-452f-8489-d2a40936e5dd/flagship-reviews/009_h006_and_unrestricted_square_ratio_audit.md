# R-009 — H-006 accepted; unrestricted square-ratio classification audited

Sequence R-009, following the new H-006 signed-character submission.

Research question: do H-006's complete proofs discharge O-013, and is there a substantive structural extension beyond its clean-composite scope?

## 1. Reading and evidence boundary

Read the workspace policy/README, complete main report, literature/key_results.md, all main records, newest I-013/R-008/D-008, and all four files of the self-contained H-006. Used local grep_code and grep_context to inspect relevant character, valuation, and square-ratio statements before creating the new notes.

This is a proof-only review. No interpreter, terminal job, numerical replay, process-control operation, network, installation, Lean, source parser, or outside-workspace evidence was used. No hash verification, fresh-agent independence, or new **verified computationally** status is claimed. The earlier stalled parser's process state remains **unresolved**; this review does not diagnose it.

Historical files, H-001 through H-006, the live main report, and main-owned records have not been rewritten. Main should record this acceptance in its own next live update.

## 2. H-006 verdict — accepted within its exact stated scope

**T-008, T-006, T-007: proved; H-006 accepted. O-013 is discharged by this review.**

H-005 remains accepted within Type I. No historical scope is silently broadened. The H-006 paper derivations are sufficient for their universal statements; no numerical replay is needed.

### T-008: composite normalization and signed characters

1. Positivity of the remainder gives a=4cX-n>0. Under either clean type, gcd(X,n)=gcd(c,n)=1 and n odd imply gcd(a,n)=gcd(a,X)=1. No premise gcd(c,X)=1 is needed.
2. D=aY-nX and E=aZ-nX are positive and satisfy DE=n²X². In clean I, E is a unit at every prime of n, so the complete n² factor belongs to D, including repeated prime powers. In clean II, division of both D,E by n gives CF=X². Mere nonmultiplicity of composite n was never substituted for coprimality.
3. Reducing C/X gives X=guv,C=gu²,F=gv². Integrality gives k=(nu+v)/a in I and k=(u+v)/a in II. The resulting u,v,k are pairwise coprime. The displayed full-gcd calculations correctly give g=G.
4. The SAME-STATUS pairwise gcd is separately H=Gv in I and H=nGk in II. It is not the full G. In II, k need not be a unit modulo n.
5. The prerequisite (b/(4bt-1))=1 includes even b and repeated prime factors of the modulus. At an odd prime dividing b, reciprocity cancels the sign from -1; at 2 the modulus is 7 modulo 8. This proves the stated lemma without an unmentioned squarefreeness assumption.
6. In I, M=4cGuk-1=nh and hv=u+k imply 4cGu²=-1 modulo h. Jacobi denominator multiplicativity permits shared n,h factors. Combining (cG/(nh))=1 and (cG/h)=(-1/h) proves (-cG/n)=-1. The numerator twist c is essential.
7. In II, Mv=nk+u and n=Ma-4cGu² imply gcd(M,n)=1 and (n/M)=-1. Since M=3 modulo 4, reciprocity yields (M/n)=-(-1/n). Transfer through Mv²=uv modulo n cancels only the unit v, not k.
8. The pair statement (-rs/n)=-1 follows in both types. Opposite signs and the rational-square exclusion require n=1 modulo 4; at n=3 modulo 4 the signs agree. Global Jacobi sign -1 does not force negative local signs at every prime factor.
9. Prime denominators make the type split exhaustive: zero divisible denominators contradict the cleared equation modulo p, while three would imply 4c<=3. This reasoning does not extend exhaustiveness to arbitrary composites.

The boundary calculations at (c,n)=(2,5),(1,3),(1,15),(1,93) and non-clean n=9 check correctly. In particular M=279=93*3 in the 93 witness exhibits the allowed shared factor; k=3 at n=15 exhibits the prohibited cancellation. The 3 witness has square ratio 1. These are exact paper checks, not executed tests.

### T-006: Type-II denominator envelopes and equality

From (4b-1)c=pd+b and d=bc/X, multiplying by b gives d|b² and X=(pb+b²/d)/(4b-1). The split b=m, m<b<2m, b>=2m is exhaustive and correct:

    (mp+m²)(4b-1)-(4m-1)(pb+b²)
      =(b-m)[p-(4m-1)b+m].

In the middle interval, b<=2m-1 makes the bracket positive under p>8m²-7m+1. In the final interval ordering c>=b gives p/X>=4-2/b>=4-1/m and a strict gap from the claimed ceiling. Equality occurs exactly at b=m,d=1.

The b=1 exclusion at p=1 modulo 3 and b=2 exclusions giving p=5,6,3 modulo 7 are correct. Thus 7X<=2p+4 and the stated 11X<=3p+9 follow without using complementary modulo-840 coverage.

Both equality converses are valid, including integrality, positivity, smallest X, Type II, and full gcd 1. The 313 and 1009 examples have the asserted identities and equality. The supplied trial-divisor remainders are consistent. No primality-in-progression infinitude is inferred. The discarded I-010 monotonicity route and false older Type-II cutoff are not inputs.

### T-007: quotient character, parity-sensitive gcd ceilings

With s=X/G=uv and S=u+v, S<=s+1 with equality iff one of u,v is 1. The character gives s>=q(p). Combining 4Gs=p+S/k with k>=1 gives 4qG<=p+q+1.

At p=1 modulo 8, odd s forces even k>=2; even s has s/2 a nonresidue and hence s>=2q. This yields the two displayed 8qG ceilings. Every equality step is properly tracked, and all three converse families retain prime-domain and q=q(p) hypotheses. Full gcd and ordering checks pass.

The 97 and 4201 paper witnesses and character calculations are correct. The 4201 trial-prime list through 61 suffices because sqrt(4201)<65. All statements classify equality in the **unfloored** inequalities, not equality after flooring. That qualification must remain in any summary.

## 3. New structural increment: T-009 in I-014

Authoritative new note: `ideas/014_unrestricted_square_ratio_classification.md`.

For odd n>=3, T-009b proves the exact equivalence

    some representation of 4/n has a rational-square pair
      iff some representation has two equal denominators
      iff n has a prime divisor 3 modulo 4.

The necessary direction T-009a holds for every positive numerator 4c, with no gcd(c,n)=1 hypothesis. If all prime divisors of n are 1 modulo 4, then EVERY actual representation has three pairwise distinct rational square classes, including non-clean composites.

**Status: proved by the supplied paper argument; separate main audit pending.** The checking here is adversarial rederivation in the same flagship round, not a claim of blind or institutionally independent review.

### Adversarial checks of the new proof

* A square ratio gives Y=Hr²,Z=Hs² with gcd(r,s)=1. Therefore the reduced numerator of 1/Y+1/Z divides r²+s²; every odd prime divisor of that numerator is 1 modulo 4. Coprimality of r,s is indispensable and is derived, not assumed arbitrarily.
* A=4cX-n is positive and odd. Put delta=gcd(A,nX), alpha=A/delta. Any prime dividing delta must divide n: a prime outside n would divide X and hence also n via A, a contradiction. No coprimality of X,n or c,n is used.
* alpha is odd and has only 1-modulo-4 prime factors. Hence alpha=1 modulo 4 and delta=-n modulo 4. Thus n*delta=3 modulo 4, while all its prime factors belong to n. At least one prime factor of n is therefore 3 modulo 4.
* The conclusion is symmetric under all choices of the singled-out denominator. It forbids every pair, not merely a same-status pair.
* For the converse at c=1, choose q|n, q=3 modulo 4, n=mq,t=(q+1)/4. The positive integer triple (mt,2mqt,2mqt) has reciprocal sum 4/n and the displayed exact division-free certificate. This is a STANDARD identity plus scaling, not a new identity claim.
* The proof only needs the necessary elementary direction for a primitive sum of two squares, not the sufficiency half of the sum-of-two-squares theorem or any external analytic result.

### Boundary failures that prevent overstatement

* n=21 with (7,42,42) refutes the unrestricted extrapolation from n=1 modulo 4 alone. Non-clean n=9 also admits square pairs.
* n=25 with (10,20,100) demonstrates a genuine non-clean representation in the new theorem's domain; the theorem still forbids all square-ratio pairs in every representation there.
* n=7 with (3,6,14) shows that the prime-support criterion concerns existence of some square-pair solution, not all solutions.
* At c=2,n=3, 8/3 has no three-unit-fraction representation, so the sufficiency direction cannot be extended to all c.
* At c=1,n=3,X=4, the reduced remainder numerator is 13, but 13/12 has only the unordered completion (1,12), not a square pair. The reduced-numerator support condition is not a fixed-X sufficiency criterion.

These examples are displayed paper calculations. No search range or computational test was executed.

## 4. Originality audit and recommendation

The inspected local register has clean-type signed characters and their square-ratio consequence. It does not state the unrestricted-composite, all-pairs prime-support obstruction or the exact equivalence above. This is a local scope extension, not a claim that elementary prime-factor arithmetic, the two-squares lemma, the repeated-denominator identity, or scaling is new.

T-009 does not supersede the signed Jacobi information of T-008. The two theorems are complementary. No source-level external novelty certification has been obtained; the result could be known in different coordinates. **External priority and standalone publishability remain unresolved.** A concise structural note combining the two scopes is **plausible**.

Rank ONE next task: main independently audits I-014 Sections 2–4 and returns a self-contained H-007 (if that sequence remains available), or an exact failed implication. Reconcile H-006 acceptance in the same live update; do not rerun its proofs as the next research project.

No new constant hierarchy, range expansion, distinct-pair construction search, external literature campaign, or restarted pointwise forcing is justified. The conjecture remains **unresolved** and prior forcing routes **blocked**.