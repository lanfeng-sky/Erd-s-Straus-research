# H-004 — Construction obstruction / A–B separator audit

Frozen main-model submission, 2026-10-04, under D-004. **T-004 proved** by
exact algebra and Jacobi reciprocity. **Universal normalized U-007 coverage:
false.** One auxiliary equality in I-008 is also **false**, with its exact
counterexample/correction retained below. No narrowed hypotheses, novelty,
Lean, network or fresh-agent claim. Erdős–Straus **unresolved**; pointwise
forcing **blocked**. This is a closure package, NOT a conjecture proof.

## Claims and scope

1. For EVERY positive integer g,h, M=4gh-1 has (g/M)=1 and (-g/M)=-1.
   Thus for EVERY positive n,g,u,v,k with u+v=k(4guv-n), a=4guv-n>0,
   n=(4guk-1)a-4gu² and (n/(4guk-1))=-1, with gcd=1. **No positive
   square n** occurs in this family. Even g, composite/repeated-factor M,
   u>1 and noncoprime u,v are included.
2. For EVERY prime p=1 mod 4 and p/4<x<p, normalize a KI-002 witness
   C|x² as x=guv,C=gu²,gcd(u,v)=1; set a=4x-p. A has
   k=(u+v)/a, p=(4guk-1)a-4gu², Legendre(4guk-1,p)=-1.
   B has k=(pu+v)/a, 4guk-1=ph, hv=u+k, and Legendre(4guk-1,p)=0.
   The positive integral triples are respectively (guv,pgku,pgkv) and
   (guv,pguk,gvk). Both normalized converses and
   **4xyz=p(xy+xz+yz)** are proved. The k values need not agree.
3. n=a(4ck-1)-4c is exactly the u=1/nested restriction of A. For n=1
   mod 4, a>=3 and ck<=(n+3)/8; the complete residue method includes
   r=M-1 -> c=(M+1)/4. The retained prime 193 has NO such parameters
   but DOES have the non-nested A certificate (50,1930,4825).

`proof_audit.md` contains the self-contained derivation, quantifiers,
normalization, denominator checks, converse conditions and limitations.
The only named standard number-theory input is elementary Jacobi reciprocity
and its supplementary laws. No external project file is needed to read it.

## Explicit erratum — historical files NOT overwritten

I-008 section 2 states n-x=c(3ak-4)-a, which is short by c. At its own
retained n=1009,(a,c,k)=(3,11,8), x=253:

    n-x=756, but c(3ak-4)-a=745.

Correct SAME-domain algebra: n-x=c(3ak-3)-a>=2a-3>0. Positivity and
the target theorem remain valid without additional assumptions. This is
recorded as a false ancillary claim, not silently repaired in I-008 or R-004.
D-004's stop rule is honored: no further lemma, search or existence hypothesis.

## Computation / reproducibility

Only the authorized flagship R-004 probe was rerun on its original domain.
Its source, exact stdout, empty stderr and environment are preserved here;
H-003's eight payload hashes and both frozen outputs matched. Historical
handoffs were not modified. The six named restricted-family tests remain:

| n | Complete (c,k) candidates | Complete h candidates | Witnesses |
|---|---:|---:|---:|
|193|60|24|0|
|1009|450|126|2|
|1129|513|141|2|
|1201|553|150|2|
|2521|1314|315|0|
|66529|52762|8316|0|

No new n, squares, offsets, groups or parameter ranges. Two complete
schedules agree within this RESTRICTED family. Bounds/pruning are proved
in `proof_audit.md`. Finite no-hit results are not conjecture counterexamples.

Python 3.12.3, Linux aarch64/glibc 2.39; exact integers, assertions enabled;
direct mounted Android workspace. Authorized reproduction exit 0, empty
stderr, elapsed 51243731388 ns. Additional retained-evidence auditor exit 0,
empty stderr, elapsed 500996385 ns. Full commands/source/output hashes are
in the two environment payloads; absolute paths there are provenance only,
NOT runtime dependencies.

Standalone reproduction (replace the path prefix with the actual mount):

    python3 <absolute-path-to-this-handoff>/check_retained.py

It uses ONLY sibling payloads, no project imports or external paths. It checks
source/stdout provenance, all six positive U certificates, the non-nested
193 A certificate, all 24 existing residue cases at 193, and the erratum on
the retained 1009 witness. It does NOT reenumerate the other (c,k) domains:
their no-hit counts retain the authorized two-schedule generator's provenance.
`authorized_probe_source.txt` is an inert source snapshot, not the standalone
entry point; the full historical probe is unnecessary to run this handoff.
Saved output is `retained_check_stdout.json`. Payload integrity:

    (cd <absolute-path-to-this-handoff> && sha256sum -c SHA256SUMS)

## Limits / review request / stop

Universal square exclusion concerns the switched family only. The separator
is a FIXED-X equivalence, not a forcing theorem. A nonresidue M does not
force M|(p+4gu²); p|M does not force (M/p)|(u+k). Undefined screenshot
half-decomposition variants cannot inherit this audit's conclusions.
No complementary modulo-840 coverage audit was performed.

H-003 accepted R-004; O-007 closed. Flagship: review this NEW audit and its
explicit ancillary erratum, then run the standalone checker. Freeze means
no future edits to H-004; any correction requires a new sequence. This route
stops **blocked**. Restart requires a genuinely new universally quantified
pointwise arithmetic implication, not more successful examples.