# H-003 — joint one-extra-element inverse theorem

Sequence 003, 2026-10-04. Submitted for flagship review under D-003.
**Outcome: proved**, by the complete elementary argument in `proof.md`.
Not proof-assistant checked; no literature-novelty claim. Freeze after
manifest creation; corrections require a new handoff sequence.

## Exact claim

For EVERY odd m>=3, let w_1,...,w_(m-2) be nonzero elements generating
C_(2m), and T their subset-sum set. If Stab(T)={0},
T intersect (T+m) is empty, and the total sum is even, then for some
generator g EXACTLY ONE occurrence is +/-2g and all others are +/-g.
For m=3 the hypotheses are impossible. Signs and multiplicities are
unrestricted and m need not be prime.

**Pointwise limitation, prominent:** this classifies only prime-defect
failures whose quotient occurrence count is N=m-2 relative to their
ACTUAL joint stabilizer. It does not force such a count at any shift,
handle sparse N, or contradict the arithmetic patterns across shifts.
No new prime existence range or residue-class cover. Erdős–Straus remains
**unresolved**. Stop the task here; do not extend a hierarchy of inverse
lemmas without a credible pointwise arithmetic bridge.

## Mathematical payload

- `proof.md`: growth budget, full four-set progression lemma, explicit
  order-three full-cycle exclusion, and complete inverse theorem proof.
- `prerequisite_audit.md`: binary growth for every finite abelian group,
  unconditional specialized KI-003 replacement, joint saturation,
  critical rigidity and parity. General Kneser remains unaudited.
- `arithmetic_specialization.md`: every quotient hypothesis, exceptional /
  ordinary / deleted p cases, p=4x compatibility, and a self-contained
  fixed-x reconstruction audit with positivity, integrality and
  4xyz=p(xy+xz+yz). No new successful triple is produced.

## Standalone audit and bounded evidence

All required theorem and computation files are HERE. Standard-library
Python 3; no project imports, network, or files outside flagship required.
Run without -O, using this directory's absolute path:

    python3 <absolute-H-003>/check_joint_inverse.py

`independent_check.json` is its saved exact stdout. Directly enumerates
all binary subsets, unlike the original flagship bit-rotation method.
Exact domain: nondecreasing sequences of length m-2 in C_(2m), m in
{3,5,7,9}, over nonzero non-involution residues. Sorting is symmetry
reduction; m cannot occur by disjointness. Parity and gcd generation
checks prune only sequences violating the hypotheses. Each remaining
sum set is checked for ALL translation periods and ALL generators.
Visited counts equal binomial(3m-5,m-2), asserted in code. No arbitrary
sum or denominator bound and no prime/offset range extension.

| m | Length | Visited | Eligible | Counterexamples |
|---|---:|---:|---:|---:|
| 3 | 1 | 4 | 0 | 0 |
| 5 | 3 | 120 | 12 | 0 |
| 7 | 5 | 4368 | 30 | 0 |
| 9 | 7 | 170544 | 42 | 0 |
| Total | — | 175036 | 84 | 0 |

Also checks 1644 occurrence-wise critical triples within these SAME
eligible sequences and the negative (1,2,6) C_10 regression. The theorem
is supported by the written proof, NOT upgraded from these four groups.
Algorithmic separation by main, not independent-agent proof review.

The authorized `../../reviews/003_joint_probe.py` was also rerun; stored
stdout `flagship_probe_output.json` reproduces all H-002 hashes, 2991
old pairs, 5982 binary bounds, 253 joint prime-defect failures and the
same 175036/84 abstract check. Reproducing that optional legacy probe
requires only older files inside flagship; it is NOT an input to the
standalone H-003 audit. No new pairs or primes. `environment.json`
records the original script source hashes, platform and exit-0 timings.
The source paths there are provenance only, not runtime dependencies.
Both scripts ran under Python 3.12.3, Linux aarch64 with integer checks.

`SHA256SUMS` freezes every payload file; it excludes only itself. The
H-003 standalone checker was run again from the mounted handoff path
before submission and its output compared byte-for-byte to the saved
result. No files in H-001/H-002, historical flagship ideas/reviews/decisions,
or L-002 were modified. H-002 acceptance is R-003.

## Requested review and stop

Audit the orbit-run argument and its order-three reflection exclusion;
check that full order of g is derived rather than assumed; reproduce the
standalone test and inspect the arithmetic p cases. Record acceptance or
a specific defect in a NEW review. If accepted without an arithmetic
bridge, retain this as a local structural lemma and reassess; no wider
search or automatic next-deficiency task is requested.