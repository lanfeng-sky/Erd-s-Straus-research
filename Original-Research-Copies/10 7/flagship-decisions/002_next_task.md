# D-002 — Move from fixed offsets to exact structural obstructions

Sequence: 002; 2026-10-03. Research question: which mechanism can force a certificate beyond KI-001? Known facts: accepted H-001/R-002, elementary I-002 and I-004, conditional I-003 with dependency L-002.

## Decision and ranking

D-001 is **complete and accepted**. Preserve H-001 unchanged. The next deliverable is an audited structural reduction, not a larger verification bound.

| Priority | Direction | Plausibility | Potential impact | Cost / decision |
|---|---|---|---|---|
| 1 | Exact two-branch divisor-ratio criterion, I-002 | High: elementary derivation with exact cross-checks | High diagnostic value; separates true local obstruction from insufficient exponents | Low; audit and adopt now |
| 2 | Divisor-set growth versus subgroup concentration, I-003 | High for the conditional lemma; low/unknown for pointwise coverage | Potentially high if simultaneous concentration across shifts can be excluded | Medium; one bounded structural report, no presumption of coverage |
| 3 | Switched factorization with BOTH g,k, I-004 | High for identity, unknown for universal forcing | Alternative route for sparse shifted integers; may reconnect existing Rosati theory | Low bounded experiment; medium theoretical work |
| 4 | Formalize I-002 reconstruction and its p-adic case split | High once main audits statement | Prevents branch/integrality mistakes, not existence | Defer install/build until theorem statement stabilizes |
| Pause | Longer fixed-offset lists, g=1 only, broad literature expansion, almost-all estimates without a pointwise bridge | Insufficient | Low as a direct proof program | Do not make these the next deliverable |

No novelty claim is authorized. Do not advertise a decisive new reduction in the literature sense until compared with existing parameterizations. The structural formulation is useful even if algebraically classical.

## Required task T-002A — audit the exact two-branch theorem

Scope: **every prime p=1 mod 4 and integer p/4<x<p**, not just the 273-prime dataset. Prove in a self-contained note:

1. gcd(4x-p,px)=1 and v_p((px)^2)=2.
2. Completion iff A or B in I-002; explicitly cover all p-adic allocations 0+2,1+1,2+0.
3. Both reconstruction formulas are integral, positive, and satisfy the division-free certificate.
4. Bounded divisor-ratio equivalence, with targets -1 and -p, including the inversion step.
5. The global existence equivalence when x runs from (p+3)/4 through floor(3p/4). State the unordered-versus-smallest-x distinction.

Independent finite validation: all 186 H-001 x0-failure primes, ALL t=0,...,15 (not stop-at-first), plus all 15 offsets t=0,...,14 for p=118801. Exactly 2991 (p,x) pairs. Compare a new compact implementation with complete factor-pair enumeration; validate every returned witness with integer arithmetic. Retain per-pair records containing a, factorization of x, A/B status, witness c or complete divisor-residue miss certificate. This is a bounded audit of the theorem, not a new global verification bound.

Acceptance: zero disagreements; every branch and integrality condition explicit; no missing ordering caveat. Regression tests must include the full-group-but-no-solution pair (1201,303) and 118801's first hit at x=29715. Failure of any implementation or proof check blocks downstream claims.

## Required task T-002B — diagnose simultaneous obstructions, not just first hits

Use exactly the 2991 pairs from T-002A. For each failed pair:

- Compute D_x, R_x, and H_x independently enough to compare the residue formulation with divisor enumeration.
- Classify: single-prime quadratic obstruction; other subgroup obstruction; or bounded-exponent miss with a target in H_x. Store a checkable witness for the classification.
- For prime a=3 mod 4 and -1 in H_x, compute h=|H_x| and all odd r|h; return a deficient K_r as in I-003 whenever branch A fails. If there is no deficiency, that is a specific contradiction to the claimed conditional lemma or to the implementation and must be investigated.
- Audit I-003's Kneser application separately. Its source theorem statement is locally recorded, but a primary/self-contained proof has not been audited. Keep this dependency explicit; do not let it contaminate T-002A's elementary status.

The main mathematical output should answer: does any actually observed relation between the obstruction witnesses at different shifts force one branch to succeed? State any candidate implication with all quantifiers, then attempt to falsify it on the complete 2991 pairs. A report concluding “no cross-shift mechanism yet” is acceptable; treating absent contradictions as proof is not.

Time/size bound: no search beyond these pairs for this task; at most two candidate cross-shift implications. If both fail, retain the smallest explicit counterexample to each and stop. Avoid an unbounded pattern hunt.

## Secondary task T-002C — test the missing switch parameter

Only the seven g=1,k<=16 failures from I-004:

    20521,31081,39841,51361,58321,66889,88729.

Search 1<=g<=16 and 1<=k<=16 in N=4gk²p+1, with complete factorization and divisors d<=sqrt(N), d=-1 mod 4gk. Fixed order: increasing g then increasing k, stop at first success for each p. Certify all triples; label a miss as failure of this finite window only. Compare each first witness with the normalized (g,k,u,v) from available branch-A witnesses in T-002A. At most 1792 (p,g,k) candidates before early stopping.

Mathematical requirement: audit the branch-A equivalence in I-004. Identify whether g=1 was an artificial restriction. Do not jump from success for seven examples to a universal g,k bound. No broad range extension is requested.

## Submission and stop rules

- Create a new self-contained frozen `handoffs/002_structure/` containing proof notes, standard-library scripts, exact records/summary, reproduction instructions, and unresolved obligations. Never revise H-001.
- Update main-model live files and its report only from the main side; R-002 is the flagship acceptance record.
- Keep statuses distinct: elementary theorem **proved**; finite checks **verified computationally**; Kneser application **proved conditional on the named input**; pointwise bridge **plausible** or **blocked**, depending on the actual findings.
- No Lean installation, reported huge-range proof, universal fixed-offset conjecture, or complete modular-cover claim is needed for this deliverable.
- Do not search the web for existing local facts. A future novelty audit of these exact formulas is permissible only after their statements stabilize.

## Strongest established result and precise remaining gap

Accepted H-001 establishes the universal iff criterion at x0. This round's strongest elementary extension is the exact fixed-x two-branch theorem and equivalent bounded-ratio reformulation, with fully explicit positive integral reconstruction. The switched family reparameterizes one branch. Neither has a proved universal existence guarantee.

The central missing theorem is:

> For every target prime p, some admissible x has R_x intersecting {-1,-p}.

Even proving this for all primes failing x0 within the six chosen classes is open here. Those six classes define the experiments; treating them as the only global obligation still requires the complementary congruence coverage audit. Overall conjecture: **unresolved**.