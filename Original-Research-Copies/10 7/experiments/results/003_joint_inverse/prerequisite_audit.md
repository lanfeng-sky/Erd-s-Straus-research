# Prerequisite audit and elementary replacement for KI-003

2026-10-04, D-003. **Proved**, separately from the historical conditional
H-002 note. General Kneser has NOT been source- or proof-audited here.
No network, Lean, or external inverse theorem was needed.

## Binary growth, for every finite abelian group

Let G be a finite abelian group, w_1,...,w_L in G (identity occurrences
allowed), S=product_i {1,w_i}, K=Stab_G(S), and N count the occurrences
outside K. Then

    |S| >= |K|(N+1).                                      (BG)

S is a union of K-cosets; therefore its image T in G/K has trivial
stabilizer. Indeed any quotient period lifts to a translation preserving
S, hence belongs to K. Delete identity factors in G/K. In any ordering
of the N remaining factors, a step P -> P union wP that fails to grow
has wP=P. This nonidentity period persists through multiplication by
every later binary factor, contradicting trivial final stabilizer.
Thus |T|>=N+1, and |S|=|K||T| proves (BG). If L=N=0,
S={1}, K={1}, and the bound also holds.

This proves the specialized inequality used in KI-003, not general
Kneser for arbitrary pairs of finite sets.

## KI-003 replacement, exact hypotheses

For every prime p=1 mod 4, prime ell=3 mod 4, and integer
x=(p+ell)/4<p, let D={d mod ell:d|x}, H=<q mod ell:q prime, q|x>,
h=|H|, and assume -1 in H. For every odd positive r|h let K_r be
the unique subgroup of H of order r, and

    N_r=sum_{q|x, q mod ell not in K_r} v_q(x).

If N_r>=h/(2r) for EVERY such r, branch A holds at this fixed x.
Conversely if A fails, the ACTUAL K=Stab_H(D) has odd order r and

    N_r <= h/(2r)-1.

Proof: H is cyclic with h=2M, M odd, since ell-1 has exactly one
factor 2. Failure of A means -1 not in DD^{-1}, so D and -D are
disjoint, giving |D|<=h/2. Even |K| would place -1 in K and give
D=-D, impossible. Thus |K|=r odd. D is the binary product with v_q(x)
copies of each q, so (BG) gives r(1+N_r)<=|D|<=h/2. This proves
both assertions and removes the external dependency for KI-003 only.
Branch B can still succeed when A fails. This is fixed-x saturation,
not a universal shift-selection theorem or a residue-class cover.

## Joint encoding and saturation, exact hypotheses

For every prime p=1 mod 4 and integer p/4<x<p set a=4x-p.
Then a is odd, gcd(a,px)=1: gcd(a,x)=gcd(p,x)=1 and
p does not divide 4x, since p is odd and 0<x<p.
Let D be the divisor-residue set of x, R=DD^{-1},
S=D union pD, and J=<q:q|x,p> in the units modulo a.

    SS^{-1}=R union pR union p^{-1}R.

R is inverse-closed. Thus -1 in SS^{-1} iff -1 or -p belongs to R,
which is exactly A or B. Equivalently S meets -S. Since p does not
divide x, S is the divisor-residue set of px and is the binary product
of the prime occurrences of x with one extra occurrence p.

When a=ell is prime (automatically ell=3 mod 4), suppose -1 in J.
Write |J|=h. For every odd r|h define K_r inside J and

    N_r^+ = sum_{q|x, q mod ell not in K_r} v_q(x)
              + indicator(p mod ell not in K_r).

The same proof shows that if all N_r^+>=h/(2r), A or B holds.
A joint failure has actual odd K=Stab_J(S), |K|=r, and
r(1+N_r^+)<=|S|<=h/2. H cannot replace J unless p in H is checked.

## Critical growth and even total

In a failed prime-defect pair, J/K is cyclic of even order 2m,
with m odd. Delete occurrences in K; the remaining N nonzero
projected elements generate J/K. Their subset-sum set T is aperiodic.
If |T|=N+1 and N>=1, all terms are +/-g for one generator g:
put any incompatible pair first, giving four distinct sums and then
at least N+2 final elements. For N=1 generation supplies g directly.
This reasoning does not assume each original prime residue has full order.

The product of all original joint occurrences is px=4x^2 mod ell,
a square. J has odd index in the full unit group, because both have
exactly one factor 2 in their orders. To see the parity claim directly,
write the ambient group as <b>, J=<b^d> with d odd. A member b^(dj)
is an ambient square iff j is even; hence ambient squares in J are J^2.
K has odd order and lies in J^2, and its deleted occurrences each lie
there. Passing to J/K therefore makes the total exponent even.
For odd N, critical growth would give an odd sum of odd generators,
a contradiction. Thus every such failure satisfies

    N+1+indicator(N odd) <= |T| <= m.

These are the audited I-005 prerequisites. The inequality does not
force N to be large for any shift. The new inverse theorem treats
only N=m-2; sparse failures remain untouched.