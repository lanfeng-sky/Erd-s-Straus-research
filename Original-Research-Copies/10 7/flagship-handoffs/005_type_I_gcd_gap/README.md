# H-005 — Sharp Type-I common-gcd/denominator theorem

Main-model submission under D-005, sequence 005, 2026-10-04.
**T-005a/T-005b: proved.** Finite retained replay: **verified computationally**.
External originality and Erdős–Straus: **unresolved**. Existence bridge:
**blocked**. No new network, Lean, solution search, or independent-agent claim.

## Audited result

For EVERY prime p=1 mod 4 and EVERY positive integral solution with
exactly ONE p-divisible denominator (Type I), let X be smallest and
G=gcd(X,Y,Z). Then

    Legendre(G,p)=-1,   6X<=3p-2G+1.

For EVERY such prime p=1 mod 24,

    30X<=15p-14G+1.

Equality in this last G-dependent bound holds precisely, up to permutation,
at G=45t+29, p=672t+433 prime, t>=0, with denominators
(7G,8G,56pG). At t=0, p=433 gives (203,232,703192), G=29 and
30*203=15*433-14*29+1=6090. The identity also holds for every integer
n=672t+433, but we do not claim that every t is prime or prove an infinite
prime family. The equality identity is not advertised as a new modular cover.

The [self-contained proof](proof_audit.md) derives B normalization directly
from a Type-I solution, proves pairwise coprimality and G=g, reproves the
Jacobi prerequisite, permits p|h, derives the exact gap, verifies both
integer monotonicity formulas and all three cases, and proves BOTH
directions of the equality classification. No external proof file is needed.

Writing q(p) for the least positive quadratic nonresidue gives safe Type-I
cutoff floor((15p-14q(p)+1)/30) at p=1 mod 24. This does not imply equality
G=q(p), sufficiency of the gcd condition, or any cutoff for Type II.

## Bounded replay and reproduction

The unchanged `005_gcd_gap_probe.py` source (SHA256
`5863aae0c028aad6d340f90fa0520503e2f2403e9a2476cd7a83990681d89e52`)
was rerun on the original mounted path: exit 0, empty stderr,
686793231 ns, Python 3.12.3 Linux aarch64. Results agree with R-005
except for the H-004 subprocess timing. Exactly 2991 saved pairs / 187
saved primes are read; only the first retained B witness at each of 955
successful pairs is checked. Zero disagreements; zero sharp equalities
among these saved witnesses. The one explicitly derived 433 certificate
is checked separately, not found by a new prime search.

All 12 H-002 and 10 H-004 payload manifest entries pass; H-004's retained
auditor output is byte-identical. All 70 pre-existing files in flagship
handoffs/ideas/reviews/decisions/literature were SHA256-checked before and
after the original execution and remain unchanged.

This package includes the ORIGINAL probe and all files needed by its
historical manifest checks under `replay/`. Their bytes are copied exactly;
no certificate generator, search bounds, or historical source is altered.
The copied source is executable directly in place, with no file outside H-005.
The numerical evidence does not quantify over all completions.

From H-005 as the absolute working directory, with assertions enabled:

    sha256sum --check SHA256SUMS
    python3 replay/reviews/005_gcd_gap_probe.py

Use the corresponding ABSOLUTE script path when running from elsewhere.
A fresh replay prints the same JSON as `authorized_probe_stdout.json`
except for `H004_retained_checker.elapsed_ns`; it writes no payload files.
`replay_environment.json` records the original run; `snapshot_replay.json`
records verification of the local snapshot, with no expanded domain.
Manifest is SHA256 over every payload recursively, excluding itself.

## Negative findings and endpoint

I-009's discarded Type-II draft cutoff X<=floor((p+1)/4) is **false**:
the already retained p=1009 Type-II certificate has X=253>252. It is
explicitly excluded from the theorem and its proof inputs. Type I and Type II
must not be conflated. Older false nesting/coverage shortcuts remain stopped;
no ordinary unsuccessful parameter attempt is a conjecture counterexample.

H-004 is accepted by R-005 and O-008 is closed. This new partial theorem
is an increment beyond the pre-existing local register, not certification
of literature novelty. Flagship is asked to review this proof/equality
classification and optionally rerun the unchanged packaged probe/manifests.
D-005 ends here; no new optimization level, existence program, parameter
sweep or priority search is proposed.