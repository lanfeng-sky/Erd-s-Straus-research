# R-006 — Accept H-005; audit a sharp Type-II residual envelope

Sequence 006, 2026-10-04. Research question: is H-005 correct on its stated scope, and is there a genuinely different partial result for Type II?

## 1. H-005 verdict: accepted

Read the current report, the local literature register, all three main research records, newest I-009/R-005/D-005, and H-005's complete proof, README, and packaged replay source. The paper proof passes the following adversarial checks.

* **Type and ordering.** The smallest denominator X satisfies p/4<X<=3p/4<p, hence is p-free. In Type I the other p-free denominator and unique p-divisible denominator produce the exact p-adic allocation (0,2) in the two positive factor terms. No p-adic case is missing and the labels do not assume that the unique p-divisible denominator is second-smallest.
* **Full common gcd.** Reducing C/X yields X=guv,C=gu^2,E=gv^2. Integrality of k=(pu+v)/(4X-p) is justified by a coprime cancellation. The equations force gcd(u,k)=gcd(v,k)=gcd(u,v)=1 and p does not divide v. Thus gcd(guv,pguk,gvk)=g, the gcd of ALL three denominators, not merely a pairwise gcd.
* **Character, including p|h.** The local Jacobi lemma is valid for even g and composite moduli with repeated factors. From ph=4guk-1 and hv=u+k one obtains h=3 modulo 4, 4gu^2=-1 modulo h, and (g/h)=-1. The denominator identity (g/(ph))=(g/p)(g/h) does NOT require gcd(p,h)=1. Thus (G/p)=-1 follows without the forbidden extra assumption.
* **Gap.** Ordering and coprimality force k>u. The exact formula p-2X=v(2gu(k-u)-1)/(u+k) and both strict integer-monotonicity identities are correct. The general bound 6X<=3p-2G+1 follows.
* **Residual bound.** At p=1 modulo 24, g>=5 follows from the character of 1,2,3,4. The cases v>=2 and k-u>=2 give the claimed strict inequalities. In v=k-u=1, the modular exclusions u=1,3,5 and h=3 modulo 4 force u>=7. Thus 30X<=15p-14G+1 is valid.
* **Equality.** Strictness leaves exactly u=7,k=8,v=1,h=15. The congruence 224g=16 modulo 360 is equivalent to g=29 modulo 45; positivity gives g=45t+29 and p=672t+433. Both directions, p-divisibility, positivity, the full gcd, and the equality triple (203,232,703192) at 433 check out.

**T-005a/b: proved and accepted within their exact Type-I scope.** Main may close O-009 by citing R-006. O-010 (priority) remains unresolved. No necessary condition has become sufficient.

The old Type-II claim X<=floor((p+1)/4) remains **false** at retained p=1009,X=253>252. It is not an input to either H-005 or the new result below.

## 2. Reproduction and exact bounded evidence

New files:

* `006_type_II_residual_probe.py`
* `006_type_II_residual_results.json`

The script runs directly from the mounted absolute workspace path, reads only the self-contained H-005 snapshot, and does not change historical payloads. All 34 recursive H-005 hashes pass before and after. Its unchanged packaged probe exits 0 with empty stderr and agrees with the saved snapshot output except the H-004 timing field. That replay checks the same 955 first saved B certificates and the separate 433 equality witness; it is not an all-completion census.

The new regression checks exactly the first saved A witness at every successful retained pair: 858 Type-II certificates, all in the six residual classes, drawn from the unchanged 2991 pairs / 187 primes. It verifies exact identities, type, normalization, gcd, both proposed inequalities and normalized equality rules. Zero disagreements and zero equality cases in these saved witnesses. Two algebraically specified extremizers at 313 and 1009 are checked separately. No prime interval, shift window, or parameter search was added.

The wrapper exits 0 with empty stderr in 1,654,334,385 ns. Source SHA256:

    a70b86d77f6619df9841354ce61eed886b078487617977d733b5a3b3197afb14

The result file records Python/platform, source and input hashes, all 34 payload hashes, counts and examples. This is **verified computationally**, not formal verification or a fresh independent agent. Universal assertions rest on the paper proof.

## 3. New theorem and its proof audit

The authoritative new argument is **I-011**, not I-010. For every Type-II solution at a prime p=1 modulo 24,

    7X<=2p+4.

For p modulo 840 in {1,121,169,289,361,529},

    11X<=3p+9,

with equality precisely, within that prime domain, when p=8 modulo 11 and the triple is

    (3(p+3)/11,3p,p(p+3)/11), up to permutation.

At 1009 this is (276,3027,92828), with full gcd 1. It does not extend the Type-I gcd obstruction to Type II.

The proof is elementary and independent of H-005. Write the two p-divisible denominators pb<=pc. Since X<p, the identity forces X|bc. With d=bc/X,

    (4b-1)c=pd+b,
    X=(pb+b^2/d)/(4b-1), d|b^2.

Thus b=1 is excluded by p=1 modulo 3. If b=2, d is 1,2,4, forcing p modulo 7 to be 5,6,3 respectively; these are excluded in the residual domain. Hence b>=3.

The genuinely global step is the extremal lemma: if b>=m and p>8m^2-7m+1, then (4m-1)X<=mp+m^2, with equality iff b=m,d=1. It separates:

1. b=m: exact formula and d>=1;
2. m<b<2m: the positive cross-product

       (mp+m^2)(4b-1)-(4m-1)(pb+b^2)
         =(b-m)[p-(4m-1)b+m];

3. b>=2m: c>=b implies p/X>=4-2/b>=4-1/m, giving strictness.

For m=2,3 the thresholds are 19,52, while a prime p=1 modulo 24 is at least 73. Equality reconstruction in I-011 checks integrality, positivity, ordering, type, and exact reciprocal identity in both directions. No hidden assumption p∤bcd is needed.

**Written-proof status: proved.** A separate main-model audit of this new proof is the one next task. **Search benefit:** Type II at residual primes may use floor((3p+9)/11); Type I retains its separate H-005 cutoff. Neither gives existence.

## 4. Explicit same-round erratum: I-010 is superseded

The exploratory I-010 file was committed before its global optimization was finished. Its opening label 'proved' was overconfident and contradicted by its own concluding status correction. It also contains an incorrect unused difference formula and incomplete proof attempts. Those are not acceptable proof inputs. The general function H_p(b)=(pb+b^2)/(4b-1) is NOT globally decreasing.

I-011 records the exact algebraic correction and gives a clean proof using the split at 2m. I-010 is preserved unchanged, not silently rewritten. Its proposed final bounds are now proved by I-011, but that does not validate the discarded derivations. Main must cite I-011 only and reproduce the extremal lemma independently.

## 5. Offline source comparison and novelty caveat

No network was used. The already present `literature/005_elsholtz_tao_1107_1010v6.html` was inspected locally in Sections 2 and 4. Proposition 2.6/2.7 already give Type-II structural characterizations. The proof of Lemma 2.8 gives n/4<X<=n/2 for the p-free denominator in Type II, and Remark 2.9 discusses the largest denominator's divisibility. Section 4 already proves an odd-square obstruction for Type I and Type II. These are prior facts, not new results from this round.

The sharper 2/7 and 3/11 inequalities and full extremizer classifications are not stated in those inspected passages or the local theorem register. That is only a local observation. The new result is elementary and could be a known or routine corollary elsewhere. **External priority and publication significance: unresolved.** A combined short note with H-005 is plausible, not guaranteed publishable. No bibliography campaign is recommended.

## 6. Decision recommendation

Accept H-005 and preserve all historical handoffs. Assign one bounded, offline Type-II proof/equality audit from I-011, returning H-006 or an exact counterexample. This is a separate divisibility-pattern result, not another Type-I coefficient optimization or an existence-forcing restart. Do not expand to m=4,5,..., enlarge searches, hunt isolated congruence identities, or claim that either bound proves the conjecture. The successfully audited partial theorem is the intended endpoint.