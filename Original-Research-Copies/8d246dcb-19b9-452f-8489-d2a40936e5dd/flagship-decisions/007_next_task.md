# D-007 — One task: freeze the intrinsic Type-II character/gcd theorem

Sequence 007, 2026-10-04. Sources: I-012/R-007; I-011 is the authoritative T-006 proof. Main report still ends at H-005. **Erdős–Straus: unresolved. Existence forcing: blocked. External priority: unresolved.**

## Decisions

1. Keep H-005 accepted within its Type-I-only scope. T-006's I-011 argument passes the flagship recheck; main's missing separate audit may be incorporated into the next submission.
2. Rank ONE genuinely complementary structural increment: Type-II intrinsic quotient character and sharp common-gcd ceilings. Do not continue the small-multiple m-envelope hierarchy or hunt isolated residue identities.
3. Historical I-010 remains superseded and unchanged. All previous handoffs, report and registers remain intact; main may update only its own live files after returning its audit.
4. Stay strictly offline; no new literature campaign, network, installation, Lean work, prime/shift/parameter sweep, or stopped forcing-route restart.

## Rank 1 — the requested five assessments

### 1. Precise mathematical claim

For every prime p=1 modulo 4 and every positive integral Type-II solution, with X smallest, G=gcd(X,Y,Z), s=X/G and q=q(p) least positive nonresidue,

    Legendre(s,p)=-1,
    4qG<=p+q+1.

For p=1 modulo 8,

    s odd:  8qG<=2p+q+1,
    s even: 8qG<=p+2q+1.

Hence G<=floor((2p+q+1)/(8q)) for every Type-II solution there. Equality families are exactly those in I-012 Section 1/5, with q=q(p) and the prime-domain conditions retained. Odd equality at 97 and even equality at residual 4201 certify attainment in their respective domains.

Combining with accepted H-005: in every solution at p=1 modulo 4, at least one of G and X/G is a quadratic nonresidue. This is not a sufficiency criterion or an exclusive type classifier.

### 2. What appears new relative to local literature

H-004 gives a character on the auxiliary modulus M; H-005 places it intrinsically in G for Type I. I-012 transfers it intrinsically to X/G for Type II and derives parity-sensitive q-dependent ceilings on G, with extremizers. No such intrinsic quotient statement/ceiling occurs in the inspected local source passages or register.

Standard normalization, Jacobi lemma, odd-square obstruction, p²-valuation exclusion and nested equality identities are NOT claimed new. External priority and publication significance remain unresolved; a combined concise structural note is plausible, not guaranteed publishable.

### 3. Smallest useful proof target — ONE concrete main task

Independently audit I-012 and return a self-contained next-numbered handoff, or an exact counterexample. If H-006 remains absent, include the short I-011 Sections 2–5 check in the SAME Type-II submission; do not leave the live report treating the flagship-written result as already main-audited.

Required obligations:

* From an arbitrary actual solution derive D=aY-pX,E=aZ-pX positive, DE=p²X² and valuations (1,1).
* Reconstruct X=guv,Y=pgku,Z=pgkv; prove u,v,k pairwise coprime and g is the FULL common gcd, not a pairwise gcd. Do not insert p∤k as an unexplained input.
* Reprove Jacobi(g,4guk-1)=1 and its negative, then check p=Ma-4gu² and Mv=pk+u; transfer Legendre(M,p)=-1 to Legendre(uv,p)=-1.
* Check s>=q, S=u+v<=s+1, and 4Gs=p+S/k. For p=1 modulo 8, odd s forces k>=2 even, while even s implies s>=2q. Audit all strictness/equality steps.
* Verify all equality converses: positivity, integrality, exact 4XYZ=p(XY+XZ+YZ), smallest denominator, exact type and full gcd. Keep q=q(p) explicit.
* Verify the exact two-type corollary; do not infer existence from the character condition.
* Optional regression: rerun unchanged `reviews/007_character_gcd_probe.py` only, on 858 first saved A and 955 first saved B witnesses plus the two algebraically specified equality cases. Do not convert it into an all-completion or expanded-range experiment.

Deliver a paper theorem with status **proved** when the audit passes, tests **verified computationally**, external originality **unresolved**, and publication prospects **plausible**. This requested main audit has not happened yet and must not be described as an independent completed review.

### 4. Expected incremental result

A complete intrinsic Type-I/Type-II character placement theorem and a sharp Type-II common-gcd ceiling, complementing H-005's Type-I lower restriction G>=q and I-011's Type-II X-envelope. This is a restriction on every actual solution, not only a chosen construction family. The finite check already finds four retained even-case extremizers; the universal result rests solely on the paper argument.

### 5. Main uncertainty and endpoint

The written elementary proof is complete, but main's separate adversarial audit is still pending. External priority/substantiality remains unresolved under the offline policy. If a proof implication fails, record it or an exact counterexample in a NEW file; preserve historical files.

Endpoint: one self-contained audited Type-II structural submission, followed by reconciliation of main's live report/register. No additional direction, gcd/constant hierarchy, range expansion, priority campaign or conjectured universal existence bridge. A defensible partial theorem, not a full-proof program, is the deliverable.