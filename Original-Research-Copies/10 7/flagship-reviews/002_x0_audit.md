# R-002 — Accept H-001; audit its limits and attack the next obstruction

Sequence: 002; 2026-10-03. Research question: is the fixed-x0 result correct and complete, and what precise mathematical obstacle remains? Reviewed immutable snapshot: `handoffs/001_x0/{README.md,proof.md,audit_x0.py}`. Also read all current main files and previous numbered records. No handoff or main-model report was edited.

## 1. Verdict on submitted mathematics: accepted — proved

KI-001 is correct as quantified: for every prime p=1 mod 24, x0=(p+3)/4 permits a positive integral completion iff x0 has a prime divisor q=2 mod 3.

Audit details which the snapshot abbreviates:

- x0=6k+1 and p=1 mod 3, so b=px0=1 mod 3 and 3 divides neither factor.
- From 3yz=b(y+z), d=3y-b obeys dz=by>0, hence d>0; similarly e>0. The positive factor pair satisfies de=b², d=e=2 mod 3.
- If no q=2 mod 3 divides x0, primality of p ensures EVERY prime factor of b is 1 mod 3. This primality use cannot simply be removed for arbitrary composite p=1 mod 3. Necessity follows.
- Conversely q|x0 gives e=b²/q integral, and qe=1 mod 3 forces e=2 mod 3. Thus both denominators (b+q)/3 and (b+e)/3 are integral and positive. The expansion in the snapshot is correct.
- Swapping y,z permits d<=e; then d<=b exactly. Conversely all positive d|b² with d<=b and both residue conditions give all completions up to swapping. There is no hidden bound on z.
- y>b/3>x0 because p>3, so adding x0<=y to the checker does not discard a valid completion in this domain.
- The bounds b/3<y<=2b/3 and z<=(b+b²)/3 are sound. No algebraic, sign, or integrality defect found.

Status does not include novelty or Lean formalization. The assertion in the report that no other x was searched applies to the submitted D-001 investigation, not to the new flagship work below.

## 2. Submitted program: accepted within its exact range

Ran the immutable script directly from its mounted workspace path under Python 3, without -O. Tool returned exit code 0:

    PASS selected=273 successes=87 failures=186 disagreements=0

The sieve is complete through 100000. `factor` scans every prime through the original square root; although inefficient in general, it is correct here, and the leftover if >1 is prime. For b=p(p+3)/4, sqrt(b)<50001 at the stated bound, so indexing the 100000-entry primality table is safe. `divisors_squared` takes every exponent 0,...,2e and forms their Cartesian products; this is complete. The checks at 1009 and 1201 pass.

**Evidence caveat, not rejection:** the two paths in the submitted script share its sieve and factor routine. The snapshot does not include the main workspace's detailed CSVs. Thus running it verifies a self-contained recomputation, not byte-for-byte integrity of inaccessible archived records. No claim of having inspected those external files is made.

To reduce common-mode risk, flagship implemented `002_structural_probe.py` independently: trial-division primality rather than a sieve; dynamically terminating factorization; explicit primality and product checks for every factorization; divisors with uniqueness/cardinality checks; complete factor pairs. It reproduced the exact 273/87/186 split with zero disagreements. This is a separate implementation by the reviewing model, not a proof-assistant build or independent fresh sub-agent.

## 3. New flagship finite diagnostics — verified computationally

These are NOT part of H-001 and do not change it.

| Test | Exact scope | Result |
|---|---|---|
| Vary x | The 186 x0 failures; allow t=0,...,63, stop at first hit | 620 actual pairs; all 186 solved; largest first t=7; compact A/B vs full factor enumeration: zero disagreements |
| First-hit branches | Same 186 stopping points | 175 both, 9 B-only, 2 A-only |
| Preceding failure types | Same 434 failed pairs | 377 single-prime quadratic obstructions, 37 other subgroup obstructions, 20 bounded-exponent obstructions |
| Full compact small-defect test | Same 186, a<=floor(sqrt(p)) | All have a hit; finite only |
| Prime defects | Same 186, prime a=3+4t, t<=63 | All have a hit; finite only |
| Switched family | Same 186, g=1,k<=16, first hit | 179 solved, seven window failures |
| Saturation sufficient condition | Same 186, prime a=3 mod 4 up to sqrt(p) | 72 pass for some a, 114 do not |
| Eight-offset falsification | Selected primes above 100000; cap 10^6, stop at first failure | p=118801 fails t=0,...,7; first later hit t=14; 46 selected primes visited, not full interval |

Exact outputs and all explicit counterexamples/formulas are described in I-002 through I-004. Sources: `002_structural_probe.py`, `002_switched_probe.py`; standard-library Python 3.12.3, Linux aarch64. Observed algorithm runtimes were 0.262731s and 0.156810s respectively (not tool startup). A cyclic-group sanity test with retained source `002_group_sanity.py` checked 416931 generating sequences, of which 4569 satisfy the saturation bound, without disagreement. All mathematical checks use arbitrary-precision integer arithmetic; timings alone use floating point.

Reproduction, with W the absolute attached flagship path:

    python3 "$W/handoffs/001_x0/audit_x0.py"
    python3 "$W/reviews/002_structural_probe.py"
    PYTHONDONTWRITEBYTECODE=1 python3 "$W/reviews/002_switched_probe.py"
    python3 "$W/reviews/002_group_sanity.py"

No script writes datasets or modifies the handoff. The switched script imports the local structural helper and is therefore not algorithmically independent of it. Its direct final integer certificates are still valid independently of how candidates were found.

## 4. Adversarial findings for the new ideas

- **Proved, elementary:** I-002 exactly reduces fixed-x completion to two divisor conditions on x². Both branches are required; keeping only the two-p-divisible-denominator family would discard observed witnesses.
- **False:** generated-subgroup membership alone guarantees completion. p=1201,x=303 generates the full unit group mod 11 but its bounded divisor-ratio set misses both targets.
- **False:** the eight offsets working through 100000 are a universal construction. p=118801 refutes it.
- **Proved conditional on a named external theorem:** I-003 derives a saturation condition and a subgroup-concentration alternative using finite Kneser. Only the theorem statement was checked in a secondary reference; primary proof audit remains open. This dependency is separate from the elementary results.
- **False:** that sufficient saturation condition always occurs at a prime defect <=sqrt(p). There are 114 misses in the exact test set, beginning with 1129 and 1201.
- **Proved, elementary:** I-004's switched-factor identity reconstructs positive integral triples; unrestricted g,k recovers branch A under its stated normalization. Its g=1 restriction is not a completeness theorem.
- **False:** x0 failure forces g=k=1 switched success; p=1129 refutes it. Also g=1,k<=16 fails on seven explicitly listed primes.

## 5. Strongest established result and exact gap

**Strongest submitted and accepted result:** the universal fixed-x0 iff criterion KI-001, plus its independently reproduced finite classification.

**Strongest new elementary result this round:** for prime p=1 mod 4 and p/4<x<p, a=4x-p, fixed-x completion is equivalent to

    exists c|x²: a|(c+x) OR a|(4c+1),

equivalently R_x intersects {-1,-p}; explicit denominator formulas are given in I-002. Taking x in the necessary smallest-denominator interval gives an exact finite equivalent reformulation of the prime problem, not a proof of existence. The switched-factor theorem is a separate constructive reparameterization of one branch.

**Exact remaining gap:** prove that for every target prime at least one admissible x has that intersection, or supply another fully proved covering mechanism. Neither subgroup generation, the tested saturation condition, a constant offset bound, nor the tested switched family achieves this. The complementary modulo-840 coverage and reported large computational bounds remain unaudited local dependencies and were NOT used to infer a global proof.

Next action: execute D-002's bounded structural tasks. Overall Erdős–Straus status: **unresolved**.