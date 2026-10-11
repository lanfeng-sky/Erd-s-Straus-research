# D-004 closure results

2026-10-04. **T-004 proved:** universal Jacobi obstruction for the full
positive switched-A family, and exact normalized fixed-x A/B character
separator. **False:** universal normalized U-007 prime coverage; also the
auxiliary n-x equality displayed in I-008 section 2. Its exact correction
and the retained counterexample are in `proof_audit.md`. No extra hypotheses
were invented. Overall conjecture unresolved; existence route blocked.

Only authorized `flagship/reviews/004_audit_probe.py` was rerun. It checked
unchanged H-003 payload hashes and reproduced both frozen outputs exactly,
then tested precisely n={193,1009,1129,1201,2521,66529}. No new primes,
squares, offsets, groups or parameter ranges. Source snapshot:
`authorized_probe_source.txt`; full stdout/stderr and `environment.json`
retain hashes, command, exact scope, interpreter, architecture and timing.

| n | Complete (c,k) candidates | Complete h candidates | U witnesses |
|---|---:|---:|---:|
|193|60|24|0|
|1009|450|126|2|
|1129|513|141|2|
|1201|553|150|2|
|2521|1314|315|0|
|66529|52762|8316|0|

Both enumeration schedules agreed. Their COMPLETE restricted-family bounds
are proved in the audit: n=1 mod 4 forces a>=3, hence ck<=(n+3)/8 and
k<=(n+4c+3)/(12c). The h method has at most one residue candidate c,
including the essential r=M-1 boundary. No early stopping or unsolved
candidate discarded; trial division independently checks the six primalities.
These results are NOT universal coverage and are NOT conjecture counterexamples.

Python 3.12.3/GCC 13.3.0, Linux aarch64/glibc 2.39, directly mounted Android
workspace. Authorized wrapper exit 0, empty stderr, elapsed 51243731388 ns.
All mathematical arithmetic is exact integers. No external source, Lean,
new agent, novelty claim or range expansion.

Standalone `check_retained.py` uses no project imports and only sibling
payloads. It checks all six retained positive U certificates, the non-nested
193 A certificate, source/output provenance, and the 24 already retained
residue cases giving a complete U no-witness certificate at 193. It does
NOT reenumerate 2521/66529 or the other (c,k) ranges; those results are
provenance from the authorized two-schedule generator, whose source and
stdout are supplied. It counterchecks the false auxiliary equality on the
existing 1009 witness. No new domain is searched.

The written reciprocity argument, not these certificate checks, proves the
universal square obstruction. The A/B separator applies to prime p=1 mod 4
and p/4<x<p; the complete switched-family obstruction also covers composite
n and unnormalized u,v. Neither forces a certificate for any arbitrary prime.

Freeze under `flagship/handoffs/004_construction_obstruction/`; flagship may
run its standalone auditor. Then STOP pending a genuine pointwise arithmetic
bridge, per D-004. H-003 accepted R-004; historical handoffs remain untouched.
