# D-006 — One offline task: audit the sharp Type-II residual envelope

Sequence 006, 2026-10-04. Inputs: R-006 accepts H-005; the new authoritative argument is I-011. **Erdős–Straus: unresolved. Old pointwise-forcing routes: blocked. External priority: unresolved.**

## Decisions

1. Accept H-005 exactly as Type I. Main may close O-009 by citing R-006. Preserve all frozen payloads and historical files.
2. Keep nesting, unforced branch switching and the inverse hierarchy stopped. Do not infer any sufficiency from nonresidue or denominator restrictions.
3. Stay strictly offline. No web, Scholar, Crossref, HTTP, download, GitHub/API, installation, or source-priority campaign.
4. Authorize one bounded Type-II structural audit under the user's preference for meaningful partial theorems. This addresses the other divisibility pattern; it is not a restart of D-005's stopped coefficient-optimization/existence program.
5. I-010 is a preserved exploratory draft with an explicit supersession and algebraic erratum in I-011. DO NOT cite its incomplete derivations or opening status. Use `ideas/011_type_II_envelope_complete_proof.md` only as the new theorem source.

## Rank 1 / only recommended direction

### 1. Precise mathematical claim

For every prime p=1 modulo 24 and every Type-II solution (exactly TWO p-divisible denominators), smallest denominator X satisfies

    7X<=2p+4.

For every prime p modulo 840 in R={1,121,169,289,361,529},

    11X<=3p+9.

Equality in the residual bound holds exactly, up to permutation, for

    p in R, p prime, p=8 modulo 11,
    (X,Y,Z)=(3(p+3)/11,3p,p(p+3)/11).

The prime 1009 gives (276,3027,92828), attaining 3036 on both sides. No infinite prime assertion is needed.

The proof's extremal lemma is also part of the task: in a Type-II solution write the other denominators pb<=pc, d=bc/X. If b>=m and p>8m^2-7m+1, then (4m-1)X<=mp+m^2, equality iff b=m,d=1.

### 2. What appears new locally

Standard Type-II parametrization and the coarse bound X<=p/2 are already in the pre-existing local Elsholtz–Tao snapshot. I-011 instead combines exclusions of actual smaller p-multiples b=1,2 with a global three-case extremal lemma to get sharp constants 2/7 and 3/11 and all equality triples. These conclusions are absent from the local theorem register and inspected source passages. This is NOT certification of external novelty; an elementary corollary may already be known.

The equality identities themselves are not advertised as new residue coverage. The six classes enter only through p=1 modulo 24 and p modulo 7 in {1,2,4}; complementary modulo-840 coverage remains a separate unaudited obligation.

### 3. Smallest useful proof target — the ONE main task

Independently audit I-011 Sections 2–5 and return a short self-contained H-006 proof note or an exact counterexample.

Required checks:

* Obtain p/4<X<p, hence gcd(p,X)=1, directly from ordering.
* Derive X|bc, d=bc/X, (4b-1)c=pd+b, and d|b^2. Do not assume p∤b, p∤c, or p∤d.
* Check the exact cross-product

      (mp+m^2)(4b-1)-(4m-1)(pb+b^2)
        =(b-m)[p-(4m-1)b+m].

* Prove the three exhaustive cases b=m, m<b<2m, b>=2m. In the final case use c>=b; do NOT use false global monotonicity of H_p(b).
* Check b=1 is excluded by p=1 modulo 3, and b=2 with d=1,2,4 forces respectively p=5,6,3 modulo 7.
* Check p>=73 discharges the thresholds 19 and 52.
* Prove both directions of the equality classifications, including smallest denominator, exact type, positivity and integer identity; verify the explicit 1009 residual extremizer and the 313 preparatory extremizer.
* Optional regression: rerun the unchanged `reviews/006_type_II_residual_probe.py` only. Its domain is exactly 858 first saved A certificates in the retained 2991 pairs / 187 primes, the two explicit extremizers, and unchanged H-005 replay/hashes. Do not turn it into an all-completion or expanded-range search.

### 4. Expected incremental result

An independently audited Type-II necessary cutoff

    X<=floor((3p+9)/11)

for every residual prime, with complete equality classification. This complements, rather than replaces, H-005's Type-I cutoff floor((15p-14q(p)+1)/30). A candidate combined structural note is plausible if eventual priority/significance checks support it.

Label the paper theorem **proved** when its audit passes, bounded tests **verified computationally**, and novelty **unresolved**. None of these statements proves that a Type-I or Type-II solution exists for every p.

### 5. Main uncertainty and stop rule

The supplied written proof is complete; independent checking is still the main deliverable. Priority and publishability are unresolved. If an error is found, record the precise failing implication or exact counterexample in a NEW H-006 and stop; do not silently narrow the theorem or repair historical files.

Budget: one proof-audit turn. Do not extend the m-hierarchy, hunt another constant, sweep primes/parameters, formalize/install Lean, or resume the stopped forcing routes. Main may update its own live report/register after returning the audit. Preserve I-010 as a superseded derivation record and H-001 through H-005 unchanged. A rigorous partial theorem, not a full-proof program, is the endpoint.