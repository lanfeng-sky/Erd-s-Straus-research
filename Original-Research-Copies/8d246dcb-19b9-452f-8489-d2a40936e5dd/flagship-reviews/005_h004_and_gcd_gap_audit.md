# R-005 — Accept H-004; audit the new common-gcd/gap theorem locally

Sequence 005; 2026-10-04. Research question: is the pending closure package correct, and can one useful structural result be extracted without restarting the failed universal-coverage route?

## 1. H-004 verdict: accepted within its exact scope

Read the local report, literature register, main records, I-008, R-004, D-004, and H-004's proof and source. The Jacobi lemma is correct for even g and composite moduli, including repeated prime factors. From n=(4guk-1)a-4gu^2, coprimality and Jacobi(n,4guk-1)=-1 follow exactly as claimed. Its square exclusion concerns the switched family only.

The fixed-x normalization C/x=u/v correctly gives x=guv and C=gu^2. Both branch reconstructions, normalized converses and p-adic allocations pass. In B, v<p justifies p|(4guk-1); the quotient h is positive. The two branches need not share k. The separator is not an existence mechanism.

The explicit correction to I-008 is valid:

    n-x=c(3ak-3)-a >=2a-3>0,

not c(3ak-4)-a. At the retained 1009 witness the old equality gives 745 instead of 756. This **false** ancillary statement does not affect the corrected theorem. Historical I-008 and R-004 are untouched.

The normalized-family bound ck<=(n+3)/8, residue boundary r=M-1, and all 24 h cases at 193 check out. Universal nested coverage remains **false**; the unrestricted conjecture remains **unresolved**. Main may close O-008 by citing this review.

## 2. Reproduction

H-004's sibling-only auditor was run directly from its mounted absolute workspace path, first during the initial review and again by the new local probe. Both runs exit 0 with empty stderr; the output is byte-identical to the frozen retained stdout. All ten H-004 manifest entries pass. The new probe also verifies every H-002 manifest entry; neither handoff was changed.

New files:

* `005_gcd_gap_probe.py`: standard-library-only exact checker; no network or project imports.
* `005_gcd_gap_results.json`: complete output, input/source hashes, platform and H-004 replay details.

The complete wrapper run exited 0 in 1,245,628,077 ns, Python 3.12.3, Linux aarch64. Script source SHA256:

    5863aae0c028aad6d340f90fa0520503e2f2403e9a2476cd7a83990681d89e52

Saved-certificate regression uses exactly H-002's 2991 pairs across 187 primes, and only the first saved B witness at each successful pair: 955 certificates, zero disagreements. It is NOT an enumeration of every completion. No prime interval, offset window, group order or parameter search was added. There is one additional explicitly derived sharpness certificate at p=433; trial primality and its exact identity were checked, not discovered by a sweep.

## 3. New proof finding, separate from H-004 acceptance

[I-009](../ideas/009_type_I_gcd_and_sharp_gap.md) proves the following for Type I, meaning exactly ONE p-divisible denominator. For p=1 mod 4, smallest denominator X and full common gcd G,

    Legendre(G,p)=-1,
    6X<=3p-2G+1.

For p=1 mod 24 this sharpens to

    30X<=15p-14G+1.

The key new step is intrinsic: in the accepted B form,

    X=guv, Y=pguk, Z=gvk,
    ph=4guk-1, hv=u+k,

the u,v,k are pairwise coprime and G=g. Since h=3 mod 4 and 4gu^2=-1 mod h, Jacobi(g,h)=-1. KI-006 gives Jacobi(g,ph)=1; denominator multiplicativity then forces Legendre(g,p)=-1 even if p divides h. It would be an error to assume gcd(p,h)=1; it is neither required nor asserted.

Ordering makes k>u. The exact gap formula

    p-2X = v*(2gu(k-u)-1)/(u+k)

allows a sharp optimization, not a probabilistic estimate. In the residual prime domain g>=5. The cases v>=2 and k-u>=2 give strict inequalities. When v=k-u=1, the congruences p=1 mod 24 exclude u=1,3,5 and h=3 mod 4 forces u odd, so u>=7. This is the additional arithmetic input beyond merely rewriting B.

Equality is exactly u=7,k=8,v=1,h=15, giving

    G=45t+29, p=672t+433 prime,
    denominators (7G,8G,56pG).

The example p=433, G=29, triple (203,232,703192) attains the inequality. No new modular-coverage claim is attached to this equality family.

**Proof status:** proved in the supplied written argument, pending a separate main-model proof audit. The same model's regression is not a fresh-agent review or formal proof. **Novelty status:** absent from the pre-existing local theorem statements; external priority **unresolved**. A short publishable note is **plausible**, not promised.

## 4. Adversarial scope checks and a discarded drafting claim

* G is the gcd of ALL three denominators, not just the p-free pair. The equality G=g requires pairwise coprimality of u,v,k, proved from the normalized B equations.
* X must be the smallest denominator. The saved checker swaps u and k when necessary before applying the bound; it does not assume every historical fixed-x choice is smallest.
* The inequality involving q(p) follows only from G>=q(p); equality in the G-bound does not imply G=q(p).
* Type I and Type II must not be conflated. A current-round drafting suggestion X<=floor((p+1)/4) for Type II was immediately withdrawn and is **false**, already at the retained p=1009, X=253 certificate. I-009 explicitly records this draft correction and retains no such theorem. The correct Type-I proof is independent of that discarded suggestion.
* A nonresidue gcd is necessary, not sufficient. It does not force the requisite divisibilities or an actual solution.
* No theorem here handles every residual prime; universal pointwise forcing remains **blocked**.

## 5. Offline compliance and provenance

The user issued an explicit no-online-search instruction during this review. No network tool/request was used after it. The current theorem and checker depend only on pre-existing local foundations and self-contained arithmetic.

Before that instruction, two web searches timed out/aborted, a scholar mirror returned a challenge, and one arXiv HTML page was read/downloaded. The existing artifact `literature/005_elsholtz_tao_1107_1010v6.html` is preserved rather than silently deleted or relabelled as pre-existing. Its provenance and the limited pre-instruction observation are in `literature/005_offline_scope_and_prior_acquisition.md`. It is not a dependency of T-005 and supplies no novelty certification. No further literature campaign is recommended or authorized.

## 6. Recommendation

Accept H-004, close O-008, retain the old universal route as stopped. Assign one new, bounded **partial-theorem audit**, not an existence program: T-005b and its equality classification. This follows the user's preference for a meaningful structural result over repeatedly demanding a full pointwise solution. Do not extend the inverse hierarchy, repair the false nested-coverage conjecture, widen solution searches, or advertise literature novelty without evidence.