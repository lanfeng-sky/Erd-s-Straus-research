# R-008 — Signed-character synthesis, composite scope, and stalled execution

Sequence 008, 2026-10-05.

Research question: whether the latest intrinsic character results support a substantive structural extension rather than another search cutoff.

## 1. Workspace and historical audit

Read the policy/README, full main report, local theorem digest, all three live main research records, newest I-012/R-007/D-007, authoritative I-011, I-006, and H-005's complete proof and README. Used local grep/context inspection before creating new files. No network access, outside-workspace evidence, installation, or historical overwrite.

The main report still ends at H-005. No H-006 or later submission was present in the handoff listing. R-006/R-007 already accepted H-005; main's separate audit of the flagship Type-II notes remains pending. New notes must not turn that missing handoff into an implied completed audit.

H-005 remains sound on the inspected paper proof: the (2,0) p-adic allocation derives B, all three normalized auxiliary parameters are pairwise coprime, g is the FULL common gcd, Jacobi multiplication permits p dividing h, ordering forces k>u, and the three-case gap proof has the stated equality iff (u,k,v,h)=(7,8,1,15). The false Type-II cutoff remains excluded.

I-011's exact cross-product and split at 2m resolve its earlier draft's optimization gap. I-012 correctly transfers the auxiliary character to X/G and proves its parity-sensitive ceilings. Neither paper argument is invalidated by the present extension. No numerical replay or hash-manifest reproduction is claimed in this round.

## 2. New mathematical finding

Authoritative new proof: `ideas/013_signed_jacobi_clean_types.md`, T-008.

For 4c/n, with c positive, n>=3 odd, gcd(c,n)=1, and G the full denominator gcd:

* Clean I: n|Y, gcd(n,XZ)=1 implies Jacobi(-cG,n)=-1.
* Clean II: n|Y,Z, gcd(n,X)=1 implies Jacobi(-X/G,n)=-1.

For the two same-status denominators U,V, reduce r=U/gcd(U,V), s=V/gcd(U,V). In both types gcd(rs,n)=1 and Jacobi(-rs,n)=-1. At n=1 mod 4 the reduced pair has opposite Jacobi signs, so U/V is not a rational square.

This statement handles general numerators 4c and odd composite n under explicit clean hypotheses; at primes those types exhaust all solutions. It is NOT a new existence criterion. It recovers the existing numerator-4 prime character theorems and the known-type odd-square obstruction.

**Status: proved on paper**, with a separate main-model audit requested. This review is same-model adversarial checking, not a fresh independent reviewer or formal proof.

## 3. Adversarial proof checks

1. **No smallest-denominator assumption needed.** Positivity alone gives a=4cX-n>0. Coprimality gcd(a,nX)=1 follows from gcd(c,n)=gcd(X,n)=1. All cancellation premises are stated.
2. **Composite type labels repaired explicitly, not silently generalized.** Clean I requires every prime factor of n absent from both free denominators. Then E=aZ-nX is a unit modulo n and DE=n^2X^2 really forces n^2|D. Merely counting multiples of composite n does not do this.
3. **Clean-II valuations.** Dividing D,E by n gives CF=X^2, a product coprime to n. No assertion that the original denominators have exactly the valuations of n is needed.
4. **Full common gcd.** The normalized triples and pairwise coprimality give g=G in both types. The pairwise gcd H in the reduced-pair statement is a DIFFERENT invariant and is explicitly computed: H=Gv in I, H=nGk in II.
5. **Numerator twist.** In I the Jacobi lemma applies to b=cG, not b=G. The example 8/5=1+1/10+1/2 has G=1 and refutes omission of c.
6. **Reciprocity sign.** M=4cGuk-1 is 3 mod 4. Reversing odd composite n and M contributes (-1/n); this yields signed negative characters for all odd n, not unsigned negative characters when n=3 mod 4.
7. **Shared n,h factors permitted.** In I, M=nh and 4cGu^2=-1 mod h. Multiplicativity in the Jacobi denominator does not require gcd(n,h)=1. The case h=1 is included by the standard symbol convention.
8. **Nonunit k permitted in II.** Character transfer uses Mv=nk+u and cancels only the unit v, never k. The paper example 4/15=1/4+1/90+1/180 has k=3. This is a real composite distinction, not an invitation to contradict the prime p^2-valuation exclusion in the local literature.
9. **Reduced-pair conclusion.** Clean-I reduced pair is (u,k), whose product character equals (cG/n); clean-II reduced pair is (u,v), whose product character is -(-1/n). This proves a single intrinsic formula. A rational-square ratio has coprime square numerator and denominator, so it is excluded precisely on the stated n=1 mod 4 domain.
10. **Jacobi is not Legendre at composite n.** No positive-Jacobi converse or per-prime negative-sign assertion is made. The n=93 example has different local signs at 3 and 31. The clean square-n exclusion does not exclude unrestricted square-n solutions: 4/9=1/3+1/12+1/36 is outside both clean types.

The scope examples in I-013 were derived and checked by displayed rational/integer arithmetic on paper. They are not labelled verified computationally.

## 4. Execution incident and evidentiary limits

One `code_runner:run_python` call attempted to read and parse the existing local HTML source in memory, using only standard-library imports. The call returned no execution result; the user reported a freeze. The submitted script contained no writes, subprocess creation, network calls, or installations.

No subsequent interpreter job, retry, replay, or process-control operation was launched. Whether the underlying process exited is UNKNOWN. The failure cause was not diagnosed; it must not be attributed confidently to regex, package infrastructure, or device load.

Do not infer successful execution, parsed source coverage, a test pass, timing, or fresh source-level originality evidence from that missing result. Continued work used ordinary file tools and paper derivations only. File-tool responses confirm creation of the new notes; they do not establish the state of the stalled process.

## 5. Originality and recommendation

The limited local markdown comparison does not display T-008's signed general-numerator/composite intrinsic statement or its uniform reduced-pair obstruction. The normalization and Jacobi lemma are standard/local-known inputs. The odd-square result is already known in the source digest; recovering it is not a novelty claim. The HTML snapshot was not fully re-parsed in this round.

External priority: **unresolved**. Value as a short synthesis with H-005/I-011/I-012: **plausible**, not established. The new result is an elementary consequence of standard structure, so modest claims are essential. No universal construction, new congruence coverage, or empirical range extension is asserted.

One concrete main task: independently audit I-013 Sections 3–6 and return a self-contained synthesis handoff, or an exact failing implication. Incorporate the still-pending Type-II audit into that submission rather than launching another direction. No computation is required, especially while the execution environment's state is uncertain.