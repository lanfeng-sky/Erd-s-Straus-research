#!/usr/bin/env python3
"""R-003: read-only H-002 audit and bounded abstract inverse-lemma falsification.
No new primes/offset records, no network, no project imports. Do not use -O.
"""
from pathlib import Path
from math import gcd, isqrt
from itertools import combinations_with_replacement
from collections import Counter
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
H = ROOT / 'handoffs' / '002_structure'


def jacobi(a, n):
    assert n > 0 and n % 2
    a %= n
    s = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                s = -s
        a, n = n, a
        if a % 4 == n % 4 == 3:
            s = -s
        a %= n
    return s if n == 1 else 0


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def group(gens, a):
    out, todo = {1}, [1]
    while todo:
        v = todo.pop()
        for g in gens:
            w = v*g % a
            if w not in out:
                out.add(w)
                todo.append(w)
    return out


def stab(S, J, a):
    return {v for v in J if {v*s % a for s in S} == S}


def bitshift(mask, k, n):
    return ((mask << k) | (mask >> (n-k))) & ((1 << n)-1)


def inverse_test():
    # Candidate: C_(2m), L=m-2, aperiodic subset sums S disjoint from S+m,
    # generating sequence with even total. Claim: one term is +/-2g,
    # every other term is +/-g, for a generator g. Fixed domain, first failure.
    visited, eligible = 0, 0
    for m in (3, 5, 7, 9):
        n, L = 2*m, m-2
        alphabet = [v for v in range(1, n) if v != m]
        for seq in combinations_with_replacement(alphabet, L):
            visited += 1
            if gcd(n, *seq) != 1 or sum(seq) % 2:
                continue
            mask = 1
            for v in seq:
                mask |= bitshift(mask, v, n)
            if mask & bitshift(mask, m, n):
                continue
            if any(bitshift(mask, k, n) == mask for k in range(1, n)):
                continue
            eligible += 1
            if not any(sum(v not in (g, (-g) % n) for v in seq) == 1
                       and all(v in (g, (-g) % n, 2*g % n, (-2*g) % n) for v in seq)
                       for g in range(1, n) if gcd(g, n) == 1):
                return {'status': 'false', 'visited': visited, 'm': m,
                        'sequence': seq,
                        'subset_sums': [k for k in range(n) if mask & (1 << k)]}
    return {'status': 'verified computationally', 'visited': visited, 'eligible': eligible,
            'domain_m': [3, 5, 7, 9], 'length': 'm-2', 'even_total': True}


def main():
    assert __debug__
    for line in (H/'SHA256SUMS').read_text().splitlines():
        digest, name = line.split(maxsplit=1)
        name = name.lstrip('*')
        assert '/' not in name and '\\' not in name
        assert hashlib.sha256((H/name).read_bytes()).hexdigest() == digest, name
    rows = [json.loads(s) for s in (H/'pairs.jsonl').read_text().splitlines()]
    counts = Counter()
    joint_examples = []
    for row in rows:
        p,x,a = (row[k] for k in ('p','x','a'))
        occurrences = [q % a for q,e in row['factor_x'] for _ in range(e)]
        for q,e in row['factor_x']:
            chi = jacobi(q,p)
            assert chi == (1 if pow(q,(p-1)//2,p) == 1 else -1)
            assert jacobi(q,a) == chi
        split = all(jacobi(q,p) == 1 for q,e in row['factor_x'])
        if split:
            assert not row['A'] and not row['B']
            counts['common_character_blocker'] += 1
            counts['common_blocker_old_'+row['obstruction']['kind']] += 1
        D = set(row['D'])
        S = D | {p*d % a for d in D}
        assert bool(row['A'] or row['B']) == bool(S & {(-s) % a for s in S})
        J = group(occurrences + [p % a], a)
        K = stab(S,J,a)
        N = sum(q not in K for q in occurrences + [p % a])
        assert len(S) >= len(K)*(1+N)
        KD = stab(D,set(row['H']),a)
        ND = sum(q not in KD for q in occurrences)
        assert len(D) >= len(KD)*(1+ND)
        counts['binary_bounds_checked'] += 2
        if prime(a) and (-1) % a in J:
            h = len(J)
            deficits = []
            for r in range(1,h+1,2):
                if h % r: continue
                Kr = {v for v in J if pow(v,r,a) == 1}
                Nr = sum(q not in Kr for q in occurrences + [p % a])
                if Nr < h//(2*r): deficits.append(r)
            sufficient = not deficits
            counts['prime_defect_joint_domain'] += 1
            if sufficient:
                assert row['A'] or row['B']
                counts['joint_saturation_pass'] += 1
                oldpass = bool(row['saturation'] and not row['saturation']['deficient'])
                if not oldpass:
                    counts['joint_pass_beyond_old_sufficient'] += 1
                    if len(joint_examples) < 3:
                        joint_examples.append([p,x,a,bool(row['A']),bool(row['B'])])
            if not row['A'] and not row['B']:
                r = len(K)
                assert r % 2 and N <= h//(2*r)-1 and deficits
                assert r*(N+1+(N % 2)) <= len(S) <= h//2
                assert jacobi(p*x, a) == 1
                counts['joint_failures_with_deficiency'] += 1
                # Critical growth equality: all nonzero quotient terms equal +/-g.
                if len(S) == r*(1+N):
                    outside = [q for q in occurrences + [p % a] if q not in K]
                    if outside:
                        g = outside[0]
                        cosets = {g*k % a for k in K} | {pow(g,-1,a)*k % a for k in K}
                        assert all(q in cosets for q in outside)
                        assert group(list(K)+[g],a) == J
                    counts['critical_equalities'] += 1
    qs = {}
    for p in sorted({r['p'] for r in rows}):
        q = next(q for q in range(2,p) if jacobi(q,p) == -1)
        assert prime(q) and q*q < p
        x0 = (p+3)//4
        t = (-x0) % q
        qs[p] = (q,t)
    q,t = qs[118801]
    existing = {r['t']:r for r in rows if r['p']==118801}
    assert q-1 in existing
    q_window_misses = all(not existing[t]['A'] and not existing[t]['B'] for t in range(q))
    out = {'result':'PASS', 'sha256_manifest':'all entries verified', 'pairs':len(rows),
           'counts':dict(counts), 'joint_sufficient_examples_beyond_old':joint_examples,
           'least_nonresidue_118801': {'q':q, 'first_multiple_offset':t,
                                     'all_t_0_through_q_minus_1_miss':q_window_misses},
           'inverse_candidate':inverse_test(), 'python':sys.version,
           'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    print(json.dumps(out,indent=2))


if __name__ == '__main__':
    main()
