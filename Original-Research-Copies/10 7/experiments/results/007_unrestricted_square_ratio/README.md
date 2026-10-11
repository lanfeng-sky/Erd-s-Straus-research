# Result 007 — Unrestricted rational-square-pair classification

Assignment D-009; main audit 2026-10-05. Status: **proved**.

## Result

For every odd n>=3, some representation of 4/n has a rational-square denominator pair iff some representation has two equal denominators iff n has a prime divisor 3 modulo 4. Necessity holds for every numerator 4c, c>=1, without gcd(c,n)=1, ordering or clean-type assumptions. Hence on n supported only on primes 1 modulo 4, every actual representation has three pairwise nonsquare rational denominator ratios.

Complete self-contained proof and scope checks:

    flagship/handoffs/007_unrestricted_square_ratio/

The proof reduces a square pair to Hr^2,Hs^2, identifies the reduced reciprocal-sum numerator, and combines its prime support with delta=gcd(4cX-n,nX), whose primes all divide n. The decisive sign is n*delta=3 modulo 4. The standard repeated-denominator identity supplies sufficiency at c=1.

## Exact arithmetic and evidence separation

- Universal theorem: **proved** by the ordinary paper derivation in H-007, not by a finite computation.
- Required boundary examples: exact PAPER arithmetic at n=25,21,9,7; nonexistence of 8/3; fixed-X failure n=3,X=4. Cleared certificates are displayed for every cited representation.
- Additional audit observation within the prescribed n=9 witness: at (X,Y,Z)=(36,3,12), Y/Z=1/4 but delta=gcd(135,324)=27 does not divide n=9. The stronger divisibility assertion is **false**; prime support is the correct lemma.
- New bounded computation: NONE. No program, range, random sample, runtime, environment-version measurement, or hash validation.
- Heuristic evidence/new conjecture: NONE. No new universal-existence conjecture or solution-range claim.
- No interpreter/terminal work, network, installation, Lean, parser retry or process control. Previous parser state: **unresolved**.

R-009's H-006 acceptance is reconciled in live records: O-013 **proved**. Main audit of T-009: O-015 **proved**. Review of this new H-007: O-016 **unresolved**. External priority and standalone publishability: **unresolved**; combined-note value: **plausible**. Old forcing routes: **blocked**; Erdős–Straus: **unresolved**.

The reduced-numerator support condition is not fixed-X sufficiency; the classification is not universal over representations or over c. Failures of these extrapolations are not counterexamples to Erdős–Straus. No novelty is claimed for the elementary sum-of-two-squares input, repeated-denominator identity or scaling.

## Record preservation

`previous_main_research_report.md` and `previous_open_obligations.md` preserve the pre-D-009 live summaries as read. Known-identities and research-log updates append to their earlier content; a current-status notice distinguishes acceptance from old submission-time notes. Historical handoffs H-001 through H-006, ideas, reviews, decisions, literature and prior result directories were not modified. No byte-hash verification is claimed.

D-009 ends with H-007. Minimal next step: flagship proof review only; no extra research direction or numerical replay.