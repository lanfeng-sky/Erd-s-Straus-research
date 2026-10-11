# D-004 — Close U-007 with an obstruction theorem; stop the inverse hierarchy

Sequence 004; 2026-10-04. Known facts used: R-004's acceptance of H-003, KI-002/KI-004, local Jacobi reciprocity, and I-008's new review derivations. **Overall conjecture: unresolved. Pointwise bridge: blocked.** This is a SHORT closure task, not authorization for a full round of parameter enumeration or another inverse lemma.

## Decisions now in force

1. **Accept H-003.** Main may close O-007 with a link to R-004. Specialized O-005 is closed by the elementary binary-growth proof; general Kneser remains unaudited and unnecessary. Preserve all frozen handoffs and historical entries.
2. **Archive the deficiency hierarchy.** T-003 is a sound local theorem. No result forces its hypotheses at an arithmetically useful shift. Do not request N=m-3, a larger abstract group, or a longer offset window.
3. **Reject the normalized U-007 construction as a universal proof route.** Its algebra is valid, but it is exactly the u=1/nested-denominator restriction of A. Complete restricted-family tests already fail at the prime 193, even though a non-nested A certificate exists. The failures at 2521 and 66529 are also complete for this family, not bounded-window artifacts.
4. **Defer ill-specified variants.** The half-decomposition and other unstable screenshot formulas have no exact local specification. Do not silently attribute I-008's completeness or obstruction theorem to every possible variant.
5. **Do not expand computation or literature.** No new primes, squares, group orders, c/M/g/k ranges, isolated classes, or almost-all estimates. In particular no repeat of the 100001² search: the Jacobi obstruction excludes the normalized family for EVERY square.

## One bounded main task: T-004, independent obstruction/separator audit

### What is new and why it is worth retaining

The key useful addition is not another identity. It is a rigorous explanation of why the newest restricted construction cannot be universal, plus an exact character distinction between the existing A and B mechanisms. It prevents a large but unproductive search campaign and keeps the omitted branch visible. No literature-priority claim is made; Rosati-type parameter algebra and reciprocity are known foundations.

### Exact target theorem to audit

**Part I — uniform obstruction.** For EVERY positive g,h, M=4gh-1 satisfies

    Jacobi(g,M)=+1,       Jacobi(-g,M)=-1.

Consequently, for EVERY positive n,g,u,v,k satisfying

    u+v=k(4guv-n),

put a=4guv-n>0. Then

    n=(4guk-1)a-4gu²,
    gcd(n,4guk-1)=1,
    Jacobi(n,4guk-1)=-1.

In particular NO positive square n belongs to this switched family. Include even g, composite M, repeated prime factors, and u>1; do not prove only the nested special case.

**Part II — exact distinction of the two branches.** For EVERY prime p=1 mod 4, p/4<x<p, a=4x-p, normalize any KI-002 witness C|x² as

    x=guv, C=gu², gcd(u,v)=1.

Then A has k=(u+v)/a and

    p=(4guk-1)a-4gu²,      Legendre(4guk-1,p)=-1,
    (x,y,z)=(guv,pgku,pgkv).

B has k=(pu+v)/a, and some positive h satisfies

    4guk-1=p h,    hv=u+k,
    (x,y,z)=(guv,pguk,gvk).

Check both converse constructions, integrality, positivity, gcd normalizations and 4xyz=p(xy+xz+yz). Explain that A/B use DIFFERENT k values in general. Do not infer that one fixed tuple represents all solutions.

**Part III — scope closure, not a new theorem hunt.** Confirm the normalized user equation n=a(4ck-1)-4c is exactly u=1 in Part I. Check the derived bound ck<=(n+3)/8 for n=1 mod 4, the M-method's boundary case r=M-1, and the short 193 no-witness certificate in I-008. It suffices to inspect the already retained six-value records; no further enumeration is needed.

### Executable instructions and strict stop

- Read I-008 and R-004; audit the displayed proofs independently rather than copying their conclusion labels.
- Use at most TWO short approaches: direct reciprocity/algebra, then a small explicit counterexample if a claimed converse or gcd condition fails. No broad search.
- Optional reproduction is ONLY `reviews/004_audit_probe.py`, which runs the existing H-003 checks and the six named inputs. Its results are already saved in `reviews/004_reproduction.json`. Use mounted paths directly; no network or project-external evidence.
- If a claim is false, record the exact counterexample, correct the status in a NEW handoff, and stop. Do not repair it by inventing narrower hypotheses during this task.
- If all claims pass, write a concise new frozen `handoffs/004_construction_obstruction/` containing the proof audit, exact scope, and links/copies of the minimal necessary existing evidence. Update only main-owned live records/report, close O-007, and retain the conjecture-level obligation as open.
- Budget: one SHORT main-model turn. Do not consume a research round rederiving the classical parameterizations already proved locally. No proof-assistant installation or literature-novelty project is required.

## Main obstruction and restart gate

The shared expression M is suggestive but does not force a certificate:

    A needs M | (p+4gu²), not merely Legendre(M,p)=-1;
    B needs p | M AND (M/p) | (u+k), not merely p | M.

This is still pointwise bounded-divisor arithmetic. No transition between the two alternatives, monotone descent, or cross-shift invariant has been established. **Do not assign a new existence conjecture merely because the formulas look symmetric.**

A subsequent proof-directed task may be proposed only after exhibiting an exact arithmetic implication that forces one of these conditions for EVERY prime in a stated genuinely broader domain, or a concrete different construction with a credible pointwise bridge. State its universal quantifiers, the extra input beyond the known parameterization, and a first falsification test. A new residue class, finite success count, or average theorem does not satisfy this gate.

If T-004 finishes without such an implication, retain the obstruction/separator as an audited local result and STOP this route. Reporting **blocked** is the intended successful closure, not permission for an open-ended hierarchy.
