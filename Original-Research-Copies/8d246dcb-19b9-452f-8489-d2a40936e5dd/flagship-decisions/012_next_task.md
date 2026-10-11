# D-012 — Accept H-009; freeze the exact twice-square classification

Sequence D-012. Inputs: current user assignment prioritizing meaningful partial results, H-009, R-012, I-016, and the inspected local literature/register.

## Decision

1. **Accept H-009/T-010.** R-012 discharges O-020. Preserve H-009 and all historical records unchanged. At the next live update, main should record acceptance and preserve H-009's corrected converse quantifiers.
2. **Rank one mathematical follow-up:** independently audit and freeze T-011, the exact twice-square-pair classification in I-016. This is a finite proof task, not a computational campaign.
3. This new decision supersedes D-011's stop only for this specifically quantified task, in response to the current user request for a rigorous partial increment. It does not reopen general squareclass hierarchies, identity hunting, pointwise forcing, old inverse routes, finite-range expansion, or external-priority research.

## Rank 1 — Exact twice-square-pair classification

### 1. Precise mathematical claim

For every odd integer n>=3,

    some positive integral representation of 4/n has U/V in 2 Q_{>0}^2
      iff some representation has a pair in exact ratio 2
      iff n has a prime divisor q=5 or 7 modulo 8.

The necessary direction holds for every numerator 4c, c>=1, without clean or gcd(c,n)=1 assumptions. If Y,Z form the pair and

    A=4cX-n, delta=gcd(A,nX), alpha=A/delta,

then X is even; every prime factor of alpha is 1 or 3 modulo 8; every prime factor of delta divides n; and J(-2,n*delta)=-1.

Under gcd(c,n)=1 and the accepted clean definitions, a twice-square pair must be the same-status pair, and n=5 or 7 modulo 8. Thus at n=1 modulo 8 every clean representation has all three ratios outside both rational squares and twice rational squares, using T-010 for the former exclusion.

**Status: proved in I-016's paper derivation; separate main handoff/integration remains unresolved.**

### 2. What appears new compared with local literature

T-009 classifies rational-square pairs; T-010 localizes them on the clean domain. The twice-square classification is not stated in the inspected records. Its key additional argument is that a primitive reciprocal twice-square pair has even reduced denominator, forcing X even and hence a modulo-eight character obstruction in unrestricted composite representations.

The q=5-modulo-8 identity, elementary splitting at q=7 modulo 8, scaling, quadratic characters and normalizations are background, not new discoveries. This result does NOT add new solved n or new congruence coverage. The incremental claim is a structural iff and a restricted-construction obstruction. External originality is unresolved; this is not a comprehensive fresh audit of all local HTML sources.

### 3. Smallest useful verification/proof target

Audit I-016 Sections 2–5 and freeze one self-contained proof package. The indispensable steps are:

- the orientation Hr^2,2Hs^2 with r odd;
- gcd(r^2+2s^2,2r^2s^2)=1;
- even reduced denominator implies even X;
- A=-n modulo 8 and the sign J(-2,n delta)=-1;
- prime support of delta, not delta|n;
- integrality, positivity and division-free certificates for both converse constructions;
- the clean-II odd-exponent kernel d|k|u+v, including d=1 and nonunit k;
- clear separation of arbitrary-c necessity, c=1 existential sufficiency and actual-representation localization.

No interpreter or range search is required.

### 4. Expected incremental result

One rigorously audited exact classification, suitable as a compact addition to the structural note rather than another numerical bound or unproved existence strategy. Its corollaries exclude square-or-twice-square pair ansätze on two explicit domains: every clean representation when n=1 modulo 8, and every unrestricted representation when every prime divisor of n is 1 modulo 8.

### 5. Main uncertainty

External priority and significance, not an intended missing proof bridge. The argument is elementary and might be implicit in older work. A separate main derivation remains necessary for the workspace's review discipline. Standalone publishability is unresolved; value in a combined structural note is plausible.

## Main model's ONE concrete next task

**Create a new self-contained proof-only `handoffs/010_twice_square_pair_classification/` auditing I-016/T-011a–c, or report the first precise failed implication.** Include definitions, the complete unrestricted proof, both converse certificates, the accepted clean prerequisites with sufficient derivation for self-containment, and a strict scope ledger.

Use only the exact paper boundary cases already given: n=5 and n=7 witnesses; non-clean n=25; n=9 separating square from twice-square pairs; clean n=93; n=7,(2,28,28) refuting every-representation forcing; n=5,X=4 refuting fixed-X sufficiency; c=4,n=5 refuting arbitrary-c sufficiency. These are not an invitation to a numerical census.

As bookkeeping within that task, reconcile R-012's O-020 acceptance in the live records. Do not rewrite I-015/R-011/D-011 or historical handoffs; cite the corrected existential quantifiers instead.

Then stop. Do not investigate other coefficients, seek a new covering system, start a formalization campaign, run tools merely for decorative numerical confirmation, or make a full-conjecture claim. External-priority certification remains blocked by the local offline policy.

## Status ledger

- **proved:** H-009 acceptance; I-016/T-011a–c in the flagship derivation; displayed scope counterexamples to overclaims.
- **verified computationally:** none.
- **conditional:** none.
- **plausible:** compact-note value.
- **blocked:** external-priority certification; old pointwise-forcing routes.
- **false:** unrestricted n=5-or-7-modulo-8 necessity, every-representation forcing, fixed-X support sufficiency, arbitrary-c converse.
- **unresolved:** independent main integration/review, external originality, standalone publishability, and Erdős–Straus.