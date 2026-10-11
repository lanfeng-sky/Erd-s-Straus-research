# H-006 — Audit checklist, exact paper checks, and limitations

Date: 2026-10-05. Status of the deductions below: **proved** by displayed exact arithmetic. These are paper calculations, NOT a newly executed regression. No process-state diagnosis, timing, numerical replay, or new solution range is claimed.

## 1. D-008 checklist

* Composite normalization: gcd(a,n)=gcd(a,X)=1 are separately proved; clean-I E is a unit at EVERY prime of n, so DE=n^2X^2 allocates all n^2 to D. Clean-II divides both factors by n and uses CF=X^2.
* Pairwise coprimality: u,v,k are pairwise coprime in both patterns. The full gcd is G=g, separately from H=Gv in I or H=nGk in II.
* Numerator twist: the clean-I Jacobi lemma uses b=cG, not G.
* Reciprocity: M=3 mod 4 retains the (-1/n) factor at general odd n.
* Shared n,h factors: denominator multiplicativity is valid without gcd(n,h)=1. The n=93 example below actually has gcd(n,h)=3.
* Nonunit k: clean II cancels v, not k. The n=15 example has gcd(k,n)=3.
* Pair obstruction: its rational-square consequence uses n=1 mod 4, not all odd n.
* Type-II pending audits: the m<b<2m cross-product and b>=2m ordering cases are independently expanded; d=1,2,4 residues and equality converses are explicit. Parity gcd ceilings track equality in each inequality, and unfloored equality is distinguished from equality after flooring.

No failed implication was found in I-013 Sections 3–6, I-011 Sections 2–5, or I-012's theorem proof. The main rederivation is not a fresh independent-agent or formal-verification claim.

## 2. Required clean-type boundary examples

### (c,n)=(2,5): omission of c is false

Take (X,Y,Z)=(1,10,2), G=1. Over denominator 10 the reciprocal numerator is 10+1+5=16, giving 8/5. Clean I holds, gcd(5,1*2)=1.

    a=3, D=25, E=1,
    (g,u,v,k,h)=(1,1,1,2,3), M=15,
    H=1, (r,s)=(1,2).

The unit squares modulo 5 are 1,4. Thus (G/5)=1, while (-cG/5)=(-2/5)=-1. The un-twisted general-numerator clean-I assertion is **false**. The signed theorem holds.

### (c,n)=(1,3): dropping the minus sign is false

Take (X,Y,Z)=(1,6,6), G=1. The reciprocal sum is (6+1+1)/6=4/3; this is clean II.

    a=1, D=E=3,
    (g,u,v,k)=(1,1,1,2), M=7,
    H=6, (r,s)=(1,1).

Here ((X/G)/3)=1 and (-(X/G)/3)=(-1/3)=-1. Also U/V=1 IS a rational square. This simultaneously checks the signed theorem and refutes an extension of the square-ratio obstruction to n=3 mod 4.

### (c,n)=(1,15): k need not be a unit in clean II

Take (X,Y,Z)=(4,90,180), G=2. Over 180 the numerator is 45+2+1=48, giving 4/15. Clean II holds and gcd(4,15)=1.

    a=1, D=30, E=120, C=2, F=8,
    (g,u,v,k)=(2,1,2,3), M=23,
    Mv=46=15*3+1, n=23-8=15,
    H=90, (r,s)=(1,2).

Thus gcd(k,n)=3. Dividing Y,Z only by n gives 6,12, whose Jacobi symbols modulo 15 are zero. The full reduction gives

    (-2/15)=(-2/3)(-2/5)=1*(-1)=-1.

The theorem holds without illegitimate cancellation of k or misidentification of H.

### (c,n)=(1,93): shared n,h factors and nonlocal signs

Take (X,Y,Z)=(35,6510,70), G=35. Over 6510 the numerator is 186+1+93=280, giving 4/93. The free denominators are coprime to 93=3*31, so this is clean I.

    a=47, nX=3255,
    D=302715=93^2*35, E=35,
    (g,u,v,k,h)=(35,1,1,2,3), M=279=93*3,
    H=35, (r,s)=(1,2).

In particular gcd(n,h)=3, a case the proof explicitly permits. Since 93=1 mod 4,

    (-35/93)=(35/93)=(2/3)(4/31)=-1.

For the reduced pair, (2/3)=-1 but (2/31)=1 by the supplementary law at 31=7 mod 8. Thus the global negative Jacobi sign does not force a negative local sign at every prime factor.

### n=9: non-clean representations must not be excluded

    4/9=1/3+1/12+1/36

because the reciprocal numerator over 36 is 12+3+1=16. There is exactly one 9-multiple, but the other denominators are not units modulo 9. Assigning X=3,Y=36,Z=12 makes gcd(9,XZ)=9, so clean I fails; clean II also fails. G=3, and (-G/9)=0, not -1. This refutes replacing the clean hypotheses by a mere count of n-multiples, not the Erdős–Straus conjecture. The odd-square corollary concerns clean types only.

## 3. Previously specified Type-II equality examples, checked on paper

For T-006a, p=313, c=45 gives p=7c-2, (X,Y,Z)=(90,626,14085). The symbolic reciprocal identity in type_II_proof.md specializes exactly, and 7*90=2*313+4=630. Full gcd is 1. Primes at most sqrt(313) are 2,3,5,7,11,13,17; the respective remainders are 1,1,3,5,5,1,7. Thus 313 is prime.

For T-006b, p=1009, c=92 gives p=11c-3, (X,Y,Z)=(276,3027,92828). Again the reciprocal identity is exact, and 11*276=3*1009+9=3036. Full gcd is 1; 1009=169 mod 840 and 8 mod 11. Primes at most sqrt(1009) are 2,3,5,7,11,13,17,19,23,29,31; the respective remainders are 1,1,4,1,8,8,6,2,20,23,17. Thus 1009 is prime.

For odd-s (Go), p=97, q=5, G=5 gives (25,970,4850). Here

    2p=(8G-1)q-1=194,
    8qG=2p+q+1=200.

Trial divisors 2,3,5,7 have remainders 1,1,2,6. Also 2 is a residue at 97=1 mod 8, 3 is a residue at 97=1 mod 12, 4 is a square, and (5/97)=(97/5)=(2/5)=-1. Thus q(97)=5. This attains the p=1 mod 8 bound, not a residual-domain sharpness assertion: 97 is outside R.

For even-s (Ge), p=4201, q=11, G=48 gives (1056,201648,4436256). Here

    p=(8G-2)q-1=4201,
    8qG=p+2q+1=4224.

The trial primes at most sqrt(4201)<65 and their exact remainders are:

    prime:      2  3  5  7 11 13 17 19 23 29 31 37 41 43 47 53 59 61
    remainder:  1  1  1  1 10  2  2  2 15 25 16 20 19 30 18 14 12 53

All are nonzero, proving primality. Supplementary laws and reciprocity give (2/p)=1, (3/p)=1 (p=1 mod 12), (5/p)=(1/5)=1, (7/p)=(1/7)=1. Every integer 1,...,10 factors into these residue primes, so all have positive character. But (11/p)=(p/11)=(10/11)=(-1/11)=-1. Hence q(4201)=11 without an Euler-test execution. Since 4201=1 mod 840, the even-case bound is attained within R.

Each identity check above uses the complete symbolic reciprocal identity already proved and positive integer denominators. Multiplying it by the positive common denominator gives exactly 4XYZ=p(XY+XZ+YZ); no floating-point equality is used.

## 4. Failed approaches and evidentiary limits

* **false:** dropping c in clean I; dropping the sign for n=3 mod 4; replacing composite clean coprimality by counts of n-multiples; extending the rational-square exclusion to all odd n. Exact scope failures appear above.
* **false:** the old Type-II cutoff X<=floor((p+1)/4) at retained p=1009,X=253>252. No claim here depends on it.
* **false:** I-010's unused difference formula. I-011 supplies the exact replacement; H-006 uses only the split-at-2m proof. Global monotonicity of (pb+b^2)/(4b-1) is not a valid route.
* **blocked:** previous existence forcing, nesting, and inverse hierarchy. The character conditions do not force the defining divisibilities or an admissible solution for each prime.
* **unresolved:** prior stalled source-parser process state; there was no returned execution result. This round launches no terminal/interpreter work and makes no diagnosis or retry.
* **verified computationally:** no NEW mathematical claim has this status in H-006. R-006/R-007's retained bounded outputs are historical evidence only and were not replayed or imported as proof premises.
* **unresolved:** external priority and Erdős–Straus. A concise combined structural note is **plausible**, not certified publishable.

No failed restricted ansatz or scope extrapolation is treated as a counterexample to Erdős–Straus. No fresh source-level originality audit, network request, installation, formalization, larger search range, or new pointwise conjecture is claimed.

## 5. Minimal next step

Flagship should review this new self-contained H-006, especially the composite normalization, shared n,h example, pairwise-versus-full gcd distinction, signed reciprocity, and the unfloored equality qualifications. Review should be a new numbered file; historical sources remain unchanged. No interpreter execution is needed to discharge this proof review.