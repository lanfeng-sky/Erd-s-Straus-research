# D-009 — Accept H-006; one task on unrestricted square-ratio classification

Sequence D-009. Inputs: new R-009, I-014, and the complete H-006 paper package.

## Decision

**Accept H-006 within its exact hypotheses.** T-006/T-007/T-008 and their stated equality classifications pass the proof audit. O-013 is discharged in R-009; main should reconcile this in its next live update. H-005 and all historical handoffs remain unchanged.

Rank ONE new direction: audit T-009, the exact prime-support classification of when a rational-square denominator pair can occur. This removes the clean-type restriction for a meaningful obstruction, rather than improving another constant. It does not restart pointwise forcing or claim new congruence coverage.

## 1. Precise mathematical claim

For every odd n>=3,

    some positive representation of 4/n has two denominators
    whose ratio is a rational square

is equivalent to

    n has a prime divisor q congruent to 3 modulo 4.

It is also equivalent to existence of a representation with two equal denominators. Repeated denominators are allowed. The claim is existential over representations, not a claim that every representation at such n has a square pair.

The necessary direction holds more generally for 4c/n, every c>=1, with NO clean-type, ordering, or gcd(c,n)=1 assumption. If all prime divisors of n are 1 modulo 4, then in every representation the three denominators have pairwise nonsquare rational ratios.

The stronger proof-level statement is: for a square pair Y/Z, put A=4cX-n, delta=gcd(A,nX), alpha=A/delta. Every prime divisor of delta divides n; alpha is odd with every prime divisor 1 modulo 4; and n*delta=3 modulo 4.

**Status: proved on paper in I-014; separate main audit pending.**

## 2. What appears new compared with the local literature

H-006 restricts clean types and a same-status reduced pair. The new obstruction applies to ALL representations, including non-clean composite ones, and to ALL three denominator pairs when n has only 1-modulo-4 prime factors. The exact existential prime-support classification is absent from the inspected local markdown register.

The elementary primitive-sum-of-two-squares fact, the q=3-modulo-4 repeated-denominator identity, and scaling are standard and are NOT originality claims. The constructive direction uses precisely those known ingredients.

External priority and standalone publishability remain **unresolved**. The theorem may be known in different language. A short structural note with the accepted clean-character theorem is **plausible**, not certified publishable. No fresh source audit or external literature campaign is authorized.

## 3. Smallest useful proof target — ONE concrete main task

Independently rederive **I-014 Sections 2–4**, then submit a new self-contained H-007 if that sequence is still available, or identify an exact failed implication/counterexample.

Audit checklist:

1. A rational-square pair has Y=Hr²,Z=Hs² with gcd(r,s)=1, and the reduced numerator of its reciprocal sum has no odd prime divisor 3 modulo 4.
2. For arbitrary X, not necessarily coprime to n, every prime divisor of gcd(4cX-n,nX) divides n. Do not replace this support statement with an unproved delta|n assertion.
3. A, delta and alpha are odd; alpha=1 modulo 4 gives delta=-n modulo 4 and n*delta=3 modulo 4. The sign is crucial.
4. Permuting the singled-out denominator covers all pairs; no clean-type assumption was smuggled back in.
5. For c=1 and q|n, q=3 modulo 4, set n=mq,t=(q+1)/4 and check (mt,2mqt,2mqt) by positivity, integrality and 4XYZ=n(XY+XZ+YZ).
6. Preserve the distinction between general-numerator necessity and numerator-4 sufficiency; repeated denominators are allowed.
7. Check the paper boundary cases: non-clean n=25; square-pair n=21 and n=9; square-pair-free representation at n=7; no representation of 8/3; and the n=3,X=4 fixed-X failure despite reduced remainder numerator 13.

In the same update, record R-009's H-006 acceptance rather than treating H-006 as pending. Do not rewrite historical payloads, reviews, or ideas.

No interpreter execution is needed. The existing stalled-process state is unconfirmed; this proof-only task should not queue diagnostic or decorative computations.

## 4. Expected incremental result

One audited theorem giving:

* a complete existential classification of rational-square pairs for odd n at numerator 4;
* an unrestricted general-numerator obstruction on an infinite multiplicative set of denominators;
* a precise explanation of why square-ratio constructions cannot solve any n supported on primes 1 modulo 4, while unrestricted representations there remain possible.

This adds a substantive domain extension and a clean iff statement, not a new denominator-envelope level, prime-range verification, or universal proof.

## 5. Main uncertainty and stop rule

The primary uncertainty is **external priority and significance**, not an intended missing arithmetic bridge. Main's separate proof audit is still pending.

* **Proved:** accepted H-006; I-014's written theorem and explicit scope calculations.
* **Verified computationally:** no new result in this round.
* **Conditional:** no new theorem depends on an unproved conjecture; explicit theorem hypotheses are not a conditional-existence claim.
* **Plausible:** value of the combined structural note.
* **Blocked:** old forcing/nesting/inverse routes and external-priority certification under the offline boundary.
* **False:** replacing prime support by n=1 modulo 4 for unrestricted composites; making the converse universal in c; requiring square pairs in every solution; promoting the reduced-numerator condition to fixed-X sufficiency.
* **Unresolved:** separate main audit of T-009, external priority, standalone publishability, previous parser process state, and Erdős–Straus itself.

Stop after the audited H-007 or a precise counterexample. No artificial second direction, squareclass hierarchy, distinct-denominator converse hunt, range expansion, further bound optimization, network, installation, or full-proof campaign.