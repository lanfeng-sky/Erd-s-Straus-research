# H-009 — Clean all-pairs square-ratio localization

Assignment D-011, 2026-10-06. One proof-only audit of I-015/T-010, following R-011's acceptance of H-008. H-001 through H-008 and all historical ideas, reviews, decisions, literature and experiment records are unchanged.

## Result — proved

Let c>=1, n>=3 odd, gcd(c,n)=1 and 4c/n=1/X+1/Y+1/Z in positive integers.

- Clean I (n|Y, gcd(n,XZ)=1): a rational-square denominator pair, if present, is necessarily (X,Z), and n=3 modulo 4.
- Clean II (n|Y,Z, gcd(n,X)=1): such a pair is necessarily (Y,Z), and n=3 modulo 4.

Both cross-status pairs are impossible at EVERY odd n within each clean type. At n=1 modulo 4 every clean representation has ALL THREE unordered pairwise ratios nonsquare, including mixed prime support and repeated prime factors. Therefore any square-pair representation there must be non-clean under every permutation.

The composite Clean-II proof uses the shared squarefree kernel of n and k when nk is square, and k|u+v. It never cancels k modulo n. The Clean-I proof uses gcd(k,n)=1, the resulting odd-square n and J(-cG,n)=-1. Same-status squares force the modulo-four sign in both types.

## Self-contained payload

- [proof.md](proof.md): exact statement, independently rederived normal forms and full/pairwise gcd, specialized Jacobi lemma, both character proofs and all six pair cases, with d=1 and nonsquarefree moduli included.
- [audit_and_scope.md](audit_and_scope.md): I-015 line mapping, false extrapolations, inherited exact scope witnesses, strict ledger and review checklist.

No outside dataset, executable, parser, historical proof file or external source is needed to review the mathematics. Standard quadratic reciprocity, its supplementary laws and unique factorization are identified inputs. These standard ingredients are not novelty claims. The cross-status/all-pairs corollary extends the inspected local register; external priority is **unresolved**, certification **blocked** by offline policy, and standalone significance **plausible** rather than certified publishability.

## Quantifier boundary

T-010 localizes possible square pairs; it is not sufficient to construct a representation and is not a nonexistence theorem for Erdős–Straus. Clean types need not exhaust composite solutions. n=3 modulo 4 does not force a square pair in every clean representation or ensure arbitrary-c solvability. At c=1, however, the familiar identity (t,2nt,2nt), t=(n+1)/4, DOES furnish some clean-II equal-pair representation for each such n. The audit makes this distinction explicit rather than repeating an ambiguous converse denial.

## Evidence and review

- Ordinary symbolic proof and exact PAPER arithmetic only: mathematical statements **proved**; main integration O-019 **proved**.
- R-011/D-011 accept historical H-008; O-018 **proved** in current live records. Acceptance of I-015's paper theorem is not a review of this new H-009 presentation: O-020 **unresolved**.
- No new **verified computationally** claim; no **conditional** dependency. No search, finite range, replay, heuristic sample, conjecture, Lean, network, hash validation or fresh agent review.
- Erdős–Straus, external priority and standalone publishability **unresolved**. Old forcing routes **blocked**.

Companion evidence-boundary record: `experiments/results/009_clean_square_pair_localization/` in the main workspace, not a dependency of this package. No numerical runtime/range, Lean version or repository commit is applicable to the proof; no environment version was measured.

D-011 is complete with this submission. Minimal follow-up: flagship reviews only the NEW H-009 proof/presentation in a new numbered review, especially the reduced cross ratios, unit odd-square Jacobi contradiction, squarefree-kernel parity, nonunit k and converse quantifiers. Then stop. No identity hunt, pointwise-forcing restart or external-priority campaign is authorized.