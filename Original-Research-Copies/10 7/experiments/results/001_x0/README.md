# E-001: smallest-denominator classifier

Date: 2026-10-03. Status: verified computationally.

Scope: ALL primes 2<=p<=100000 with p mod 840 in
{1,121,169,289,361,529}. Of 9592 primes in the interval, 273 are
selected. Other primes, all composites and all n outside the interval are
excluded. These classes define the dataset; no complementary coverage is assumed.

Result: 87 positive certificates; 186 records labelled "no completion at x0";
zero per-prime factor-pair disagreements. Exact coverage within this dataset:
87/273=29/91. All success triples satisfy positivity and
4*x*y*z=p*(x*y+x*z+y*z). Failure factorizations are complete and checked.

Algorithm: [classifier](../../scripts/classify_x0.py) uses an integer
Eratosthenes sieve, trial-divides x0=(p+3)/4, chooses its least prime factor
q=2 mod 3 and reconstructs y,z by KI-001. It imports Certificate.valid()
from the existing verifier, but does NOT invoke that utility's bounded search.
[Checker](../../scripts/check_x0_dataset.py) uses a separately implemented
sieve/factorization, checks unique complete dataset membership, prime factors
(by sieve and trial division), factor products and every positive divisor
1<=d<=b of b^2, b=p*x0. It checks both congruences and the full certificate.
All divisors are generated from complete factorizations, not a truncated scan.

Bounds: x is ONLY x0, at most 25000; b at most 2500000000.
For ordered completions, b/3<y<=floor(2b/3) and
z<=(b+b^2)/3. These are mathematical bounds; no artificial y/z cutoff is
applied. The exhaustive assertion is solely about completion at fixed x0.

Artifacts: [success.csv](success.csv), [failure.csv](failure.csv),
[generation.json](generation.json), [audit.json](audit.json).
JSON records retain runtime, source hashes and environment. Initial generator
runtime: 50676385 ns; initial checker runtime: 278935385 ns, excluding tool
startup. Python 3.12.3, standard library, Linux/aarch64. No external sources.

Reproduce from the workspace root:

```sh
python3 experiments/scripts/classify_x0.py
python3 experiments/scripts/check_x0_dataset.py
```

Use ordinary Python, not python -O (assertions are checks). The first command
regenerates CSVs and metadata; the second regenerates audit metadata. No other
x is searched. Regression outcomes: 1009 succeeds with q=11, x0=253;
1201 fails at x0=301=7*43. No conjectural counterexamples follow.

Proof: [KI-001](../../../flagship/main/known_identities.md). Separate algorithms are an
implementation cross-check, not an independent-agent or formal proof audit.
The finite result neither proves universal existence nor establishes novelty.