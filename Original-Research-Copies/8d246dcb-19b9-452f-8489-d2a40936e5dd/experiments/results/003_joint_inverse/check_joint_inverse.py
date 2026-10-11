#!/usr/bin/env python3
"""D-003 independent bounded unit test; standard library, no project imports.
Exact domain: nondecreasing nonzero non-involution sequences in C_(2m),
m in (3,5,7,9), length m-2. Run without -O. No universal proof by testing.
Unlike the flagship bit-rotation probe, recompute all binary subset sums.
"""
from itertools import combinations_with_replacement, product, combinations
from math import gcd, comb
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys


def sums(seq, n):
    return {sum(v for v, take in zip(seq, flags) if take) % n
            for flags in product((False, True), repeat=len(seq))}


def inverse_generators(seq, n):
    return [g for g in range(1, n) if gcd(g, n) == 1
            and sum(v in (2*g % n, -2*g % n) for v in seq) == 1
            and all(v in (g, -g % n, 2*g % n, -2*g % n) for v in seq)]


def main():
    assert __debug__, 'Run without -O'
    results = []
    eligible_payload = []
    triple_checks = 0
    for m in (3, 5, 7, 9):
        n, L = 2*m, m-2
        visited = eligible = 0
        histogram = Counter()
        for seq in combinations_with_replacement([v for v in range(1, n) if v != m], L):
            visited += 1
            if sum(seq) % 2 or gcd(n, *seq) != 1:
                continue
            T = sums(seq, n)
            if T.intersection({(t+m) % n for t in T}):
                continue
            if any({(t+k) % n for t in T} == T for k in range(1, n)):
                continue
            eligible += 1
            assert len(T) == m, (m, seq, sorted(T))
            gs = inverse_generators(seq, n)
            assert gs, (m, seq, sorted(T))
            histogram[len(gs)] += 1
            eligible_payload.append([m, list(seq), sorted(T), gs])
            # Test the proof's critical triple statement on the SAME eligible list.
            for i, j in combinations(range(L), 2):
                u, v = seq[i], seq[j]
                if u in (v, -v % n):
                    continue
                P = sums((u, v), n)
                assert len(P) == 4
                for k in range(L):
                    if k in (i, j):
                        continue
                    w = seq[k]
                    assert len(P | {(t+w) % n for t in P}) == 5
                    assert ((u in (w, -w % n) and v in (2*w % n, -2*w % n))
                            or (v in (w, -w % n) and u in (2*w % n, -2*w % n)))
                    triple_checks += 1
        assert visited == comb((n-2)+L-1, L)
        results.append({'m': m, 'length': L, 'visited': visited,
                        'eligible': eligible, 'counterexamples': 0,
                        'generator_count_histogram': dict(histogram)})
    # Regression: the weakened condition m not in T is not the real hypothesis.
    T = sums((1, 2, 6), 10)
    assert 5 not in T and T & {(t+5) % 10 for t in T}
    payload = json.dumps(eligible_payload, separators=(',', ':')).encode()
    print(json.dumps({'result': 'PASS', 'domain_m': [3, 5, 7, 9],
                      'domain': 'nondecreasing sequences; nonzero and no involution; length m-2',
                      'groups': results, 'visited': sum(r['visited'] for r in results),
                      'eligible': sum(r['eligible'] for r in results),
                      'counterexamples': 0, 'critical_triple_checks': triple_checks,
                      'eligible_payload_sha256': hashlib.sha256(payload).hexdigest(),
                      'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      'python': sys.version,
                      'limitations': 'Four groups only; not a universal theorem or an Erdos-Straus existence search.'}, indent=2))


if __name__ == '__main__':
    main()
