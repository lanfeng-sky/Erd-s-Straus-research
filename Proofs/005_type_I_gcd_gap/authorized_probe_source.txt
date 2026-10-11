#!/usr/bin/env python3
"""R-005 local-only reproduction and Type-I gcd/gap certificate regression.
No network, project imports, prime interval, offset expansion, or new solution search.
Read-only on historical handoffs. Run with assertions enabled.
"""
from pathlib import Path
from math import gcd, isqrt
from collections import Counter
import hashlib
import json
import platform
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest(folder):
    result = []
    for line in (folder / 'SHA256SUMS').read_text().splitlines():
        digest, name = line.split(maxsplit=1)
        name = name.lstrip('*')
        assert Path(name).name == name
        assert sha(folder / name) == digest, name
        result.append({'file': name, 'sha256': digest})
    return result


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def chi(a, p):
    r = pow(a % p, (p-1)//2, p)
    assert r in (0, 1, p-1)
    return -1 if r == p-1 else r


def certificate(p, x, y, z):
    assert min(p, x, y, z) > 0
    assert 4*x*y*z == p*(x*y + x*z + y*z)


def main():
    assert __debug__
    h4 = ROOT / 'handoffs/004_construction_obstruction'
    h2 = ROOT / 'handoffs/002_structure'
    hashes4 = manifest(h4)
    hashes2 = manifest(h2)
    started = time.perf_counter_ns()
    run = subprocess.run(['python3', str(h4 / 'check_retained.py')],
                         text=True, capture_output=True)
    elapsed = time.perf_counter_ns() - started
    assert run.returncode == 0 and not run.stderr
    assert run.stdout.encode() == (h4 / 'retained_check_stdout.json').read_bytes()
    rows = [json.loads(line) for line in (h2 / 'pairs.jsonl').read_text().splitlines()]
    assert len(rows) == 2991
    primes = sorted({r['p'] for r in rows})
    assert len(primes) == 187 and all(prime(p) for p in primes)
    # Same least-nonresidue domain already used by R-003; no new primes.
    qs = {p: next(q for q in range(2, p) if chi(q, p) == -1) for p in primes}
    assert all(prime(q) and q*q < p and q >= 5 for p, q in qs.items())
    counts = Counter()
    example = None
    for row in rows:
        p, x, a = (row[s] for s in ('p', 'x', 'a'))
        assert p % 24 == 1 and a == 4*x-p
        w = row['B']
        if w is None:
            continue
        C, y, z = (w[s] for s in ('c', 'y', 'z'))
        certificate(p, x, y, z)
        assert p//4 < x < p and x % p and z % p and y % p == 0
        d0 = gcd(C, x)
        u, v = C//d0, x//d0
        assert d0 % u == 0
        g = d0//u
        assert x == g*u*v and C == g*u*u and gcd(u, v) == 1
        assert (p*u+v) % a == 0
        k = (p*u+v)//a
        assert (y, z) == (p*g*u*k, g*v*k)
        M = 4*g*u*k-1
        assert M % p == 0
        h = M//p
        assert h*v == u+k and h % 4 == 3
        assert gcd(u, k) == gcd(v, k) == 1
        G = gcd(x, gcd(y, z))
        assert G == g and chi(g, p) == -1 and g >= qs[p]
        # Sort the two p-free denominators by swapping u and k.
        U, K = sorted((u, k))
        assert U < K
        X, Z = g*U*v, g*K*v
        assert X == min(x, y, z) and Z == max(x, z)
        delta = p-2*X
        assert delta*(U+K) == v*(2*g*U*(K-U)-1)
        assert 3*delta >= 2*g-1
        assert 15*delta >= 14*g-1
        assert 30*X <= 15*p-14*g+1 <= 15*p-14*qs[p]+1
        equality = 15*delta == 14*g-1
        assert equality == (U == 7 and K == 8 and v == 1)
        if equality:
            assert g % 45 == 29 and p == (224*g-1)//15
            counts['sharp_equalities_in_retained_B'] += 1
        counts['retained_B_certificates'] += 1
        if example is None:
            example = {'p': p, 'triple': [x, y, z], 'G': G,
                       'q': qs[p], 'normalized': [g, U, v, K, h],
                       'delta': delta}
    assert counts['retained_B_certificates'] == 955
    # One explicitly derived sharpness certificate, not a search or prime interval.
    p, g = 433, 29
    assert prime(p) and p % 24 == 1
    X, Z, Y = 7*g, 8*g, 56*p*g
    certificate(p, X, Z, Y)
    assert gcd(X, gcd(Z, Y)) == g and chi(g, p) == -1
    assert X == min(X, Z, Y) and 30*X == 15*p-14*g+1
    out = {
        'result': 'PASS', 'python': platform.python_version(),
        'platform': platform.platform(), 'source_sha256': sha(Path(__file__)),
        'H004_manifest': hashes4, 'H002_manifest': hashes2,
        'H004_retained_checker': {'exit_code': run.returncode, 'stderr': run.stderr,
                                  'elapsed_ns': elapsed, 'stdout_byte_identical': True,
                                  'stdout': json.loads(run.stdout)},
        'domain': {'saved_pairs': len(rows), 'saved_primes': len(primes),
                   'new_search_ranges': [], 'sharpness_certificate_only': 433},
        'counts': dict(counts), 'first_retained_B_example': example,
        'sharpness_example': {'p': p, 'G': g, 'triple': [X, Z, Y]},
        'limits': 'Only the first saved B witness per successful pair was checked, not all completions. Universal claims rest on the written proof. No network, new solution search, formalization, or external novelty claim.'
    }
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
