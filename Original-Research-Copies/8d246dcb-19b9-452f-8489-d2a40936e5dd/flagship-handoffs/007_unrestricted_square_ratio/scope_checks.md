# H-007 — Scope audit and exact paper checks

Date: 2026-10-05. Status of the displayed deductions: **proved**. These are exact PAPER calculations, not newly executed tests, sampled data, or a finite search.

## 1. D-009 checklist

1. Square-pair normalization: with H=gcd(Y,Z), coprime Y/H,Z/H have even prime valuations, giving Hr^2,Hs^2. The reduced sum numerator is (r^2+s^2)/gcd(r^2+s^2,H), not necessarily r^2+s^2 itself.
2. Gcd support: every prime divisor of delta=gcd(4cX-n,nX) divides n. No coprimality with c or X is used, and delta|n is not asserted. Section 4 gives an actual counterexample to that stronger assertion.
3. Parity and sign: A,delta,alpha are odd; alpha=1 modulo 4 gives delta=-n, not delta=n, modulo 4, and n*delta=3 modulo 4. alpha=1 is included.
4. Quantifiers: the singled-out denominator is arbitrary, so every pair is covered by permutation. No clean-type or ordering premise occurs.
5. Converse: only at c=1, m=n/q,t=(q+1)/4 give positive integral (mt,2mqt,2mqt). The sibling proof explicitly expands 4XYZ=n(XY+XZ+YZ).
6. Necessity versus sufficiency: no universal-c converse and no assertion about every representation at supported n. Equal denominators are permitted.
7. All prescribed boundary cases are checked below. No failed implication was found in the assigned I-014 Sections 2–4.

## 2. Non-clean n=25: a genuine domain extension

For (X,Y,Z)=(10,20,100),

    1/10+1/20+1/100 = 16/100 = 4/25,
    4XYZ = 80000,
    25*(XY+XZ+YZ) = 25*(200+1000+2000) = 80000.

Exactly one denominator is a 25-multiple, but the others are not units modulo 25: gcd(25,10)=gcd(25,20)=5. Thus neither clean type applies, under any permutation. The three reduced ratios are 1/2,1/10,1/5, all nonsquares by odd prime valuations.

T-009a proves the nonsquare-pair conclusion for EVERY representation of 4c/25, every c>=1, not just this example. It similarly applies to arbitrary products of primes 1 modulo 4 with arbitrary exponents, an infinite set containing all 5^a, a>=1. It is not an existence theorem on that set. In particular this valid representation of 4/25 shows that the obstruction is not nonexistence of Erdős–Straus representations.

## 3. n=1 modulo 4 does not replace the prime-support hypothesis

At n=21,

    (X,Y,Z)=(7,42,42),
    1/7+1/42+1/42 = 8/42 = 4/21,
    4XYZ = 49392 = 21*(294+294+1764).

Although 21=1 modulo 4, the pair Y=Z is a square pair. Here A=7, delta=gcd(7,147)=7, alpha=1 and n*delta=147=3 modulo 4. The support includes 3 and 7, both 3 modulo 4. Thus the unrestricted composite obstruction based merely on n=1 modulo 4 is **false**.

This does not contradict H-006, whose n=1-modulo-4 square-ratio obstruction concerns a clean same-status pair.

## 4. n=9: non-clean square pairs and support versus divisibility

The standard scaled equal-pair witness is

    4/9 = 1/3+1/18+1/18,
    4*(3*18*18) = 3888 = 9*(54+54+324).

At X=3, A=3, delta=3, alpha=1, n*delta=27=3 modulo 4. Clean II fails because gcd(3,9)>1.

The prescribed historical witness also gives

    4/9 = 1/3+1/12+1/36 = 16/36.

To expose its square pair, label (X,Y,Z)=(36,3,12). Then Y/Z=1/4=(1/2)^2, and

    4XYZ = 5184 = 9*(108+432+36),
    A=4*36-9=135,     nX=324,
    324=2*135+54,     135=2*54+27,
    delta=gcd(135,324)=27,   alpha=5,
    A/(nX)=5/12=1/3+1/12,
    H=3, r=1, s=2, r^2+s^2=5,
    n*delta=243=3 modulo 4.

Here delta=27 does NOT divide n=9, although all its prime divisors divide n. This directly shows that strengthening the support lemma to delta|n is **false**, even under the full hypothesis of an actual square-pair solution. It is an additional audit observation within the already prescribed example, not a new search or theorem hierarchy.

These examples also prohibit replacing 'n has a prime divisor 3 modulo 4' by 'n itself is 3 modulo 4' or by an odd-exponent requirement on such primes in n. The odd exponent needed in the proof belongs to n*delta, not necessarily n.

## 5. The criterion is existential over representations

At n=7,

    1/3+1/6+1/14 = (14+7+3)/42 = 4/7,
    4*(3*6*14) = 1008 = 7*(18+42+84).

The ratios reduce to 1/2,3/14,3/7. Each has a prime of odd valuation, so none is a rational square. Yet q=7,m=1,t=2 in the proved converse gives (2,28,28):

    1/2+1/28+1/28=4/7,
    4*(2*28*28)=6272=7*(56+56+784).

Thus a 3-modulo-4 prime divisor permits a square pair in SOME representation; requiring such a pair in EVERY representation is **false**.

## 6. Universal-c sufficiency is false: no representation of 8/3

Take c=2,n=3, even with gcd(c,n)=1. If at most one denominator is 1, a three-term reciprocal sum is at most 1+1/2+1/2=2<8/3. Three denominators equal to 1 give 3, not 8/3. If exactly two denominators equal 1, the remaining reciprocal must be 2/3, requiring the noninteger denominator 3/2.

All cases are impossible. Thus 8/3 has no three-positive-integer-unit-fraction representation at all. This refutes a converse for every c, not Erdős–Straus, whose numerator is 4. T-009a's arbitrary-c necessity is unaffected.

## 7. Reduced-numerator support does not suffice at fixed X

Take c=1,n=3,X=4. Then

    A=13, delta=gcd(13,12)=1, alpha=13,
    A/(nX)=13/12,   n*delta=3 modulo 4.

The prime 13 is 1 modulo 4, so the stronger necessary numerator-support condition also holds. If 13/12=1/Y+1/Z and both denominators were at least 2, the sum would be at most 1. Hence at least one denominator equals 1. The other is forced to be 12; this gives the only unordered completion. Their ratio 1/12 is not a rational square (its valuation at 3 is odd).

There IS an ordinary three-term representation (4,1,12):

    4XYZ=192=3*(4+48+12).

It simply has no square-pair completion at the specified X=4. Thus promoting the numerator-support condition to a fixed-X sufficiency criterion is **false**. No failure of unrestricted Erdős–Straus existence is inferred.

## 8. Evidence and limitations ledger

- **proved:** T-009a/b by the sibling universal proof; all paper calculations above.
- **false:** delta|n strengthening; unrestricted n=1-modulo-4 obstruction; universal-c converse; every-representation square-pair claim; fixed-X sufficiency from reduced-numerator support.
- **verified computationally:** no new claim; no program or numerical range was executed.
- **conditional:** no theorem here depends on an unproved conjecture.
- **plausible:** usefulness of a combined structural note with accepted H-006.
- **blocked:** old pointwise forcing/nesting/inverse routes; external-priority certification under the offline boundary.
- **unresolved:** flagship review of NEW H-007, external priority, standalone publishability, previous parser process state, and Erdős–Straus.

No network, installation, Lean, source parser, process diagnosis, timing or hash audit. No heuristic evidence or new existence conjecture was introduced. These exact failures of extrapolated claims are not counterexamples to Erdős–Straus. Stop after this D-009 audit.