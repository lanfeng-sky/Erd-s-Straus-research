# D-002 exact structural findings

2026-10-04. **Conclusion:** elementary fixed-x theorem proved; prescribed
finite audit verified computationally; saturation application conditional;
pointwise/cross-shift forcing **blocked**. Overall conjecture unresolved.

## Complete domain, exclusions, algorithms

Let S={1,121,169,289,361,529} modulo 840. Regenerate all primes
2<=p<=100000 in S (273), using a sieve and independent full trial
primality test. Select precisely the 186 whose x0=(p+3)/4 has all prime
factors 1 modulo 3; accepted KI-001 says these fail at x0. Test EVERY
t=0,...,15 for each of these p, regardless of earlier hits. Separately
include the single prime 118801 at EVERY t=0,...,14. Exactly
186*16+15=2991 pairs, x=x0+t, a=3+4t. No other primes, offsets,
composites, or x values are claimed checked. Every tested x is <p.
The six classes select the dataset; complementary class coverage is
not assumed or audited by this experiment.

For each pair enumerate c|x^2 by the Cartesian product of ALL prime
exponents 0,...,2e_q. Check A and B separately, and check integrality,
positivity and 4xyz=p(xy+xz+yz) for EVERY returned c. Independently
factor b=px using a different trial schedule and recursively enumerate
ALL d|b^2 with d<=b, testing both complementary residues. Classify
its p-adic allocation and compare branches separately. The proven
bound d<=b loses no completion up to swapping y,z; no y,z cutoff
or smallest-x filter is used. Trial factoring terminates only when the
current candidate squared exceeds the remaining unfactored integer;
each factorization is checked for primality and product.

Independently construct D, R=DD^{-1}, the signed exponent set, and H.
For every failure save the complete c-residue set (with factorization
and divisor count), D,R,H, targets, and a character/subgroup/bounded
miss witness. For EVERY prime-defect pair with -1 in H, compute ALL
odd r|h, ALL K_r, N_r, and the stabilizer of D. This includes B-only
successes as well as full failures; no deficiency means A must succeed.

A separate checker imports nothing from the generator. It scans all
integer divisors through sqrt(x^2)=x and completes each pair, reconstructs
D with a direct scan, computes H by products of complete cyclic power
sets, and rescans switched N divisors through sqrt(N). This reduces
common-mode factoring/enumeration risk. Both implementations are by the
same execution model, not an independent-agent or proof-assistant audit.

## All-pair counts (not stop-at-first counts)

| Branch status | Pairs |
|---|---:|
| Both A and B | 757 |
| A only | 101 |
| B only | 198 |
| Neither | 1935 |
| Total | 2991 |

Zero branch-by-branch disagreements against complete factor pairs.
The generator checked 6064 divisor-formula certificates and 4285
ordered factor-pair certificates (not distinct triples globally).
The separate direct scanner checked all branch classifications and
1813 saved first-per-branch certificates (=2*757+101+198).

| Exclusive failure certificate type | Pairs |
|---|---:|
| Single-prime quadratic obstruction | 1059 |
| Other subgroup obstruction | 465 |
| Target in H but bounded exponent miss | 411 |
| Total failures | 1935 |

Prime a, -1 in H: 941 pairs. Among them 342 fail A and every one
has an explicit deficient odd subgroup, including its actual stabilizer.
Of those, 253 fail both branches and 89 succeed in B. These are bounded
checks of the conditional lemma's consequence, not a proof of Kneser.

All 186 selected x0 failures have some hit by t=7; first-t histogram:
1:55, 2:83, 3:11, 4:16, 5:15, 6:1, 7:5. This does NOT give a uniform
bound. For p=118801 all t=0,...,13 are independently classified as
failures by full factor-pair enumeration in THIS audit. At t=14,
x=29715,a=59, both branches succeed. The known triple
(29715,59834124,5077395546660) is a B certificate; the stored first A
triple is (29715,59875704,84724121160). Both pass the exact identity.
This closes the prior independent-check gap at t=8,...,13.

## Exactly two cross-shift implications tested, both false

For each proposed implication below, quantify over ALL primes p in S
with x0 failing and ALL eligible shifts. The finite tests use only shifts
whose compared pairs belong to the complete prescribed 2991-pair domain.
They falsify the universal implications; no larger search was performed.
Smallest means lexicographically smallest (p,t) IN THIS dataset, not
smallest over all primes or all shifts. No further repair/pattern hunt
was attempted after these two failures.

**C1 (false):** For every such p and integer t>=0 with
x_t=(p+3)/4+t and x_{t+1}<p, if x_t fails both branches but has no
single-prime quadratic obstruction, then x_{t+1} succeeds in A or B.
This was a possible “loss of quadratic obstruction forces next hit” rule.
861 eligible antecedents; 510 counterinstances. Smallest: p=1129,t=12.

- x_12=295=5*59, a=51, H is the full unit group of size 32,
  R={1,5,7,8,22,32,37,40,41}, targets={50,44}. Both targets in H,
  both absent from R. No quadratic blocker; e.g. 5 is nonsquare mod 3.
- x_13=296=2^3*37, a=55, H is the full unit group of size 40,
  R={1,2,3,4,6,7,8,12,14,19,21,23,24,28,29,37,38,39,42,46},
  targets={54,26}. Again both targets are absent from R.

There are even consecutive full-group bounded-exponent failures;
subgroup generation cannot be the hoped-for cross-shift contradiction.

**C2 (false):** For every such p and consecutive primes ell<ell' both
3 modulo 4 (with no prime 3 modulo 4 strictly between them), such that
x=(p+ell)/4<p and x'=(p+ell')/4<p, if -1 belongs to BOTH generated
subgroups H_x,H_x', then at least one of these two x values succeeds
in A or B. 534 eligible antecedents; 29 counterinstances. Smallest:
p=2521, ell=11 (t=2), ell'=19 (t=4).

- x=633=3*211: H is full of order 10, R={1,2,3,4,6,7,8},
  targets={10,9}. Deficient K_1={1} has N_1=2<5.
- x'=635=5*127: H is full of order 18,
  R={1,3,4,5,8,12,13,14,15}, targets={18,6}.
  K_1 has N_1=2<9; K_3={1,7,11} has N_3=2<3.

Both prime defects permit -1 in H, both carry explicit deficiency
certificates, and both miss A AND B. Simultaneous concentration at two
nearby prime defects is arithmetically consistent. No observed relation
in this bounded audit proves that one branch must succeed for every p.

## Seven-prime switched audit (fixed order, finite window)

Only p in {20521,31081,39841,51361,58321,66889,88729} were searched.
Enumerate 1<=g<=16 then 1<=k<=16 lexicographically, stopping at the
first hit per p. Factor N=4gk^2p+1 completely, enumerate all divisors
d with d^2<=N, require d=-1 modulo 4gk; e=N/d then has the same
residue. No bound on u,v or x is imposed. Exactly 147 candidates
visited out of at most 1792. All seven succeed; every g=1,k<=16
candidate is verified to fail. First witnesses use the smallest eligible d.

| p | g,k | d,e | x,y,z |
|---|---|---|---|
|20521|2,1|87,1887|5192,451462,9685912|
|31081|3,5|59,158039|7902,466215,1228010310|
|39841|2,2|207,6159|10010,2071732,61355140|
|51361|2,7|111,181383|12956,1438108,2329015906|
|58321|2,1|47,9927|14892,699852,144752722|
|66889|2,2|463,4623|16762,7759124,77323684|
|88729|2,1|87,8159|22440,1952038,181007160|

Every numerator quotient is integral, all denominators positive, all
seven pass 4xyz=p(xy+xz+yz). Allowing g is useful here: g=1 was an
artificial bottleneck. This does NOT prove that g<=3,k<=7, or any
fixed finite g,k window, suffices universally.

For comparison normalize the FIRST saved A witness at each x in the
2991 pairs, not all possible A witnesses. Complete available lists are
in `switch_comparison.json`. The earliest x with A for each of these p
has normalized (g,k,u,v) as follows:

    20521: t=2, (59,8,1,87)
    31081: t=3, (26,20,1,299)
    39841: t=1, (34,42,1,293)
    51361: t=2, (3,130,3,1427)
    58321: t=2, (3,442,1,4861)
    66889: t=5, (4,91,2,2091)
    88729: t=1, (118,27,1,188)

These exceed the switch window in g and/or k, whereas the new first
switched witnesses use different, larger x. The windows sample the SAME
branch-A parameterization differently; neither window contains all of it.

## Environment, outputs, limitations, next step

Python 3.12.3 standard library, Linux aarch64 in mounted Ubuntu/proot,
GCC 13.3.0, glibc 2.39; kernel 6.1.138-android14. Exact mathematical
operations use arbitrary-precision integers (including modular inverses
and isqrt). Integer nanosecond timings: generation 5552022847 ns,
independent scanner 14297017155 ns, excluding tool startup. No external
network, no Lean, no floating-point mathematical tests. Source and record
hashes are in `environment.json` and `independent_check.json`.

Retained outputs: `pairs.jsonl`, `switches.jsonl`, `switch_comparison.json`,
`summary.json`, `environment.json`, `independent_check.json`, proof notes,
and the two standalone scripts in the handoff. Failure of a finite window
is not a conjecture counterexample; success is not a universal theorem.

Minimal next executable step: flagship run both frozen audit scripts and
review the p-adic split, inversion, ordering caveat and normalized switch
map. Only then choose a genuinely new pointwise lemma; simply expanding
fixed windows is not justified by this report.