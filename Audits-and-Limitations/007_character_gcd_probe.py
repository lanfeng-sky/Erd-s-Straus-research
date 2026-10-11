#!/usr/bin/env python3
"""Offline T-007 regression: existing first A/B certificates, no solution search.
Run directly from the mounted workspace; stdout is the only output.
The two new equality examples are algebraically specified, not searched.
"""
from pathlib import Path
from math import gcd, isqrt
from collections import Counter
import hashlib
import json
import platform
import time

BASE = Path('/data/user/0/com.ai.assistance.operit/files/workspace/8d246dcb-19b9-452f-8489-d2a40936e5dd')
ROOT = BASE / 'flagship'
H5 = ROOT / 'handoffs/005_type_I_gcd_gap'
SOURCE = H5 / 'replay/handoffs/002_structure/pairs.jsonl'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def historical_hashes():
    out = {}
    for directory in ('ideas', 'reviews', 'decisions', 'handoffs', 'literature', 'main'):
        for path in sorted((ROOT / directory).rglob('*')):
            if not path.is_file():
                continue
            # Exclude only this round's new entries, never an old payload.
            name = path.name
            if directory == 'ideas' and name.startswith('012_'):
                continue
            if directory in ('reviews', 'decisions') and name.startswith('007_'):
                continue
            out[str(path.relative_to(ROOT))] = sha(path)
    out['main_research_report.md'] = sha(ROOT / 'main_research_report.md')
    return out


def manifest():
    count = 0
    for line in (H5 / 'SHA256SUMS').read_text().splitlines():
        digest, name = line.split(maxsplit=1)
        path = (H5 / name.lstrip('*')).resolve()
        assert path.is_relative_to(H5.resolve())
        assert sha(path) == digest, str(path)
        count += 1
    assert count == 34
    return count


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def legendre(a, p):
    r = pow(a % p, (p - 1) // 2, p)
    assert r in (0, 1, p - 1)
    return -1 if r == p - 1 else r


def least_nr(p):
    # An auxiliary exact character scan, not a prime/solution/shift search.
    for q in range(1, p):
        if legendre(q, p) == -1:
            assert prime(q)
            return q
    raise AssertionError('No nonresidue')


def certificate(p, x, y, z):
    assert min(p, x, y, z) > 0
    assert 4*x*y*z == p*(x*y + x*z + y*z)
    assert x == min(x, y, z)


def test_A(p, x, y, z, C, a, q):
    certificate(p, x, y, z)
    assert x % p and y % p == z % p == 0
    d0 = gcd(C, x)
    u, v = C // d0, x // d0
    assert d0 % u == 0
    g = d0 // u
    assert (u + v) % a == 0
    k = (u + v) // a
    assert x == g*u*v and C == g*u*u
    assert (y, z) == (p*g*k*u, p*g*k*v)
    assert gcd(u, v) == gcd(u, k) == gcd(v, k) == 1
    assert gcd(x, gcd(y, z)) == g
    assert k*p == 4*g*k*u*v - u - v
    M = 4*g*u*k - 1
    assert gcd(M, p) == 1 and legendre(M, p) == -1
    assert legendre(u*v, p) == -1
    s = u*v
    assert s >= q and 4*q*g <= p + q + 1
    assert (4*q*g == p + q + 1) == (s == q and min(u, v) == 1 and k == 1)
    record = {'p': p, 'triple': [x, y, z], 'G': g, 's': s, 'q': q,
              'normalization': [g, u, v, k]}
    if p % 8 == 1:
        assert legendre(2, p) == 1
        assert 8*q*g <= 2*p + q + 1
        if s % 2:
            assert k % 2 == 0 and k >= 2
            assert 8*q*g <= 2*p + q + 1
            eq = 8*q*g == 2*p + q + 1
            assert eq == (s == q and min(u, v) == 1 and k == 2)
        else:
            assert legendre(s // 2, p) == -1 and s >= 2*q
            assert 8*q*g <= p + 2*q + 1
            eq = 8*q*g == p + 2*q + 1
            assert eq == (s == 2*q and min(u, v) == 1 and k == 1)
    return record


def main():
    assert __debug__
    start = time.perf_counter_ns()
    before = historical_hashes()
    manifest()
    rows = [json.loads(line) for line in SOURCE.read_text().splitlines()]
    primes = sorted({r['p'] for r in rows})
    assert len(rows) == 2991 and len(primes) == 187
    assert all(prime(p) and p % 24 == 1 for p in primes)
    qs = {p: least_nr(p) for p in primes}
    counts = Counter()
    examples = {}
    for row in rows:
        p, x, a = (row[key] for key in ('p', 'x', 'a'))
        assert a == 4*x - p
        A = row['A']
        if A is not None:
            r = test_A(p, x, A['y'], A['z'], A['c'], a, qs[p])
            counts['retained_A'] += 1
            counts['odd_s' if r['s'] % 2 else 'even_s'] += 1
            examples.setdefault('odd_s' if r['s'] % 2 else 'even_s', r)
            counts['odd_bound_equalities' if r['s'] % 2 else 'even_bound_equalities'] += int(
                8*r['q']*r['G'] == (2*p + r['q'] + 1 if r['s'] % 2 else p + 2*r['q'] + 1))
        B = row['B']
        if B is not None:
            y, z = B['y'], B['z']
            certificate(p, x, y, z)
            G = gcd(x, gcd(y, z))
            assert sum(t % p == 0 for t in (x, y, z)) == 1
            assert legendre(G, p) == -1  # accepted H-005, contrast only
            # T-007 corollary: both intrinsic factors cannot be residues.
            assert not (legendre(G, p) == legendre(x // G, p) == 1)
            counts['retained_B_contrast'] += 1
    assert counts['retained_A'] == 858 and counts['retained_B_contrast'] == 955
    # Explicit equality examples derived before this check. Neither is a sweep.
    explicit = []
    for p, g, u, v, k in [(97, 5, 1, 5, 2), (4201, 48, 1, 22, 1)]:
        assert prime(p) and p % 24 == 1
        x, y, z = g*u*v, p*g*k*u, p*g*k*v
        r = test_A(p, x, y, z, g*u*u, 4*x-p, least_nr(p))
        assert 8*r['q']*g == (2*p + r['q'] + 1 if u*v % 2 else p + 2*r['q'] + 1)
        r['residue_mod_840'] = p % 840
        explicit.append(r)
    assert before == historical_hashes()
    assert manifest() == 34
    print(json.dumps({
        'result': 'PASS', 'python': platform.python_version(),
        'platform': platform.platform(), 'elapsed_ns': time.perf_counter_ns()-start,
        'source_sha256': sha(Path(__file__)), 'input_sha256': sha(SOURCE),
        'input': str(SOURCE.relative_to(ROOT)), 'saved_pairs': len(rows),
        'saved_primes': len(primes), 'least_nr_range': [min(qs.values()), max(qs.values())],
        'H005_manifest_count': 34, 'historical_files_checked': len(before),
        'historical_aggregate_sha256': hashlib.sha256(json.dumps(before, sort_keys=True).encode()).hexdigest(),
        'historical_payloads_unchanged': True, 'counts': dict(counts),
        'examples': examples, 'explicit_equalities': explicit,
        'limits': 'First saved A/B certificate per retained pair only; not all solutions. No new prime interval, shifts, or parameter sweep. Exact least-nonresidue scan at the retained 187 primes plus explicit 97 and retained 4201. No historical script replay, network, installation, Lean, or independent-agent claim. Paper proofs carry universal quantifiers.'
    }, indent=2))


if __name__ == '__main__':
    main()
