# D-005 — One offline task: audit the sharp Type-I denominator/gcd theorem

Sequence 005, 2026-10-04. Inputs: R-005's acceptance of H-004, pre-existing KI-002/KI-006, and the self-contained new I-009 proof. **Overall Erdős–Straus: unresolved. Existence bridge: blocked. External novelty: unresolved.**

## Decisions

1. Accept H-004 and permit main to close O-008 by reference to R-005. Preserve all historical files and frozen handoffs, including the explicit I-008 erratum.
2. Keep universal nesting, unforced branch switching and the inverse-deficiency hierarchy stopped. Do not turn this result into a full-proof program.
3. The user's no-online-search instruction governs this and future work until changed. No browsing, download, web/Scholar query, network API or network-enabled package is needed. Do not pursue a literature-priority check now.
4. Under the user's explicit preference for incremental theorems, authorize ONE structural partial-result task, rather than D-004's stricter existence-only restart gate. This does not restart the archived existence route.

## Rank 1: sharp Type-I exclusion region with equality classification

Only one direction is recommended; no artificial second track.

### 1. Precise claim

For every prime p=1 mod 4 and every positive integer solution with exactly ONE denominator divisible by p, let X be the smallest denominator and G the common gcd of all three. Then

    Legendre(G,p)=-1,
    6X<=3p-2G+1.

For every prime p=1 mod 24 this strengthens to

    30X<=15p-14G+1.

Equality holds precisely, up to permutation, at

    G=45t+29, p=672t+433 prime, t>=0,
    (X,Z,Y)=(7G,8G,56pG).

Consequently G is not a square; writing q(p) for the least nonresidue gives the safe Type-I cutoff floor((15p-14q(p)+1)/30). No Type-II pruning is authorized.

### 2. What appears new locally

H-004's B separator records only p|(4guk-1). I-009 exploits the quotient h and identifies its character to prove that the intrinsic common gcd is a nonresidue. Ordering and the exclusions u=1,3,5 at p=1 mod 24 then give a sharp quantitative bound with all extremizers classified. None of these conclusions is stated in the pre-existing local theorem register. This is not proof of external priority. The equality family's congruence identity is not itself advertised as new.

### 3. Smallest useful verification/proof target — the ONE main task

Independently audit T-005b, including its common-gcd prerequisite and equality classification, and return a short self-contained H-005 proof note or a precise counterexample.

Required checks:

* At the smallest denominator, justify B normalization and u,v,k pairwise coprime, hence G=g. Do not import a pairwise-gcd assertion without proof.
* Prove Legendre(g,p)=-1 using h=3 mod 4 and Jacobi multiplicativity; explicitly allow p|h.
* Derive the exact identity p-2X=v*(2gu(k-u)-1)/(u+k).
* Check monotonicity by cross multiplication if desired, and exhaust the three cases v>=2; v=1,k-u>=2; v=k-u=1.
* Verify the mod-8/mod-24 contradictions for u=1,3,5, and both directions of the equality classification.
* Check the concrete equality certificate p=433, (203,232,703192), G=29.
* Optional executable replay: ONLY `reviews/005_gcd_gap_probe.py` on its unchanged inputs. Its 955 saved B checks are regression evidence, not an exhaustive new solution census.

### 4. Expected incremental result

An independently audited, locally self-contained structural theorem: every Type-I completion for a residual prime has a nonresidue common factor and lies below a sharp gcd-dependent denominator boundary. This could support a concise note or certified Type-I search pruning if originality/significance are eventually established. Main should label paper proof **proved**, finite replay **verified computationally**, and external novelty **unresolved**.

### 5. Main uncertainty and stop rule

Priority and publication value remain unresolved; mathematical usefulness is **plausible**. No claim forces a Type-I solution or rules out all solutions of a prime. If the audit finds an error, record the exact counterexample in a NEW handoff and stop. Do not silently narrow hypotheses, infer sufficiency, assign another optimization level, enlarge parameter ranges or claim an infinite prime family from finite checks.

## Deliverable discipline

Budget: one bounded proof-audit turn. New H-005 only; main may subsequently update its own live report/register to reflect the audit outcome. Do not edit I-009, historical reviews/decisions or frozen handoffs. Explicitly note that I-009's discarded Type-II draft cutoff was false and is not a theorem/input. No Lean installation, external bibliography, new prime interval or independent-agent claim is required. A successfully audited partial theorem is the intended endpoint.