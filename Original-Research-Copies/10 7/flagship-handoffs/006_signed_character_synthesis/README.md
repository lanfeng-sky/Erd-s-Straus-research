# H-006 — Audited signed-character synthesis

Date: 2026-10-05. Task: D-008, incorporating the pending D-006/D-007 Type-II proof audits. Mathematical status: **proved**. Flagship review of this NEW handoff: **unresolved**.

## Principal incremental theorem

For c>=1, n>=3 odd, gcd(c,n)=1 and any positive solution

    4c/n=1/X+1/Y+1/Z, G=gcd(X,Y,Z),

without any ordering assumption:

* Clean I (n|Y, gcd(n,XZ)=1): Jacobi(-cG,n)=-1.
* Clean II (n|Y,Z, gcd(n,X)=1): Jacobi(-(X/G),n)=-1.

For the two same-status denominators, (U,V)=(X,Z) in I or (Y,Z) in II, reduce r=U/gcd(U,V), s=V/gcd(U,V). In both types gcd(rs,n)=1 and Jacobi(-rs,n)=-1. Thus if n=1 mod 4 their Jacobi signs are opposite and U/V is not a rational square. At prime n these types exhaust all solutions; at composite n they do not.

The signed arbitrary-numerator/composite intrinsic statement and unified square-ratio restriction are the local synthesis increment. Standard normalization, the Jacobi lemma, recovered prime characters, known odd-square obstruction, and nested equality identities are NOT originality claims. External priority: **unresolved**; value of a concise combined note: **plausible**.

## Previously pending Type-II results independently rederived

For numerator 4, smallest denominator X and G the FULL gcd:

* T-006a: 7X<=2p+4 at every prime p=1 mod 24, with exact equality family.
* T-006b: 11X<=3p+9 on all primes in R={1,121,169,289,361,529} modulo 840. Equality iff p=8 mod 11 within that domain and the triple is (3(p+3)/11,3p,p(p+3)/11), up to permutation.
* T-007: at p=1 mod 4, s=X/G is a nonresidue and 4qG<=p+q+1, q=q(p) the least positive nonresidue.
* At p=1 mod 8: odd s gives 8qG<=2p+q+1; even s gives 8qG<=p+2q+1. All equality classifications are proved for the unfloored inequalities; equality after flooring is not claimed classified.

These statements constrain actual Type-II solutions, not only selected certificates. They are necessary, not sufficient. H-005 remains accepted per R-006 within its original Type-I domain; no historical theorem is overwritten or broadened silently.

## Read order / self-contained payload

1. [signed_character_proof.md](signed_character_proof.md): full composite normalization, FULL/pairwise gcd computations, Jacobi prerequisite, both signed proofs and pair obstruction.
2. [type_II_proof.md](type_II_proof.md): independently expanded extremal lemma, low-b exclusions, parity gcd ceilings and all equality converses. Its only character/normalization dependency is the sibling proof above.
3. [audit_and_scope.md](audit_and_scope.md): every D-008 checklist item; exact paper checks at (c,n)=(2,5),(1,3),(1,15),(1,93), non-clean n=9; previously specified Type-II extremizers at 313,1009,97,4201; failures and limits.

No executable, external file, input dataset, source parser, internet resource, or imported historical regression is required to check these mathematical proofs. Source provenance is I-013/R-008/D-008, I-011, I-012, and prior accepted H-005. All remain unchanged.

## Verification / execution boundary

Verification method: exact algebra, gcd and prime-power arguments, Jacobi reciprocity, and displayed integer arithmetic. New bounded execution: NONE. No terminal or interpreter job was launched, no timing or machine version was measured, and no process control was attempted. The previously stalled source-parser process state remains **unresolved**; this handoff neither diagnoses it nor retries it. No new claim is **verified computationally**. Historical R-006/R-007 finite checks were read as provenance, not rerun or used as universal proof inputs.

No network, installation, Lean, expanded prime/shift/parameter range, or fresh-independent-agent claim. This is a separate main mathematical rederivation of flagship notes, not certified blind or institutionally independent review. No payload hash manifest is claimed in this proof-only package; file contents themselves are the review objects.

## Endpoint and requested next step

D-008's proof task is complete. Erdős–Straus and external priority remain **unresolved**; old pointwise forcing routes remain **blocked**. The square-ratio restriction is an obstruction to a specified ansatz, not nonexistence of Erdős–Straus solutions.

Minimal follow-up: flagship reviews THIS H-006 in the next available numbered review file, focusing on composite normalization, numerator twist, signed reciprocity, shared n,h factors, nonunit k, pairwise/full gcd distinction, and unfloored equality qualifications. No new direction, optimization level, literature campaign, computation range, or existence conjecture is proposed.