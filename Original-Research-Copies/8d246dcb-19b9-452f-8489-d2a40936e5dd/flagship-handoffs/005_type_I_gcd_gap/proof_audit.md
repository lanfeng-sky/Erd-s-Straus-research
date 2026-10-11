# T-005 — Intrinsic Type-I common gcd and sharp denominator gap

D-005 main-model audit, sequence 005, 2026-10-04. **Status: proved.**
This note supplies the entire derivation, including the normalization and
Jacobi prerequisite; no other workspace file is needed to read the proof.
Only elementary quadratic reciprocity and its supplementary laws are used
as standard inputs. The finite replay is not an input to the universal proof.

## 1. Statement and scope

Let p be a prime congruent to 1 modulo 4 and let positive integers X,Y,Z
satisfy

    4XYZ = p(XY+XZ+YZ).

Assume X is a smallest denominator and exactly ONE of the three
denominators is divisible by p (Type I). Write G=gcd(X,Y,Z), the gcd of
ALL THREE denominators. Then

    (G/p) = -1,                         [Legendre symbol]
    6X <= 3p-2G+1.                      [T-005a]

If p is congruent to 1 modulo 24, then

    30X <= 15p-14G+1.                   [T-005b]

Equality in T-005b holds if and only if, up to permutation,

    G=45t+29, p=672t+433 is prime, t>=0,
    (X,Z,Y)=(7G,8G,56pG).

Consequently G is not a square, including G=1. If q(p) is the least
positive quadratic nonresidue, G>=q(p), so safe Type-I upper cutoffs are
floor((3p-2q(p)+1)/6), and, at p=1 mod 24,
floor((15p-14q(p)+1)/30). These are necessary conditions only.
No statement here prunes Type II, forces a Type-I solution, or proves
Erdős–Straus for a new prime range. External priority is **unresolved**.

## 2. Derive the normalized B form from any such solution

Because X is smallest, positivity gives p/4<X<=3p/4<p. Thus X is p-free.
Label Y as the unique p-divisible denominator and Z as the other p-free
denominator; Y need not be the second-smallest. Put a=4X-p>0. Since
p is prime and 0<X<p, gcd(a,pX)=1. The equation becomes

    aYZ=pX(Y+Z).

Define d=aY-pX and e=aZ-pX. They are positive because dZ=pXY>0 and
eY=pXZ>0, and multiplication gives de=p²X². Modulo p, e=aZ is nonzero,
whereas d is divisible by p. Therefore the p-adic valuation of d is EXACTLY
2 and that of e is 0. Write

    d=p²C, e=E, CE=X², pC+X=0 mod a.

Now reduce C/X=u/v to lowest terms: with d0=gcd(C,X), C=d0*u and
X=d0*v, gcd(u,v)=1. Since C divides X², u divides d0*v², hence u divides
d0. Write d0=gu. Then

    X=guv, C=gu², E=gv², gcd(u,v)=1.

All these are positive integers; p divides none of g,u,v. As gcd(a,gu)=1,
the congruence pC+X=gu(pu+v)=0 mod a makes

    k=(pu+v)/a

positive and integral. Reconstruction yields

    Y=(pX+p²C)/a=pguk,   Z=(pX+E)/a=gvk.

Moreover p does not divide k: modulo p, ak=v is nonzero. Substituting
a=4guv-p into ak=pu+v gives

    v(4guk-1)=p(u+k).

Since p does not divide v, some positive integer h satisfies

    4guk-1=ph,   hv=u+k.                [B]

Here h=3 mod 4, since p=1 mod 4 and 4guk-1=3 mod 4; in particular h>=3.
This derivation does not assume that p and h are coprime.

If a divisor divides u and k, ak=pu+v makes it divide v; so gcd(u,k)=1.
If a divisor divides v and k, the same equation makes it divide pu; as
p is prime, p does not divide v, and gcd(u,v)=1, this gives gcd(v,k)=1.
Thus u,v,k are pairwise coprime. In particular

    gcd(uv,vk)=v,   gcd(v,puk)=1,
    gcd(guv,pguk,gvk)=g.

Therefore the intrinsic full common gcd is G=g, not merely a pairwise gcd.
Ordering X<=Z gives u<=k. Equality would imply u=k=1 by coprimality,
then hv=2, impossible since h>=3. Hence k>u.

## 3. Character prerequisite and intrinsic obstruction

For arbitrary positive integers b,s, put M=4bs-1. Then M is odd,
M=3 mod 4, and gcd(b,M)=1. For any odd prime r dividing b, M=-1 mod r,
so quadratic reciprocity for Jacobi symbols gives

    (r/M)=(-1)^((r-1)/2)(M/r)
         =(-1)^((r-1)/2)(-1/r)=1.

If 2 divides b, M=7 mod 8 and (2/M)=1. Multiplying over the prime
factorization of b, with multiplicity, proves

    (b/(4bs-1))=1.                     [Jacobi lemma]

This includes b=1 and composite M with repeated factors.

Apply it to b=g,s=uk, so M=ph. Reducing [B] modulo h gives k=-u,
therefore 4gu²=-1 mod h. The equation 4guk-ph=1 also shows that 2,g,u
are units modulo h. Since h=3 mod 4,

    (g/h)=(4gu²/h)=(-1/h)=-1.

The Jacobi symbol is multiplicative in its odd denominator, even when
its factors share primes. Thus, explicitly ALLOWING p|h,

    1=(g/(ph))=(g/p)(g/h),
    (g/p)=-1.

As G=g and p does not divide g, this proves the character assertion,
G>=q(p), and the exclusion of every square common gcd.

## 4. Exact gap and integer monotonicity

Put r=k-u>=1 and delta=p-2X. Using ph=4guk-1 and hv=u+k gives

    delta=(2gu(k-u)-1)/h
         =v*(2gur-1)/(2u+r).           [D]

For g>=1 write F_g(u,r)=(2gur-1)/(2u+r). This is positive for positive
integer u,r. The following exact cross-products show strict monotonicity:

    F_g(U,r)-F_g(u,r)
      = 2(gr²+1)(U-u)/((2U+r)(2u+r)) > 0   if U>u;

    F_g(u,R)-F_g(u,r)
      = (4gu²+1)(R-r)/((2u+R)(2u+r)) > 0   if R>r.

No real approximation or numerical optimization is used. Since v>=1,
[D] implies

    delta>=F_g(1,1)=(2g-1)/3>0,
    6X<=3p-2g+1.

In particular X<p/2 for Type I. This proves T-005a on all its hypotheses.

## 5. Sharp improvement at p=1 mod 24

The supplementary law makes (2/p)=1, and reciprocity makes (3/p)=1
because p=1 mod 12. Also 1 and 4 are squares. Consequently q(p)>=5,
and the character obstruction gives g>=5. The following three cases
exhaust all positive integer v,r.

1. If v>=2, [D] and monotonicity give

       delta >= 2(2g-1)/3 > (14g-1)/15,

   since the difference is (6g-9)/15>0.

2. If v=1 and r>=2, they give

       delta >= F_g(1,2)=(4g-1)/4 > (14g-1)/15,

   since the difference is (4g-11)/60>0.

3. If v=r=1, then k=u+1 and h=2u+1. As h=3 mod 4, u is odd.
   The first three positive odd values are impossible:

   * u=1 implies 8g=3p+1; modulo 8 its right side is 4, not 0.
   * u=3 implies 48g=7p+1; modulo 24 its right side is 8, not 0.
   * u=5 implies 120g=11p+1; modulo 24 its right side is 12, not 0.

   Thus u>=7, and strict monotonicity gives

       delta=F_g(u,1)>=F_g(7,1)=(14g-1)/15.

Altogether 15(p-2X)>=14g-1, or 30X<=15p-14G+1. In cases 1 and 2
it is strict; in case 3 equality holds exactly when u=7. Hence every
equality solution has

    (u,k,v,h)=(7,8,1,15),   15p+1=224g.

Requiring p=1 mod 24 means 224g=16 mod 360, equivalently
28g=2 mod 45. Since 28 is invertible modulo 45, g=29 mod 45. Positivity
then gives g=45t+29 with integer t>=0, and p=672t+433. Reconstruction
is exactly (X,Z,Y)=(7g,8g,56pg). This proves necessity of the complete
equality classification.

Conversely, for every integer t>=0 put g=45t+29 and n=672t+433. Then
15n+1=224g, and all three denominators 7g,8g,56ng are positive integers.
Their reciprocal sum is exactly

    1/(7g)+1/(8g)+1/(56ng)
      =(15n+1)/(56ng)=4/n.

If n=p is prime, then p=1 mod 24 and p>=433, so p does not divide 56;
also 224g-15p=1 shows p does not divide g. Thus precisely the denominator
56pg is p-divisible, gcd(7g,8g,56pg)=g, and 7g is smallest. Finally
30*7g=15p-14g+1. This proves sufficiency without assuming every t gives
a prime or asserting an infinite prime family.

## 6. Attainment, discarded claim, and limits

At t=0, p=433 and g=29. Trial division by the primes at most sqrt(433),
namely 2,3,5,7,11,13,17,19, confirms primality. The equality triple is

    (203,232,703192), G=29,
    30*203=15*433-14*29+1=6090.

The reciprocal calculation above proves its division-free certificate;
the authorized exact replay also checks it. Therefore the bound is attained,
not only an asymptotic estimate. In particular its coefficient 14 cannot
be increased while keeping the remaining terms unchanged.

I-009's discarded draft assertion for Type II,
X<=floor((p+1)/4), is **false**, already at the retained p=1009 Type-II
certificate with X=253 whereas floor(1010/4)=252. It is neither an input
nor a conclusion of this theorem. Necessary nonresidue gcd conditions
are not sufficient construction rules; primitive Type-II solutions are
not excluded. The older unsuccessful nesting and inverse routes remain
**blocked**, not counterexamples to Erdős–Straus. The full conjecture and
external originality are **unresolved**. No network, Lean, new solution
search, or fresh-independent-agent review was used or claimed.

## 7. Bounded evidence, distinct from proof

Only the unchanged R-005 probe was rerun: 2991 retained pairs / 187
retained primes; exactly the first saved B witness at each of 955 successful
pairs. It checks positivity, the division-free identity, normalization,
pairwise coprimality, the full gcd, character, ordering, both gaps and
equality criterion. There are zero equality cases among these 955 saved
witnesses; the single algebraically derived 433 certificate attains equality.
It also checks the original H-002/H-004 manifests and reproduces H-004's
retained output byte-for-byte. **Status: verified computationally.**
This is not enumeration of all Type-I solutions. Universal quantifiers
in sections 1–5 follow from the written argument, not from these tests.
