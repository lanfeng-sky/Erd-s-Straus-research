#!/usr/bin/env python3
"""R-004 read-only audit. No project imports, network, writes, or range extension.
Reproduce H-003, then test ONLY six explicitly named U-007 examples/exceptions.
Run without -O. JSON stdout may be retained outside historical handoffs.
"""
from pathlib import Path
from math import isqrt
import hashlib
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
H = ROOT / 'handoffs' / '003_joint_inverse'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def certificates(n, triples):
    out = []
    for a, c, k in sorted(triples):
        assert a >= 3 and a % 4 == 3 and c > 0 and k > 0
        assert n == a*(4*c*k-1)-4*c
        m = a*k-1
        x, y, z = c*m, c*k*n, c*m*k*n
        assert 0 < x < n <= y <= z
        assert 4*x*y*z == n*(x*y+x*z+y*z)
        out.append({'a': a, 'c': c, 'k': k, 'triple': [x, y, z]})
    return out


def ck_enumeration(n):
    # Derived bounds: c <= (n+3)/8; 3 <= a=(n+4c)/(4ck-1).
    out, count = set(), 0
    for c in range(1, (n+3)//8+1):
        for k in range(1, (n+4*c+3)//(12*c)+1):
            count += 1
            M = 4*c*k-1
            if (n+4*c) % M == 0:
                out.add(((n+4*c)//M, c, k))
    return out, count


def m_enumeration(n):
    # h=ck <= (n+3)/8. The residue determines c uniquely when it exists.
    out = set()
    for h in range(1, (n+3)//8+1):
        M = 4*h-1
        r = n % M
        if r == M-1:
            c = h  # 4c=M+1: the essential boundary correction.
        elif (M-r) % 4 == 0:
            c = (M-r)//4
        else:
            continue
        if c > 0 and h % c == 0:
            a = (n+4*c)//M
            assert (n+4*c) % M == 0 and a >= 3
            out.add((a, c, h//c))
    return out


def main():
    assert __debug__, 'Run without -O'
    hashes = {}
    for line in (H/'SHA256SUMS').read_text().splitlines():
        want, name = line.split(maxsplit=1)
        name = name.lstrip('*')
        assert '/' not in name and '\\' not in name
        got = digest(H/name)
        assert got == want, name
        hashes[name] = got
    runs = []
    for script, saved in [(H/'check_joint_inverse.py', H/'independent_check.json'),
                          (ROOT/'reviews'/'003_joint_probe.py', H/'flagship_probe_output.json')]:
        start = time.perf_counter_ns()
        r = subprocess.run([sys.executable, str(script)], capture_output=True, timeout=90)
        elapsed = time.perf_counter_ns()-start
        assert r.returncode == 0, (str(script), r.returncode, r.stderr)
        assert r.stdout == saved.read_bytes(), str(script)
        runs.append({'script': str(script.relative_to(ROOT)), 'source_sha256': digest(script),
                     'saved_stdout': str(saved.relative_to(ROOT)), 'exit_code': r.returncode,
                     'byte_identical': True, 'stdout_sha256': hashlib.sha256(r.stdout).hexdigest(),
                     'elapsed_ns': elapsed, 'stderr': r.stderr.decode()})
    rows = []
    for n in (193, 1009, 1129, 1201, 2521, 66529):
        assert all(n % d for d in range(2, isqrt(n)+1))
        by_ck, count = ck_enumeration(n)
        by_m = m_enumeration(n)
        assert by_ck == by_m, n
        rows.append({'n': n, 'prime_by_trial_division': True, 'ck_candidates': count,
                     'M_candidates': (n+3)//8, 'witnesses': certificates(n, by_ck)})
    assert [len(r['witnesses']) for r in rows] == [0, 2, 2, 2, 0, 0]
    n, x, y, z = 193, 50, 1930, 4825
    assert 4*x*y*z == n*(x*y+x*z+y*z)
    assert (4*5*2-1)*7-4*5*2**2 == 193  # full A: g=5,u=2,v=5,k=1,a=7.
    print(json.dumps({'result': 'PASS', 'python': sys.version,
                      'source_sha256': digest(Path(__file__)), 'H003_payload_hashes': hashes,
                      'reproduction': runs, 'U007_exact_domain': rows,
                      '193_full_A_certificate': [x, y, z],
                      'limitations': 'H-003 has four abstract test groups only. U-007 audit covers the exact normalized family on six named values only, not every screenshot formula. No square scan; the square obstruction is proved on paper. No universal existence or literature-novelty claim.'}, indent=2))


if __name__ == '__main__':
    main()
