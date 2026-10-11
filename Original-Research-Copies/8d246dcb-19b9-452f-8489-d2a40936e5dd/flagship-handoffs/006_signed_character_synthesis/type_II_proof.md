# H-006 — Pending Type-II audits: T-006 and T-007

Date: 2026-10-05. Main rederivation of I-011 and I-012 under D-008.
Status of the universal statements and equality classifications: **proved**.
No new constants, classes, searches, or computational ranges are introduced.

## 1. Domain and intrinsic normalization

Here the numerator is 4, p is prime, and Type II means exactly two denominators are p-divisible. Let X be smallest and G=gcd(X,Y,Z). Positivity and ordering imply

    p/4<X<=3p/4<p.

Thus X is p-free and the others may be denoted Y,Z. Apply the normalization proved in the sibling signed_character_proof.md, with c=1,n=p. It gives positive pairwise-coprime u,v,k and

    X=Guv, Y=pGku, Z=pGkv,
    a=4X-p>0, ka=u+v,
    4Guv=p+(u+v)/k.                                 (1.1)

In particular g=G is the FULL denominator gcd, not a pairwise gcd. No assumption p not dividing k is needed for this derivation. Put s=X/G=uv and S=u+v. The sibling's signed clean-II character at p=1 mod 4 gives

    Legendre(s,p)=-1.                                (1.2)

For completeness, the character transfer is exactly M=4Guk-1, Mv=pk+u, p=Ma-4Gu^2. The Jacobi lemma gives (p/M)=-1; reciprocity at p=1 mod 4 gives (M/p)=-1; Mv^2=uv mod p transfers this sign to s. Only v, never k, is cancelled modulo p.

These facts follow from arbitrary actual solutions, not from first saved certificates.

## 2. T-007: gcd ceilings and equality

Let q=q(p) be the least positive quadratic nonresidue. For p=1 mod 4, s>=q by (1.2). Since

    (u-1)(v-1)>=0, S<=s+1,

with equality iff u=1 or v=1, (1.1) yields

    4G = p/s + S/(ks)
       <= 1+(p+1)/s
       <= 1+(p+1)/q.

Hence

    4qG<=p+q+1.                                     (G4)

Every equality step is reversible precisely when s=q, k=1 and {u,v}={1,q}. Thus equality in (G4) occurs exactly, up to permutation, when

    p=(4G-1)q-1, (X,Y,Z)=(Gq,Gp,Gpq),

on the stated prime domain with q=q(p).

### Parity when p=1 mod 8

Here 2 is a residue. The least nonresidue q is an odd prime: a composite least nonresidue would have a smaller nonresidue prime factor; 1 and 2 are residues. Also q<p, since there is a nonresidue among 1,...,p-1.

If s is odd, u,v are odd. The defect a is odd, so ka=S forces k even and k>=2. Then

    4G<=p/s+(s+1)/(2s)
       =1/2+(p+1/2)/s
       <=1/2+(p+1/2)/q,

which gives

    8qG<=2p+q+1.                                    (Go)

Equality iff s=q, k=2 and {u,v}={1,q}. Equivalently

    2p=(8G-1)q-1,
    (X,Y,Z)=(Gq,2Gp,2Gpq).

If s is even, s/2 is also a nonresidue because 2 is a residue, so s>=2q. The (G4) chain with 2q in place of q gives

    8qG<=p+2q+1.                                    (Ge)

Equality iff s=2q, k=1 and {u,v}={1,2q}. Equivalently

    p=(8G-2)q-1,
    (X,Y,Z)=(2Gq,Gp,2Gpq).

Since q<p, the (Ge) right side is strictly smaller than the (Go) right side. Thus for EVERY Type-II solution at p=1 mod 8, without a parity assumption,

    G<=floor((2p+q+1)/(8q)),

and equality in the underlying unfloored universal inequality can only be the odd family above. Equality after flooring is not classified by that assertion.

### Equality converses, full gcd, and ordering

Each displayed family includes the hypotheses that p is prime in its stated domain and q=q(p). These are not automatic parameter consequences.

* (G4): the reciprocal numerator over Gpq is p+q+1=4Gq. Also p-Gq=(3G-1)q-1>0 and q<p. The full gcd is G because gcd(q,p)=1.
* (Go): over 2Gpq the numerator is 2p+q+1=8Gq. Also p-Gq=((6G-1)q-1)/2>0. Since q is odd and gcd(q,p)=1, gcd(q,2p)=1 and the full gcd is G.
* (Ge): over 2Gpq the numerator is p+2q+1=8Gq. Also p-2Gq=(6G-2)q-1>0. Since gcd(2q,p)=1, the full gcd is G.

In each case X is smallest and p-free and both other denominators are p-divisible. This proves both directions of all equality classifications, positivity, and the exact three-unit-fraction identity. No infinite-prime assertion is made.

## 3. T-006: a separate direct denominator envelope

Write the two p-divisible denominators pb<=pc, with integers b,c>=1. Clearing the original equation gives

    4Xbc=pbc+X(b+c).

Since gcd(X,p)=1, X|bc. Set the positive integer d=bc/X. Dividing by X gives

    4bc=pd+b+c,
    (4b-1)c=pd+b.                                   (3.1)

Multiplying by b and using bc=dX gives

    (4b-1)dX=pbd+b^2,
    d|b^2,
    X=(pb+b^2/d)/(4b-1).                            (3.2)

This proof does not assume p-coprimality of b,c,d or invoke an unproved valuation shortcut.

### Extremal lemma: exact global proof

For m>=1, if b>=m and p>8m^2-7m+1, then

    (4m-1)X<=mp+m^2,                                (3.3)

with equality iff b=m,d=1.

There are three exhaustive cases:

1. b=m: (3.2) gives (4m-1)X=mp+m^2/d<=mp+m^2; equality iff d=1.
2. m<b<2m: d>=1 gives X<=(pb+b^2)/(4b-1). The exact cross-product difference is

       (mp+m^2)(4b-1)-(4m-1)(pb+b^2)
         =(b-m)[p-(4m-1)b+m].

   This expansion can be checked term-by-term: the p term is p(b-m), and the remainder is -(b-m)((4m-1)b-m). Since b<=2m-1, (4m-1)b-m<=8m^2-7m+1<p, giving strictness.
3. b>=2m: c>=b implies p/X=4-1/b-1/c>=4-2/b>=4-1/m. Thus X<=mp/(4m-1)<(mp+m^2)/(4m-1), again strict.

No global monotonicity in b is assumed. This closes I-011's global step without using I-010's discarded formulas.

### Apply only the already assigned m=2,3 cases

A prime p=1 mod 24 is at least 73 (the smaller positive candidates 1,25,49 are not prime). Thus the thresholds p>19 for m=2 and p>52 for m=3 both hold.

For b=1, d|b^2 forces d=1; (3.1) would give 3c=p+1, impossible at p=1 mod 3. Hence b>=2 and

    7X<=2p+4                                        (T-006a)

for every Type-II solution at p=1 mod 24.

On the broader domain p=1 mod 24 and p mod 7 in {1,2,4}, b=2 is also impossible. Here d is 1,2,4; 7c=pd+2 would force p mod 7 equal to 5,6,3 respectively. Hence b>=3 and

    11X<=3p+9.                                      (T-006b)

Every residue in R={1,121,169,289,361,529} modulo 840 is 1 mod 24 and has residue 1,2,4 modulo 7 (respectively 1,2,1,2,4,4). Thus T-006b holds on ALL six stated residual prime classes. No claim about complementary coverage is used.

### Equality, both directions

For m=2, equality means b=2,d=1; put c=(p+2)/7 and X=2c. Combining p=7c-2 with p=1 mod 24 gives c=21 mod 24, so

    c=24t+21, p=168t+145 prime, t>=0,
    (X,Y,Z)=(48t+42,2p,(24t+21)p).

Conversely these are positive integers and the reciprocal numerator over 2pc is p+c+2=8c, giving 4/p. Since c>=21, X=2c<p and the triple has Type II. Its full gcd is 1: c is odd, gcd(c,p)=gcd(c,2)=1, and the residual factor 2 is absent from pc.

For m=3, equality means b=3,d=1. Hence

    c=(p+3)/11, p=8 mod 11,
    (X,Y,Z)=(3c,3p,pc).

Conversely for p in the specified domain with p=8 mod 11, c is positive integral, p=11c-3, and

    1/(3c)+1/(3p)+1/(pc)=(p+c+3)/(3pc)=4/p.

We have 3c<p for p>=73, so X is smallest and p-free. The full gcd is 1: p=1 mod 3 and 11c=p+3 imply 3 not dividing c; also p divides neither 3 nor c. Thus both equality implications and the claimed primitive status hold.

Paper attainment checks, including exact primality/nonresidue checks for the cited examples, are in audit_and_scope.md. The inequalities and classifications above do not rely on computation or prime-progression theorems.

## 4. Two-type corollary and limits

At every prime p=1 mod 4, the type split is exhaustive. H-005 gives (G/p)=-1 in Type I; (1.2) gives ((X/G)/p)=-1 in Type II. Therefore at least one of G,X/G is a nonresidue in EVERY solution. If G is a residue, the solution must be Type II and X is a nonresidue. If X is a residue, both G and X/G must be nonresidues. Both invariants being nonresidues does not determine the type.

T-006 and T-007 restrict every actual Type-II solution but do not force one to exist. They do not import the Type-I gcd condition into Type II. The older X<=floor((p+1)/4) Type-II draft remains **false**, not an input. I-010 is superseded by I-011; its failed global-monotonicity route remains discarded. Standard normalization, odd-square obstruction, and nested equality identities are not originality claims. External priority and publication significance remain **unresolved** and **plausible**, respectively.