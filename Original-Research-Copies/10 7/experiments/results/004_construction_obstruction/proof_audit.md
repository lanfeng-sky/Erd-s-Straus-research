# T-004: obstruction and branch separator — independent audit

2026-10-04, main execution under D-004. **Target theorem: proved** by
reciprocity and exact algebra, not by the finite runs. One ancillary equality
in I-008 is **false**, corrected explicitly in section 5 below. No narrower
hypotheses are introduced. Overall Erdős–Straus: **unresolved**; pointwise
existence route: **blocked**. No novelty, Lean, network or fresh-agent claim.

## 1. Jacobi lemma, including even g and composite moduli

For EVERY positive integer g,h, put M=4gh-1. Then M>=3 is odd,
M=3 mod 4 and gcd(g,M)=1. We use the standard Jacobi symbol with odd
positive denominator, including repeated prime factors, and its elementary
reciprocity and supplementary laws.

For any odd prime r dividing g, M=-1 mod r. Jacobi reciprocity gives

    (r/M)=(-1)^((r-1)/2) (M/r)
         =(-1)^((r-1)/2) (-1/r)=1.

If g is even, M=7 mod 8 and (2/M)=1. Factoring g and multiplying these
symbols, with their actual multiplicities, yields (g/M)=1. Also
(-1/M)=-1, hence **(-g/M)=-1**. g=1 is covered by the empty product.
Neither primality nor squarefreeness of M is assumed.

For EVERY positive n,g,u,v,k satisfying

    u+v=k(4guv-n),

set a=4guv-n=(u+v)/k>0 and M=4guk-1. Substituting v=ka-u gives

    n=M a-4gu².

Since gcd(gu,M)=1 and M is odd, gcd(n,M)=1. Apply the lemma with
h=uk: (n/M)=(-4gu²/M)=(-g/M)=-1. A positive square coprime to an
odd modulus has Jacobi symbol +1. Therefore **NO positive square n**
has such parameters, with NO size restriction and without gcd(u,v)=1.
This is an obstruction to this family, NOT to three-unit-fraction existence.

These parameters do produce positive integer denominators
x=guv, y=ngku, z=ngkv. Since a yz=nx(y+z),

    4xyz=(n+a)yz=n(xy+xz+yz).

Thus integrality, positivity and the exact certificate are all independent
of the character argument.

## 2. Fixed-x setup, normalization and completeness

For EVERY prime p=1 mod 4 and integer p/4<x<p, put a=4x-p and b=px.
Then a>=3, a=3 mod 4 and gcd(a,px)=1. The fixed-x completion is
unordered: x need NOT be the smallest denominator.

For completeness, the certificate is equivalent to ayz=b(y+z).
For any positive completion, d=ay-b and e=az-b satisfy dz=by>0,
ey=bz>0, de=b² and d=e=-b mod a. Conversely such a positive factor
pair reconstructs positive integer y=(b+d)/a,z=(b+e)/a and the identity.
Since p does not divide x, the p-adic valuations of d,e sum to 2.
After an allowed interchange, they are (1,1) or (2,0):

* (1,1): d=pC,e=pE, CE=x², C=-x mod a — branch A.
* (2,0): d=p²C,e=E, CE=x², pC=-x mod a. Because p=4x mod a,
  this is 4C=-1 mod a — branch B.

The complementary factor has the required residue in either case since
all of C,E,p,x are units modulo a. This establishes the two-branch iff,
not a theorem forcing a witness at any x.

Normalize ANY positive witness C|x² by C/x=u/v in lowest terms.
If d0=gcd(C,x), then C=d0*u and x=d0*v. From C|x² and gcd(u,v)=1,
u|d0. Thus d0=gu and

    x=guv, C=gu², E=x²/C=gv², gcd(u,v)=1.

All parameters are positive integers, g,u,v<=x<p, and gcd(a,guv)=1.

## 3. A and B: exact equations, converses and certificates

### A

C+x=gu(u+v), so A is equivalent to a|(u+v). Set k=(u+v)/a>0.
Any common divisor of u and k divides v, so gcd(u,k)=1. Then

    M=4guk-1, p=M a-4gu²,
    (x,y,z)=(guv,pgku,pgkv).

The two last expressions equal p(x+C)/a and p(x+E)/a respectively;
they are positive integers. By section 1, (p/M)=-1 and gcd(p,M)=1.
Since p=1 mod 4, reciprocity gives the exact **Legendre(M,p)=-1**,
also for composite M.

Converse, with ALL conditions explicit: given positive g,u,k,a, let
v=ka-u>0. Assume gcd(u,v)=1, p=(4guk-1)a-4gu² is prime 1 mod 4,
and p/4<guv<p. Then 4guv-p=a and u+v=ka; C=gu² divides x²
and satisfies A. These are sufficient equations, not just a nonresidue test.

### B

Since p=4x mod a, B is equivalent to pC+x=gu(pu+v)=0 mod a.
Set k=(pu+v)/a>0. Again gcd(u,k)=1, since a common divisor divides v.
The positive integral reconstruction is

    (x,y,z)=(guv,pguk,gvk).

Indeed these equal p(x+pC)/a and (px+E)/a. Substitution gives

    v(4guk-1)=p(u+k).

Because 0<v<p and p is prime, p divides M=4guk-1. Thus some
positive integer h satisfies M=ph and hv=u+k, and Legendre(M,p)=0.

Converse: given positive g,u,k,h with M=4guk-1=ph, h|(u+k),
let v=(u+k)/h. Assume gcd(u,v)=1, p prime 1 mod 4 and p/4<guv<p.
Multiplying hv=u+k by p and using M=ph gives

    k(4guv-p)=pu+v>0.

Hence a=4guv-p>0 and k=(pu+v)/a, which yields B and its reconstruction.
The gcd hypotheses are explicitly imposed for the NORMALIZED converse;
no claim says that arbitrary unnormalized tuples are already normalized.

### Division-free check, both branches

For A, a=k^(-1)(u+v), giving a yz=px(y+z).
For B, a=k^(-1)(pu+v), giving the SAME a yz=px(y+z).
All denominators above are products of positive integers. Since a=4x-p,

    4xyz=p(xy+xz+yz).

No floating-point equality or ordering assumption is used. A and B generally
have DIFFERENT k: k_A=(u+v)/a and k_B=(pu+v)/a. Even when the same
C witnesses both, those values differ. Different completions need not share
(g,u,k); the separator does not exhaust all solutions using ONE fixed tuple.

## 4. Exact normalized U-007 scope and complete bounds

For positive P,n,k with kP>1, the core identity
P/n=1/m+1/(kn)+1/(mkn) holds iff m=(kn+1)/(kP-1) is a positive
integer. Because gcd(P,kP-1)=1 and
P(kn+1)-n(kP-1)=P+n, integrality is equivalent to (kP-1)|(P+n).
Reducing m(kP-1)=kn+1 modulo k gives m=ak-1 for a positive integer a.
Then n=a(Pk-1)-P. Setting P=4c and dividing by c gives precisely

    n=a(4ck-1)-4c, m=ak-1,
    (x,y,z)=(c(ak-1),ckn,c(ak-1)kn).

For EVERY positive n=1 mod 4 and positive a,c,k satisfying this equation,
a=3 mod 4 and a>=3, so m>=2. This is exactly section 1 with
g=c,u=1,v=ak-1. Conversely u=1 gives this equation, up to swapping
u and v. It describes the nested-denominator restriction of A for prime n
in the fixed-x domain: in normalized A, y|z iff u|v iff u=1, and the
opposite divisibility iff v=1. It is not all of A and does not describe B.
The positive integral triple satisfies the identity by section 1.

Since a>=3,

    n>=12ck-4c-3>=8ck-3,
    ck<=(n+3)/8,
    k<=(n+4c+3)/(12c).

These are PROVED completeness bounds for this family, not conjectural pruning.
For h=ck, M=4h-1 and r=n mod M, the possible c obeys
4c=-r mod M and 4<=4c<=M+1. Thus exactly the following candidate rule:

* r=M-1: c=(M+1)/4=h. This is the indispensable boundary case.
* Otherwise c=(M-r)/4 if this is a positive integer; else no candidate.

Test c|h and set k=h/c,a=(n+4c)/M. In the bounded h range an accepted
a is positive, integral, 3 mod 4 and hence >=3. Every witness appears.
There is no hidden arbitrary cutoff and no primality reduction in this method.

## 5. Found false equality; exact counterexample and correction

I-008 section 2 displays n-x=c(3ak-4)-a. This equality is **false**:
it is short by c. The retained witness n=1009,(a,c,k)=(3,11,8) gives
x=253 and n-x=756, while the displayed right side is 745.
The correct exact expansion, on the SAME hypotheses, is

    n-x=c(3ak-3)-a >= 2a-3 > 0.

The lower bound follows from c,k>=1 and a>=3. Thus x<n, x>n/4
because 4x-n=a>0, and n<=y<=z because c,k>=1,m>=2.
No target theorem is invalidated; this correction is NOT a restriction or a
repair by new assumptions. Historical I-008 and R-004 are left untouched.
Per D-004, record this false ancillary claim here and stop the route.

## 6. Compact prime no-witness certificate, already retained domain

At n=193 the complete bound is 1<=h<=24. Evaluating the exact rule in
section 4, the ONLY positive integral residue candidates are

    (h,c)=(5,4),(8,6),(17,2),(18,5),(19,8),
          (20,11),(21,14),(22,17),(23,20),(24,23).

None has c|h; the other fourteen h yield no integral candidate. Hence NO
positive (a,c,k) exists for this n. Yet the non-nested A parameters
(g,u,v,k,a)=(5,2,5,1,7) give (x,y,z)=(50,1930,4825), all positive,
with 4xyz=193(xy+xz+yz); neither last denominator divides the other.
This disproves universal normalized U-007 coverage even for A-solvable primes,
NOT Erdős–Straus. The theorem excluding every positive square is universal;
this particular prime no-witness certificate is finite.

## 7. Evidence, limitations, restart gate

Only the authorized reviews/004_audit_probe.py was rerun on its UNCHANGED
domain: existing H-003 checks and n in {193,1009,1129,1201,2521,66529}.
Both original enumeration schedules agreed; witness counts 0/2/2/2/0/0.
The saved source/stdout/environment are supplied; the standalone auditor
checks retained certificates and the compact 193 certificate, not new ranges.
Other no-hit records retain the authorized generator's provenance and limits.

No square scan, new prime, offset, group order or parameter range; no external
source or Lean proof. Reciprocity is the named standard input. The full
switched-family square obstruction is a universal conditional-family theorem;
the A/B separator is a fixed-x equivalence. Neither forces existence for a prime.
A nonresidue M does not force M|(p+4gu²). p|M does not force (M/p)|(u+k).

Minimal next action: flagship review this frozen audit, including the explicitly
false auxiliary equality, and run check_retained.py. No further search is
requested. Restart only with a precise new pointwise arithmetic implication.
