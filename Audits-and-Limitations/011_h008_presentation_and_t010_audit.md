# R-011 — H-008 presentation audit and T-010 clean-pair localization

Date: 2026-10-06. Sequence after R-010/D-010.

## Verdict on H-008

**H-008 is accepted as mathematically correct within its stated hypotheses.** The compressed manuscript preserves the two distinct scopes and does not promote a restricted obstruction to an Erdős–Straus solvability claim. Its proof content is **proved** by the written derivation. No new computational status is attached. External priority, standalone publishability, and the conjecture itself remain **unresolved**.

The presentation review finds no fatal algebraic or quantifier gap. The following checks pass.

### T-009 unrestricted theorem

1. From a rational-square pair, unique factorization gives Y=Hr^2 and Z=Hs^2 with gcd(r,s)=1. The reduced numerator of the reciprocal pair is exactly

       (r^2+s^2)/gcd(r^2+s^2,H).

   The possible factor 2 is handled by the later fact that A, delta and alpha are odd. Every odd prime in the numerator is 1 modulo 4 by the order-four argument.

2. For A=4cX-n and delta=gcd(A,nX), positivity gives A>0. Since n is odd, A, delta and alpha=A/delta are odd. A prime in delta but not n would divide X and then divide n=4cX-A, a contradiction. This proves prime support, not delta|n.

3. Alpha is 1 modulo 4, so A=delta alpha=-n modulo 4 and n delta=3 modulo 4. Since every prime factor of n delta belongs to n, n has a prime factor 3 modulo 4. Permuting the singled-out denominator covers all three unordered pairs.

4. The c=1 converse is correctly restricted to numerator 4 and uses q|n, q=3 modulo 4, t=(q+1)/4 and (mt,2mqt,2mqt). Positivity, integrality, reciprocal sum and the division-free certificate all pass. Repeated denominators are explicitly allowed.

### T-008 clean theorem

1. The definitions of Clean I and Clean II are stronger than merely counting multiples of n. The manuscript retains gcd(c,n)=1 and the full gcd G.

2. The D,E factorization and prime-power allocation correctly yield

       Clean I: (X,Y,Z)=(Guv,nGuk,Gvk),
       Clean II: (X,Y,Z)=(Guv,nGku,nGkv),

   with the required coprimality. The full G is not confused with the pairwise gcd: H=Gv in I and H=nGk in II.

3. Clean I keeps c, permits gcd(n,h)>1 in M=nh, and uses Jacobi multiplicativity without silently imposing coprimality of n and h. Clean II retains the reciprocity sign and cancels only the unit v; it does not assume k is a unit modulo n.

4. The reduced-pair character J(-rs,n)=-1 and the n=1 modulo 4 nonsquare consequence are correctly scoped to the specified same-status pair. At n=3 modulo 4 no nonsquare conclusion is asserted.

### Scope and evidence

The n=25 non-clean example and n=93 mixed-support clean example genuinely separate the two results. The false extrapolations are correctly marked: delta|n, unrestricted n=1-modulo-4 exclusion, arbitrary-c sufficiency, every-representation forcing, and fixed-X sufficiency. The ledger correctly says there is no new verified computation, no conditional proof dependency, and no external-priority certification.

## Minor editorial recommendations, not mathematical objections

1. In the abstract and Theorem 1 prose, say “all three unordered pairwise ratios” rather than “all three denominator ratios,” to eliminate any possible ambiguity about ordered quotients.
2. Near the reduced numerator, explicitly say that alpha is odd because A is odd; this makes the cancellation of the possible factor 2 in r^2+s^2 completely transparent.
3. In the normalization paragraph, retain the displayed facts gcd(a,n)=gcd(a,X)=1 immediately before using gcd(a,Gu)=1. The current text contains the facts, but one extra connective phrase would improve readability.
4. Keep the status sentence “proved” for the mathematics separate from “reviewed/accepted” for the compressed presentation. H-008 already does this in the README and ledger; the distinction should survive any typeset version.

These are editorial improvements only. H-008 should not be rewritten as a historical file.

## New derived result: T-010

The audit exposes one useful, non-artificial strengthening that is not stated in H-008. The separate idea record is [I-015](../ideas/015_clean_square_pair_localization.md).

**T-010 (proved on paper; main integration pending).** Under gcd(c,n)=1, for a clean representation of 4c/n:

- in Clean I, any rational-square denominator pair must be (X,Z), and then n=3 modulo 4;
- in Clean II, any rational-square denominator pair must be (Y,Z), and then n=3 modulo 4.

Therefore every clean representation at n=1 modulo 4 has all three pairwise denominator ratios nonsquare, including mixed-support composite n.

### Proof check

The accepted normal forms are enough.

In Clean I,

    (X,Y,Z)=(Guv,nGuk,Gvk),

with u,v,k pairwise coprime, gcd(uv,n)=1 and gcd(k,n)=1. The same-status ratio is u/k, and T-008 excludes it when n=1 modulo 4. The cross ratios reduce to v/(nk) and nu/v. A square cross ratio forces n to be a square because gcd(n,k)=1 in the first case and gcd(n,u)=1 in the second. But Clean-I T-008 gives J(-cG,n)=-1, impossible for a unit Jacobi symbol modulo an odd square. Thus no cross pair exists.

In Clean II,

    (X,Y,Z)=(Guv,nGku,nGkv),

with u,v,k pairwise coprime, gcd(uv,n)=1 and k|u+v. The same-status ratio u/v is excluded at n=1 modulo 4 by T-008. For X/Y, a square ratio gives v=r^2 and nk=s^2. Let d be the squarefree kernel shared by n and k. Since d|k|u+v, -u is a square modulo d, so J(-u,n)=1. But v is a square unit and T-008 gives J(-uv,n)=-1, hence J(-u,n)=-1, a contradiction. X/Z is symmetric, with -v a square modulo d.

This proof deliberately does not cancel k modulo n. It is valid when gcd(k,n)>1, which is the main composite-domain hazard.

## Classification

- **proved:** H-008 mathematics within its exact hypotheses; T-010 by the displayed case analysis;
- **verified computationally:** none in this review;
- **conditional:** none;
- **plausible:** T-010's usefulness as a compact extension and the value of the combined structural note;
- **blocked:** external-priority certification under the offline boundary and old pointwise-forcing routes;
- **false:** any converse saying n=3 modulo 4 forces a clean square pair, or any inference from T-010 to nonexistence of unrestricted representations;
- **unresolved:** main-model integration of T-010, external priority, standalone publishability, and Erdős–Straus.

## Recommendation

Do not launch a new computation or reopen H-001 through H-008. Have the main model perform one proof-only task: independently audit and freeze T-010 as a short corollary, preserving the distinction between a proved necessary localization and a sufficiency statement. After that, reassess publication value or seek explicit authorization for an external-priority audit; no pointwise-forcing restart is justified by the present evidence.
