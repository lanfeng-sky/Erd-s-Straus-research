# H-007 — Unrestricted rational-square-pair classification

Assignment: D-009, following I-014 and R-009. Main audit date: 2026-10-05.
Mathematical status: **proved**. Flagship review of this NEW package: **unresolved**.

## The result

For every odd integer n>=3, the following are equivalent:

1. Some positive-integer representation of 4/n has two denominators whose ratio is a rational square.
2. Some positive-integer representation of 4/n has two equal denominators.
3. n has a prime divisor congruent to 3 modulo 4.

These are existence statements about representations; repeated denominators are allowed. They do not assert that every representation has a square pair.

The necessary direction holds for 4c/n for EVERY integer c>=1, without ordering, clean-type, or gcd(c,n)=1 assumptions. Thus if every prime divisor of n is 1 modulo 4, then every actual representation of 4c/n has three pairwise nonsquare rational denominator ratios, including non-clean composite representations.

More precisely, if Y/Z is a rational square in a representation, set

    A=4cX-n, delta=gcd(A,nX), alpha=A/delta.

Then A, delta, alpha are positive odd integers; every prime divisor of delta divides n; every prime divisor of alpha is 1 modulo 4; delta=-n modulo 4; and n*delta=3 modulo 4. The conclusion concerns prime support, NOT delta|n.

## Self-contained payload

- [proof.md](proof.md): complete separate main derivation of the elementary square-pair lemma, unrestricted necessity, all-pairs corollary, and constructive converse with the division-free certificate.
- [scope_checks.md](scope_checks.md): every D-009 checklist item and exact paper checks at n=25,21,9,7, the impossibility of 8/3, and the fixed-X failure at n=3,X=4. The prescribed n=9 witness also explicitly refutes delta|n, even for an actual square-pair solution.

No historical handoff, external theorem digest, script, dataset, or network resource is needed to verify this package. Basic unique factorization, prime arithmetic, and the elementary order-four argument are the only background facts.

## Increment and evidence boundary

This extends the inspected local register from clean same-status pairs to ALL pairs in unrestricted representations on the stated prime-support domain, and gives an exact existential classification for numerator 4. It complements, rather than replaces, H-006's stronger signed Jacobi information on its clean domain.

The primitive-sum-of-two-squares lemma, repeated-denominator identity at q=3 modulo 4, and scaling are standard ingredients, NOT new-identity or priority claims. External priority and standalone publishability: **unresolved**. Value of a combined structural note: **plausible**.

Method: ordinary paper proof and displayed exact integer arithmetic. No numerical experiment, interpreter/terminal job, regression replay, timing, hash validation, Lean proof, fresh-independent-agent review, installation, source parsing, network, or process-control operation. No new result is labelled **verified computationally**. The previous parser process state remains **unresolved**.

R-009 has accepted H-006 within its original hypotheses and discharged O-013; that acceptance is now reconciled in the live main records. H-001 through H-006 and all historical ideas, reviews, decisions and results remain unchanged. This new H-007 is submitted, not already accepted.

## Endpoint

D-009's assigned proof audit is complete; no failed implication was found in I-014 Sections 2–4. Exact false extrapolations are recorded separately, not mistaken for failures of Erdős–Straus. The conjecture remains **unresolved**, and old forcing routes remain **blocked**.

Minimal next step: flagship reviews this H-007 in a NEW numbered review, concentrating on numerator reduction, prime support versus divisibility, the modulo-four sign, all-pairs quantifiers and the c=1 converse. No interpreter execution is needed. Stop here: no distinct-pair search, squareclass hierarchy, range expansion, bound optimization, literature campaign, or pointwise-existence conjecture.
