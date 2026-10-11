# T-003: one-extra-element inverse theorem — proved

2026-10-04. Elementary proof, submitted for adversarial flagship review; no
Lean or literature-novelty claim. This is a universal CYCLIC-GROUP theorem,
not an Erdős–Straus existence theorem. Computation is not a premise.

## Exact statement

For every odd integer m>=3, let G=Z/(2m)Z, L=m-2, and let
w_1,...,w_L be nonzero elements generating G. Define

    T = {sum_{i in I} w_i : I subset {1,...,L}}.

Assume Stab_G(T)={0}, T intersect (T+m) is empty, and sum_i w_i is
even modulo 2m. Then there is a generator g of G such that EXACTLY ONE
occurrence belongs to {2g,-2g}, and all others belong to {g,-g}.
Occurrences, not distinct values, are counted; m need not be prime.
For m=3 the hypotheses are impossible. No assertion about arbitrary
shorter lists or an admissible shift for every prime is made.

## 1. Growth bookkeeping

A translation period of any partial subset-sum set persists after addition
of every remaining binary set {0,w_i}. Thus every partial set, in every
ordering of the list, is aperiodic. A nonzero binary step must increase
cardinality: equality |P union (P+w)|=|P| would give P+w=P and a nonzero
period of the final T. Starting at {0}, every step increases by >=1.

Consequently |T|>=L+1. Equality forces all terms to be equal up to sign:
put any pair u,v first. If u!=v and u!=-v, its four sums
{0,u,v,u+v} are distinct, yielding |T|>=4+(L-2)=L+2.
If every pair is equal up to sign, generation forces their common value
g to generate G. For odd L the total of L signed generators is odd.
Therefore even total excludes |T|=L+1. Disjointness from T+m gives
|T|<=m, so

    |T|=m=L+2.

For m=3, L=1: an even element does not generate C_6. Hence no such list.
From now on m>=5, so L>=3 and 2m>=10.

The total growth excess above one per binary step is exactly one, in
EVERY ordering. In particular, whenever u!=+/-v are placed first, their
four-element set consumes that excess. Each remaining term w must satisfy

    |P union (P+w)|=5,    P={0,u,v,u+v}.                  (1)

There is at least one such incompatible pair: otherwise generation and
odd L would again make the total odd.

## 2. Four-element progression lemma (including the short-cycle case)

**Lemma.** In G=C_(2m), m odd, let u,v,w be nonzero, u!=+/-v, and
P={0,u,v,u+v}. Suppose P is aperiodic, P intersect (P+m) is empty, and
(1) holds. Then, in some order,

    u is in {w,-w},    v is in {2w,-2w}.                  (2)

**Proof.** Put H=<w>, d=ord(w). Partition G into H-cosets, and mark
which elements of each cyclic w-orbit belong to P. On a nonempty proper
orbit, |(P+w) minus P| counts the runs of occupied consecutive elements.
Indeed each run contributes its successor, and those successors are
exactly the newly occupied elements. A full orbit contributes zero.
By (1) there is exactly ONE proper occupied orbit and exactly ONE run
in it; every other occupied orbit is full.

A full orbit of even order is impossible: its subgroup contains the
unique involution m, so it would meet its translate by m. A full orbit
of odd order has d>=3 because w!=0. Since |P|=4, the ONLY possible
full-orbit case is d=3, with one full orbit C and a singleton {s} in a
different orbit. We now exclude that case without a prime-order assumption.

P is invariant under reflection z -> u+v-z. This reflection sends full
H-cosets to full H-cosets. The unique full orbit C must map to itself,
and the remaining singleton s must be fixed. Writing c for the class
of C and b for that of s in G/H, we get

    2c=[u+v]=2b,    b!=c.

Thus b-c has order two in the cyclic quotient G/H. Since |H|=3 is odd,
the image of m is the quotient's unique involution. Hence b-c=[m],
so s+m lies in the full orbit C. This contradicts P intersect (P+m)
being empty. This is the potentially dangerous order-three exception;
it has not been silently discarded.

There are therefore no full occupied orbits. P is one proper run of
length four:

    P={b,b+w,b+2w,b+3w},    d>=5.                         (3)

The natural reflection z -> 2b+3w-z preserves (3); so does
z -> u+v-z. Composing the reflections is translation by
(u+v)-(2b+3w). Aperiodicity of P makes this translation zero, hence

    u+v=2b+3w.

This reflection pairs indices 0 with 3, and 1 with 2 in (3). Since
d>=5 these four elements are distinct and these pairs have no fixed
point. The pair {0,u+v} must be one of those two pairs, leaving {u,v}
as the other. If 0 has index 0,1,2,3 respectively, the other two
values are {w,2w}, {-w,2w}, {-2w,w}, {-2w,-w}, respectively.
This proves (2). Nothing in this lemma assumes that w generates G. QED.

## 3. Finish the inverse theorem

Fix an incompatible pair u,v, and choose a third occurrence w. All of
the lemma's hypotheses hold: P is a partial sum set, and both its
aperiodicity and disjointness follow from those of T. By the lemma,
after swapping u,v if necessary,

    u=+/-w,    v=+/-2w.

For EVERY other occurrence s (outside the two chosen occurrences), the
same lemma applied to u,v,s says that s equals +/-u or +/-v. Thus all
terms lie in <w>, and all lie in {w,-w,2w,-2w}. Since the entire list
generates G, w generates G. Write g=w.

There is already a term in {2g,-2g}. There cannot be another one.
If there were, use a {g,-g} occurrence, the original {2g,-2g}
occurrence and the second {2g,-2g} occurrence as the first three.
The lemma applied with this third term s=+/-2g would require the pair's
{g,-g} term to be +/-s or +/-2s. These alternatives require

    1=+/-2 modulo 2m,    or    1=+/-4 modulo 2m,

both impossible for even 2m>=10. Hence precisely one occurrence is
+/-2g and all others are +/-g. QED.

## Adversarial checkpoints and limitation

- Periods of partial sets P need not equal those of T in a general problem;
  here persistence proves they are all trivial. No stabilizer was guessed.
- Only generation of the whole list is assumed. Full order of g is derived
  AFTER the four-set analysis; w initially may have small order.
- The only possible full short cycle (order three plus a singleton) is
  ruled out using reflection and the quotient involution, not by pretending
  that m is prime. The case m=3 is handled explicitly.
- Avoiding m in T is NOT enough: (1,2,6) in C_10 avoids 5 as a sum, but
  its sum set meets its translate by 5. The real difference-set condition
  is essential.
- This proof uses direct reordered growth with an internal short-cycle
  lemma; it does not invoke Kneser, an external inverse theorem, or tests
  outside the authorized four-group domain.
- The arithmetic specialization in `arithmetic_specialization.md` classifies
  only failed pairs with N=m-2 relative to their ACTUAL joint stabilizer.
  It provides no forcing of such N, no cross-shift contradiction, and no
  solution for every prime. Erdős–Straus remains **unresolved**.
