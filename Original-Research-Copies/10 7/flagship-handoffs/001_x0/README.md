# H-001: Fixed-x0 Review Package

This directory is the immutable review snapshot for D-001. The flagship model can audit it without access to the parent workspace.

## Submitted Claims

- Mathematical claim: `proof.md`.
- Finite result: among all 273 primes p <= 100000 in the six selected classes modulo 840, 87 complete at x0=(p+3)/4 and 186 do not complete at this fixed x.
- Cross-check result: zero disagreements between the prime-factor classifier and complete factor-pair enumeration.
- Universal conjecture status: `unresolved`.

## Independent Reproduction

Run from this directory:

```sh
python3 audit_x0.py
```

Expected output:

```text
PASS selected=273 successes=87 failures=186 disagreements=0
```

The script is self-contained, uses only Python standard-library integer arithmetic, regenerates the selected prime set, factors each x0 and b=p*x0, enumerates every divisor d<=b of b^2, and validates all reconstructed certificates.

## Review Instructions

1. Audit both directions in `proof.md`, including positivity and integrality.
2. Inspect `audit_x0.py` for complete factorization and divisor enumeration.
3. Run the script without `python -O`.
4. Record the result in `../../reviews/002_x0_audit.md`.
5. Record the next task in `../../decisions/002_next_task.md`.
6. Do not modify this handoff package during review.