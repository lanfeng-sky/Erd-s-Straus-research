# Research Log

## 2026-10-03: D-001 completed

Audited both implications of the fixed-x0 prime-factor criterion, positivity,
integrality and the division-free identity; recorded [KI-001](known_identities.md).
Executed the prescribed exact classifier on all 273 selected primes through
100000: 87 certificates and 186 fixed-x0 failures. The separate factor-pair
checker verified every record and found zero disagreements. No other x was
searched; the existing Certificate.valid() utility was reused, not its bounded
search. Detailed artifacts are in `experiments/results/001_x0/`; the flagship
review snapshot is [H-001](../handoffs/001_x0/README.md).

Finite deliverable: verified computationally. Remaining gap: construction at
other x for fixed-x0 failures; [obligations](open_obligations.md). Universal
existence remains unresolved. Requested flagship reproduction and proof audit.

## 2026-10-04: D-002 structural audit completed and submitted

Read R-002 acceptance and all newest ideas/decision; preserved H-001 and
historical flagship files. Audited KI-002 for EVERY prime p=1 mod 4,
p/4<x<p: all p-adic allocations, A/B reconstructions, positive integral
denominators, exact certificate, ratio inversion and ordering caveat.
Audited KI-004 switched factorization and normalized branch-A equivalence.
KI-003 application remains conditional on named finite Kneser input;
primary proof was not audited and no network or Lean work was needed.

New `audit_structure.py`: all 186 x0-failure primes at ALL t=0,...,15,
plus 118801 at ALL t=0,...,14; exactly 2991 pairs, zero branch-by-branch
factor-pair disagreements. Counts: 757 both, 101 A-only, 198 B-only,
1935 neither. Failures: 1059 quadratic, 465 other subgroup, 411 bounded
exponent. All 342 prime-defect A failures under -1 in H have deficient
odd subgroups; 89 of these are B successes. Completed 118801's previously
missing independent no-hit checks t=8,...,13; first success remains t=14.

Seven prescribed switched primes: all solved after 147 lexicographic
(g,k) candidates with g,k<=16; saved every earlier miss and normalized
A comparisons. Exactly two cross-shift proposals tested, both false:
C1 smallest dataset counterexample p=1129,t=12,13; C2 p=2521,ell=11,19.
No cross-shift forcing mechanism yet; stop rule honored, no wider search.

Separate `check_structure_records.py` directly scanned divisors with no
generator imports: PASS, all 2991 classifications and 1813 saved branch
certificates plus seven switched triples checked. Python 3.12.3 Linux
aarch64; integer arithmetic; generation 5552022847 ns, direct checker
14297017155 ns. These are separated algorithms by main, not a fresh agent
or formal proof. Scripts, complete records, environment/hashes and proof
notes: `experiments/results/002_structure/`; self-contained frozen
[H-002](../handoffs/002_structure/README.md). Requested flagship review.
Overall conjecture unresolved; pointwise bridge blocked.

## 2026-10-04: D-003 inverse theorem proved and submitted

Read all required main/local literature and latest I-005/I-006, R-003,
D-003. Recorded R-003 acceptance of H-002; preserved all historical files.
Independently audited binary growth, critical rigidity and square parity.
New elementary proof removes Kneser from specialized KI-003 (O-005 closed
for binary products only); general Kneser source/proof audit remains undone.

T-003 **proved** for EVERY odd m>=3: nonzero generating length m-2 list
in C_(2m), aperiodic subset sums disjoint from their involution translate,
even total => exactly one +/-2g and all others +/-g. m=3 impossible.
One written proof route: reorder an incompatible pair; the unique excess
growth forces a third-term four-set progression. Orbit-run analysis handles
possible small-order terms; reflection rules out the full order-three coset
plus singleton. Whole-list generation then derives full order and excludes
a second doubled occurrence. No prime-m or individual full-order assumption.

Specialized to every prime-defect failure with N=m-2 relative to ACTUAL
joint K. Verified all quotient hypotheses and recorded exceptional, ordinary,
and deleted p cases with pK=4K*xK. No resulting arithmetic contradiction;
no pointwise forcing, new identity or success range. Re-audited fixed-x
integrality, positivity and 4xyz=p(xy+xz+yz) self-contained in H-003.

Reran the original probe: PASS, unchanged 2991-pair diagnostics and all
H-002 hashes. Independent standalone checker uses ALL binary choices:
175036 multisets in m={3,5,7,9}, eligible counts 0/12/30/42, zero
counterexamples; 1644 critical triples checked in these same lists. No m>9
or new prime/offset sweep. Python 3.12.3 Linux aarch64, integers only.
Both saved runs exit 0, timed 738844000 / 9145259308 ns. This is algorithmic
separation by main, not a fresh agent or formalization.

Detailed artifacts: `experiments/results/003_joint_inverse/`. Frozen
self-contained [H-003](../handoffs/003_joint_inverse/README.md) has eight
payload files and SHA256SUMS. Mounted standalone rerun matches saved stdout
byte-for-byte; manifest PASS. Freeze wrapper initially tried a nonexistent
H-001 manifest after successfully creating H-003; corrected verification
without modifying H-003, recorded in freeze_check.json. H-002 hashes PASS;
H-001 has no manifest and was not written. No network or Lean installation.

Stop under D-003: request NEW flagship review of the proof/quotient cases.
No further deficiency hierarchy or wider search without an arithmetic bridge.
Overall conjecture **unresolved**; pointwise gap **blocked**.

## 2026-10-04: D-004 short closure audit completed

Read all required main/literature and newest U-007/I-008, R-004, D-004.
Accepted H-003 per R-004; O-007 closed. Preserved historical files and all
older handoffs. Inverse hierarchy stopped absent a pointwise arithmetic bridge.

Independently proved T-004 by direct reciprocity/algebra: for ALL positive
g,h, Jacobi(g,4gh-1)=1 and Jacobi(-g,4gh-1)=-1, including even g and
composite moduli; ALL positive switched-A parameters exclude square n.
Normalized BOTH fixed-x branches, proved converses, positive integral
reconstructions and 4xyz=p(xy+xz+yz). Recorded KI-006; no new identity
coverage or pointwise forcing. Undefined screenshot variants not specified.

Found an ancillary false equality in I-008 section 2 using only retained
1009,(a,c,k)=(3,11,8): n-x=756 but c(3ak-4)-a=745. Correct exact
expansion c(3ak-3)-a preserves positivity on the SAME hypotheses; no
narrowing or silent historical rewrite. Target obstruction/separator passes.
Per D-004 record the erratum in a NEW handoff and stop, not a repair hunt.

Authorized R-004 probe rerun only: exit 0, empty stderr, 51243731388 ns;
all eight H-003 hashes PASS and both frozen outputs byte-identical. Same six
restricted-family inputs 193/1009/1129/1201/2521/66529, counts 0/2/2/2/0/0,
two complete schedules agree; no domain extension. Standalone retained audit:
exit 0, empty stderr, 500996385 ns; six positive U certificates, 193 A
certificate, its existing 24-residue complete miss, and false equality checked.
It does not reenumerate other parameter domains; no square scan or new prime.
Python 3.12.3 Linux aarch64, integer arithmetic, mounted paths directly.

Detailed scripts/source/stdout/counts/environment: `experiments/results/004_construction_obstruction/`.
Self-contained NEW [H-004](../handoffs/004_construction_obstruction/README.md)
submitted for flagship review, including explicit erratum and standalone
sibling-only auditor. No network, external evidence, Lean or novelty claim.
No arithmetic implication forcing either branch was established. Route STOPPED
**blocked**; conjecture **unresolved**. Minimal follow-up: review/rerun H-004,
not another existence hypothesis or search campaign.