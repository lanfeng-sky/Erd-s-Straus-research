#!/usr/bin/env python3
"""D-001: exact fixed-x0 classifier; no search at other x."""
import csv
import hashlib
import json
import platform
import sys
from math import isqrt
from pathlib import Path
from time import perf_counter_ns

from verify_representation import Certificate

LIMIT = 100000
RESIDUES = {1, 121, 169, 289, 361, 529}
OUT = Path(__file__).resolve().parents[1] / 'results' / '001_x0'


def sieve(limit):
    flags = bytearray(b'\x01') * (limit + 1)
    flags[:2] = b'\x00\x00'
    for q in range(2, isqrt(limit) + 1):
        if flags[q]:
            flags[q*q:limit+1:q] = b'\x00' * ((limit-q*q)//q+1)
    return [p for p in range(2, limit+1) if flags[p]]


def factor(n, primes):
    result = []
    for q in primes:
        if q*q > n:
            break
        exponent = 0
        while n % q == 0:
            n //= q
            exponent += 1
        if exponent:
            result.append((q, exponent))
    if n > 1:
        result.append((n, 1))
    return result


def main():
    start = perf_counter_ns()
    primes = sieve(LIMIT)
    selected = [p for p in primes if p % 840 in RESIDUES]
    successes, failures = [], []
    for p in selected:
        x = (p+3)//4
        factors = factor(x, primes)
        encoded = ';'.join(f'{q}^{a}' for q, a in factors)
        q = next((q for q, _ in factors if q % 3 == 2), None)
        if q is None:
            failures.append((p, x, encoded, 'no completion at x0'))
            continue
        b = p*x
        assert b*b % q == 0
        e = b*b//q
        assert (b+q) % 3 == (b+e) % 3 == 0
        y, z = (b+q)//3, (b+e)//3
        assert x <= y <= z and Certificate(p, x, y, z).valid()
        successes.append((p, x, q, y, z))
    OUT.mkdir(parents=True, exist_ok=True)
    for name, header, rows in (
        ('success.csv', ('p', 'x0', 'q', 'y', 'z'), successes),
        ('failure.csv', ('p', 'x0', 'factorization', 'verdict'), failures),
    ):
        with (OUT/name).open('w', newline='', encoding='ascii') as stream:
            writer = csv.writer(stream)
            writer.writerow(header)
            writer.writerows(rows)
    summary = {
        'status': 'verified computationally', 'n_range_inclusive': [2, LIMIT],
        'residues_mod_840': sorted(RESIDUES), 'all_primes_in_range': len(primes),
        'selected': len(selected), 'successes': len(successes),
        'no_completion_at_x0': len(failures),
        'runtime_ns': perf_counter_ns()-start,
        'python': sys.version, 'os': platform.platform(),
        'architecture': platform.machine(),
        'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in (Path(__file__), Path(__file__).with_name('verify_representation.py'))},
        'limits': 'Only x=(p+3)//4; no other x; no conjecture counterexample claim.',
    }
    (OUT/'generation.json').write_text(json.dumps(summary, indent=2)+'\n', encoding='ascii')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
