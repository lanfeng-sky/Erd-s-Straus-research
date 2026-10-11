# Result 006 — Proof-only signed-character synthesis

Date: 2026-10-05. Assignment: flagship D-008. Status of the structural theorems and exact paper checks: **proved**.

Self-contained review package:

    flagship/handoffs/006_signed_character_synthesis/

The package contains the complete signed clean-type proof, pending Type-II envelope/gcd proof audits, and exact scope examples. The mathematical work is general theorem proof, not an experiment extending a finite solution range.

## Result and scope

For arbitrary c>=1 and odd n>=3 coprime to c, clean I forces Jacobi(-cG,n)=-1; clean II forces Jacobi(-(X/G),n)=-1. Both same-status reduced pairs satisfy Jacobi(-rs,n)=-1, ruling out rational-square ratios when n=1 mod 4. The proof permits composite n, repeated prime factors, shared n,h in I, and nonunit k in II. At composite n unrestricted solutions need not be clean.

Main separately closes the I-011/I-012 proof-audit obligations: T-006's exact Type-II X envelopes and equality, T-007's intrinsic quotient character and parity-sensitive G ceilings and equality.

## Exact arithmetic and evidence separation

* Symbolic universal statements: **proved**, with full derivations in H-006.
* Boundary/equality examples: exact PAPER arithmetic at (c,n)=(2,5),(1,3),(1,15),(1,93), n=9, and the previously specified p=313,1009,97,4201. These are not executed test records.
* New bounded computation: NONE. No script was run and no runtime, environment version, test-pass count, or hash-validation claim is made.
* Prior R-006/R-007 outputs: historical bounded evidence only, not reproduced in this round and not proof inputs.
* Prior stalled parser process: **unresolved**. No retry or process-control operation.
* Heuristic/existence conjecture: NONE introduced. Erdős–Straus: **unresolved**. Stopped forcing routes: **blocked**.

No network or formal verification. Local source-level originality was not re-audited. External priority is **unresolved**; combined-note significance **plausible**.

`audit_record.json` records the concrete scope and absence of execution. `previous_main_research_report.md` and `previous_open_obligations.md` preserve the pre-update live summaries. The known-identities and research-log updates append new sections, preserving their earlier entries. Historical ideas, decisions, reviews, handoffs, literature, and result directories are unchanged.

Minimal next step: flagship reviews H-006's paper proof. Do not infer nonexistence from a failed ansatz or restart a stopped search.