# Main Research Report

## Current state — 2026-10-04, D-004 closure complete

H-001 accepted R-002; H-002 accepted R-003; H-003 accepted
[R-004](reviews/004_inverse_and_construction_audit.md). All unchanged.
O-007 closed. Inverse hierarchy STOPPED without an arithmetic bridge.
New [H-004](handoffs/004_construction_obstruction/README.md) submitted:
T-004 **proved**; universal normalized U-007 coverage **false**; one ancillary
I-008 equality **false** and explicitly corrected on the same domain.
Pointwise forcing **blocked**; Erdős–Straus **unresolved**. No novelty,
fresh-agent proof review, network or Lean claim. General Kneser remains
unaudited and unnecessary to specialized KI-003's elementary proof.

## New closure theorem: switched obstruction and fixed-x separator

For EVERY positive g,h, Jacobi(g,4gh-1)=1 and Jacobi(-g,4gh-1)=-1.
For EVERY positive n,g,u,v,k with u+v=k(4guv-n), put a=4guv-n>0:

    n=(4guk-1)a-4gu², gcd(n,4guk-1)=1,
    Jacobi(n,4guk-1)=-1.

Thus NO positive square n belongs to this entire switched family, including
even g, composite moduli and u>1. Not a nonexistence theorem for the equation.
For prime p=1 mod 4 and p/4<x<p, normalize a witness C|x² as
x=guv,C=gu²,gcd(u,v)=1. With a=4x-p the exact branches are:

    A: k=(u+v)/a; p=(4guk-1)a-4gu²; Legendre(4guk-1,p)=-1.
    B: k=(pu+v)/a; 4guk-1=ph; hv=u+k; Legendre(4guk-1,p)=0.

Positive integer triples (guv,pgku,pgkv) and (guv,pguk,gvk) respectively
satisfy 4xyz=p(xy+xz+yz). Both normalized converses and gcd checks are
in [H-004's self-contained proof](handoffs/004_construction_obstruction/proof_audit.md).
This is fixed-x organization, NOT existence forcing; k generally differs.

Normalized U-007 n=a(4ck-1)-4c is exactly u=1/nested A. Complete bounds
ck<=(n+3)/8 for n=1 mod 4 and the r=M-1 boundary are audited. At prime
193 the complete 24-residue certificate excludes this family, while ordinary
A gives (50,1930,4825). Undefined screenshot variants remain unspecified.
Explicit new erratum: I-008 says n-x=c(3ak-4)-a; retained 1009 witness
has n-x=756 vs claimed 745. Correct equality c(3ak-3)-a>=2a-3>0
preserves positivity without narrower assumptions. Historical files untouched.

Authorized R-004 probe ONLY rerun: all H-003 hashes PASS, both outputs
byte-identical; same six n={193,1009,1129,1201,2521,66529}, full-family
witness counts 0/2/2/2/0/0 with both complete schedules agreeing. Exact
Python 3.12.3 Linux aarch64; exit 0, empty stderr, 51243731388 ns.
Standalone retained checker exit 0, 500996385 ns: six positive certificates,
193 A certificate and existing 24-residue miss, plus erratum verified. It does
not reenumerate other ranges. No new squares/primes/offsets/groups/parameters.
Full scripts/source/output/counts/environment in H-004 and
`experiments/results/004_construction_obstruction/`. Written proof, not tests,
establishes the universal character obstruction. No new existence range.

## Accepted theorem: exact one-extra-element inverse structure

For EVERY odd m>=3, let a nonzero generating list w_1,...,w_(m-2)
in C_(2m) have subset-sum set T. Assume Stab(T)={0},
T disjoint from T+m, and even total. Then for a generator g EXACTLY ONE
occurrence is +/-2g and every other occurrence is +/-g. For m=3 the
hypotheses are impossible. m need not be prime; multiplicities retained.

[Complete proof](handoffs/003_joint_inverse/proof.md): binary period
persistence and parity force |T|=m=L+2. Put an incompatible pair first;
its four sums consume the only excess unit. Every third term must extend
that set by exactly one. Orbit-run analysis makes it a four-term progression,
except potentially a full order-three coset plus singleton. Reflection
forces that singleton an involution away from the full coset, violating
disjointness. The progression's two reflections identify the terms as
+/-w and +/-2w. Whole-list generation derives full order, and another
doubled occurrence would require 1=+/-2 or +/-4 mod 2m>=10. Thus exactly
one. No external inverse theorem or computed classification is assumed.

## Elementary replacement and arithmetic scope

[Prerequisite audit](handoffs/003_joint_inverse/prerequisite_audit.md):
for ANY finite abelian group and binary product S, actual K=Stab(S),
|S|>=|K|(N+1), where N counts occurrences outside K. In G/K every
nonidentity step grows, or a period persists to the final aperiodic set.
This closes O-005 for specialized KI-003 only, preserving H-002/L-002.

For EVERY prime p=1 mod 4 and integer p/4<x<p, set a=4x-p,
D={d mod a:d|x}, R=DD^{-1}, S=D union pD. KI-002's exact unordered
fixed-x criterion remains A: c=-x mod a or B: 4c=-1 mod a, c|x^2.
With E=x^2/c, A gives y=p(x+c)/a,z=p(x+E)/a; B gives
y=p(x+pc)/a,z=(px+E)/a. H-003 re-audits integrality, positivity,
p-adic completeness and **4xyz=p(xy+xz+yz)** self-contained.
Equivalently A or B iff S meets -S; inverse closure is not product closure.
Running x through (p+3)/4,...,floor(3p/4) is an exact existence
reformulation, not a forcing theorem. No ordering filter in fixed-x iff.

When a=ell is prime and -1 in J=<q:q|x,p>, a failure has odd actual
K=Stab_J(S), |J/K|=2m, m odd. Delete occurrences in K. The remaining
N occurrences generate J/K, have aperiodic subset sums avoiding the
involution in their DIFFERENCE set, and even total because px=4x^2 mod ell.
Hence N+1+indicator(N odd)<=|T|<=m. At N=m-2, T-003 gives ONE
g^{+/-2}K occurrence and all others g^{+/-1}K, with |S|=|J|/2.

[Arithmetic specialization](handoffs/003_joint_inverse/arithmetic_specialization.md)
records p exceptional, ordinary, OR deleted in K. For pK=gamma^beta,
xK=gamma^A, 4K=gamma^delta, beta=delta+A and delta even. All three
patterns remain compatible with parity. **No contradiction is proved.**
Nothing forces N=m-2 (or saturation) at any shift. Sparse N remains untreated.

## Authorized exact tests — no enlarged range

Reran `reviews/003_joint_probe.py`: PASS, all H-002 hashes, original
2991 pairs, 5982 binary bounds, 941 prime-defect pairs with -1 in J,
253 joint failures, 106 joint sufficient passes (33 beyond old A-only
sufficiency), 14 critical equalities. These are pairs, not new solved primes.

New standalone `check_joint_inverse.py` uses ALL binary subset choices,
not bit rotation. Complete abstract domain: nondecreasing nonzero
non-involution lists, length m-2, m in {3,5,7,9}. Sorting is permutation
symmetry; involution exclusion follows from disjointness. Even-total and
gcd generation are exact hypothesis filters. All translation periods and
all generators checked; no sum cutoff or early success stopping.

| m | Length | Visited multisets | Eligible | Counterexamples |
|---|---:|---:|---:|---:|
| 3 | 1 | 4 | 0 | 0 |
| 5 | 3 | 120 | 12 | 0 |
| 7 | 5 | 4368 | 30 | 0 |
| 9 | 7 | 170544 | 42 | 0 |
| Total | — | 175036 | 84 | 0 |

Also 1644 critical triples within SAME eligible lists, and negative C_10
regression (1,2,6): no involution among sums does NOT mean disjointness.
Both scripts exit 0. Python 3.12.3 Linux aarch64, exact integers. Source
hashes, full stdout, counts, bounds, limitations and environment are inside
H-003 and `experiments/results/003_joint_inverse/`. Mounted H-003 rerun
matches saved stdout byte-for-byte; eight payload hashes PASS. Initial
freeze-wrapper attempt hit H-001's absent manifest after creating H-003;
verification was completed without changing H-003 and recorded locally.
The complete WRITTEN proof, not this finite test, establishes T-003.

## Accepted finite legacy results and stopped shortcuts

H-002 exact domain remains 186 x0-failure primes at t=0,...,15 plus
118801 at t=0,...,14: 2991 pairs; both/A-only/B-only/neither counts
757/101/198/1935, zero full factor-pair disagreements. Seven g=1 switch
misses succeed with both g,k allowed, 147 tested candidates; no universal
bound inferred. Full certificates and independent scanner accepted R-003.

Stopped, not repaired: next-shift nonquadratic forcing (p=1129,t=12,13);
two-prime-defect forcing (p=2521,ell=11,19); least-nonresidue q-window
forcing (p=118801,q=13, all t=0,...,12 fail). The t=4 escape x=29705,
a=19 has full H but misses both targets. First hit remains t=14, not a
conjecture counterexample. Reciprocity escapes one character obstruction,
not sparse bounded-exponent misses. No wider hunt.

## Review request and stop

Flagship: review NEW H-004's obstruction/separator and explicit ancillary
erratum, then run its sibling-only retained auditor and manifest check.
H-004 needs no file outside flagship (indeed only sibling payloads at runtime).
All historical handoffs/numbered files preserved. O-007 closed R-004;
O-008 requests closure review ONLY. Modulo-840 complementary coverage
remains unaudited; no task here used it as a proof input.

D-004 ends here as intended: route STOPPED **blocked**. A nonresidue M
does not force M|(p+4gu²); p|M does not force (M/p)|(u+k).
No new hypothesis, search, inverse level or literature task is proposed.
The exact unsolved goal remains: for EVERY target prime, force SOME
admissible x with R intersecting {-1,-p}, or another proved construction.
Restart requires a precise pointwise implication genuinely beyond the
known parameterization, with universal quantifiers and a first falsification test.
