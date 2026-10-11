# D-011 — Accept H-008; audit the clean all-pairs localization T-010

Date: 2026-10-06. Inputs: H-008, R-011, and I-015.

## Decision

Accept H-008 as a correct compressed synthesis within its exact hypotheses. Preserve H-008 and all historical files unchanged. The only substantive follow-up justified now is the direct clean-domain corollary T-010 below; do not manufacture another envelope, identity search, or pointwise-forcing direction.

## Rank 1 — T-010 clean all-pairs square-ratio localization

1. **Precise mathematical claim.** Let c>=1, n>=3 be odd, gcd(c,n)=1, and let 4c/n have a positive integral clean representation. In Clean I, any rational-square pair must be the two n-free denominators (X,Z), and n must be 3 modulo 4. In Clean II, any rational-square pair must be the two n-divisible denominators (Y,Z), and n must be 3 modulo 4. Hence at n=1 modulo 4 every clean representation has all three pairwise ratios nonsquare, even for mixed prime support.
2. **What appears new locally.** T-008 only excludes the specified same-status pair at n=1 modulo 4. T-009 excludes all pairs without clean hypotheses only when every prime factor of n is 1 modulo 4. The cross-status impossibility, including the composite Clean-II case where gcd(k,n) may exceed 1, is not stated in the inspected register. External priority is unresolved.
3. **Smallest useful proof target.** Re-derive the accepted normal forms and check the three unordered ratios in each type. In Clean I, use gcd(k,n)=1 to show a cross square forces n to be an odd square, then use the clean Jacobi sign. In Clean II, use the shared squarefree kernel of n and k and k|u+v; never cancel k modulo n. No computation is needed.
4. **Expected incremental result.** A self-contained structural corollary saying that, at n=1 modulo 4, any square-ratio representation must be non-clean. Combined with T-009, this isolates non-clean representations as the only remaining square-ratio target for mixed-support n=1 modulo 4, while leaving unrestricted solvability untouched.
5. **Main uncertainty.** T-010 may be an implicit consequence of the accepted normalization and may not merit a standalone theorem externally. The proof appears rigorous, but main-model freeze, external priority, and publishability are unresolved.

## Main model’s one concrete next task

Create a self-contained proof-only H-009 (or an equivalent appended theorem record) that audits I-015/T-010 line by line, especially:

- the reduced cross ratios in both normal forms;
- the odd-square Jacobi contradiction in Clean I;
- the squarefree-kernel argument in Clean II;
- the fact that T-010 is necessary/localizing only, not sufficient and not a counterexample.

Then stop. Do not run a search, expand a finite range, restart the inverse hierarchy, or claim new congruence coverage. Any external-priority investigation remains blocked until explicitly authorized under the local offline policy.

## Status boundary

- **proved:** H-008 review; T-010 in the flagship paper derivation, pending main integration;
- **verified computationally:** none;
- **conditional:** none;
- **plausible:** compact-note and T-010 significance;
- **blocked:** external-priority certification and old forcing routes;
- **false:** n=3 modulo 4 as a sufficiency condition for a clean square pair; any universal-solvability inference;
- **unresolved:** main integration, external priority, standalone publishability, and Erdős–Straus.
