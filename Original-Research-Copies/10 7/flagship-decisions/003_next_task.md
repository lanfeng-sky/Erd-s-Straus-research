# D-003 — One proof-or-counterexample task on the joint bounded-exponent obstruction

Sequence 003; 2026-10-04. Research question: can near-minimal joint divisor growth be converted into an exact structural theorem? Known facts: accepted R-003/H-002, proved elementary I-005 Sections 1–5, proved reciprocity obstruction I-006. **Decision: D-002 accepted; authorize only T-003 below.** Overall conjecture **unresolved**. Proposed target **plausible**, pointwise extension **blocked**.

## Why this task, and what is new

The main obstacle is not further enumeration: H-002 already exhibits full generated groups missing both bounded-ratio targets. I-005 removes the unnecessary Kneser dependency, combines A and B into S=D union pD, and adds a genuine arithmetic constraint: the product of all joint generators is px=4x^2 modulo a prime defect, so their total discrete-log parity is even.

The new target is an inverse statement at ONE precise deficiency level. It would replace a scalar count with explicit cosets for every occurrence, including the p occurrence. This is incremental mathematics beyond the submitted reductions, not a new universal identity or a claim to solve all sparse cases. It has not been checked for literature novelty. Classical divisor collision and reciprocity facts are foundations, not deliverables to rediscover.

## T-003 — exact target theorem (proof or explicit refutation)

For EVERY odd m>=3, consider nonzero w_1,...,w_(m-2) in C_(2m). Let

    T = {sum_{i in I} w_i : I subset {1,...,m-2}}.

Assume all four conditions:

1. the w_i generate C_(2m);
2. Stab(T)={0};
3. T intersects T+m in the empty set;
4. sum_i w_i is even modulo 2m.

**Target:** there is a generator g of C_(2m) such that exactly one occurrence w_i is in {2g,-2g} and every other occurrence is in {g,-g}.

Signs and multiplicities are arbitrary. m need not be prime. The involution m cannot occur under condition 3. For m=3, show directly that the hypotheses are impossible rather than silently removing the case.

## Executable work plan and strict bounds

Treat the following as ONE deliverable, not a new open-ended research campaign.

1. **Audit prerequisites briefly.** Independently check I-005's elementary growth, critical equality, and even-total arguments. If a premise is false, give a counterexample and stop; do not build on it. Record the resulting elementary proof of KI-003 as a replacement proof, without editing H-002 or claiming a general Kneser proof.
2. **Adversarial proof attempt.** Use |T|<=m and the even-total refinement to deduce |T|=m=(m-2)+2. Every ordering has total growth excess exactly one above the binary minimum. Reorder conflicting pairs/triples to try to force two excess units or a persistent period. Analyze small-order cycles explicitly. Do not assume prime modulus, full order of each w_i, or that a partial product has the same stabilizer as T.
3. **Computation is a unit test only.** Rerun `reviews/003_joint_probe.py`; optionally write an independent verifier of the SAME domain m in {3,5,7,9}, length m-2. Current result: 175036 sequences visited, 84 satisfy all hypotheses, zero counterexamples. No m>9 sweep, new primes/offsets, or longer parameter windows. A theoretically derived explicit counterexample at any m may of course be checked directly.
4. **If proved, specialize without handwaving.** For a failed prime-defect pair let J=<q:q|x,p>, K=Stab_J(D union pD), |J/K|=2m. Delete occurrences in K, retaining multiplicities. Verify that the projected list generates J/K, has trivial subset-set stabilizer, avoids its involution in its DIFFERENCE set, and has even total. When its length is m-2, conclude the exact coset description: one occurrence in g^{+/-2}K and the rest in g^{+/-1}K. State whether the distinguished p occurrence is exceptional or ordinary; both cases are allowed. Express p=4x in the quotient and state the remaining arithmetic compatibility rather than asserting a contradiction.
5. **If false or blocked, stop.** Retain a minimal explicit counterexample if available, or a precise unproved sublemma. Do not repair by adding hypotheses, varying the deficiency, or extending computation within this round. A rigorously explained blocked result is preferable to a guessed theorem.

Reasoning budget: one main-model round; at most two written proof approaches (direct reordered growth, then quotient/short-cycle analysis). If neither yields a complete finite argument, classify the target **blocked** and end the task. No broad literature or Lean installation is required. Network only if a precisely named missing inverse theorem becomes indispensable; first check local files and record any useful external statement inside flagship with all hypotheses.

## Acceptance and submission

Create a new self-contained frozen `handoffs/003_joint_inverse/` containing:

- exact target and outcome label (`proved`, `false`, or `blocked`);
- full proof or explicit counterexample, not just the finite test;
- prerequisite audit and any arithmetic specialization;
- a small independent test script only if needed, exact tested domain and output;
- the pointwise limitation below stated prominently.

Update main live files/report from the main side after checking the new arguments. Link R-003 as acceptance of H-002. Preserve both older handoffs, all historical numbered files, and L-002. In particular O-005 can be closed for the SPECIALIZED binary growth application after audit; the general Kneser source audit remains unperformed and unnecessary here.

## Stop/pause decisions

- **Stop:** least-nonresidue q-offset forcing. It is already false at p=118801,q=13; I-006 records the full-group miss at t=4 and all misses t=0,...,12.
- **Pause:** a universal saturation claim. No theorem forces a large quotient occurrence count at any shift.
- **Pause:** enlarging finite fixed-x, g,k, group-order, or modular-cover searches.
- **Pause:** elementary rederivation of more Rosati/congruence formulas without an independent forcing mechanism.
- **Defer:** broad novelty/source comparison until there is a stable structural theorem worth comparing.

## What even a successful T-003 would NOT prove

A proof would classify only failed pairs with N=m-2 relative to their ACTUAL joint stabilizer. It does not cover N far smaller, does not force prime defects to exist in a chosen progression, and does not link exceptional patterns at different shifts strongly enough to eliminate all p. The exact conjecture-level target remains: for every prime p, force some admissible x with R_x meeting {-1,-p}, or supply another construction. If T-003 succeeds but offers no credible arithmetic bridge, archive it as a local structural lemma and reassess; do not authorize an indefinite hierarchy of inverse lemmas merely because each is provable.