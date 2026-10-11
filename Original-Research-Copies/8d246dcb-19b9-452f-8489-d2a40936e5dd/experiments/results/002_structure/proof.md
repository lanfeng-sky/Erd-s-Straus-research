# Elementary theorem audit: KI-002 and KI-004

2026-10-04. **Status: proved by elementary derivation.** No novelty claim,
Lean build, universal existence bound, or modular-cover claim is made.
This note is self-contained and independent of the Kneser input.

## 1. Exact fixed-x statement

For every prime p congruent to 1 modulo 4 and every integer x satisfying
p/4 < x < p, set a=4x-p and b=px. Positive integers y,z satisfy

    4xyz = p(xy+xz+yz)

if and only if at least one of these conditions holds:

    A: there is a positive divisor c of x^2 with c+x = 0 modulo a;
    B: there is a positive divisor c of x^2 with 4c+1 = 0 modulo a.

A and B need not be disjoint. Their formulas describe different p-divisibility
patterns of completions. This is an **unordered fixed-x equivalence**, not
an existence theorem asserting that some x always works.

Since p is odd, a is odd; more precisely a=3 modulo 4, hence a>=3.
Since 0<x<p and p is prime, gcd(p,x)=1. Thus

    gcd(a,x)=gcd(p,x)=1,
    gcd(a,p)=gcd(4x,p)=1,
    gcd(a,px)=1, and v_p((px)^2)=2.

All residues used below are units modulo a.

## 2. Positive factor pairs and necessity

The certificate is equivalent to ayz=b(y+z). Define d=ay-b and e=az-b.
Then dz=by>0 and ey=bz>0, so d,e are positive integers. Expanding gives

    de=(ay-b)(az-b)=b^2,
    d=e=-b modulo a.

Conversely any positive d,e with de=b^2 and d=e=-b modulo a gives
positive integral y=(b+d)/a and z=(b+e)/a. Expansion gives

    a^2 yz=ab(y+z), hence ayz=b(y+z),
    hence 4xyz=p(xy+xz+yz).

There are exactly three possible p-adic allocations in de=p^2 x^2:

- **1+1:** d=pc, e=pE, with cE=x^2. Cancelling p in
  pc=-px modulo a gives c=-x, so A holds.
- **2+0:** d=p^2 c, e=E, with cE=x^2. Cancelling p gives
  pc=-x. Since p=4x modulo a and x is a unit, 4c=-1; B holds.
- **0+2:** d=E, e=p^2 c is the same B argument with factors exchanged.

These cases are exhaustive because v_p(b^2)=2 and p does not divide x.
No restriction on the relative size of x,y,z was used.

## 3. Reconstruction, integrality, positivity, certificate

For a permitted c put E=x^2/c, a positive integer.

**A:** c=-x implies cE=x^2 and E=-x modulo a. Define

    y=p(x+c)/a, z=p(x+E)/a.

Both x+c and x+E are multiples of a, so y,z are integral and divisible
by p. Every numerator and a are positive. The factor pair is (pc,pE),
whose product is b^2 and whose two residues are -b. The expansion above
therefore proves exactly 4xyz=p(xy+xz+yz).

**B:** 4c=-1 and p=4x imply pc=-x modulo a. Also
E=x^2/c=-4x^2=-px modulo a. Define

    y=p(x+pc)/a, z=(px+E)/a.

Both displayed numerators are divisible by a. Moreover (x+pc)/a is
an integer, so p divides y; p does not divide z because az=px+E and
p divides neither a nor E. All numerators and a are positive.
The factor pair is (p^2 c,E), with product b^2 and both residues -b.
The same expansion proves exactly 4xyz=p(xy+xz+yz).

Thus both branches explicitly prove integrality and positivity before
using the identity. The finite audit also checks the division-free
certificate on every reconstructed divisor witness, not only the first.

## 4. Exact bounded-ratio formulation

Factor x as product(q^e_q). In the finite abelian unit group modulo a put

    D_x={d modulo a: d is a positive divisor of x},
    R_x=D_x D_x^{-1},
    H_x=<q modulo a: q prime and q|x>.

An exponent in a ratio of divisors runs through every integer -e_q,...,e_q:
choose exponents max(j,0) and max(-j,0). An exponent in c/x with c|x^2
runs through the same range, since the exponent in c is 0,...,2e_q.
Consequently

    R_x={c/x modulo a: c|x^2}
       ={product(q^j_q) modulo a: -e_q<=j_q<=e_q}.

A is precisely -1 in R_x. For B,

    4c=-1 iff p(c/x)=-1 iff c/x=-p^{-1} modulo a.

Every ratio can be inverted by exchanging its two divisors; thus R_x is
inverse-closed. Inverting -p^{-1} gives -p, so B is precisely -p in R_x.
We do NOT assume that R_x is closed under multiplication. Therefore

    fixed-x completion iff R_x intersects {-1,-p} modulo a.

H_x is a subgroup containing R_x, but subgroup membership alone is not
sufficient. At p=1201,x=303=3*101,a=11,

    D={1,2,3,6}, R={1,2,3,4,6,7,8}, H={1,2,...,10},
    targets={10,9}.

Both targets are in H but absent from R, so there is no completion at
this x. This is not a counterexample to Erdős–Straus.

## 5. Global finite equivalence, not pointwise forcing

For every prime p=1 modulo 4, existence of any positive integral
Erdős–Straus representation is equivalent to existence of an integer x in

    (p+3)/4 <= x <= floor(3p/4)

with the above target intersection. For necessity, sort a representation
as x<=y<=z. Positivity of the other fractions gives 4/p>1/x, hence
x>p/4. Also 4/p<=3/x gives x<=3p/4. Its x is therefore in the stated
integer interval and strictly below p, so Sections 1-4 apply.
For sufficiency, any x in the interval with either branch reconstructs
a representation; sort the triple if desired.

The fixed-x equivalence itself has NO smallest-denominator filter.
Since ay-b>0, every completion has y,z>b/a. If x<=p/2, then a<=p
and b/a>=x, so x is automatically smallest. For x>p/2 this is not
automatic. Imposing x<=y,z in a fixed-x audit would change its claim.

To enumerate ALL completions at a fixed x, exchange y,z to arrange
d<=e. Then 1<=d<=b, de=b^2, and both residue tests are necessary
and sufficient. This is a proved factor-pair bound, with no cutoff on z.
The scripts never discard a pair because another offset already worked.

## 6. Elementary failure certificates

Suppose a prime ell|a has ell=3 modulo 4 and every prime q|x is a
quadratic residue modulo ell. Then x and every divisor c of x^2 are
squares modulo ell, whereas -1 is a nonsquare. Also p=4x is a square.
Thus every ratio in R_x and every element of H_x is a square, and both
-1 and -p are nonsquares. Neither branch can hold.

More generally, if H_x contains neither target, R_x contains neither.
Otherwise a failure is a bounded-exponent miss: H_x permits at least
one target, but the exact signed-exponent box does not reach it.
These three failure types are exclusive by using the quadratic type
first, the remaining subgroup type second, and the bounded-exponent
miss last. The scripts save a prime-character witness, the entire group,
and/or the complete divisor-residue set as applicable.

## 7. Switched theorem and precise branch-A equivalence

For EVERY positive integer p, and EVERY positive integers g,k,d,e with

    de=4gk^2p+1, d=e=-1 modulo 4gk,

define u=(d+1)/(4gk), v=(e+1)/(4gk) and

    x=g*u*v, y=p*g*k*u, z=p*g*k*v.

The congruences give integral u,v; positive d,e ensure positive u,v.
All three denominators are therefore positive integers. Expanding the
factor equation gives

    4gk uv-u-v=kp, hence u+v=k(4g uv-p).

For an explicit division-free check let T=p*g^2*k*u*v. Then

    xy+xz+yz=T*(u+v+pk),
    4xyz=4*p^2*g^3*k^2*u^2*v^2,
    u+v+pk=4gk uv,
    p(xy+xz+yz)=4*p^2*g^3*k^2*u^2*v^2.

So the certificate holds. This sufficient forward theorem does not
require primality, an x-range, or gcd(u,v)=1. Since N=4gk^2p+1 is
1 modulo m=4gk, d=-1 modulo m implies its complement e=-1 too.
Exchanging factors proves the complete bound d<=floor(sqrt(N)).

For prime p=1 modulo 4 and p/4<x<p, A holds if and only if there are
coprime positive u,v with uv|x and a|(u+v). To see necessity, reduce
c/x=u/v. Prime-by-prime the exponents of u,v are the positive and
negative parts of exponent(c)-exponent(x), so they are disjoint and
uv|x. Since v|x, it is a unit modulo a, and c/x=-1 is equivalent to
u+v=0 modulo a. Conversely, uv|x lets c=xu/v be a positive divisor
of x^2, and c/x=-1 gives A.

Set g=x/(uv)>0 and k=(u+v)/a>0. Then d=4gku-1 and e=4gkv-1
are positive, are -1 modulo 4gk, and their expansion is

    de=16g^2k^2uv-4gk(u+v)+1=4gk^2p+1.

The switched y=p*g*k*u=p(x+c)/a and z=p*g*k*v=p(x+E)/a
are exactly the branch-A completion. Conversely a switched witness
with gcd(u,v)=1 and the stated x-range supplies uv|x and a|(u+v),
hence A. An unnormalized forward witness still produces the solution;
reducing u/v recovers a normalized branch-A witness.

Both g and k are needed for this exact reparameterization; g=1 alone
is an artificial restriction. This says nothing about whether some g,k
always occurs. Branch B remains a separate indispensable possibility.

## Limitations and next step

These are exact fixed-x theorems, an existence equivalence with a finite
x-interval, and a switched construction. No pointwise existence theorem
for every prime has been proved. No complementary modulo-840 coverage
was used. The minimal next step is adversarial review of these statements
and reproduction of the frozen 2991-pair and seven-prime audit.
