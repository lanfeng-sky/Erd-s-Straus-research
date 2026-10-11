#!/usr/bin/env python3
"""Standalone H-004 saved-evidence audit; no project imports or new search.
Checks six named records, their six positive certificates, the 193 A certificate,
and the complete 24-residue no-witness certificate for 193 already in I-008.
Does NOT rerun full c,k searches for other inputs or prove reciprocity.
Run without -O in this directory or anywhere using an absolute script path.
"""
from pathlib import Path
from math import gcd, isqrt
import hashlib
import json

HERE = Path(__file__).resolve().parent
NS = (193, 1009, 1129, 1201, 2521, 66529)
COUNTS = (0, 2, 2, 2, 0, 0)
CK_COUNTS = (60, 450, 513, 553, 1314, 52762)
RESIDUES_193 = ((5, 4), (8, 6), (17, 2), (18, 5), (19, 8),
                (20, 11), (21, 14), (22, 17), (23, 20), (24, 23))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def certificate(n, x, y, z):
    assert all(type(t) is int and t > 0 for t in (n, x, y, z))
    assert 4*x*y*z == n*(x*y+x*z+y*z)


def jacobi(a, m):
    # Exact Euclidean reciprocity algorithm, odd positive m; not factorization.
    assert m > 0 and m % 2 == 1
    a %= m
    sign = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if m % 8 in (3, 5):
                sign = -sign
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3:
            sign = -sign
        a %= m
    return sign if m == 1 else 0


def main():
    assert __debug__, 'Assertions must be enabled'
    raw = HERE/'authorized_probe_stdout.json'
    env = json.loads((HERE/'environment.json').read_text())
    data = json.loads(raw.read_text())
    assert sha(raw) == env['stdout_sha256']
    assert sha(HERE/'authorized_probe_source.txt') == env['source_sha256']
    assert data['source_sha256'] == env['source_sha256']
    assert data['result'] == 'PASS' and env['exit_code'] == 0 and not env['stderr']
    rows = data['U007_exact_domain']
    assert tuple(r['n'] for r in rows) == NS
    assert tuple(len(r['witnesses']) for r in rows) == COUNTS
    assert tuple(r['ck_candidates'] for r in rows) == CK_COUNTS
    checked = 0
    for r in rows:
        n = r['n']
        assert all(n % d for d in range(2, isqrt(n)+1))
        assert r['prime_by_trial_division'] and r['M_candidates'] == (n+3)//8
        for w in r['witnesses']:
            a, c, k = w['a'], w['c'], w['k']
            assert a >= 3 and a % 4 == 3 and c > 0 and k > 0
            assert n == a*(4*c*k-1)-4*c
            assert 8*c*k <= n+3 and 12*c*k <= n+4*c+3
            m = a*k-1
            x, y, z = w['triple']
            assert (x, y, z) == (c*m, c*k*n, c*m*k*n)
            assert 0 < x < n <= y <= z and 4*x-n == a
            certificate(n, x, y, z)
            M = 4*c*k-1
            assert gcd(n, M) == gcd(c, M) == 1
            assert jacobi(c, M) == 1 and jacobi(-c, M) == jacobi(n, M) == -1
            checked += 1

    # Reevaluate ONLY the existing compact 193 certificate, all 24 h.
    candidates = []
    for h in range(1, 25):
        M = 4*h-1
        r = 193 % M
        if r == M-1:
            c = h
        elif (M-r) % 4 == 0:
            c = (M-r)//4
        else:
            continue
        assert c > 0
        candidates.append((h, c))
        assert h % c != 0
    assert tuple(candidates) == RESIDUES_193

    x, y, z = data['193_full_A_certificate']
    assert (x, y, z) == (50, 1930, 4825)
    g, u, v, k, a, p = 5, 2, 5, 1, 7, 193
    assert gcd(u, v) == gcd(u, k) == 1
    assert x == g*u*v and u+v == k*a and 4*x-p == a
    assert (y, z) == (p*g*k*u, p*g*k*v)
    assert z % y and y % z
    M = 4*g*u*k-1
    assert p == M*a-4*g*u*u and jacobi(p, M) == -1
    certificate(p, x, y, z)

    # Exact countercheck of I-008's false auxiliary equality on RETAINED data.
    w = rows[1]['witnesses'][0]
    n, a, c, k, x = 1009, w['a'], w['c'], w['k'], w['triple'][0]
    assert (a, c, k, x) == (3, 11, 8, 253)
    assert n-x == 756 and c*(3*a*k-4)-a == 745
    assert n-x != c*(3*a*k-4)-a
    assert n-x == c*(3*a*k-3)-a

    print(json.dumps({'result': 'PASS', 'source_sha256': sha(Path(__file__)),
                      'domain_n': NS, 'retained_U_certificates_checked': checked,
                      '193_full_A_certificate_checked': True,
                      '193_h_checked': 24, '193_integral_residue_candidates': candidates,
                      '193_U_witnesses': 0, 'I008_auxiliary_equality': 'false: 756 != 745',
                      'limits': 'Saved certificate audit and existing compact 193 proof only. Other inputs no-hit counts are retained provenance, not reenumerated here. No parameter or prime domain extension; universal Jacobi theorem proved on paper.'}, indent=2))


if __name__ == '__main__':
    main()
