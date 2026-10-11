# R-007 — Type-II intrinsic character and sharp gcd ceilings

Sequence 007, 2026-10-04. Research question: what substantive partial theorem remains beyond the latest Type-II X-envelope, without restarting stopped pointwise forcing?

## 1. Workspace and prior-result audit

Read root/desk policy, `literature/key_results.md`, full current main report, all live main research records, newest I-010/I-011, R-006/D-006, H-005's complete proof, and the retained regression source. Read the existing Elsholtz–Tao HTML OFFLINE in Sections 2 and 4. H-005's Type-I theorem remains accepted as in R-006; its gcd symbol, p|h allowance and equality classification are not changed here.

**T-006 in I-011: proved on paper.** Rechecked X|bc and d|b², the sign and expansion of (b-m)[p-(4m-1)b+m], the exhaustive split at 2m, low-b residue exclusions, and both equality converses. No repair or new m-level is needed. I-010 remains superseded; its abandoned formulas are not proof inputs. There is still no H-006 in the desk, so main's separate audit remains pending. The main report is stale relative to R-006/I-011; it was not silently edited.

The pre-existing local source's Proposition 2.11 additionally excludes p²-divisible denominators at numerator 4. I-011's allowance of p|b,c,d is a harmless weakening of its hypotheses, not an example or a new high-valuation claim. Do not advertise that allowance as novel.

## 2. New result and proof checks

Authoritative source: `ideas/012_type_II_character_and_gcd_ceiling.md` (T-007).

For any prime p=1 modulo 4 and any Type-II solution, let X be smallest and G the full common gcd, s=X/G, q=q(p) the least positive nonresidue. Then

    Legendre(s,p)=-1,
    4qG<=p+q+1.

At p=1 modulo 8,

    s odd:  8qG<=2p+q+1,
    s even: 8qG<=p+2q+1.

Consequently G<=floor((2p+q+1)/(8q)) for every Type-II solution there. Full equality triples are classified in I-012.

Adversarial checks:

* **Actual solutions, not selected certificates.** Starting with arbitrary X,Y,Z, smallest X is p-free, and D=aY-pX,E=aZ-pX are positive with DE=p²X². Both factor terms are p-divisible, forcing exact valuations (1,1); normalize their p-free quotient C/X. Nothing assumes that all solution witnesses are the saved first witnesses.
* **Full gcd.** C/X=u/v gives X=guv, C=gu². Cancellation yields k=(u+v)/a and denominators (guv,pgku,pgkv). All pairs u,v,k are coprime. With p∤uv, gcd(uv,pku,pkv)=1, hence G=g. No pairwise gcd is mistaken for the gcd of all three.
* **Character transfer.** With M=4guk-1, the two exact equations are p=Ma-4gu² and Mv=pk+u. The Jacobi lemma gives (p/M)=-1, and p=1 modulo 4 permits reciprocity without a sign. Then Mv²=uv modulo p proves (X/G/p)=-1. p∤M follows from gcd(M,gu)=1, including even g and repeated factors in M.
* **No accidental Type-I import.** The conclusion is about X/G, NOT G. The existing Type-I condition Legendre(G,p)=-1 is used only in the two-type corollary. Primitive Type-II solutions are permitted, as they must be.
* **Ceilings.** With s=uv, S=u+v<=s+1 and 4Gs=p+S/k, (G4) follows from s>=q. At p=1 modulo 8, odd s forces k even>=2; even s has s/2 a nonresidue, hence s>=2q. Every monotone step has a positive numerator and equality explicitly tracked. There is no false global monotonicity in b or unbounded optimization left over.
* **Equality converses.** All three displayed families have positive integral denominators, exact reciprocal identities, p-free smallest X, type II, and full gcd G. The conditions q=q(p) and p in the relevant prime domain are essential, not optional or automatically true for every parameter.
* **Attainment domains.** Universal p=1 modulo 8 equality is exhibited at 97, NOT claimed attained in the six residual classes. Even-s equality is exhibited at 4201=1 modulo 840. Do not promote an attainment example outside a domain into domain-specific sharpness.
* **Corollary scope.** At least one of G,X/G is a nonresidue for every solution at p=1 modulo 4; this does not characterize its type uniquely when both are nonresidues, and does not force either type to exist.

**Written proof: proved.** This is same-model derivation/adversarial checking, not a fresh independent reviewer or formal verification. Main's separate proof audit is requested.

## 3. Exact computational evidence

Created `007_character_gcd_probe.py` and `007_character_gcd_results.json`. Executed the mounted source directly using code_runner with Python 3.12.3, Linux aarch64, standard library only, exact integers. PASS in 990757231 ns, no stderr reported. Source SHA256:

    821cbbfdc2609d070b9278b38a09ef9630cfbfa0f3a4695de36a3a37fc5858b0

Input SHA256:

    5eb5717274f4b7f9b4cacbff7cfc17047f431f05eb57fa31a94444423ee93e5d

Domain remains the H-005 frozen snapshot's 2991 pairs / 187 primes. Exactly 858 first saved A certificates pass character and gcd assertions: 403 odd-s and 455 even-s. There are zero odd-bound equalities and four even-bound equalities in the retained witnesses. Separately 955 first saved B witnesses check the accepted Type-I contrast and two-type corollary.

Exact q computation scans Euler characters at those 187 primes (range 11..29); it is not a new prime/solution search. Two algebraically specified equality certificates: 97,(25,970,4850),q=5,G=5, and retained prime 4201,(1056,201648,4436256),q=11,G=48. Exact identity, primality by trial division, minimal nonresidue, normalization, type and gcd all pass.

All 34 H-005 manifest hashes pass before/after. 116 pre-existing desk files have identical pre/post hashes, aggregate listed in the JSON. The script writes no files and does not run historical probes. No expanded prime interval, shift window, parameter sweep, all-solution census, network, installation, or Lean theorem. **Status: verified computationally on these inputs only.** Universal scope rests on I-012's written proof.

## 4. Local originality audit and recommendation

The local source already has the parameterization, coarse X<=p/2 envelope, odd-square obstruction, and valuation exclusion. H-004 already proves the auxiliary M nonresidue. None of these are new. The inspected source passages and local theorem register do not state the intrinsic quotient character or sharp q-dependent gcd ceilings. This is a limited local comparison; the character transfer itself is an elementary corollary, not evidence of external novelty.

**External priority: unresolved. Publication significance: plausible, not certified.** Prefer a concise combined note with H-005's intrinsic Type-I gcd result and T-006/T-007's complementary Type-II restrictions. Do not call it a new congruence cover or promote nested equality formulas as original.

One main task: independently audit/freeze I-012, incorporating the short I-011 audit if H-006 is still absent. Preserve all historical files and use the next available handoff number. No existence forcing, m-hierarchy, new range, priority campaign or artificial second direction. A self-contained proved partial theorem with honest novelty limits is the endpoint.