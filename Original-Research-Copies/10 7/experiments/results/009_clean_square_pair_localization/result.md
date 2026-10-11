# D-011 — Proof-only result and evidence boundary

Date: 2026-10-06. Conclusion: **proved** T-010 within its clean hypotheses; Erdős–Straus **unresolved**.

## Objects and method

c>=1, n>=3 odd, gcd(c,n)=1; positive integers X,Y,Z with 4cXYZ=n(XY+XZ+YZ). Full G=gcd(X,Y,Z). Main rederived the D,E factorization and normal forms:

    I:  (Guv,nGuk,Gvk),    (4cGuv-n)k=nu+v;
    II: (Guv,nGku,nGkv),   (4cGuv-n)k=u+v.

Pairwise-coprime u,v,k; gcd(uv,n)=1 in both types and gcd(k,n)=1 only in I. Exact Jacobi derivations give J(-cG,n)=J(-uk,n)=-1 in I and J(-uv,n)=-1 in II. All six unordered pair cases were audited.

**proved:** cross-status square pairs are impossible in either clean type for every odd n. A same-status square pair forces n=3 modulo 4. Thus at n=1 modulo 4 every clean representation has all three unordered pairwise ratios nonsquare; a successful square-pair representation there must be non-clean under every permutation. Mixed prime support and repeated prime factors are allowed.

Clean-II cross pairs use d, the product of primes with odd exponent in n. If nk is square, n=d w^2 and k=d t^2. From k|u+v and one of u,v square, the negative of the other is a square at every prime of d, contradicting the signed Jacobi identity. d=1 and gcd(d,w)>1 cause no gap. No nonunit k is cancelled modulo n.

## Evidence classification and scope

- **proved:** ordinary symbolic arithmetic and Jacobi reciprocity; paper scope checks of inherited n=3,7,15,21,93 examples. No experiment is a theorem premise.
- **verified computationally:** no new claim. No script, replay, search interval, denominator range, parameter sweep or numerical runtime.
- **conditional:** no unproved dependency.
- **false:** cross extrapolations such as unit k in Clean II, squarefree kernel=radical, square pair in every clean representation at n=3 mod 4, or arbitrary-c sufficiency from n=3 mod 4. These failures do not refute Erdős–Straus.
- **proved:** the standard c=1 existential clean-II equal-pair identity at n=3 mod 4 remains valid. The ambiguous historical sufficiency denial was qualified, not reproduced as a universal existential denial.
- **plausible:** value as a compact strengthening of the existing structural note.
- **blocked:** external-priority certification under the offline rule; historical forcing routes.
- **unresolved:** new H-009 presentation review O-020, external priority, standalone publishability, Erdős–Straus and prior parser process state (not investigated).

Access was local on 2026-10-06. Only Android workspace file tools were used; no terminal/interpreter execution, network, installation, Lean, process control, hash validation or fresh-independent-agent review. Architecture, runtime/tool versions and repository commit were not measured; they are not proof inputs. Historical Python/aarch64 measurements were not rerun or presented as current observations.

## Artifacts and preservation

Self-contained proof package: `flagship/handoffs/009_clean_square_pair_localization/`, with README.md, proof.md and audit_and_scope.md. It does not depend on this result file. R-011/D-011 acceptance discharges historical H-008 review O-018; main T-010 audit O-019 **proved**, NEW H-009 review O-020 **unresolved**. Updated main known identities (KI-013), obligations, log and report. H-001 through H-008, existing ideas/reviews/decisions/literature and earlier experiment results are unchanged. The live report retains its pre-D-011 text as explicitly superseded history.

Minimal executable follow-up: flagship performs a NEW paper review of H-009's reduced ratios, odd-square character contradiction, squarefree-kernel parity/d=1/nonunit k and converse quantifiers. Then stop. No search, pointwise-forcing restart, new coverage claim or external-priority audit is authorized.