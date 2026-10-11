# R-001 — Initial audit and exact smoke check

Sequence: 001. Question: can a fixed-first-denominator failure be cleanly separated from failure of Erdős–Straus?

## Workspace audit

- **unresolved:** The main report records no research yet. It has not been rewritten by the flagship model.
- **blocked** (local evidence audit only): The literature register has no source links, full construction list for the 834 covered classes, or reproducible artifacts for the reported large bounds. Treat the modulo-840 coverage, restricted-polynomial obstruction, almost-all theorem, representation counts, and reported bounds as background awaiting source-level audit before using them as project proof dependencies. This is not a claim that those published results are false. No unnecessary literature search was made.
- **proved:** Prime scaling, the division-free certificate, and the elementary factorization used here have direct proofs; see [I-001](../ideas/001_initial_strategy.md). In particular the smallest-denominator criterion does not depend on any unaudited coverage theorem.

## Smoke experiment — verified computationally

Source: [001_initial_smoke.py](001_initial_smoke.py), retaining the algorithm executed via `code_runner:run_python` in this session. Standard-library Python 3.12.3, Linux, aarch64; measured algorithm runtime 0.034060 seconds (excludes tool startup).

Scope: ONLY `n=1009` and `n=1201`, not every integer in the interval between them. No residue-based exclusion is used. Both primalities were checked by trial division through `isqrt(n)`.

Search plan: for each n, start at `x0=floor(n/4)+1`, allow `x0 <= x <= min(x0+15,floor(3n/4))`, and stop at the first certificate. Actual x values: 253 for 1009; 301 through 306 for 1201.

Method A: factor `b=n*x`, enumerate every positive divisor `d<=b` of `b^2`, set `e=b^2/d`, require both `(d+b) mod a=0` and `(e+b) mod a=0`, where `a=4x-n>0`. Recover `y,z` and require `x<=y<=z`.

Method B: scan every integer

`max(x,floor(b/a)+1) <= y <= floor(2b/a)`

and test the exact quotient `z=b*y/(a*y-b)` for integrality and `z>=y`. No independent arbitrary bound on z is imposed. Both methods then check positivity and the full integer certificate.

**proved** (bound justification): from `a/b=1/y+1/z` and `y<=z`, one obtains `y>b/a` and `y<=2b/a`; the quotient for z follows by rearranging. For Method A the positive factors satisfy `de=b^2` and `d<=e`, hence `d<=b`. Thus both searches are complete for a fixed x under the ordering convention, not for all possible x.

| n | n mod 840 | first successful x | y | z | both sides of integer certificate |
|---|---:|---:|---:|---:|---:|
| 1009 | 169 | 253 | 85096 | 1974822872 | 170066121441100544 |
| 1201 | 361 | 306 | 15980 | 172727820 | 3378473249846400 |

**verified computationally:** 2 n values tested, 2 certificates, 7 (n,x) pairs compared, zero algorithm disagreements. Both searches returned no ordered completion for 1201 at x=301,302,303,304,305. All arithmetic affecting the mathematical result used arbitrary-precision integers. Runtime measurement alone used a timer.

**proved:** At x=301 for n=1201, the factorization `301=7*43` already proves failure by the lemma in I-001: all prime factors of `b=1201*7*43` are 1 modulo 3, so no divisor of `b^2` can be 2 modulo 3. This argument even rules out unordered completions at this x.

**false:** “Failure at the smallest x is a counterexample to the conjecture.” The certificate at x=306 explicitly disproves this inference here.

## Limitations / next action

- **unresolved:** The universal conjecture; no finite checked interval is claimed. The proposed range through 100000 has NOT been run.
- **plausible:** Next build and independently check the finite fixed-x0 classifier specified in I-001 and D-001.
- No Lean verification was performed. No independent sub-agent tool was available; distinct algorithms run by the same model are not an independent-agent audit. They still provide a useful implementation cross-check.
