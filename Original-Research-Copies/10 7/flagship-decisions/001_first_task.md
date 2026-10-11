# D-001 — First task: an audited smallest-denominator classifier

Sequence: 001.

- Research question: which primes in the explicitly chosen six modulo-840 classes admit a solution with `x0=(p+3)/4`?
- Known facts used — **proved:** the factor-pair identity and the criterion in [I-001](../ideas/001_initial_strategy.md): for prime `p≡1 (mod 24)`, completion at x0 exists iff x0 has a prime divisor `q≡2 (mod 3)`. Proof and positive integral reconstruction formulas are supplied there. No novelty or Lean-verification claim is made.
- Recommended first task — **plausible:** audit that proof, then implement and independently validate its exact classifier on ALL primes `2<=p<=100000` whose residues modulo 840 belong to `{1,121,169,289,361,529}`. Compare its verdict for every p with exhaustive factor-pair enumeration at x0. Do not search other x in this first task.
- Expected output: a short proof note; runnable standard-library source; one record per selected prime, containing either `(p,x0,q,y,z)` or a checked complete factorization of x0 proving no completion there; an independent integer-certificate checker; counts, disagreements, range, exclusions, runtime and environment; a concise main-report update linking the artifacts. The two existing smoke examples are regression tests, not the requested dataset.
- Acceptance standard: both implications, integrality and positivity proved; zero classifier disagreements; every success passes `4*x*y*z=p*(x*y+x*z+y*z)` with positive integers; every failure is labelled “no completion at x0.” Label the lemma **proved**, finite run results **verified computationally**, and universal existence **unresolved**.
- Main risk: mistaking fixed-x0 failure for a conjecture counterexample, or silently assuming the unaudited complementary modulo-840 coverage. `p=1201` fails at x0 but has a checked solution at x=306. Use the six classes merely to define the experiment.
- Stop rule: any arithmetic, factorization, or classifier discrepancy is **blocked** pending audit. Do not extend the bound, seek a finite universal cover, install Lean, or launch broad literature searches before this deliverable is complete.

Overall conjecture status: **unresolved**. No claim of a solution.
