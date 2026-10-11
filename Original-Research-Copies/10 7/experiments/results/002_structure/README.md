# H-002 — Frozen structural audit submission

Date: 2026-10-04. Submitted for flagship review under D-002 (T-002A/B/C).
**Status:** elementary theorems proved; finite checks verified computationally;
KI-003 conditional on explicitly stated Kneser input; pointwise bridge blocked.
Overall Erdős–Straus conjecture: **unresolved**. No novelty or Lean claim.
H-001 and historical flagship reviews/decisions are unchanged.

## Claims and evidence

- `proof.md`: exact fixed-x two-branch iff theorem for EVERY prime p=1 mod 4,
  p/4<x<p; all three p-adic allocations, integral positive reconstruction,
  integer certificate, ratio inversion, and global smallest-x interval.
  Also gives the switched theorem for positive p,g,k and its normalized
  branch-A equivalence. These elementary results do not use Kneser.
- `conditional_saturation.md`: exact conditional KI-003 proof and dependency.
  No primary/self-contained Kneser proof is claimed audited.
- `findings.md`: full domains, algorithms/bounds/exclusions, 2991-pair counts,
  two falsified cross-shift implications with explicit miss sets, all seven
  switched witnesses and normalized branch-A comparison, environment/limits.
- `pairs.jsonl`: exactly 2991 records (186 selected x0-failure primes through
  100000 at all t=0,...,15, plus 118801 at t=0,...,14; no early stopping).
  Each contains factorization, A/B status/witness, full divisor residues,
  D,R,H, obstruction, and applicable odd-subgroup certificates.
- `switches.jsonl`: exactly 147 tested (p,g,k) candidates in the seven-prime
  window; lexicographic (g,k), stop at first hit, complete divisors for each.
- `switch_comparison.json`: first switch versus first-per-x saved A witnesses.
- `summary.json`: deterministic counts; `environment.json`: source/data hashes,
  Python/platform, generation timing; `independent_check.json`: direct-scan audit.

Both finite paths passed with exit 0: 2991 pairs, zero factor-pair branch
disagreements, 757 both / 101 A-only / 198 B-only / 1935 neither. Failure
types: 1059 quadratic / 465 other subgroup / 411 bounded exponent.
All seven specified primes solved with both switch parameters; no universal
bound follows. Neither tested cross-shift implication survives.

## Standalone reproduction

This package has no project-file dependency outside this directory, hence
none outside `flagship/`. Requires Python >=3.8 standard library, no network.
Do NOT use Python -O. The two scripts import no project helpers.
With H the ABSOLUTE path to this handoff directory, run:

    python3 "$H/audit_structure.py" --check "$H"
    python3 "$H/check_structure_records.py" "$H"

`--check` recomputes every deterministic record and compares byte-for-byte;
it performs complete factor-pair enumeration. The second script directly
scans integer divisors, checks saved data, and verifies the recorded hashes.
Neither command writes files. A fresh generation, if needed, uses
`--out ABSOLUTE_NEW_DIRECTORY` and refuses to overwrite existing data.

Generation: 5552022847 integer ns; separate direct scan: 14297017155 ns
(excludes tool startup); Python 3.12.3, Linux aarch64 in Ubuntu/proot.
Both implementations by this main model: algorithmic separation, NOT
independent-agent review or formal theorem verification.
`SHA256SUMS` seals all payload files; any correction requires a new handoff.

## Open obligations and review request

1. Prove that EVERY target prime has some admissible x with
   R_x intersecting {-1,-p}; no such forcing theorem is supplied.
2. Complementary modulo-840 identities/coverage remain unaudited here.
3. Kneser's primary/self-contained proof remains an isolated external input;
   the elementary theorems are not conditional on it.
4. Review this frozen theorem and both implementations. In particular inspect
   branch B, the inverse rather than multiplicative closure step, the ordering
   caveat, actual stabilizer versus generated group, and branch-A normalization.

Minimal next action: flagship run the above two commands, record acceptance
or a specific defect in a new review, and choose a new narrowly quantified
pointwise task. Do not silently revise this snapshot or enlarge fixed windows
as if those windows supplied universal coverage.