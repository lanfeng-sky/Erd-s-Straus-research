# D-008 — One task: audit and freeze the signed-character synthesis

Sequence 008, 2026-10-05. Sources: I-013/R-008, with H-005 and I-011/I-012 as prior structural results.

## Decision

Rank ONE direction: a general signed-character theorem and reduced-pair obstruction, not another bound optimization. Main should produce one self-contained audited structural submission, incorporating the previously pending Type-II checks. Do not manufacture additional research directions or a pointwise existence conjecture.

This extends D-007's intended synthesis, not its stopped existence/search program. Keep all historical files unchanged. The live main report is stale relative to the flagship notes; only main should reconcile it after the independent audit, without describing an absent handoff as completed.

## 1. Precise mathematical claim

Let c>=1, n>=3 odd, gcd(c,n)=1, and let positive integers solve

    4c/n=1/X+1/Y+1/Z, G=gcd(X,Y,Z).

Clean I means n|Y and gcd(n,XZ)=1; then

    Jacobi(-cG,n)=-1.

Clean II means n|Y,Z and gcd(n,X)=1; then

    Jacobi(-X/G,n)=-1.

If U,V are the two same-status denominators, reduce r=U/gcd(U,V), s=V/gcd(U,V). In both types

    gcd(rs,n)=1, Jacobi(-rs,n)=-1.

When n=1 mod 4 this gives opposite Jacobi signs and excludes U/V from being a rational square. At prime n these two types exhaust all solutions; at composite n they do not. No ordering premise is needed.

The claim is **proved** in I-013 by an elementary paper derivation; separate main audit remains pending.

## 2. What appears new relative to local literature

The signed extension to arbitrary numerators 4c and odd composite denominators with clean divisibility, plus the same reduced-pair obstruction for both types, is absent from the inspected local markdown register. It is a structural restriction on actual clean-type solutions and rules out a specified square-ratio construction method.

The existing numerator-4 prime character results, A/B normalization, Jacobi lemma, and known odd-square obstruction are NOT new claims. General m/n counting is also already in the literature digest. The stalled HTML parsing produced no additional source audit. External priority and standalone publishability are **unresolved**. A concise combined structural note is **plausible**.

## 3. Smallest useful verification/proof target — one concrete task

Independently audit I-013 Sections 3–6, then return the next available self-contained handoff (H-006 if still available), or record an exact failed implication/counterexample in a new file.

The critical checklist is short:

* Derive composite normalization from DE=n^2X^2 under the stated clean conditions, without treating composite “not divisible by n” as coprimality.
* Establish pairwise coprimality and g=the FULL denominator gcd.
* Retain c in clean-I character; retain the minus sign for general odd n.
* Allow shared factors of n,h in I and nonunit k modulo n in II.
* Compute the SAME-STATUS pairwise gcd separately and prove Jacobi(-rs,n)=-1.
* Derive the rational-square obstruction only when n=1 mod 4.
* Recheck the paper boundary examples at (c,n)=(2,5),(1,3),(1,15),(1,93), and the non-clean square example n=9. Do not confuse displayed paper checks with an executed regression.

Within that SAME submission, close the still-pending main audit of I-011/I-012 so the synthesis rests on independently rederived Type-II statements. Do not add new constants, equality searches, classes, or auxiliary hierarchies.

No interpreter execution is required. One prior source-parser call stalled and its process state is unconfirmed; do not queue further computation merely to decorate a proof with tests. If execution is later resumed, report its actual result separately and use a small explicit bounded checker, not a retry of the large parser by default.

## 4. Expected incremental result

An audited intrinsic character theorem for 4c/n on clean types, recovering H-005/I-012 at the original prime domain, together with a rigorously quantified square-ratio obstruction. This provides a unified structural statement to accompany the existing sharp prime-denominator bounds. It is more useful than another isolated equality identity, but does not establish new universal existence or coverage.

## 5. Main uncertainty and stopping point

* **Proved:** I-013's written theorem, subject to the requested separate audit.
* **Verified computationally:** no new result in this round; no output returned from the attempted execution.
* **Conditional:** no conditional existence theorem is proposed; clean-type assumptions are explicit theorem hypotheses.
* **Plausible:** value of the combined structural note.
* **Blocked:** older pointwise forcing routes; fresh source-level priority certification under current offline constraints.
* **False:** omitting c from the general-numerator Type-I claim; dropping the reciprocity sign for n=3 mod 4; replacing composite clean coprimality by a mere count of n-multiples.
* **Unresolved:** external priority, main's separate audit, execution-process state, and Erdős–Straus itself.

Endpoint: one audited, carefully scoped partial-theorem submission. Preserve provenance; remain offline; no new solution range, network, installation, literature campaign, or restarted forcing program.