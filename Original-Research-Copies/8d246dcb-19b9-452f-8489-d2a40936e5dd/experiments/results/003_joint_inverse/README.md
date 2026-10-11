# D-003 results: joint one-extra-element inverse theorem

2026-10-04. **T-003 proved** by an elementary universal cyclic-group
argument in `proof.md`, independently of the finite tests. Prerequisites
are audited in `prerequisite_audit.md`; this supplies a new unconditional
proof of specialized KI-003, not a general Kneser proof. Exact prime-defect
specialization and remaining arithmetic compatibility are in
`arithmetic_specialization.md`.

**Pointwise limitation:** no theorem forces the quotient occurrence count
N=m-2 at any shift; no contradiction between different shifts is proved.
Sparse failures remain untreated. Erdős–Straus remains **unresolved**.
No network, new prime/offset domain, m>9 sweep, Lean or novelty claim.
Older handoffs and historical flagship files are unchanged.

## Reproduction and complete finite domain

Execute mounted workspace scripts directly with Python 3, without -O:

    python3 <absolute-workspace>/flagship/reviews/003_joint_probe.py
    python3 <absolute-workspace>/experiments/scripts/check_joint_inverse.py

The original flagship probe verifies all H-002 hashes and recomputes its
joint diagnostics on exactly the old 2991 pairs, with no added offsets:
5982 binary bounds, 941 prime-defect pairs with -1 in J, 253 joint failures,
106 joint saturation passes (33 beyond the old A-only sufficient test),
14 critical equalities; all PASS. It also checks the fixed-character tests
and the already recorded 118801 counterexample; no existence range added.
The stored `flagship_probe_output.json` is stdout from this rerun.

The standalone independent checker in `check_joint_inverse.py` uses direct
binary-choice enumeration, rather than the original bit-rotation method,
with no project imports or inputs. Its COMPLETE abstract domain is:

- m in {3,5,7,9}, G=C_(2m), length m-2;
- nondecreasing sequences over 1,...,2m-1 excluding m;
- no zero terms, as in the target; excluding m is justified because any
  occurrence m puts 0 and m in T, violating T intersect (T+m)=empty;
- sorting removes order redundancy only: all hypotheses and conclusions
  are invariant under permutation, with multiplicities preserved;
- only even-total generating sequences are expensive-tested. Generation
  is exactly gcd(2m,w_1,...,w_L)=1. These are necessary hypotheses, not
  conjectural pruning. No quotient order or prime search is performed.
- every remaining T is computed by ALL 2^(m-2) binary choices; every
  nonzero translation is tested for stabilization, and every generator
  for the claimed signed-coset pattern. No arbitrary sum cutoff.

| m | Length | Visited multisets | Satisfy all hypotheses | Counterexamples |
|---|---:|---:|---:|---:|
| 3 | 1 | 4 | 0 | 0 |
| 5 | 3 | 120 | 12 | 0 |
| 7 | 5 | 4368 | 30 | 0 |
| 9 | 7 | 170544 | 42 | 0 |
| Total | — | 175036 | 84 | 0 |

Visited count for each m is binomial((2m-2)+(m-2)-1,m-2), asserted
in code. There is no early stopping on successful sequences. The script
also checks all 1644 occurrence-wise critical triples within these eligible
sequences against the four-set lemma; this adds no sequence domain. It
checks the negative regression (1,2,6) in C_10 to guard against replacing
translate-disjointness by mere absence of the involution in T.

`independent_check.json` retains exact stdout, eligible-payload and source
SHA256 digests. `environment.json` retains commands' source paths/hashes,
exit codes, runtimes, stderr, interpreter and OS. Python 3.12.3, GCC 13.3.0,
Linux aarch64, integer arithmetic. Both saved runs exited 0; timed runtimes
were 738844000 ns and 9145259308 ns (including Python subprocess startup).
No floating point is used in mathematical checks.

This is algorithmic separation by the main execution model, not a fresh
independent-agent proof audit. Finite results prove only these four groups;
the complete written argument, not the count, supports the theorem.
A self-contained immutable review package is frozen as H-003 under
`flagship/handoffs/003_joint_inverse/`.