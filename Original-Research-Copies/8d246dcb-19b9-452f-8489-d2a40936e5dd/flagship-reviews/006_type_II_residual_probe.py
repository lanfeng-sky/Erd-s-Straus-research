#!/usr/bin/env python3
"""R-006: unchanged H-005 replay plus retained Type-II regression.
Offline, standard library, no search or writes to historical inputs.
The new regression reads only the first saved A witness at each retained pair.
"""
from pathlib import Path
from math import gcd, isqrt
from collections import Counter
import hashlib
import json
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
H5 = ROOT / 'handoffs/005_type_I_gcd_gap'
RESIDUAL = {1, 121, 169, 289, 361, 529}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def manifest():
    out = []
    for line in (H5 / 'SHA256SUMS').read_text().splitlines():
        digest, name = line.split(maxsplit=1)
        name = name.lstrip('*')
        p = (H5 / name).resolve()
        assert p.is_relative_to(H5.resolve())
        assert sha(p) == digest, name
        out.append({'file': name, 'sha256': digest})
    return out


def certificate(p, x, y, z):
    assert min(p, x, y, z) > 0
    assert 4*x*y*z == p*(x*y + x*z + y*z)


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def main():
    assert __debug__
    before = manifest()
    run = subprocess.run([sys.executable, str(H5 / 'replay/reviews/005_gcd_gap_probe.py')],
                         text=True, capture_output=True)
    assert run.returncode == 0 and not run.stderr
    replay = json.loads(run.stdout)
    expected = json.loads((H5 / 'snapshot_replay_stdout.json').read_text())
    elapsed = replay['H004_retained_checker'].pop('elapsed_ns')
    expected['H004_retained_checker'].pop('elapsed_ns')
    assert replay == expected
    source = H5 / 'replay/handoffs/002_structure/pairs.jsonl'
    rows = [json.loads(s) for s in source.read_text().splitlines()]
    assert len(rows) == 2991
    ps = {r['p'] for r in rows}
    assert len(ps) == 187 and all(prime(p) for p in ps)
    counts = Counter()
    examples = {}
    for row in rows:
        w = row['A']
        if w is None:
            continue
        p, x, a = (row[s] for s in ('p', 'x', 'a'))
        C, y, z = (w[s] for s in ('c', 'y', 'z'))
        assert p % 24 == 1 and a == 4*x-p
        certificate(p, x, y, z)
        assert x % p and y % p == z % p == 0 and x == min(x, y, z)
        d = gcd(C, x)
        u, v = C//d, x//d
        assert d % u == 0
        g = d//u
        assert x == g*u*v and C == g*u*u and (u+v) % a == 0
        k = (u+v)//a
        assert (y, z) == (p*g*k*u, p*g*k*v)
        assert gcd(u, v) == gcd(u, k) == gcd(v, k) == 1
        assert gcd(x, gcd(y, z)) == g
        u, v = sorted((u, v))
        b = g*k*u
        assert b == min(y, z)//p
        assert k*p == (4*b-1)*v-u
        assert b >= 2
        assert 7*x <= 2*p+4
        assert (7*x == 2*p+4) == (g == k == 1 and u == 2)
        counts['retained_A_certificates'] += 1
        if p % 840 in RESIDUAL:
            assert p % 7 in {1, 2, 4}
            assert b >= 3
            assert 11*x <= 3*p+9
            assert (11*x == 3*p+9) == (g == k == 1 and u == 3)
            if 11*x == 3*p+9:
                assert p % 11 == 8
                counts['residual_equalities_in_retained_A'] += 1
            counts['residual_A_certificates'] += 1
            examples.setdefault('first_residual', {'p': p, 'triple': [x, y, z],
                                                  'normalized': [g, u, v, k], 'b': b})
    assert counts['retained_A_certificates'] == 858
    # Two algebraically specified extremizers, not an interval/parameter search.
    for p, m in [(313, 2), (1009, 3)]:
        assert prime(p) and p % 24 == 1
        assert (p+m) % (4*m-1) == 0
        v = (p+m)//(4*m-1)
        x, y, z = m*v, m*p, v*p
        certificate(p, x, y, z)
        assert gcd(x, gcd(y, z)) == 1 and x == min(x, y, z)
        assert x % p and y % p == z % p == 0
        assert (4*m-1)*x == m*p+m*m
        if m == 3:
            assert p % 840 in RESIDUAL
        examples[f'explicit_m{m}'] = {'p': p, 'triple': [x, y, z], 'G': 1,
                                      'bound_both_sides': (4*m-1)*x}
    assert before == manifest()
    result = {'result': 'PASS', 'python': platform.python_version(),
              'platform': platform.platform(), 'source_sha256': sha(Path(__file__)),
              'H005_manifest_count': len(before), 'H005_manifest': before,
              'H005_payloads_unchanged': True,
              'H005_replay': {'exit_code': run.returncode, 'stderr': run.stderr,
                              'agrees_except_timing': True,
                              'H004_elapsed_ns': elapsed,
                              'counts': replay['counts']},
              'input': {'path': str(source.relative_to(ROOT)), 'sha256': sha(source),
                        'saved_pairs': len(rows), 'saved_primes': len(ps)},
              'counts': dict(counts), 'examples': examples,
              'limits': 'First retained A certificates only, not all completions. No new prime interval or parameter sweep. Explicit 313 and 1009 extremizers only. Universal claims depend on the written proof, not this regression. No network or formal verification.'}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
