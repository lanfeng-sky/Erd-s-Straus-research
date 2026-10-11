# R-010 — Flagship audit of H-007 unrestricted square-ratio classification

## Verdict

**H-007 is accepted as proved within its stated hypotheses.** O-016 is discharged. No computational status is attached. The Erdős–Straus conjecture remains unresolved, and external priority/standalone publishability remain unresolved.

## Audit

Let a pair satisfy Y/Z=(r/s)^2 in lowest terms. Unique factorization gives Y=Hr^2, Z=Hs^2 with gcd(r,s)=1. Hence

\[
1/Y+1/Z=(r^2+s^2)/(Hr^2s^2).
\]
Since gcd(r^2+s^2,r^2s^2)=1, its reduced numerator is
\[
\alpha=(r^2+s^2)/\gcd(r^2+s^2,H).
\]
Every odd prime dividing r^2+s^2 makes -1 a quadratic residue modulo that prime, hence is 1 modulo 4. The same is true for every odd prime divisor of alpha. This is a necessary prime-support statement only; it is not a two-term sufficiency criterion.

For 4c/n=1/X+1/Y+1/Z, set A=4cX-n. Positivity gives A>0. Subtraction gives A/(nX)=1/Y+1/Z. With delta=gcd(A,nX), the reduced numerator is alpha=A/delta. Since n is odd, A, delta, alpha are odd. If a prime divides delta, it divides A and nX; if it does not divide n, it divides X, and A=4cX-n then forces it to divide n, contradiction. Thus every prime divisor of delta divides n; importantly, this proves support, not delta|n.

Because alpha has only 1-modulo-4 prime factors and is odd, alpha=1 mod 4. Since A=delta alpha=4cX-n, delta=-n mod 4 and n delta=3 mod 4. All prime factors of n delta are prime factors of n. Therefore n has a prime factor 3 mod 4. The argument is symmetric after permuting X,Y,Z, so if n is supported on primes 1 mod 4, no pair among the three denominators has a rational-square quotient, without clean, ordering, primality, or coprimality assumptions.

For the converse at numerator 4, choose q|n with q=3 mod 4, write n=mq and t=(q+1)/4. Then
\[
(X,Y,Z)=(mt,2mqt,2mqt)
\]
is positive integral and
\[
1/(mt)+2/(2mqt)=(q+1)/(mqt)=4/(mq)=4/n.
\]
Thus Y/Z=1. The displayed division-free certificate also checks exactly. This proves the existential equivalence between a square-ratio pair, an equal pair, and a 3-modulo-4 prime divisor of n.

## Scope and boundary checks

The theorem is existential at c=1, not universal over all representations. It does not claim all solutions at n with a 3-modulo-4 factor have a square pair. It does not extend sufficiency to arbitrary c. It does not assert delta|n. The examples n=25, n=21, n=9, n=7, c=2,n=3, and c=1,n=3,X=4 correctly expose these boundaries. In particular, the n=9 witness with X=36 gives delta=27, so the stronger divisibility claim is false even under the square-pair hypothesis.

## Classification of claims

- **Proved:** T-009a and T-009b exactly as stated; all-pairs permutation and constructive certificate.
- **Verified computationally:** none in this review; the examples are exact paper arithmetic.
- **Conditional:** none in the theorem's proof.
- **Plausible:** usefulness of a concise note combining T-009 with H-006.
- **Blocked:** external-priority certification under the current evidence boundary; old pointwise-forcing routes.
- **False:** replacing prime support by delta|n; replacing prime support by n=1 mod 4 for unrestricted composites; extending the converse to every c; treating reduced-numerator support as fixed-X sufficiency.
- **Unresolved:** external priority, standalone publishability, and Erdős–Straus itself.

The result is a structural obstruction to a restricted square-ratio construction method, not a solvability theorem or counterexample to Erdős–Straus.
