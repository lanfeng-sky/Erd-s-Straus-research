# H-009 — Line audit, scope and strict ledger

D-011 / I-015 audit, 2026-10-06. The proof is entirely in [proof.md](proof.md). All examples below are inherited exact paper checks, not a numerical search.

## I-015 line-by-line audit mapping

| I-015 lines | Claim checked | Main derivation | Status |
| --- | --- | --- | --- |
| 13–33 | Odd n, gcd(c,n)=1, clean definitions; conditional localization within an actual representation | proof §1 | proved |
| 39–45 | Clean-I normalization with full G, pairwise-coprime u,v,k and gcd(uvk,n)=1 | proof §2, D,E factorization and prime-power allocation | proved |
| 47–51 | Reduced same-status u/k and J(-uk,n)=-1 force n=3 mod 4 if square | proof §§3.2,4 | proved |
| 53–59 | Both reduced cross ratios; square cross pair forces odd-square n, contradicting unit J(-cG,n)=-1 | proof §4 | proved |
| 63–71 | Clean-II normalization and same-status u/v; gcd(k,n)=1 is not required | proof §§2,3.3,5 | proved |
| 73–85 | Cross pair v/(nk); shared squarefree kernel; k divides u+v; Jacobi contradiction | proof §5, with exponent-parity kernel definition and d=1 included | proved |
| 87–93 | Symmetric cross pair u/(nk) | proof §5, -v local square and J(-uv,n) contradiction | proved |
| 95–122 | Precisely scoped extension of the inspected local register | proof §6; this scope record | proved |

No failed implication was found in I-015's mathematical case analysis. Two useful explicit refinements of presentation are retained: use w,t rather than reusing a=4cX-n in n=d w^2; and define the squarefree kernel as the primes with ODD exponent, not all primes dividing n. The kernel may be 1 and may share prime factors with w.

## Failure modes ruled out, not new research routes

- **false:** gcd(k,n)=1 in every Clean-II normalization. The inherited n=15,(4,90,180) has G=2,u=1,v=2,k=3,a=1 and gcd(k,n)=3. Its reciprocal sum is (45+2+1)/180=4/15. Correct cross ratios are 2/45 and 1/45; the kernel proof, not cancellation of k, covers this case.
- **false:** replacing the squarefree kernel by the radical and assuming n=rad(n)*w^2 for every odd n. Unique factorization uses exponent parity. No such invalid decomposition is a proof step.
- **false:** n=3 mod 4 forces a square pair in EVERY clean representation. At n=7 take Clean I (X,Y,Z)=(3,14,6), with G=1,u=1,v=3,k=2 and a=5. The exact sum is (14+3+7)/42=4/7; gcd(7,3*6)=1. Ratios 3/14,1/2,7/3 are nonsquares (respectively an odd 3-, 2-, or 7-valuation). This valid representation refutes a universal-over-representations converse, not Erdős–Straus.
- **false:** n=3 mod 4 alone suffices for a square-pair representation for arbitrary c coprime to n. For c=2,n=3, no representation of 8/3 exists: at most one denominator 1 gives sum at most 2; exactly two denominators 1 would require a reciprocal 2/3; three give 3. This is not an Erdős–Straus counterexample, whose numerator is 4.
- **proved:** at c=1 there IS some clean-II equal-pair representation for every n=3 mod 4, namely (t,2nt,2nt), t=(n+1)/4. Thus the shorthand “n=3 mod 4 is not sufficient” in I-015/R-011/D-011 must be read with the preceding quantifiers: not a guarantee in a given representation, and not an arbitrary-c existence condition. The standard c=1 existential statement is not false. Historical files are not rewritten.

## Exact scope checks

1. **Allowed same-status square pair.** At n=3,c=1, (1,6,6) is clean II and 1+1/6+1/6=4/3. Here G=u=v=1,k=2; Y/Z=1. Cross pairs have ratio 1/6 and are nonsquare. T-010 localizes the actual square pair correctly.
2. **Clean mixed-support n=1 mod 4.** At n=93,c=1, (35,6510,70) is clean I: (186+1+93)/6510=280/6510=4/93 and gcd(93,35*70)=1. Here G=35,u=v=1,k=2,a=47. Ratios X/Z=1/2, X/Y=1/186 and Y/Z=93 are nonsquares. T-010's all-pairs corollary applies even though 3 and 31, both 3 mod 4, divide n. T-009's all-1-mod-4 support hypothesis is unavailable.
3. **Non-clean square pair at n=1 mod 4.** At n=21,c=1, (7,42,42) has exact sum 6/42+1/42+1/42=4/21. The equal pair is square, but gcd(21,7)=7 prevents clean II, and two n-multiples prevent clean I. No permutation fixes this. This supplies the non-clean domain isolated by T-010; it does not contradict it.

These exact examples support scope only. The universal theorem is proved symbolically, not by examples.

## Strict theorem/evidence ledger

| Claim or assessment | Status | Evidence or boundary |
| --- | --- | --- |
| Composite clean normalization; full G versus pairwise H; all reduced ratios | proved | proof §2, §§4–5 |
| Clean-I unit signs, shared n,h permitted; Clean-II sign, k not cancelled | proved | proof §3 |
| All four cross-status exclusions at every odd n on the clean domain | proved | proof §§4–5 |
| A same-status square pair forces n=3 mod 4 | proved | proof §§4–5 |
| Clean n=1 mod 4 all three unordered ratios nonsquare; any square-pair representation there non-clean | proved | proof §§1,4–5 |
| Main audit/integration of I-015/T-010, O-019 | proved | this mapping and proof.md |
| New H-009 presentation/freeze review, O-020 | unresolved | Flagship has not reviewed this submission |
| Proof uses no finite verification or unproved mathematical assumption | proved | All prerequisites are derived in proof §§2–3; clean hypotheses are theorem hypotheses |
| Value as a compact extension of the combined structural note | plausible | Local assessment only |
| External-priority certification; old forcing routes | blocked | Offline rule; no arithmetic forcing bridge |
| Invalid extrapolations listed above | false | Exact paper witnesses and exponent-parity argument |
| External priority, standalone publishability, Erdős–Straus | unresolved | No universal existence argument or authorized external audit |

No heuristic evidence or new conjecture. No search, interval expansion, identity hunt, congruence coverage, Lean compilation, network access, hash audit or fresh-independent-agent claim. The minimal next action is a new flagship paper review of H-009, especially kernel parity, d=1, nonunit k and converse quantifiers; then stop.