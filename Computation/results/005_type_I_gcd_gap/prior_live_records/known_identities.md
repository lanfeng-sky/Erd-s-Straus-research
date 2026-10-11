# Known Identities

## KI-001: fixed smallest denominator criterion (proved)

For every prime p congruent to 1 modulo 24, let x=(p+3)/4 and b=p*x.
A positive integral completion at x exists if and only if x has a prime
factor q congruent to 2 modulo 3. This is a fixed-x result, not universal
existence; no novelty or Lean verification is claimed.

Proof audit: write p=24k+1. Since p is prime, k>=1; x=6k+1 and b=1 mod 3.
The remainder is 3/b. A completion gives 3yz=b(y+z), hence
 d=3y-b>0 (because dz=by>0), e=3z-b>0,
 de=b^2, and d=e=2 mod 3.
If no prime factor of x is 2 mod 3, every prime factor of b is 1 mod 3:
3 divides neither x nor p, and p=1 mod 3. All divisors of b^2 would then
be 1 mod 3, contradicting d. This proves necessity.

Conversely choose a prime q|x with q=2 mod 3. Define

    e=b^2/q, y=(b+q)/3, z=(b+e)/3.

Here e is integral and e=2 mod 3, so y,z are positive integers.
Since q<=x<=b, q<=e and y<=z; y>b/3>x because p>3.
Expanding gives 9yz=(b+q)(b+e)=b(2b+q+e)=3b(y+z),
so 3yz=b(y+z). With b=px and 4x-p=3, this implies exactly

    4xyz=p(xy+xz+yz).

For any positive ordered solution, x>p/4 and x<=3p/4. Thus this x is
the smallest possible first denominator, not merely a convenient choice.

Factor-pair completeness: every completion can be ordered y<=z, giving
1<=d<=b and de=b^2. Conversely every such pair with d+b and e+b
multiples of 3 reconstructs a positive completion. In this domain y>x
automatically. Exact bounds: b/3<y<=2b/3 and z<=(b+b^2)/3;
no arbitrary denominator cutoff is needed.

Audit of [I-001](../ideas/001_initial_strategy.md), executed under
[D-001](../decisions/001_first_task.md). Frozen review snapshot:
[H-001](../handoffs/001_x0/README.md). Detailed experiment artifacts remain
in the main workspace under `experiments/results/001_x0/`.
Accepted by flagship in R-002; H-001 remains unchanged.

## KI-002: exact two-branch fixed-x criterion (proved)

For EVERY prime p=1 modulo 4 and integer p/4<x<p set a=4x-p.
A positive integral unordered completion exists iff

    A: some c|x^2 has c=-x modulo a, OR
    B: some c|x^2 has 4c=-1 modulo a.

With E=x^2/c, the respective formulas are

    A: y=p(x+c)/a, z=p(x+E)/a;
    B: y=p(x+pc)/a, z=(px+E)/a.

The [self-contained proof](../handoffs/002_structure/proof.md) proves
all p-adic cases, integrality, positivity, and 4xyz=p(xy+xz+yz).
Equivalently, D_x={d mod a:d|x}, R_x=D_x D_x^{-1}; the exact condition
is R_x intersecting {-1,-p}. The inverse step does NOT assert multiplicative
closure. For every such p, existence of any representation is equivalent
to a target hit for some (p+3)/4<=x<=floor(3p/4). This is a reformulation,
not a theorem forcing that hit. The fixed-x iff has no ordering filter;
x is automatically smallest for x<=p/2, but not in general above p/2.

Counterexample to subgroup sufficiency: p=1201,x=303,a=11 has
H_x={1,...,10}, R_x={1,2,3,4,6,7,8}, targets={10,9}; both branches fail.

## KI-003: prime-defect saturation (proved; elementary replacement)

For EVERY prime p=1 mod 4, prime ell=3 mod 4, x=(p+ell)/4<p, assume
-1 in H_x=<q mod ell:q prime, q|x>. Write h=|H_x|. For every odd r|h
let K_r be its unique order-r subgroup and N_r=sum(e_q:q not in K_r).
If EVERY N_r>=h/(2r), A holds and KI-002 reconstructs positive integers
with 4xyz=p(xy+xz+yz). Failure of A implies a deficient K_r, including
its actual stabilizer. Branch B is NOT discarded. No pointwise bridge.

New self-contained [replacement proof](../handoffs/003_joint_inverse/prerequisite_audit.md):
for ANY binary product S in a finite abelian group and K=Stab(S),
|S|>=|K|(1+number of occurrences outside K). In the aperiodic quotient
every nonidentity binary step grows; otherwise a period persists to the
final set. Combine with D disjoint from -D and odd actual K.
The historical [conditional H-002 note](../handoffs/002_structure/conditional_saturation.md)
is unchanged. General Kneser's primary/proof audit remains unperformed
and is no longer a dependency of specialized KI-003. H-002 accepted R-003.

## KI-004: switched factorization (proved)

For ALL positive integers p,g,k,d,e with de=4gk^2p+1 and
positive d=e=-1 modulo 4gk, put u=(d+1)/(4gk), v=(e+1)/(4gk).
Then x=guv,y=pgku,z=pgkv are positive integers and
4xyz=p(xy+xz+yz). For prime p=1 mod 4 and p/4<x<p, normalized
coprime u,v, uv|x and a|(u+v) are equivalent to A; g=x/(uv),
k=(u+v)/a yields the switched pair. Both g and k are required.
See [proof, section 7](../handoffs/002_structure/proof.md).
No theorem forces suitable parameters for every p.

All D-002 finite counts and counterchecks are in
[H-002 findings](../handoffs/002_structure/findings.md). H-002 accepted
in [R-003](../reviews/003_structure_audit.md); frozen files unchanged.

## KI-005: joint saturation, parity and inverse structure (proved)

For EVERY prime p=1 mod 4 and integer p/4<x<p with prime ell=4x-p,
let D={d mod ell:d|x}, S=D union pD and J=<q:q|x,p>. Then
A or B iff S meets -S. If -1 in J, |J|=h, and for EVERY odd r|h
its subgroup K_r has joint occurrence count N_r^+>=h/(2r), a completion
exists by KI-002 with positive integral denominators and the exact certificate.
N_r^+ includes all prime occurrences of x outside K_r and ONE p occurrence.

For a failure under -1 in J, its ACTUAL K=Stab_J(S) is odd;
write |J/K|=2m, m odd. The N nonidentity projected occurrences generate this quotient,
have even total, and their aperiodic subset-sum set T avoids T+m.
Thus N+1+indicator(N odd)<=|T|<=m. If |T|=N+1 and N>=1,
all occurrences are +/-g for a generator g.

**New T-003 inverse theorem:** for EVERY odd m>=3, a generating
nonzero list of length m-2 in C_(2m), with aperiodic subset-sum set T,
T disjoint from T+m, and even total, has EXACTLY ONE occurrence +/-2g
and all others +/-g for a generator g. m=3 hypotheses are impossible.
[Full proof](../handoffs/003_joint_inverse/proof.md) handles the order-three
cycle exception, with no prime-m or full-order premise.

Applied to failures with N=m-2, this gives one g^{+/-2}K occurrence and
all others g^{+/-1}K. The p occurrence may be exceptional, ordinary, or
deleted in K; all three p=4x compatibility cases are stated in the
[arithmetic specialization](../handoffs/003_joint_inverse/arithmetic_specialization.md).
No case is proved impossible. No theorem forces such N at any shift.
Universal prime existence remains unresolved. H-003 accepted by
[R-004](../reviews/004_inverse_and_construction_audit.md); frozen files unchanged.
No novelty or Lean claim. Finite unit tests cover m in {3,5,7,9} ONLY.
The inverse hierarchy is stopped under D-004 absent an arithmetic bridge.

## KI-006: switched-family Jacobi obstruction and A/B separator (proved)

For EVERY positive g,h, M=4gh-1 satisfies gcd(g,M)=1, Jacobi(g,M)=1
and Jacobi(-g,M)=-1, including even g and composite M. Thus for EVERY
positive n,g,u,v,k with u+v=k(4guv-n), set a=4guv-n>0:

    n=(4guk-1)a-4gu², gcd(n,4guk-1)=1,
    Jacobi(n,4guk-1)=-1.

NO positive square n occurs in this family, without any size bound or
coprimality hypothesis on u,v. This is not a nonexistence claim for the
Erdős–Straus equation. Switched denominators (guv,ngku,ngkv) are positive
integers and satisfy 4xyz=n(xy+xz+yz).

For EVERY prime p=1 mod 4, p/4<x<p and witness C|x², normalize
x=guv,C=gu²,gcd(u,v)=1; put a=4x-p. The exact branches become:

    A: k=(u+v)/a, p=(4guk-1)a-4gu²,
       Legendre(4guk-1,p)=-1; (x,y,z)=(guv,pgku,pgkv).
    B: k=(pu+v)/a, 4guk-1=ph, hv=u+k, h>0,
       Legendre(4guk-1,p)=0; (x,y,z)=(guv,pguk,gvk).

Both converse constructions, gcd normalizations, denominator positivity and
integrality, and exact identity are in the self-contained
[H-004 audit](../handoffs/004_construction_obstruction/proof_audit.md).
A/B generally have DIFFERENT k. No single fixed tuple exhausts all solutions.
Neither character condition forces the required divisibilities or existence.

Normalized U-007 n=a(4ck-1)-4c is exactly u=1, hence nested A only.
For n=1 mod 4, ck<=(n+3)/8; the complete h=ck method needs the
r=M-1 boundary c=h. Universal coverage is FALSE: at prime 193 no witness
exists, but A gives (50,1930,4825). The six retained finite inputs ONLY
have counts 0/2/2/2/0/0. Undefined screenshot variants remain unspecified.

Explicit erratum: I-008's ancillary n-x=c(3ak-4)-a is FALSE (retained
1009 witness gives 756 vs 745). Correct same-domain equality is
n-x=c(3ak-3)-a>=2a-3>0; positivity and T-004 are unaffected.
Historical files unchanged. H-004 submitted for review; no novelty/Lean
claim. Route stopped BLOCKED under D-004; overall conjecture unresolved.