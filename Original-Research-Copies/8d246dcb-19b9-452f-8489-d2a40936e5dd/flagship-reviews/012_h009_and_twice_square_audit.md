# R-012 — Accept H-009; audit the twice-square extension

Sequence R-012, after R-011/D-011. Inputs read: root policies and report; literature/key_results.md and primary_source_comparison_notes.md; main/ live records; latest I-015/R-011/D-011; all three H-009 files. Focused local searches were used before writing. No network, terminal, computation, Lean, or fresh-agent review was performed.

## 1. Verdict on the submitted H-009

**Accept H-009/T-010 within its exact hypotheses. O-020 is discharged by this review: proved.** Main should reconcile the live pending notice during its next update. Historical files, including H-009 and the main report, have not been modified by this review.

### Normalization and full gcd

- With a=4cX-n, positivity and gcd(cX,n)=1 give a>0 and gcd(a,n)=gcd(a,X)=1.
- D=aY-nX and E=aZ-nX are positive and DE=n^2 X^2. In Clean I, E is a unit modulo n, so the entire valuation 2v_ell(n) lies in D at every ell|n. In Clean II, dividing D,E by n gives a product X^2, whose factors are units modulo n. This works for composite n and repeated prime factors.
- Reducing C/X gives C=gu^2, X=guv, F=gv^2. Integrality of Y and gcd(a,ngu)=1 justify introducing integral k. The displayed equations force pairwise coprimality of u,v,k.
- The full gcd is indeed g=G in both normal forms, whereas the same-status pairwise gcd is Gv in I and nGk in II. Clean I has gcd(k,n)=1; Clean II need not.

### Character prerequisites

- J(b,4bt-1)=1 follows from reciprocity prime by prime, with even b handled by 4bt-1=7 modulo 8. Thus J(-b,4bt-1)=-1.
- Clean I uses M=nh and hv=u+k. The deduction J(cG,h)=J(-1,h) is valid, including h=1. Multiplicativity in the denominator does not require gcd(n,h)=1. The retained numerator c is essential.
- Clean II has n=Ma-4cGu^2 and gcd(M,n)=1. The reciprocity sign is correct. Only the unit square v^2 is cancelled in passing from Mv^2=uv modulo n to J(-uv,n)=-1. No cancellation of k occurs.

### All six pair cases

- Clean I ratios u/k, v/(nk), nu/v are reduced. Either cross square forces odd-square n because the relevant parameters are units modulo n. This contradicts the negative unit Jacobi symbol. A same-status square forces J(-1,n)=-1.
- Clean II ratios u/v, v/(nk), u/(nk) are reduced even for nonunit k. A cross square gives nk square. The kernel d consists of primes with ODD exponent in n, not rad(n). Exponent parity gives n=d w^2 and k=d t^2, hence d|k|u+v. The local square implication at primes dividing d and the square-modulus factor yield the claimed contradiction. This includes d=1 and gcd(d,w)>1.
- Therefore the n=1-modulo-4 all-pairs conclusion has exactly the stated clean domain. The non-clean witness at n=21 does not contradict it.

No failed implication was found. This is an ordinary mathematical review, not a claim of machine verification.

## 2. Important correction to the previous status language

H-009 correctly repairs the ambiguous categorical entries in I-015, R-011 and D-011 that marked sufficiency of n=3 modulo 4 as false without preserving quantifiers.

At c=1, the statement

    n=3 modulo 4 implies existence of SOME clean square-pair representation

is **proved and true**, by (t,2nt,2nt), t=(n+1)/4. What is false is that every clean representation must contain a square pair, or that n=3 modulo 4 suffices for arbitrary-c solvability. The old categorical wording is not safe as a standalone statement; future ledgers must use the corrected quantifiers, not repeat it unqualified. Historical records remain untouched.

## 3. New proposal I-016 / T-011: adversarial paper audit

The separate idea file supplies a full proof of one adjacent exact classification:

    some representation of 4/n has a ratio in 2 Q_{>0}^2
      iff some representation has a pair in exact ratio 2
      iff n has a prime divisor 5 or 7 modulo 8.

Necessary direction: arbitrary c>=1, odd n>=3, no clean or gcd(c,n)=1 premise. Converse: c=1 only. Its complementary clean localization is also proved using H-009's accepted characters. This is a mathematical extension proposed under the current user assignment; it is not prior acceptance of a main-model handoff that does not yet exist.

### Delicate checks that pass

1. **Orientation.** After taking the pairwise gcd, a twice-square pair is Hr^2,2Hs^2, with gcd(r,s)=1 and r odd. Both orientations of the original pair are included. The 2-adic exponent on the even side may be any positive odd exponent.
2. **Reduced fraction.** For S=r^2+2s^2, gcd(S,2r^2s^2)=1. The reduced reciprocal sum is (S/g)/(2(H/g)r^2s^2), g=gcd(S,H). Its denominator is even, regardless of H's parity.
3. **The new parity step.** A=4cX-n and delta=gcd(A,nX) are odd. Thus an even reduced denominator nX/delta forces X even. This is what permits A=-n modulo EIGHT; merely knowing A=-n modulo four would not prove the new obstruction.
4. **Character sign.** Every prime in alpha=A/delta divides a primitive r^2+2s^2, and is 1 or 3 modulo 8. With chi=chi_{-8}, chi(alpha)=1 and chi(A)=-chi(n). Consequently chi(n delta)=-1. The proof asserts prime support of delta, not delta|n, and does not assert chi(n)=-1.
5. **General numerator.** The support argument never divides by c and survives gcd(c,n)>1. c is an arbitrary positive integer, not assumed odd.
6. **Converse certificates.** For n=mq, q=5 modulo 8, t=(q+3)/8, the triple (2mt,mqt,2mqt) is positive integral and has division-free certificate 16m^3q^2t^3. For q=7 modulo 8, t=(q+1)/8, the triple (2mt,3mqt,6mqt) has certificate 144m^3q^2t^3. Both contain exact ratio 2.
7. **Clean-II hazard.** A cross twice-square ratio gives even valuation in nk at each odd prime dividing n. Thus the exponent-parity kernel d divides k. From d|u+v one directly gets -uv=v^2 at each prime of d, contradicting J(-uv,n)=-1. This requires neither k invertible modulo n nor a square parameter on a specified side. d=1 is included.
8. **Clean same-status conclusion.** A twice-square reduced ratio r/s has rs=2h^2. The signed-pair character forces J(-2,n)=-1, precisely n=5 or 7 modulo 8.

### Attempts at overstatement and their boundary witnesses

- **False:** unrestricted twice-square existence forces n=5 or 7 modulo 8. At n=25, (10,25,50) is a valid non-clean counterexample to that extrapolation, not to Erdős–Straus.
- **False:** prime-support allowance forces a pair in every solution. At n=7, (2,28,28) has no twice-square pair.
- **False:** the reduced numerator condition plus even X is sufficient at a prescribed X. At n=5,X=4, alpha/beta=11/20. The primitive denominator condition would force r^2s^2|10, then r=s=1 and alpha|3, a contradiction. An ordinary completion (4,2,20) exists.
- **False:** the c=1 converse extends to all c. At c=4,n=5, 16/5>3 precludes any representation.
- **Proved distinction:** n=9 admits square pairs but no twice-square pairs; n=5 admits twice-square pairs but no square pairs. The extension is not just renaming T-009.

## 4. Local originality audit, deliberately limited

The local digest includes the standard 5-modulo-8 identity and general two-term factorization; the comparison memo records equal-denominator prior art and type/character methods. I-014/T-009 treats rational-square pairs, and I-015/T-010 treats their clean localization. The exact twice-square iff, unrestricted parity argument and clean corollary are not stated in those inspected records.

This supports only **an increment relative to the inspected local register**. This round did not line-audit all retained HTML sources, acquire missing Monks–Velingker/Jiang texts, or certify external priority. Known identities, scaling, elementary character laws and standard normalization are not new claims. T-011 adds no newly solved residue class, because its sufficiency classes are already classically covered. Its potential value is a classification and restricted-method obstruction.

## 5. Strict ledger and recommendation

- **proved:** H-009 acceptance/O-020; corrected c=1 existential statement; T-011a/b/c in I-016's written derivation and the above audit.
- **verified computationally:** none in this review.
- **conditional:** none.
- **plausible:** T-011 as a compact extension of the structural note.
- **blocked:** external-priority certification under the offline rule; old universal pointwise-forcing routes.
- **false:** the explicitly quantified extrapolations in Sections 2–3.
- **unresolved:** main integration and separate review of a future H-010; external priority; standalone publishability; Erdős–Straus.

Recommend one bounded proof-only task: independently rederive and freeze I-016 as H-010, including the scope witnesses and clean corollary. Do not start a squareclass hierarchy or numerical search. D-012 specifies this narrow next task and supersedes the prior stop only to that extent.