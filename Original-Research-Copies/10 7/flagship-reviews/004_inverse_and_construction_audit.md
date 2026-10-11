# R-004 — Accept H-003; close the nested-coverage shortcut; no pointwise breakthrough

Sequence 004; 2026-10-04. Research question: is H-003's universal group lemma sound, and does the newest user construction offer a genuinely different route to Erdős–Straus? Read README, local policy, report, literature register, all main records, newest ideas/review/decision, and all mathematical/source payloads of H-003.

**Verdict:** H-003 accepted within its exact stated scope (**proved**). U-007's normalized identity is **proved but restricted**; its universal prime-coverage claim is **false**. The conjecture remains **unresolved** and the pointwise bridge **blocked**. No historical file, frozen handoff, or main-model conclusion was overwritten. No network, external workspace dependency, Lean build, or independent sub-agent was used.

## 1. H-003 proof audit — accepted

### Growth and parity

A period of ANY partial binary sumset persists under the remaining additions. Thus aperiodicity of the final T really does imply aperiodicity of every partial sumset, in every ordering; this is not the generally false assertion that stabilizers always stay equal. Each nonzero step grows by at least one. Any pair unequal up to sign consumes one extra growth unit. Equality |T|=L+1 would force all entries to be signed copies of one generator; odd L then contradicts even total. With L=m-2 and disjointness, |T|=m=L+2 follows. The m=3 impossibility is handled correctly.

### Four-set orbit lemma

For P={0,u,v,u+v}, |(P+w)\P|=1 says exactly one proper occupied w-orbit has exactly one occupied run; all other occupied orbits must be full. A full even-order orbit violates involution avoidance. Since |P|=4, the only remaining full-orbit possibility is an order-three coset plus a singleton.

The exclusion of that exception is correct: the reflection z -> u+v-z must preserve the unique full coset and fix the singleton. In G/<w>, their distinct classes have equal doubles and so differ by the unique involution. Because |<w>|=3 is odd, this is the image of m. The singleton's m-translate therefore lies in the full coset, a contradiction. No prime-m assumption is hidden here.

Without full orbits, P is a four-element proper progression of step w. Its progression reflection and its binary-sum reflection differ by a period of P, hence are equal. Listing the four possible positions of 0 gives {u,v}={+/-w,+/-2w} with independent signs. The proof does not prematurely assume full order of w.

### Full order and uniqueness of the exception

For any third occurrence s, the same lemma implies that one of the fixed pair u,v is +/-s, so s lies in {+/-u,+/-v}. All occurrences therefore lie in <w>. Generation of the WHOLE list, not of an individual term, makes w a generator. A second doubled occurrence would force 1=+/-2 or +/-4 modulo 2m>=10. Both alternatives are impossible. Exactly one doubled occurrence is established.

**Accepted theorem:** every odd m>=3 satisfies T-003 under ALL its stated hypotheses. The written proof, not the four-group test, supports this status. No literature-novelty claim is accepted or needed.

## 2. Prerequisites and arithmetic specialization — accepted

- Binary growth |S|>=|K|(N+1) follows from quotient aperiodicity and period persistence for any finite abelian group. This closes O-005 for the specialized application, NOT for general Kneser.
- S=D union pD correctly encodes both A and B through S intersect -S; inverse closure is not mistaken for product closure.
- In the prime-defect case J has exactly one factor of 2 in its order, as does the ambient unit group. Therefore J has odd index, ambient squares in J equal J², and the odd stabilizer K lies in J². The even-total claim from px=4x² is valid after deleting K-occurrences.
- Actual quotient generation, aperiodicity, and avoidance of the involution in the DIFFERENCE set are all justified.
- The p occurrence may be exceptional, ordinary, or deleted. All three cases and beta=delta+A are correctly recorded. None yields an arithmetic contradiction merely from parity.
- The self-contained fixed-x certificate audit has correct positivity, p-adic allocation, integrality and unordered scope. No branch has disappeared.

O-007 can be closed from the main side, citing this review. Nothing forces N=m-2 at any shift, and sparse N remains untreated. Do not authorize another deficiency-level inverse theorem by inertia.

## 3. Computational audit — reproduced, exact scope only

Inspected the standalone checker before execution. It enumerates nondecreasing lists as a permutation-symmetry reduction, excludes only the forbidden zero/involution entries, computes ALL binary subset sums, tests ALL nonzero periods, and searches ALL possible generators. Parity and gcd filters match the hypotheses. The 1644 triple checks occur only within the same 84 eligible lists; they are not an exhaustive independent test of the four-set lemma in all groups.

Executed directly from the mounted flagship paths, with Python 3.12.3 and assertions enabled:

    python3 <absolute flagship>/reviews/004_audit_probe.py

This verifies all eight H-003 payload hashes, runs the frozen standalone checker and the previous flagship probe, and compares both outputs byte-for-byte with H-003's saved stdout. Both exit 0, empty stderr. Results:

| Check | Result |
|---|---:|
| H-003 payload hashes | 8/8 PASS |
| Abstract m | 3,5,7,9 only |
| Visited lists | 175036 |
| Eligible lists | 84 |
| Counterexamples in that domain | 0 |
| Critical triples in eligible lists | 1644 |
| Legacy fixed-x pairs | 2991, unchanged |
| Legacy joint prime-defect failures | 253 |
| Legacy joint sufficient passes | 106, including 33 beyond A-only sufficiency |

The final retained reproduction took 9247172308 ns for the standalone script and 693454769 ns for the legacy probe, excluding wrapper startup. Full hashes, outputs, six named U-007 records, environment and timings are in `004_reproduction.json`. An earlier read-only reproduction also matched both outputs. No new abstract group, prime interval, or offset window was added.

## 4. U-007 — separate the identity from the coverage claim

Full derivations and precise qualifications are in [I-008](../ideas/008_nested_family_and_branch_separator.md). The original user note remains unchanged. Only its locally available normalized formulas, not unavailable screenshots or unstable variable variants, have been audited.

### Accepted algebra, not a new construction beyond the local foundations

For positive P,n,k with kP>1,

    m=(kn+1)/(kP-1) is integral iff (kP-1)|(P+n).

The given sufficient integrality condition is actually necessary too. Reducing modulo k forces m=ak-1. Setting P=4c gives

    n=a(4ck-1)-4c,
    (x,y,z)=(c(ak-1), ckn, c(ak-1)kn).

For n=1 mod 4, a=3 mod 4 and all positivity conditions follow. This is exactly KI-004 with u=1, g=c, v=ak-1. It describes nested branch-A denominators (one of the two n-divisible denominators divides the other), not all of A and not B. The reported 1129 construction reproduces I-004's existing triple exactly.

### Finite exceptions are genuine failures of the entire normalized family

The proved bound ck<=(n+3)/8 gives a COMPLETE finite test of this family, not an arbitrary search cutoff. Two enumeration schedules agree on the six explicitly named inputs:

    n:          193  1009  1129  1201  2521  66529
    witnesses:   0     2     2     2     0      0

Every witness is checked by 4xyz=n(xy+xz+yz). Trial primality and all tested bounds are recorded. A compact 24-residue proof of the miss at 193 is also in I-008; an initial prose transcription of that short list was detected by direct evaluation and corrected before this review was finalized. The actual exhaustive scripts consistently returned the same no-hit result.

Nevertheless 193 has the ordinary non-nested A certificate (50,1930,4825). Therefore universal nesting, even restricted to A-solvable primes, is **false**. A new c/M search would be re-enumerating a disproved universal route. An undefined broader half-decomposition scheme cannot inherit either completeness or falsity from this audit; its exact specification remains **unresolved**.

## 5. Incremental mathematics from the audit

### Square obstruction — proved, not a finite experiment

For M=4gh-1, elementary reciprocity gives Jacobi(g,M)=+1 and Jacobi(-g,M)=-1. The restricted family satisfies n=-4c mod (4ck-1), hence Jacobi(n,4ck-1)=-1. Consequently **every positive square is excluded from the family**, with no search bound at all. The reported test at 100001² has a mathematical explanation; no larger square search is justified.

More strongly, the full switched A equation can be written

    n=(4guk-1)a-4gu².

Thus Jacobi(n,4guk-1)=-1 for the ENTIRE switched A family. Restoring the suppressed u does not remove the square obstruction. This is an obstruction to that parameterization, not a nonexistence theorem for three unit fractions.

### Exact comparison with branch B — proved, not pointwise forcing

For normalized fixed-x data x=guv, C=gu², gcd(u,v)=1, the two branches admit the SAME auxiliary expression M=4guk-1, but distinct equations:

    A: k=(u+v)/a,       p=M a-4gu²,       Legendre(M,p)=-1;
    B: k=(pu+v)/a,      M=p h, hv=u+k,    Legendre(M,p)=0.

B reconstructs (guv,pguk,gvk); A reconstructs (guv,pgku,pgkv). The square/nonresidue argument and the explicit distinction from B are additional local understanding; the parameter identities are elementary Rosati-type reformulations, not claimed as original research.

**Adversarial limitation:** a nonresidue M does not force M|(p+4gu²), and a multiple-of-p M does not force (M/p)|(u+k). Nor is the same parameter tuple shared by unrelated completions. Therefore character escape, parameter symmetry, or restored u alone does not supply a bridge. This direction is **blocked** as an existence proof. No conjecture-level progress is claimed from renaming the divisor conditions.

## 6. Strategic decision

Accept H-003 and archive the inverse hierarchy unless an arithmetic bridge appears. Reject the exact normalized U-007 family as a universal proof program, while retaining its valid identity and precise failure mechanism. Defer ill-specified screenshot variants rather than invent missing hypotheses.

D-004 assigns ONE short closure audit: independently check the new Jacobi/branch-separator theorem and record the exact scope of U-007. No new search, inverse level, isolated residue class, almost-all argument, or broad literature project is authorized. If no pointwise implication beyond the displayed equivalences can be proved, stop rather than spend a full research round repackaging them.

**Strongest accepted research result:** T-003 is now adversarially audited as a universal local group theorem. **Strongest new result in this review:** a uniform obstruction and exact A/B character separation that rule out the latest shortcut. **Still missing:** for EVERY target prime, a construction or theorem forcing SOME admissible parameters/shift. Erdős–Straus remains **unresolved**.