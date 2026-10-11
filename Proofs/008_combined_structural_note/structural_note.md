# Square-ratio obstructions in three-unit-fraction representations

D-010 structural-note draft, 2026-10-06. Mathematical statements: **proved**. External priority and standalone publishability: **unresolved**.

## Abstract and conventions

For odd n, we classify exactly when some representation of 4/n by three positive integral unit fractions can have a rational-square denominator ratio: precisely when n has a prime divisor congruent to 3 modulo 4. Necessity holds for every numerator 4c, without divisibility-type assumptions. Separately, clean divisibility types admit signed Jacobi identities for the full denominator gcd and for a reduced same-status pair. The two results have complementary scopes: unrestricted all-pairs exclusion on a prime-support domain, versus stronger character information on a restricted clean domain. Neither is an obstruction to unrestricted Erdős–Straus solvability.

All variables are positive integers unless stated otherwise; n>=3 is odd and c>=1. A representation means

    4c/n = 1/X + 1/Y + 1/Z.                              (1)

No ordering or distinctness is required. A square pair is a pair U,V with U/V the square of a positive rational. Write J(a,m) for the Jacobi symbol at odd m, with J(a,1)=1. We use unique factorization, quadratic reciprocity, and the standard supplementary laws for Jacobi symbols; all specialized lemmas are proved below.

## 1. Unrestricted prime-support theorem

**Theorem 1 (T-009a/b).** In any representation (1), if Y/Z is a rational square, set

    A=4cX-n, delta=gcd(A,nX), alpha=A/delta.

Then A,delta,alpha are positive odd integers, every prime divisor of delta divides n, and every prime divisor of alpha is 1 modulo 4 (alpha=1 allowed). Moreover,

    delta=-n (mod 4),      n*delta=3 (mod 4).             (2)

Thus n has a prime divisor 3 modulo 4. In particular, if all prime divisors of n are 1 modulo 4, every representation (1) has all three denominator ratios nonsquare in the rationals.

For c=1 the following are equivalent:

1. Some representation of 4/n has a square pair.
2. Some representation of 4/n has two equal denominators.
3. n has a prime divisor 3 modulo 4.

These are existential statements over representations, not assertions about every representation at a given n. No coprimality, clean-type, primality, or squarefreeness assumption occurs in this theorem.

**Proof.** If Y/Z is a rational square, unique factorization applied after dividing by H=gcd(Y,Z) gives

    Y=Hr^2, Z=Hs^2, gcd(r,s)=1.

Let S=r^2+s^2. Since gcd(S,r^2*s^2)=1, the reduced numerator of 1/Y+1/Z=S/(Hr^2*s^2) is S/gcd(S,H). For an odd prime ell|S, neither r nor s is zero modulo ell. The residue r/s has square -1 and order four, so 4 divides ell-1. Every odd prime of the reduced numerator is therefore 1 modulo 4. S itself need not be odd: its factor 2 may cancel against H.

Subtracting 1/X in (1) gives A/(nX)=1/Y+1/Z>0, hence A>0. As n is odd, A,delta,alpha are odd. A prime ell|delta divides A and nX. If ell did not divide n, it would divide X, and then divide 4cX-A=n, a contradiction. This proves prime support, not delta|n. Uniqueness of the reduced fraction identifies alpha with S/gcd(S,H). Thus alpha=1 modulo 4, including alpha=1. As A=delta*alpha=4cX-n, (2) follows. All primes of n*delta divide n; an odd integer 3 modulo 4 must have a prime factor 3 modulo 4. Permuting the singled-out denominator proves the all-pairs corollary.

At c=1, the first statement implies the third by this necessity, and the second plainly implies the first. Conversely choose a prime q|n with q=3 modulo 4 and set

    m=n/q, t=(q+1)/4, (X,Y,Z)=(mt,2mqt,2mqt).

All denominators are positive integers and their reciprocal sum is (q+1)/(mqt)=4/n. The division-free certificate is

    4XYZ=16m^3*q^2*t^3,
    n(XY+XZ+YZ)=4m^3*q^2*t^2*(q+1)=16m^3*q^2*t^3.

The equal pair proves the converse. This standard identity and scaling are not new-identity claims. QED.

## 2. Clean signed-character theorem

**Theorem 2 (T-008).** Assume additionally gcd(c,n)=1, and put G=gcd(X,Y,Z), the full three-denominator gcd. Define:

- Clean I: n|Y and gcd(n,XZ)=1.
- Clean II: n|Y,Z and gcd(n,X)=1.

Then

    Clean I:  J(-cG,n)=-1;
    Clean II: J(-(X/G),n)=-1.                           (3)

For (U,V)=(X,Z) in I or (Y,Z) in II, put H=gcd(U,V), r=U/H, s=V/H. In both types,

    gcd(r,s)=1, gcd(rs,n)=1, J(-rs,n)=-1.                (4)

If n=1 modulo 4, r and s have opposite Jacobi signs, so U/V is not a rational square. If n=3 modulo 4 their signs agree; no square-pair exclusion follows from (4) there. At composite n the clean hypotheses are restrictive, not merely counts of denominators divisible by n.

**Proof: normalization.** Put a=4cX-n>0. In either clean type gcd(n,X)=1, whence

    gcd(a,n)=gcd(4cX,n)=1, gcd(a,X)=gcd(n,X)=1.

With D=aY-nX and E=aZ-nX, (1) gives

    DZ=nXY>0, EY=nXZ>0, DE=n^2*X^2.

In I, E=aZ modulo n is a unit. For each ell^e exactly dividing n, E has valuation zero, so D has valuation 2e. Write D=n^2*C, E=F, CF=X^2. In II, both D,E are n-divisible; write D=nC, E=nF, again CF=X^2. In either case C,F are coprime to n.

Reduce C/X=u/v with gcd(u,v)=1. Writing C=d*u, X=d*v, the divisibility C|X^2 implies u|d. Thus d=gu and

    X=guv, C=gu^2, F=gv^2, gcd(guv,n)=1.

Integrality of Y, gcd(a,n)=1 and gcd(a,gu)=1 give respectively a|nu+v or a|u+v. Set k=(nu+v)/a in I, k=(u+v)/a in II. Reconstruction yields

    I:  (X,Y,Z)=(guv,nguk,gvk),    ak=nu+v;
    II: (X,Y,Z)=(guv,ngku,ngkv),   ak=u+v.              (5)

Indeed Z=(gv^2+nX)/a in I and Z=n(gv^2+X)/a in II, giving exactly (5). A divisor common to u,k divides v; one common to v,k divides nu in I and u in II. As gcd(v,nu)=1 in I, u,v,k are pairwise coprime. In I, ak=v modulo n also makes k a unit modulo n. Therefore the full gcd is g in both types: in I use gcd(uv,vk)=v and gcd(v,nuk)=1; in II use gcd(nku,nkv)=nk and gcd(uv,nk)=1. Thus g=G, whereas

    I:  H=Gv,  (r,s)=(u,k);
    II: H=nGk, (r,s)=(u,v).                             (6)

In II, k need not be a unit modulo n; (6) nevertheless gives unit r,s.

**Jacobi lemma.** For positive b,t, L=4bt-1 is odd, gcd(b,L)=1, and

    J(b,L)=1, J(-b,L)=-1.                              (7)

For every odd prime ell|b, reciprocity and L=-1 modulo ell give

    J(ell,L)=(-1)^((ell-1)/2)*J(L,ell)
            =(-1)^((ell-1)/2)*J(-1,ell)=1.

If 2|b, L=7 modulo 8, giving J(2,L)=1. Multiply over all prime factors of b with their exponents. Finally J(-1,L)=-1. This includes even b and nonsquarefree L.

**Clean I.** Let M=4cGuk-1. Equation (5) gives vM=n(u+k). Since v is a unit modulo n, M=nh for positive odd h and hv=u+k. Lemma (7) with b=cG,t=uk gives J(cG,nh)=1. Modulo h, k=-u and 4cGuk=1; hence 4cGu^2=-1 and J(cG,h)=J(-1,h). Here 2u is a unit modulo h since h|M. The modulus-one convention covers h=1. Denominator multiplicativity, valid even if gcd(n,h)>1, gives J(cG,n)=J(-1,h). Since nh=3 modulo 4, J(-1,n)J(-1,h)=-1, proving the first identity in (3). Also 4cGuk=1 modulo n gives J(uk,n)=J(cG,n), so (6) implies (4).

**Clean II.** For the same M, (5) gives

    Mv=nk+u,       n=Ma-4cGu^2.

Since gcd(M,cGu)=1, the second identity makes gcd(M,n)=1. Lemma (7) gives J(n,M)=J(-4cGu^2,M)=J(-cG,M)=-1. Reciprocity, retaining M=3 modulo 4, yields

    J(M,n)=J(-1,n)J(n,M)=-J(-1,n).

Multiplying Mv=nk+u by v modulo n gives Mv^2=uv. Because v is a unit, J(uv,n)=J(M,n). As X/G=uv, this proves both the second identity in (3) and (4). No cancellation of k modulo n is made.

Finally, (4) is J(r,n)J(s,n)=-J(-1,n), giving the stated signs. A rational-square ratio r/s in lowest terms forces both r,s to be integer squares, contradicting opposite signs at n=1 modulo 4. QED.

## 3. Complementarity, examples, and limitations

| Result | Required domain | Conclusion |
| --- | --- | --- |
| Theorem 1 | Any representation; all prime divisors of n are 1 mod 4; any c | All three ratios are rational nonsquares, even outside clean types |
| Theorem 2 | Clean I or II; gcd(c,n)=1; n=1 mod 4 | Specified reduced same-status pair has opposite Jacobi signs, including mixed prime support |

For a non-clean example, (X,Y,Z)=(10,20,100) represents 4/25, with

    4XYZ=80000=25*(200+1000+2000).

Only 100 is a 25-multiple, but gcd(25,10)=gcd(25,20)=5; neither clean type applies under any permutation. Theorem 1 nevertheless excludes every square pair in every representation of 4c/25. It does not exclude this valid representation.

Conversely, at n=93=3*31, (35,6510,70) is clean I: its sum is 280/6510=4/93 and gcd(93,35*70)=1. Here G=H=35, (r,s)=(1,2), J(2,93)=J(2,3)J(2,31)=-1. Thus Theorem 2 applies although Theorem 1's all-pairs exclusion hypothesis does not. In its proof u=v=1,k=2,h=3, so gcd(n,h)=3; a negative global Jacobi sign is not a negative local sign at every prime factor.

The prime-support condition cannot be replaced by n=1 modulo 4 on unrestricted solutions: (7,42,42) represents 4/21. Nor does the sign exclusion apply at n=3 modulo 4: (1,6,6) is clean II at n=3. Prime support of delta is not divisibility: at n=9, (X,Y,Z)=(36,3,12) gives Y/Z=1/4 and delta=gcd(135,324)=27, which does not divide 9. Clean-II k need not be a unit: at n=15, (4,90,180) has G=2,u=1,v=2,k=3.

Necessity for every c is not sufficiency for every c. For example 8/3 has no three-unit-fraction representation: with at most one denominator 1 the sum is at most 2; exactly two would require the remaining reciprocal 2/3; three give 3. Theorem 1's converse remains at c=1. Its condition permits some square-pair representation, not a square pair in every solution: (3,6,14) at n=7 has reciprocal sum (14+7+3)/42=4/7, but the ratios 1/2,3/14,3/7 each have an odd prime valuation. Reduced-numerator support is not fixed-X sufficiency: at n=3,X=4 the remainder is 13/12, with reduced numerator 13=1 mod 4. Both remainder denominators cannot be at least 2, since their sum would be at most 1; one must be 1 and the other 12. This unique unordered completion has nonsquare ratio 1/12.

These are obstructions to specified construction targets, not counterexamples to Erdős–Straus. Both proofs are exact ordinary mathematics, independent of finite experiments. This draft synthesizes accepted T-008 and T-009; it asserts no new theorem beyond them, no new identity coverage, and no certified external originality. The sum-of-squares prime argument, normalization, Jacobi lemma, repeated-denominator identity, and scaling are standard ingredients. No computation or heuristic evidence is used; external priority and publishability remain **unresolved**, with certification **blocked** by the offline boundary.
