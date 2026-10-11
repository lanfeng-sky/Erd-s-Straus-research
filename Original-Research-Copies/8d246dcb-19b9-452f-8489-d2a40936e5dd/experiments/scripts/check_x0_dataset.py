#!/usr/bin/env python3
"""Independent factor-pair audit for classify_x0.py output."""
import csv
import hashlib
import json
import platform
import sys
from time import perf_counter_ns
from math import isqrt
from pathlib import Path
from verify_representation import Certificate

ROOT = Path(__file__).resolve().parents[1] / 'results' / '001_x0'
LIMIT = 100000
RESIDUES = {1, 121, 169, 289, 361, 529}

def sieve(limit):
    a = [True] * (limit + 1)
    a[:2] = [False, False]
    for q in range(2, isqrt(limit)+1):
        if a[q]:
            for m in range(q*q, limit+1, q): a[m] = False
    return a

def factor(n, primes):
    out = []
    for q in range(2, isqrt(n)+1):
        if primes[q] and n % q == 0:
            e = 0
            while n % q == 0: n, e = n//q, e+1
            out.append((q, e))
    if n > 1: out.append((n, 1))
    return out

def divisors_squared(factors):
    ds = [1]
    for q, e in factors:
        old = list(ds)
        powers = [q**j for j in range(1, 2*e+1)]
        ds = old + [d*m for d in old for m in powers]
    return sorted(ds)

def parse_factorization(text):
    return [] if not text else [tuple(map(int, term.split('^'))) for term in text.split(';')]

def main():
    start = perf_counter_ns()
    prime = sieve(LIMIT)
    selected = [p for p in range(2, LIMIT+1) if prime[p] and p % 840 in RESIDUES]
    rows = {}
    for name in ('success.csv', 'failure.csv'):
        with (ROOT/name).open(newline='', encoding='ascii') as f:
            for row in csv.DictReader(f):
                p = int(row['p'])
                assert p not in rows, ('duplicate', p)
                rows[p] = (name, row)
    assert set(rows) == set(selected), (len(rows), len(selected))
    disagreements = []
    checked_successes = 0
    for p in selected:
        x = (p+3)//4
        factors = factor(x, prime)
        assert isqrt(x) ** 2 <= x < (isqrt(x)+1)**2
        product = 1
        for q, e in factors:
            assert prime[q]
            product *= q**e
        assert product == x
        b = p*x
        admissible = []
        b_factors = factor(b, prime)
        rebuilt = 1
        for r, exponent in b_factors:
            assert 2 <= r <= LIMIT and prime[r] and exponent > 0
            assert all(r % t for t in range(2, isqrt(r)+1))
            rebuilt *= r**exponent
        assert rebuilt == b
        for d in divisors_squared(b_factors):
            if d > b:
                continue
            assert b*b % d == 0
            e = b*b//d
            if (d+b) % 3 == 0 and (e+b) % 3 == 0:
                y, z = (d+b)//3, (e+b)//3
                if x <= y <= z and Certificate(p, x, y, z).valid():
                    admissible.append((d, y, z))
        found = bool(admissible)
        kind, row = rows[p]
        assert int(row['x0']) == x
        reported = kind == 'success.csv'
        if found != reported: disagreements.append((p, found, reported))
        if reported:
            assert len(admissible) > 0
            q, y, z = (int(row[key]) for key in ('q', 'y', 'z'))
            assert q == min(r for r, _ in factors if r % 3 == 2)
            assert min(x, y, z) > 0
            assert 4*x*y*z == p*(x*y+x*z+y*z)
            assert (q, y, z) in admissible
            checked_successes += 1
        else:
            assert row['verdict'] == 'no completion at x0'
            assert parse_factorization(row['factorization']) == factors
    result = {'range': [2, LIMIT], 'selected': len(selected), 'successes_checked': checked_successes,
              'failures_checked': len(selected)-checked_successes,
              'factor_pair_disagreements': len(disagreements), 'disagreements': disagreements,
              'runtime_ns': perf_counter_ns()-start,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'python': sys.version,
              'os': platform.platform(), 'architecture': platform.machine(),
              'result': 'PASS' if not disagreements else 'BLOCKED'}
    print(result)
    (ROOT/'audit.json').write_text(json.dumps(result, indent=2)+'\n', encoding='ascii')
    assert not disagreements

if __name__ == '__main__': main()
