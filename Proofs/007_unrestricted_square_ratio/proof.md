# H-007 — Complete proof of T-009

Status: **proved**. Separate main derivation under D-009, 2026-10-05.
This is an ordinary mathematical proof, not bounded computation or formal verification.

## 1. Statement and quantifiers

Let c>=1 and n>=3 be integers, n odd, and let X,Y,Z be positive integers with

    4c/n = 1/X + 1/Y + 1/Z.                         (1)

No ordering, clean-type, primality, squarefreeness, gcd(c,n)=1, or gcd(X,n)=1 assumption is imposed.

**T-009a.** If Y/Z is a square of a positive rational number, define

    A=4cX-n, delta=gcd(A,nX), alpha=A/delta.

Then A, delta and alpha are positive odd integers. Every prime divisor of delta divides n; every prime divisor of alpha is 1 modulo 4 (alpha=1 allowed); and

    delta = -n (mod 4),     n*delta = 3 (mod 4).      (2)

In particular, n has a prime divisor 3 modulo 4. The assertion applies to any pair by permuting (X,Y,Z).

**Corollary.** If every prime divisor of n is 1 modulo 4, then in EVERY representation (1), each of X/Y, X/Z and Y/Z is a nonsquare in the positive rationals. This includes non-clean composite representations and arbitrary c.

**T-009b.** For every odd n>=3, the following are equivalent:

    (i) Some positive integral representation of 4/n has a rational-square pair.
    (ii) Some positive integral representation of 4/n has two equal denominators.
    (iii) n has a prime divisor q congruent to 3 modulo 4.

Repeated denominators are allowed. Statements (i) and (ii) quantify over representations separately; no transformation preserving a specified X or a specified original pair is asserted. Sufficiency is claimed only for c=1.

## 2. Elementary lemma on a square-ratio pair

Suppose Y/Z is a rational square and H=gcd(Y,Z). Put a=Y/H,b=Z/H, so gcd(a,b)=1. In a rational square every prime valuation is even. Since a,b are coprime, each exponent in a and b is therefore even. Hence for positive coprime integers r,s,

    Y=Hr^2, Z=Hs^2, gcd(r,s)=1.

Set S=r^2+s^2. If a prime divides S and r*s, it divides both r and s, which is impossible. Thus gcd(S,r^2*s^2)=1, and

    1/Y+1/Z = S/(H*r^2*s^2)

has reduced numerator

    N = S/gcd(S,H).                                  (3)

The denominator is reduced by the same gcd. This gcd identity follows prime by prime from gcd(S,r^2*s^2)=1; it does not assume gcd(S,H)=1.

For any odd prime ell|S, neither r nor s vanishes modulo ell. Thus u=r/s modulo ell satisfies u^2=-1. Since ell is odd, u^2 is not 1, whereas u^4=1. The order of u in the group of nonzero residues is exactly four, so 4 divides ell-1. Every odd prime divisor of S, and therefore of N, is 1 modulo 4.

If N is odd, all its prime divisors are 1 modulo 4 and consequently N=1 modulo 4. This includes N=1. We do NOT claim S itself is always odd: if r,s are both odd, S=2 modulo 4 and its factor 2 must be cancelled for N to be odd. No sufficiency half of the sum-of-two-squares theorem is needed.

## 3. Unrestricted necessity: prime support and the sign

Subtract 1/X from (1). The right side below is positive:

    A/(nX) = 1/Y+1/Z > 0,    A=4cX-n.

Therefore A>0. Since n is odd and 4cX is divisible by 4, A is odd; its positive divisor delta and the quotient alpha are odd too. The fraction A/(nX) has reduced numerator alpha.

For a prime ell dividing delta, we have ell|A and ell|nX. If ell did not divide n, primality would give ell|X. But then ell would divide 4cX-A=n, a contradiction. Consequently

    every prime divisor of delta divides n.           (4)

This argument never cancels c and never assumes X is coprime to n. It controls support, not exponents: delta|n does NOT follow.

If Y/Z is a rational square, Section 2 and uniqueness of a reduced positive fraction give alpha=N in (3). Since alpha is odd, every prime divisor of alpha is 1 modulo 4. Hence alpha=1 modulo 4. Now

    A=delta*alpha = delta (mod 4),
    A=4cX-n = -n (mod 4).

Thus delta=-n modulo 4. Multiplying by odd n and using n^2=1 modulo 4 yields

    n*delta = -n^2 = -1 = 3 (mod 4).

By (4), every prime divisor of n*delta divides n. If all prime divisors of n were 1 modulo 4, their product with any nonnegative exponents would be 1 modulo 4, contradicting the last display. Hence a prime q|n satisfies q=3 modulo 4. This proves T-009a including its stronger reduced-numerator statement.

For the corollary, suppose any one of the three denominator ratios were a rational square. Single out the remaining denominator as X and repeat this proof. The conclusion would contradict the prime support of n. Since the argument never required X to be smallest, a unit modulo n, or of a specified divisibility type, it applies to all three pairs. There is no assertion that a representation exists for each c.

## 4. Exact existential classification and constructive converse

For c=1, (i) implies (iii) by Section 3. Equal denominators have ratio 1, so (ii) implies (i).

Assume (iii), and choose a prime divisor q=3 modulo 4. Set

    m=n/q,  t=(q+1)/4,
    X=mt,   Y=Z=2mqt.                                (5)

Both m,t are positive integers, so the three denominators are positive integers. Direct exact addition gives

    1/X+1/Y+1/Z
      = 1/(mt)+1/(mqt)
      = (q+1)/(mqt)
      = 4/(mq) = 4/n.

Independently expanding the requested division-free certificate gives

    XYZ = 4m^3*q^2*t^3,
    XY+XZ+YZ = 4m^2*q*t^2*(q+1),
    4XYZ = 16m^3*q^2*t^3
          = n*(XY+XZ+YZ),

because n=mq and q+1=4t. Thus (iii) implies (ii), completing the equivalence. Primality is needed only to choose q from n's support; formula (5) also works for any positive divisor q=3 modulo 4.

The converse uses the standard repeated-denominator identity and scaling, not a newly discovered infinite identity. The incremental content is the unrestricted obstruction for arbitrary rational-square pairs, together with the resulting exact existential classification.

## 5. Audit conclusion and limits

No failed implication was found in I-014 Sections 2–4. The proof does not rely on H-006, its Jacobi symbols, clean normalization, or any finite result. It does not assert new congruence coverage, unrestricted nonexistence, or a proof of Erdős–Straus.

The necessary conditions at a chosen X need not suffice for a square-pair completion. A prime divisor 3 modulo 4 need not force a square pair in every representation. The c=1 sufficiency does not extend to every c. See scope_checks.md for exact failures of these extrapolations and an actual square-pair solution with delta not dividing n.

External priority and standalone publishability remain **unresolved**; the result is a proved extension of the inspected local register, not certified external novelty.