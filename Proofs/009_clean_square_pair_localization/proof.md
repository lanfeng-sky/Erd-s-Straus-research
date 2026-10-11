# T-010 — Clean all-pairs square-ratio localization

D-011 main-model proof audit, 2026-10-06. Mathematical status: **proved**. This file includes the normalization and character prerequisites; no sibling or historical file is needed for the proof.

## 1. Statement and conventions

Let c>=1 and n>=3 be integers, with n odd and gcd(c,n)=1. Let X,Y,Z be positive integers satisfying

    4c/n = 1/X + 1/Y + 1/Z,
    equivalently 4cXYZ = n(XY+XZ+YZ).

No ordering or distinctness is assumed. A square pair means an unordered pair U,V for which U/V is a square in the positive rationals; the condition is unchanged on reversing the quotient. Define

- **Clean I:** n|Y and gcd(n,XZ)=1;
- **Clean II:** n|Y,Z and gcd(n,X)=1.

**T-010.** In Clean I the cross-status pairs (X,Y) and (Y,Z) are never square pairs. If a square pair occurs, it is (X,Z), and n is 3 modulo 4. In Clean II the cross-status pairs (X,Y) and (X,Z) are never square pairs. If a square pair occurs, it is (Y,Z), and n is 3 modulo 4.

Consequently, every clean representation at n=1 modulo 4 has all three unordered pairwise ratios nonsquare in Q. This includes mixed prime support and nonsquarefree n. Thus at n=1 modulo 4 any successful square-pair representation must be non-clean under every permutation.

The theorem is necessary/localizing only. It neither forces a square pair at n=3 modulo 4 in a given representation nor forbids representations without square pairs.

Write J(b,m) for the Jacobi symbol at positive odd m, with J(b,1)=1. Background inputs are unique factorization, Jacobi multiplicativity, quadratic reciprocity and its supplementary laws. In particular, for a unit b, J(b,w^2)=1 for odd w, and J(-1,m)=(-1)^((m-1)/2). Multiplicativity in the odd denominator does not require the factors to be coprime.

## 2. Normalization independently rederived

Put a=4cX-n. Subtracting 1/X gives a/(nX)=1/Y+1/Z>0, hence a>0. Both clean types have gcd(n,X)=1, so

    gcd(a,n)=gcd(4cX,n)=1,    gcd(a,X)=gcd(n,X)=1.

Define D=aY-nX and E=aZ-nX. The representation implies

    DZ=nXY>0,    EY=nXZ>0,    DE=n^2 X^2.

In Clean I, E=aZ modulo n is a unit. For each prime ell with ell^e exactly dividing n, E has ell-valuation zero; since X is a unit modulo n, D has ell-valuation 2e. Thus D=n^2 C, E=F, where C,F are positive, CF=X^2, and gcd(CF,n)=1. This is prime-power allocation, not just the observation n|D.

In Clean II, D and E are divisible by n. Write D=nC,E=nF. Again CF=X^2 and gcd(CF,n)=1. No primality or squarefreeness of n is used.

Reduce C/X=u/v with gcd(u,v)=1. Write C=d0*u and X=d0*v. From CF=X^2 obtain uF=d0*v^2, so u|d0. Writing d0=gu yields

    C=gu^2,    X=guv,    F=gv^2,    gcd(guv,n)=1.

In Clean I the reconstruction gives

    Y=ngu(nu+v)/a,    Z=gv(nu+v)/a.

In Clean II it gives

    Y=ngu(u+v)/a,     Z=ngv(u+v)/a.

Since gu divides X, gcd(a,X)=1 implies gcd(a,gu)=1. Together with gcd(a,n)=1, integrality of Y proves a|nu+v in I and a|u+v in II. Define positive k by the appropriate quotient. Hence

    I:  (X,Y,Z)=(guv,nguk,gvk),    ak=nu+v;
    II: (X,Y,Z)=(guv,ngku,ngkv),   ak=u+v.              (N)

The parameters u,v,k are pairwise coprime. A prime dividing u and k would divide v by (N), contradicting gcd(u,v)=1. A prime dividing v and k would divide nu in I; since gcd(v,n)=gcd(v,u)=1 this is impossible. In II it would divide u, also impossible. In I, ak=v modulo n proves gcd(k,n)=1. No such conclusion is made in II.

Let G=gcd(X,Y,Z), the full gcd. In I,

    gcd(uv,vk)=v,    gcd(v,nuk)=1,

so G=g. In II,

    gcd(nku,nkv)=nk,    gcd(uv,nk)=1,

so again G=g. In particular gcd(G,n)=1. The separate same-status pairwise gcd H is

    I:  H=gcd(X,Z)=Gv,    reduced pair (u,k);
    II: H=gcd(Y,Z)=nGk,   reduced pair (u,v).

All u,v are units modulo n; k is also a unit in I, but may be a nonunit in II. The full G and pairwise H are not interchangeable.

## 3. Character prerequisites independently rederived

### 3.1 Specialized Jacobi lemma

For positive b,t put L=4bt-1. Then L is odd, gcd(b,L)=1 and

    J(b,L)=1,    J(-b,L)=-1.                           (J)

Indeed, for each odd prime ell|b, reciprocity (L=3 modulo 4) and L=-1 modulo ell give

    J(ell,L)=(-1)^((ell-1)/2) J(L,ell)
            =(-1)^((ell-1)/2) J(-1,ell)=1.

If 2|b, L=7 modulo 8 and J(2,L)=1. Multiply over the prime factors of b with their exponents. Finally J(-1,L)=-1. Repeated prime factors in L and even b are allowed.

### 3.2 Clean I

Replace g by the full G in (N), and set M=4cGuk-1. Substituting a=4cGuv-n into ak=nu+v gives

    Mv=n(u+k).

Since gcd(v,n)=1, write M=nh with positive odd h; then hv=u+k. Applying (J) with b=cG,t=uk gives J(cG,nh)=1. Modulo h, k=-u and 4cGuk=1, so

    4cGu^2=-1 modulo h.

The factor 2u is a unit modulo h because h|M and gcd(2u,M)=1. Thus J(cG,h)=J(-1,h), including h=1. Denominator multiplicativity yields

    1=J(cG,n)J(cG,h),    J(cG,n)=J(-1,h).

This is valid even when gcd(n,h)>1. Since nh=3 modulo 4,

    J(-cG,n)=J(-1,n)J(-1,h)=-1.                        (I1)

Also 4cGuk=1 modulo n, so J(uk,n)=J(cG,n) and

    J(-uk,n)=-1.                                      (I2)

### 3.3 Clean II

For the same M, substituting ak=u+v gives

    Mv=nk+u,    n=Ma-4cGu^2.

Since M is odd and gcd(M,cGu)=1, gcd(M,n)=1. By (J),

    J(n,M)=J(-4cGu^2,M)=J(-cG,M)=-1.

Reciprocity with M=3 modulo 4 gives

    J(M,n)=J(-1,n)J(n,M)=-J(-1,n).

Multiplying Mv=nk+u by v modulo n gives Mv^2=uv modulo n. The unit v has J(v^2,n)=1, so

    J(uv,n)=J(M,n),    J(-uv,n)=-1.                    (II)

The only cancelled quadratic factor is the unit v^2. The proof never cancels k modulo n or assumes gcd(k,n)=1.

## 4. All three unordered pairs in Clean I

The reduced ratios from (N) are

    X/Z=u/k,    X/Y=v/(nk),    Y/Z=nu/v.

They are in lowest terms: u,v,k are pairwise coprime and all three are units modulo n. A positive fraction in lowest terms is a rational square exactly when its numerator and denominator are integer squares, by prime-exponent parity.

**Same-status pair (X,Z).** If u/k is a rational square, u and k are squares. Hence J(-uk,n)=J(-1,n). Identity (I2) makes J(-1,n)=-1, so n=3 modulo 4.

**Cross-status pair (X,Y).** If v/(nk) is a rational square, v and nk are squares. Because gcd(n,k)=1, every prime exponent in n is even: n is an odd square. But cG is a unit modulo n, and an odd square modulus has J(-cG,n)=1, contradicting (I1).

**Cross-status pair (Y,Z).** If nu/v is a rational square, nu and v are squares. Because gcd(n,u)=1, n is again an odd square, giving the same contradiction to (I1).

Both cross-status pairs are therefore impossible, for either odd congruence class of n.

## 5. All three unordered pairs in Clean II

The reduced ratios are

    Y/Z=u/v,    X/Y=v/(nk),    X/Z=u/(nk).

Here gcd(u,v)=1 and gcd(u,nk)=gcd(v,nk)=1 even when gcd(k,n)>1.

**Same-status pair (Y,Z).** A rational-square u/v forces square u and v, so (II) gives J(-1,n)=-1, hence n=3 modulo 4.

**Cross-status pair (X,Y).** A rational-square v/(nk) gives

    v=r^2,    nk=s^2

with positive r,s. Define the squarefree kernel precisely by

    d = product of primes ell for which the exponent of ell in n is odd.

This is not necessarily the radical of n. It is odd and may be 1. Since each exponent in nk is even, the exponent parities in n and k coincide. Thus for positive integers w,t,

    n=d w^2,    k=d t^2.

There is no requirement gcd(d,w)=1. From k|u+v in (N), d|u+r^2. For every prime ell|d,

    -u = r^2 modulo ell,    gcd(r,ell)=1.

Thus each local Legendre symbol of -u at ell|d is +1 and J(-u,d)=1 (empty product if d=1). Since gcd(u,n)=1, denominator multiplicativity and the square modulus give

    J(-u,n)=J(-u,d)J(-u,w^2)=1.

As v=r^2 is a unit modulo n, J(v,n)=1. It follows that J(-uv,n)=1, contradicting (II).

**Cross-status pair (X,Z).** A rational-square u/(nk) similarly gives u=r^2 and nk=s^2. With the same kernel d, k|u+v gives -v=r^2 modulo each prime ell|d. Since gcd(r,n)=gcd(v,n)=1,

    J(-v,d)=1,    J(-v,n)=1,    J(u,n)=1,
    J(-uv,n)=1,

again contradicting (II).

This proves the cross-status impossibility even for nonunit k, repeated prime factors of n, and d=1. No step divides by k modulo n. Sections 4 and 5 prove T-010 and its n=1-modulo-4 all-pairs corollary. QED.

## 6. Scope, quantifiers and local increment

T-008 already supplies the character of the same-status pair. T-010 adds exclusion of both cross-status pairs at every odd n, and thus excludes all pairs in clean representations at n=1 modulo 4. T-009's unrestricted all-pairs exclusion instead assumes every prime factor of n is 1 modulo 4 and needs neither clean hypotheses nor gcd(c,n)=1. On mixed-support n=1 modulo 4, T-010 says square pairs can occur only outside the clean domain; it does not say they cannot occur.

No sufficiency for arbitrary c is asserted. Nor does n=3 modulo 4 guarantee a square pair in each clean representation. For c=1, the familiar equal-pair identity with t=(n+1)/4, (t,2nt,2nt), DOES give a clean-II representation whenever n=3 modulo 4, since gcd(n,t)=1. This standard existential fact is not contradicted by T-010 and is not a new result here. Existence of some such representation must not be confused with a square pair in a specified representation or with arbitrary-c sufficiency.

The proof uses exact symbolic integer arithmetic; no finite computation, empirical conjecture, Lean compilation, or heuristic input is involved. Clean types need not exhaust composite solutions. No unrestricted Erdős–Straus nonexistence or new congruence coverage follows. The cross-status corollary extends the inspected local register; normalization, the Jacobi inputs and exponent-parity arguments are standard ingredients. External priority and standalone publishability remain **unresolved**; priority certification is **blocked** under the offline policy.
