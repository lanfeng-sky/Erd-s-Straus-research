# H-001: Compressed Fixed-x0 Review Package

> COMPRESSED HISTORICAL RECORD. The long proof and review prose were consolidated into `flagship/historical_compression.md`. The executable `audit_x0.py` remains as the original compact reproduction payload. Ask the user before restoring omitted detail from backup.

## Retained claim

For prime p=1 mod 24 and x0=(p+3)/4, fixed-x0 completion exists iff x0 has a prime factor q=2 mod 3. Finite scope: 273 selected primes through 100000; 87 successes; 186 no-completion-at-x0 records; zero factor-pair disagreements. Universal existence remains unresolved.

## Reproduction

Run the retained `audit_x0.py` without `python -O` to reproduce the expected classification. The script uses exact standard-library integer arithmetic. A fixed-x0 failure is not a conjecture counterexample.

## Historical status

Accepted as KI-001 in R-002. This route was superseded by the exact varying-x two-branch theorem. Long human-readable payloads were compressed; the raw executable remains for optional user-authorized inspection.