# D-005 results — Type-I intrinsic gcd and sharp gap

Sequence 005, 2026-10-04. **Paper proof: proved.** **Retained replay:
verified computationally.** **External priority and full conjecture:
unresolved.** **Pointwise existence bridge: blocked.**

## Mathematical result

For every prime p=1 mod 4 and every positive Type-I solution (exactly one
p-divisible denominator), with smallest denominator X and G the gcd of
all three denominators,

    Legendre(G,p)=-1,  6X<=3p-2G+1.

At p=1 mod 24,

    30X<=15p-14G+1.

Equality iff, up to permutation, G=45t+29, p=672t+433 prime, t>=0,
and denominators are (7G,8G,56pG). At p=433 the triple
(203,232,703192), G=29, attains 6090 on both sides. The complete
self-contained derivation is `proof_audit.md`; the same bytes are frozen
in `flagship/handoffs/005_type_I_gcd_gap/`.

## Exact bounded computation

ONLY the unchanged authorized R-005 probe was run, first at its original
mounted path and then from the self-contained H-005 snapshot. No source
algorithm or input domain was changed. Exact integers, Python 3.12.3,
Linux aarch64; assertions enabled. Original run: exit 0, empty stderr,
686793231 ns. Snapshot run: exit 0, empty stderr, 639550539 ns.

The 2991 retained pairs span 187 retained primes; only the FIRST saved B
witness at each of 955 successful pairs is checked. Zero disagreements,
zero sharp equalities among those witnesses; the one explicit algebraically
derived 433 witness is checked separately. This is not a census of all
Type-I solutions. Both outputs match R-005 except the H-004 subprocess
timing. H-004's retained stdout is byte-identical; all 12 H-002 and 10
H-004 payload hashes pass. All 34 recursive H-005 payload hashes pass.

`authorized_probe_source.txt`, full stdout/stderr, `replay_environment.json`
and `snapshot_replay*` record complete source/version, execution environment,
input hashes and counts. `H005_SHA256SUMS` and `handoff_manifest_check.txt`
record package integrity. `historical_hashes_before.json` records all 70
pre-existing flagship historical files; `final_integrity.json` verifies them
unchanged. The four LIVE records were archived byte-for-byte under
`prior_live_records/` before their requested updates. These archival copies
are not computational inputs.

## Limits and negative findings

No prime interval, offset, group-order or parameter expansion; no network,
Lean, priority check or independent-agent claim. The universal theorem
rests on the written proof, not bounded computation. Character and gap
conditions are necessary only and cannot prune Type II. The discarded
Type-II X<=floor((p+1)/4) claim is **false** at retained p=1009, X=253>252,
and is not an input. Failed old family searches are not conjecture
counterexamples. No new optimization or existence program is proposed.

H-004 accepted R-005; O-008 closed. H-005 is submitted for flagship review,
tracked by O-009; external priority is O-010 **unresolved**.