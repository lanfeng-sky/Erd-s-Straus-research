# Arithmetic specialization — proved, local only

2026-10-04. The inverse theorem classifies one exact deficiency layer.
**It does not force a successful shift for any prime.** No residue-class
cover, universal Erdős–Straus theorem, or new finite existence range.

## Statement and verification of all quotient hypotheses

For EVERY prime p=1 mod 4 and integer p/4<x<p with prime
ell=4x-p (thus ell=3 mod 4), define D={d mod ell:d|x},
S=D union pD and J=<q mod ell:q prime, q|x, together with p mod ell>.
Assume -1 in J and no positive integral completion at this fixed x.
Let K=Stab_J(S), r=|K|, |J/K|=2m. Count, with multiplicities, all
prime occurrences of x and ONE p occurrence outside K; call the count N.

Then K has odd order and m is odd. If N=m-2 and m>=3, the following
conclusion holds (m=3 is impossible): for a generator gamma of J/K,
exactly one retained occurrence belongs to gamma^{+/-2}, and every
other retained occurrence belongs to gamma^{+/-1}. Equivalently, for
any lift g in J of gamma, these are g^{+/-2}K and g^{+/-1}K.
All deleted occurrences are in K. In this case |S|=rm=|J|/2.

Verification:
1. gcd(ell,px)=1, and p does not divide x. Hence S is exactly the
   binary product of all the joint prime occurrences. Its generators
   generate J, and their nonidentity images after deletion generate J/K.
2. The fixed-x criterion proved below makes failure equivalent to
   S intersect -S empty. Hence |S|<=|J|/2. An even-order K would
   contain -1 and give S=-S; therefore r is odd, and |J/K|=2m with m odd.
3. S is a union of K-cosets. Its quotient image T is exactly the
   subset-product set of the retained list, and has trivial stabilizer:
   any quotient period would lift to a member of Stab_J(S)=K.
4. The image of -1 is the unique involution gamma^m, since K is odd.
   If T met gamma^m T, lifting the intersection and using SK=S would
   make S meet -S. Thus the DIFFERENCE set of T avoids the involution;
   it is not merely absent among the products themselves.
5. The product of all original occurrences is px=4x^2 mod ell.
   Since J has odd index in the ambient unit group, this lies in J^2.
   Deleted occurrences belong to odd-order K, hence also to J^2.
   Thus the product of retained images is a square in J/K: their total
   additive exponent in C_(2m) is even. See `prerequisite_audit.md`
   for the direct exponent proof.

All hypotheses of `proof.md` now hold when N=m-2, proving the claim.
This uses the ACTUAL joint stabilizer, not that of D or DD^{-1}.

## Distinguished p occurrence and remaining compatibility

No case has been silently ruled out. Let beta be the exponent of pK
in generator gamma coordinates, and A the exponent of xK, the sum of
ALL x occurrences (deleted ones contribute zero). Since p=4x mod ell,
4 belongs to J. Write 4K=gamma^delta. Then necessarily

    beta = delta + A modulo 2m,       beta+A is even,
    delta is even.                                         (AC)

The last assertion follows either by subtraction of 2A, or from 4 being
an ambient square in J. There are three cases:

- p is the exceptional retained occurrence: beta=+/-2; the m-3 retained
  x occurrences are ordinary +/-1, so A is their signed sum.
- p is an ordinary retained occurrence: beta=+/-1; x has one +/-2
  occurrence and m-4 ordinary +/-1 occurrences; A is their signed sum.
- p was deleted because p lies in K: beta=0; x has the entire retained
  list, one +/-2 and m-3 ordinary +/-1 occurrences.

In the first and third cases A is even; in the second A is odd.
All three are compatible with the EVENNESS in (AC). These necessary
congruences must coexist with actual prime factors of x, the prime
relation ell=4x-p, and the actual stabilizer. Nothing here proves these
arithmetic patterns impossible, nor couples their occurrence at different
shifts. No universal contradiction or bound on g,k is inferred.

## Self-contained fixed-x certificate audit (no new identity claim)

For EVERY prime p=1 mod 4 and integer p/4<x<p set a=4x-p,
b=px. Then a>0 and gcd(a,b)=1, as proved in `prerequisite_audit.md`.
A completion satisfies ayz=b(y+z). Put d=ay-b, e=az-b.
The equations dz=by and ey=bz imply d,e>0, and expansion gives

    de=b^2=p^2*x^2,     d=e=-b modulo a.

Conversely positive d,e with these properties give positive integers
y=(b+d)/a, z=(b+e)/a and ayz=b(y+z).
Since p does not divide x, allocating its two prime occurrences in de
gives, up to swapping d,e, either (pc,pE) or (p^2*c,E), where
c,E are positive integers with cE=x^2.

- Allocation 1+1 gives c=-x modulo a (branch A). It also gives
  E=-x, since c is a unit and cE=x^2.
- Allocation 2+0 gives pc=-x; because p=4x modulo a and x is a
  unit, this is 4c=-1 (branch B). It gives E=-px modulo a.

Thus A or B is an iff for the fixed unordered x. Its respective formulas:

    A: y=p(x+c)/a,     z=p(x+E)/a;
    B: y=p(x+pc)/a,    z=(px+E)/a.

Integrality follows from the displayed congruences; positivity from
p,x,c,E,a>0. Each reconstructed pair has (ay-b)(az-b)=b^2.
Expanding gives ayz=b(y+z); using a=4x-p and b=px gives exactly

    4*x*y*z = p*(x*y+x*z+y*z).

For completeness, {c/x:c|x^2}=DD^{-1}: each prime exponent in c/x
ranges from -v_q(x) to v_q(x), exactly the differences of two divisor
exponents. This set R is inverse-closed. A is -1 in R; B is
-p^{-1} in R, equivalent by inversion to -p in R. Finally
SS^{-1}=R union pR union p^{-1}R, so A or B is exactly -1 in
SS^{-1}, or S intersect -S nonempty. No product-closure of R is used.

This audit certifies constructions WHEN a sufficient condition holds.
The new inverse theorem concerns failures, so it produces no new
positive triple. It has no denominator cutoff or ordering assumption;
it is a local structure theorem, not a fixed-x success theorem.