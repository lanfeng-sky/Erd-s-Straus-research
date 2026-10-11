# R-003 — Accept H-002; remove an unnecessary dependency; retain the pointwise gap

Sequence 003; 2026-10-04. Research question: are H-002's fixed-x/switch results and computations sound, and is there an incremental mathematical route beyond them? Read all required root/main files, latest ideas/reviews/decisions, H-002 proof/source/records and local literature. **Verdict: accept H-002 within its stated scope. Overall conjecture unresolved.** Historical files and both handoffs were not changed. No network was needed.

## 1. Submitted elementary mathematics — proved, accepted

- For prime p=1 mod 4 and p/4<x<p, a=4x-p is odd and gcd(a,px)=1. In a completion d=ay-px and e=az-px are positive, since dz=px*y and ey=px*z. Their product is p^2*x^2. These sign checks correctly rule out negative-factor artifacts.
- Primality and x<p imply p does not divide x, so the allocations 1+1, 2+0, 0+2 are exhaustive. Cancelling units yields exactly A: c=-x mod a and B: 4c=-1 mod a, c|x^2. No third branch is missing.
- Both reconstruction formulas in the report are integral and positive. In B, E=x^2/c=-px mod a, p divides y and does not divide z; the certificate follows from the factor pair (p^2*c,E). In A both reconstructed denominators are divisible by p.
- The ratio set R={c/x:c|x^2}=DD^{-1} is inverse-closed, not presumed product-closed. Inverting -p^{-1} legitimately converts the second target to -p.
- The global interval [(p+3)/4,floor(3p/4)] follows by sorting an existing solution. The fixed-x iff is unordered; filtering y,z>=x outside x<=p/2 would invalidate it. The submission states the distinction correctly.
- KI-004's switched expansion and division-free certificate are correct for all stated positive integer parameters. Reducing c/x=u/v proves uv|x and a|(u+v); g=x/(uv), k=(u+v)/a recover the exact A denominators. Conversely the switched relation implies the A congruence in the stated prime/x domain. Restricting g=1 is not completeness.

No sign, p-adic, normalization, or boundary defect found. The elementary content is mainly a careful classical factorization/Rosati-type reformulation; this is NOT evidence of literature novelty or a universal construction.

## 2. Conditional submission and new elementary replacement

H-002's Kneser application is valid conditional on its explicitly stated finite theorem. Quotient aperiodicity, persistence of partial-product periods, multiplicity counts, the ACTUAL stabilizer, and the odd-order conclusion are all used correctly. The reported primary-proof audit gap is honest.

**New result this review, proved:** general Kneser is unnecessary for the binary products actually used. If S=product {1,w_i} and K=Stab(S), then |S|>=|K|(1+#{i:w_i not in K}). In the quotient, each nonidentity binary step must grow, since otherwise it creates a period that persists to the final set. Full proof: [I-005, Section 1](../ideas/005_elementary_joint_growth.md).

Therefore KI-003's specialized conclusion can now be promoted to **proved by a separate elementary argument** after main audits this replacement. This does NOT mean Kneser's general theorem has been audited; L-002 and H-002 remain unchanged as historical evidence. O-005 need no longer block the specialized saturation result.

## 3. Computation — verified computationally, accepted on exact domain

Executed the mounted frozen scripts directly under Python 3.12.3, no -O and no writes:

    python3 "$W/handoffs/002_structure/audit_structure.py" --check "$W/handoffs/002_structure"
    python3 "$W/handoffs/002_structure/check_structure_records.py" "$W/handoffs/002_structure"

Here W is the absolute attached flagship path. Both returned PASS, exit 0. The first reproduced all deterministic files byte-for-byte, the second used direct divisor scans and checked hashes. The new flagship probe independently verified every entry of SHA256SUMS, including proof/source/metadata payloads.

| Check | Reproduced result |
|---|---:|
| Exact pairs | 2991 |
| Both / A-only / B-only / neither | 757 / 101 / 198 / 1935 |
| Factor-pair branch disagreements | 0 |
| Quadratic / other subgroup / bounded exponent failures | 1059 / 465 / 411 |
| Compact / full-factor certificates checked by generator | 6064 / 4285 |
| Saved branch witnesses checked by direct scanner | 1813 |
| Switched candidates / solved specified primes | 147 / 7 |
| Prime-defect A failures under -1 in H | 342, including 89 B successes |

Source review confirms complete divisor exponent boxes, independently scheduled factorization of px, the exact d<=px factor-pair bound, independent trial primality versus sieve domain selection, and no early stop across offsets. The direct scanner does not independently rederive every scalar summary field or full factor-pair count; the generator's separate exhaustive path and byte comparison supply those checks. This distinction is not a rejection, but prevents overstating algorithmic independence.

The reported counterexamples C1 at (1129,t=12,13) and C2 at (2521,ell=11,19) reproduce. Their 'smallest' qualifier is only within the prescribed dataset. The previously missing 118801 offsets t=8,...,13 are now exhaustively audited along with t=0,...,7; first hit remains t=14. Seven switch successes do not imply any universal g,k bound.

Observed runtimes: generator 1544425307 ns; direct scanner 2427108923 ns, excluding tool startup. Exact hashes/results retained in `003_reproduction.json`. This is reviewer-model reproduction and source inspection, not a proof-assistant build or a fresh independent sub-agent.

## 4. What is actually new relative to this desk

### Proved incremental results

1. **Elementary dependency removal:** the binary growth proof above.
2. **Joint failure structure:** S=D union pD satisfies A or B iff S intersects -S. Applying binary growth to S keeps both branches and adds the p occurrence to the deficiency count. As a divisor-set encoding this is classical; the useful incremental work is its joint inverse-structure analysis.
3. **Rigidity and parity:** minimal growth in the aperiodic quotient forces every nonidentity occurrence into {g,-g}. The identity px=4x^2 mod ell makes the total quotient exponent even. Hence odd occurrence count requires an extra unit of growth. These are proved in I-005, including all cyclic/odd-stabilizer hypotheses.
4. **Cross-shift character identification:** for EVERY q|x, Jacobi(q,4x-p)=Legendre(q,p), including q=2. Thus a successful x must contain a nonresidue prime factor modulo the fixed p. The least such prime q is <sqrt(p), by a short elementary argument, and every q consecutive admissible x contains a multiple of q. This escapes one obstruction pointwise, NOT all obstructions. See [I-006](../ideas/006_reciprocity_across_shifts.md).

These are mathematically meaningful local improvements, but not a decisive reduction to a known solvable problem. No literature priority claim is made; reciprocity, divisor collisions, and least-nonresidue reasoning are standard foundations.

### False / blocked

- **False:** the first q offsets must solve p when q is its least nonresidue. Already p=118801 has q=13 and no hit in t=0,...,12. The forced multiple at t=4, x=29705, has full H modulo 19 yet misses both targets. No larger-window repair was attempted.
- **Blocked:** residue-only forcing. A pointwise nonresidue factor does not supply enough exponents to hit either target.
- **Blocked:** broad saturation as a universal program. Sparse quotient occurrence counts remain far below all available bounds; no theorem forces a saturated shift.
- **Unresolved:** an exact one-extra-element inverse theorem, stated in I-005 Section 6. It passed a bounded abstract test, but is not promoted to proved.

### New finite diagnostic, not a range extension

`003_joint_probe.py` checks the existing 2991 records only. The joint sufficient condition certifies 106 prime-defect pairs, 33 beyond the previous A-only sufficient test; these are NOT new primes solved. All 253 joint failures in the prime-defect domain have the predicted deficiency; 14 critical equalities satisfy the rigid pattern. A fixed-character obstruction explains 1485 failed pairs, including 463 formerly labeled other subgroup.

For the proposed inverse lemma, 175036 nondecreasing sequences in four groups C_6,C_10,C_14,C_18 were visited, 84 met all hypotheses, zero counterexamples. It is **verified computationally only there**. A draft filter confused 'm absent from subset sums' with 'm absent from their differences'; this was detected and corrected before the retained results, documented in I-005. That development error is not hidden as a theorem counterexample.

## 5. Decision and strongest remaining gap

D-002 is complete and accepted. Preserve H-002. No wider prime search, longer switch window, or Kneser primary-paper project is justified next.

Authorize only D-003's bounded proof-or-counterexample task: classify the next-to-critical joint obstruction, with an exact cyclic-group theorem and an explicit arithmetic specialization. Stop if it fails or no short proof route remains; do not iterate unquantified variants.

**Strongest result this round:** unconditional elementary joint-branch saturation plus critical rigidity/parity, and a fixed-character comparison across shifts. **Exact unsolved obligation:** for EVERY target p, force a shift where BOTH the character and bounded-exponent obstacles are overcome, or construct a solution outside this mechanism. Neither the new inverse target nor its finite verification presently supplies that theorem. Erdős–Straus remains **unresolved**.