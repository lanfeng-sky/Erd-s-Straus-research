# H-006 — Signed characters and the reduced-pair obstruction

Date: 2026-10-05. Main-model audit of I-013 Sections 3–6 under D-008.
Status: **proved**. This is a self-contained ordinary mathematical proof, not a Lean theorem, executed regression, or fresh-agent review. External priority: **unresolved**.

## 1. Statement and scope

Let c>=1, n>=3 odd, gcd(c,n)=1, and let positive integers satisfy

    4c/n = 1/X + 1/Y + 1/Z,
    G = gcd(X,Y,Z).

There is no ordering assumption. Define the two CLEAN types explicitly:

* Clean I: n|Y and gcd(n,XZ)=1.
* Clean II: n|Y,Z and gcd(n,X)=1.

With Jacobi symbols, the conclusions are

    Clean I:  (-cG/n) = -1;
    Clean II: (-(X/G)/n) = -1.

In I put (U,V)=(X,Z); in II put (U,V)=(Y,Z). Let

    H=gcd(U,V), r=U/H, s=V/H.

Then gcd(r,s)=1, gcd(rs,n)=1, and in BOTH types

    (-rs/n)=-1,     (rs/n)=-(-1/n).                 (P)

Here (a/b) denotes the Jacobi symbol, with (a/1)=1. All character numerators asserted to have sign +/-1 are units in their respective moduli.

If n=1 mod 4, (P) gives opposite Jacobi signs for r,s, and U/V cannot be a rational square. If n=3 mod 4 their signs agree; the rational-square exclusion is not asserted there.

These are necessary restrictions on actual solutions, not sufficient conditions or a universal construction. At composite n, the clean hypotheses are essential and do not exhaust all solutions.

## 2. Derive the normalization from an arbitrary actual solution

Put a=4cX-n. Subtracting 1/X from the equation gives

    aYZ=nX(Y+Z),

so a>0. In both clean types gcd(n,X)=1. Since n is odd and gcd(c,n)=1,

    gcd(a,n)=gcd(4cX,n)=1,
    gcd(a,X)=gcd(n,X)=1,
    gcd(a,nX)=1.                                      (2.1)

This separately justifies BOTH coprimalities; no premise gcd(c,X)=1 is needed.

Define D=aY-nX and E=aZ-nX. Then

    DZ=nXY>0, EY=nXZ>0, DE=n^2 X^2.                  (2.2)

For clean I, E=aZ mod n is a unit modulo n. For every prime power ell^e exactly dividing n, its valuation in E is zero; (2.2) forces its valuation in D to be 2e. Thus n^2|D, and

    D=n^2 C, E=F, CF=X^2.

This argument uses gcd(n,Z)=1, not merely n not dividing Z.

For clean II, n divides both D and E. Dividing each by n gives

    D=nC, E=nF, CF=X^2.

In each type C,F are positive and coprime to n because their product X^2 is. This covers repeated prime factors of n; no prime-denominator assumption is being made.

Reduce C/X=u/v to lowest terms. If d0=gcd(C,X), then C=d0u, X=d0v, gcd(u,v)=1. Since C|X^2, u|d0v^2 and therefore u|d0. Write d0=gu. We obtain

    X=guv, C=gu^2, F=gv^2,
    gcd(u,v)=1, gcd(guv,n)=1.                        (2.3)

Reconstructing Y and using gcd(a,n)=1 gives a|nC+X in I and a|C+X in II. Since gu|X, (2.1) permits cancelling gu. Consequently

    I:  k=(nu+v)/a, (X,Y,Z)=(guv, nguk, gvk);
    II: k=(u+v)/a,  (X,Y,Z)=(guv, ngku, ngkv).        (2.4)

Each k is a positive integer. The Z formula follows using F=gv^2 and the same defining equation for k; it is not an additional integrality assumption.

### Pairwise coprimality and the FULL denominator gcd

In either type a divisor common to u,k divides v, hence is 1. In I a divisor common to v,k divides nu, and gcd(v,nu)=1; in II it divides u. Thus u,v,k are pairwise coprime.

In I, ak=nu+v modulo n and (2.1) show gcd(k,n)=1. Moreover

    gcd(uv,vk)=v, gcd(v,nuk)=1,

so gcd(guv,nguk,gvk)=g.

In II,

    gcd(nku,nkv)=nk, gcd(uv,nk)=1,

so gcd(guv,ngku,ngkv)=g. This does NOT require gcd(k,n)=1.

Hence g=G in BOTH types. The pairwise gcd H is a different invariant:

    I:  H=gcd(X,Z)=Gv,    (r,s)=(u,k);
    II: H=gcd(Y,Z)=nGk,   (r,s)=(u,v).                (2.5)

All r,s here are units modulo n. In particular, dividing Y,Z only by n in II is generally insufficient to get a unit reduced pair.

## 3. Jacobi prerequisite, including even numerators

For positive b,t set L=4bt-1. Then L>=3 is odd, L=3 mod 4, gcd(b,L)=1, and

    (b/L)=1, (-b/L)=-1.                              (3.1)

Indeed, for every odd prime ell|b, L=-1 mod ell. Quadratic reciprocity for the prime ell and odd L gives

    (ell/L)=(-1)^((ell-1)/2)(L/ell)
           =(-1)^((ell-1)/2)(-1/ell)=1.

If 2|b, L=7 mod 8 and (2/L)=1. Multiply over the prime factors of b with their actual exponents. Finally (-1/L)=-1. This proves (3.1) for even b and nonsquarefree composite L as well as the odd case.

## 4. Clean I: retain the numerator twist and allow shared n,h factors

From (2.4), ak=nu+v and a=4cGuv-n. Rearranging gives

    vM=n(u+k), M=4cGuk-1.

Since gcd(v,n)=1, n|M. Define positive h by

    M=nh, hv=u+k.                                   (4.1)

Both n,h are odd, M=3 mod 4, and gcd(cGu,M)=1. Apply (3.1) with b=cG, t=uk:

    (cG/(nh))=1.                                    (4.2)

Modulo h, (4.1) gives k=-u and 4cGuk=1. Hence

    4cGu^2=-1 mod h, (cG/h)=(-1/h).                  (4.3)

The cancellation of 4u^2 in this character is valid since gcd(2u,h)=1. The convention for modulus 1 covers h=1.

Jacobi multiplicativity in its denominator does not require gcd(n,h)=1. Thus (4.2) and (4.3) give

    (cG/n)=(-1/h).

Since nh=3 mod 4, (-1/n)(-1/h)=-1, proving

    (-cG/n)=-1.

For the pair in (2.5), 4cGuk=1 mod n. Its character says

    (uk/n)=(cG/n),

because 4 is a unit square and the character of a unit equals that of its inverse. Multiplying by (-1/n) proves (P).

No gcd(n,h)=1 assertion or cancellation of a possibly nonunit factor occurs.

## 5. Clean II: retain reciprocity sign and permit nonunit k

Set again M=4cGuk-1. The equations ka=u+v and a=4cGuv-n give BOTH

    Mv=nk+u,
    n=Ma-4cGu^2.                                    (5.1)

For the second identity, Ma=4cGu(ka)-a=4cGu(u+v)-a=n+4cGu^2.

M is odd and gcd(M,cGu)=1, so gcd(M,n)=1. By (3.1),

    (n/M)=(-4cGu^2/M)=(-cG/M)=-1.

M=3 mod 4; Jacobi reciprocity therefore yields

    (M/n)=(-1/n)(n/M)=-(-1/n).                       (5.2)

Multiplying the first equation of (5.1) by v gives Mv^2=uv mod n. Since gcd(v,n)=1,

    (uv/n)=(M/n)=-(-1/n).

As X/G=uv, this proves (-(X/G)/n)=-1. Equation (2.5) also proves (P) for the same-status pair.

We never cancelled k modulo n. The proof allows gcd(k,n)>1 in clean II, as it must at some composite n.

## 6. Intrinsic corollaries and prime specialization

If n=1 mod 4, (P) is (r/n)(s/n)=-1. These nonzero signs are opposite. If U/V=r/s is a rational square, unique factorization and gcd(r,s)=1 force both r,s to be positive integer squares. Then (rs/n)=1, a contradiction.

At an odd prime p=1 mod 4 the ratio r/s modulo p is a quadratic nonresidue, since its character is (r/p)(s/p). At composite n only the Jacobi obstruction is proved: negative sign does not mean nonresidue at EVERY prime factor, and positive sign is not a converse to quadratic residuosity.

If n is an odd square, every Jacobi symbol with unit numerator is +1. Thus neither clean type exists. This recovers a known-type odd-square obstruction and does not rule out unrestricted representations of squares.

For n=p an odd prime with p not dividing c, clearing denominators modulo p forces p|XYZ. All three denominators cannot be p-divisible: writing them pA,pB,pC would give 4c=1/A+1/B+1/C<=3, impossible. Primality makes the remaining p-free denominators units. Thus the two clean types exhaust ALL solutions up to permutation.

For c=1, p=1 mod 4, this recovers

    Type I:  (G/p)=-1;
    Type II: ((X/G)/p)=-1.

The first is the accepted H-005 character result; the second is the I-012 result separately developed with bounds in type_II_proof.md. For p=3 mod 4 the corresponding unsigned signs are +1. The signed theorem, not an unsigned extrapolation, is the general statement.

## 7. Audit verdict and limitations

The independent main rederivation finds no failed implication in I-013 Sections 3–6. It explicitly supplies both gcd calculations behind (2.1), the composite valuation argument, the separate FULL and pairwise gcds, the numerator c and reciprocity sign, and both prohibited-cancellation checks.

Status of T-008 and its precisely scoped square-ratio obstruction: **proved**. Boundary calculations are in audit_and_scope.md; no new executed numerical evidence is asserted. Normalization, reciprocity, and the known odd-square special case are not novelty claims. The general 4c/n intrinsic signed statement is an increment relative to the inspected local register, not certified external originality. Erdős–Straus remains **unresolved**.
