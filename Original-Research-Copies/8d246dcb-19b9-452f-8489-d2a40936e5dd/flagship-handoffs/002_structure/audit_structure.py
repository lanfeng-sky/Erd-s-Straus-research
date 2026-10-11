#!/usr/bin/env python3
"""D-002: exact prescribed domain only. Standard library; no external imports.
--out ABSOLUTE_DIR writes records; --check ABSOLUTE_DIR recomputes and compares.
Without arguments, recompute without writes. Do not run with python -O.
"""
import argparse
from collections import Counter
from itertools import product
from math import gcd, isqrt, prod
from pathlib import Path
import hashlib
import json
import platform
import sys
from time import perf_counter_ns

RESIDUES = {1, 121, 169, 289, 361, 529}
SEVEN = [20521, 31081, 39841, 51361, 58321, 66889, 88729]


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def sieve(n):
    f = [True] * (n + 1)
    f[0] = f[1] = False
    for d in range(2, isqrt(n) + 1):
        if f[d]:
            for j in range(d*d, n + 1, d):
                f[j] = False
    return [j for j in range(2, n + 1) if f[j]]


def factor(n):
    original, fs, d = n, [], 2
    while d*d <= n:
        e = 0
        while n % d == 0:
            n //= d
            e += 1
        if e:
            fs.append((d, e))
        d = 3 if d == 2 else d + 2
    if n > 1:
        fs.append((n, 1))
    assert prod(q**e for q, e in fs) == original
    assert all(prime(q) and e > 0 for q, e in fs)
    return fs


def reference_factor(n):
    # Different trial schedule: 2,3, then 6j+-1; factor px afresh.
    original, fs = n, []
    for d in (2, 3):
        e = 0
        while n % d == 0:
            n //= d
            e += 1
        if e:
            fs.append((d, e))
    d, step = 5, 2
    while d*d <= n:
        e = 0
        while n % d == 0:
            n //= d
            e += 1
        if e:
            fs.append((d, e))
        d, step = d + step, 6 - step
    if n > 1:
        fs.append((n, 1))
    assert prod(q**e for q, e in fs) == original
    assert all(prime(q) and e > 0 for q, e in fs)
    return fs


def divisors(fs, scale=1):
    ds = sorted(prod(q**j for (q, _), j in zip(fs, exps))
                for exps in product(*(range(scale*e + 1) for _, e in fs)))
    assert len(ds) == len(set(ds)) == prod(scale*e + 1 for _, e in fs)
    return ds


def reference_divisors(fs, scale=1):
    def walk(i, v):
        if i == len(fs):
            yield v
            return
        q, e = fs[i]
        for _ in range(scale*e + 1):
            yield from walk(i + 1, v)
            v *= q
    out = sorted(walk(0, 1))
    assert len(out) == len(set(out)) == prod(scale*e + 1 for _, e in fs)
    return out


def certificate(p, x, y, z):
    assert all(type(v) is int and v > 0 for v in (p, x, y, z))
    assert 4*x*y*z == p*(x*y + x*z + y*z)


def reconstruct(p, x, c, branch):
    a, E = 4*x - p, x*x // c
    assert x*x % c == 0
    nums = (p*(x+c), p*(x+E)) if branch == 'A' else (p*(x+p*c), p*x+E)
    assert all(n > 0 and n % a == 0 for n in nums)
    y, z = (n // a for n in nums)
    certificate(p, x, y, z)
    assert y % p == 0
    assert (z % p == 0) == (branch == 'A')
    return {'c': c, 'E': E, 'y': y, 'z': z}


def normalized(p, x, c):
    w = gcd(c, x)
    u, v = c // w, x // w
    assert gcd(u, v) == 1 and x % (u*v) == 0
    g, a = x // (u*v), 4*x-p
    assert (u+v) % a == 0
    k = (u+v) // a
    d, e = 4*g*k*u-1, 4*g*k*v-1
    assert min(g, k, d, e) > 0
    assert d*e == 4*g*k*k*p+1
    certificate(p, g*u*v, p*g*k*u, p*g*k*v)
    return {'g': g, 'k': k, 'u': u, 'v': v, 'd': d, 'e': e}


def pair(p, t):
    x = (p+3)//4 + t
    a, b = 4*x-p, p*x
    assert p % 4 == 1 and p//4 < x < p and gcd(a, b) == 1
    fx = factor(x)
    cs = divisors(fx, 2)
    As = [c for c in cs if (c+x) % a == 0]
    Bs = [c for c in cs if (4*c+1) % a == 0]
    # Check EVERY returned c, not only the retained first witness.
    wa = [reconstruct(p, x, c, 'A') for c in As]
    wb = [reconstruct(p, x, c, 'B') for c in Bs]
    ref = Counter()
    for d in reference_divisors(reference_factor(b), 2):
        if d > b:
            break  # Swap positive factors; d<=sqrt(b^2)=b is complete.
        e = b*b // d
        assert d*e == b*b
        if (d+b) % a or (e+b) % a:
            continue
        y, z = (d+b)//a, (e+b)//a
        certificate(p, x, y, z)
        vp = 0
        j = d
        while j % p == 0:
            j //= p
            vp += 1
        assert vp in (0, 1, 2)
        ref['A' if vp == 1 else 'B'] += 1
    assert bool(As) == bool(ref['A']) and bool(Bs) == bool(ref['B']), (p, x)
    D = set(d % a for d in divisors(fx))
    R = {u*pow(v, -1, a) % a for u in D for v in D}
    C = {c % a for c in cs}
    assert R == {c*pow(x, -1, a) % a for c in C}
    # A third residue construction, via signed exponent boxes.
    signed = {prod(pow(q % a, j, a) for (q, _), j in zip(fx, js)) % a
              for js in product(*(range(-e, e+1) for _, e in fx))}
    assert R == signed
    H, todo = {1}, [1]
    while todo:
        v = todo.pop()
        for q, _ in fx:
            w = v*q % a
            if w not in H:
                H.add(w)
                todo.append(w)
    assert R <= H
    ta, tb = (-1) % a, (-p) % a
    assert bool(As) == (ta in R) and bool(Bs) == (tb in R)
    assert (tb in R) == ((-pow(p, -1, a)) % a in R)
    row = {'p': p, 't': t, 'x': x, 'a': a, 'factor_x': fx,
           'A': wa[0] if wa else None, 'B': wb[0] if wb else None,
           'A_count': len(As), 'B_count': len(Bs), 'factor_pairs': dict(ref),
           'c_residues': sorted(C), 'c_count': len(cs),
           'D': sorted(D), 'R': sorted(R), 'H': sorted(H),
           'targets': [ta, tb], 'obstruction': None, 'saturation': None}
    if not As and not Bs:
        blockers = [ell for ell, _ in factor(a) if ell % 4 == 3 and
                    all(pow(q % ell, (ell-1)//2, ell) == 1 for q, _ in fx)]
        if blockers:
            assert ta not in H and tb not in H
            row['obstruction'] = {'kind': 'quadratic', 'ell': min(blockers),
                                  'legendre': [[q, pow(q % min(blockers), (min(blockers)-1)//2, min(blockers))] for q, _ in fx]}
        elif ta not in H and tb not in H:
            row['obstruction'] = {'kind': 'subgroup_other', 'excluded_targets': [ta, tb]}
        else:
            row['obstruction'] = {'kind': 'bounded_exponent',
                                  'permitted_targets': sorted({ta, tb} & H)}
    # Check all prime-defect branch-A failures, including possible B-only hits.
    if prime(a) and a % 4 == 3 and ta in H:
        h = len(H)
        assert h % 2 == 0 and (h//2) % 2 == 1
        checks = []
        for r in range(1, h+1, 2):
            if h % r:
                continue
            K = sorted(v for v in H if pow(v, r, a) == 1)
            assert len(K) == r
            N = sum(e for q, e in fx if q % a not in K)
            checks.append({'r': r, 'K': K, 'N': N, 'threshold': h//(2*r)})
        stabilizer = sorted(v for v in H if {v*d % a for d in D} == D)
        s = len(stabilizer)
        Ns = sum(e for q, e in fx if q % a not in stabilizer)
        assert len(D) >= s*(1+Ns)  # Bounded check of the conditional input's consequence.
        deficient = [v for v in checks if v['N'] < v['threshold']]
        if not As:
            assert deficient and s % 2 == 1 and Ns <= h//(2*s)-1
        if not deficient:
            assert As
        row['saturation'] = {'h': h, 'all_odd_subgroups': checks,
                             'deficient': deficient, 'stabilizer': stabilizer}
    if wa:
        row['normalized_A'] = normalized(p, x, wa[0]['c'])
    return row


def switch(p, g, k):
    N, m = 4*g*k*k*p+1, 4*g*k
    fs = factor(N)
    assert fs == reference_factor(N)
    ds = divisors(fs)
    assert ds == reference_divisors(fs)
    small = [d for d in ds if d*d <= N]
    hits = [d for d in small if d % m == m-1]
    row = {'p': p, 'g': g, 'k': k, 'N': N, 'modulus': m,
           'factor_N': fs, 'small_divisor_count': len(small), 'witness': None}
    if hits:
        d, e = hits[0], N // hits[0]
        assert e % m == m-1
        u, v = (d+1)//m, (e+1)//m
        x, y, z = g*u*v, p*g*k*u, p*g*k*v
        certificate(p, x, y, z)
        assert u+v == k*(4*x-p)
        row['witness'] = {'d': d, 'e': e, 'u': u, 'v': v, 'x': x, 'y': y, 'z': z}
    return row


def compute():
    selected = [p for p in sieve(100000) if p % 840 in RESIDUES]
    independent = [p for p in range(2, 100001) if p % 840 in RESIDUES and prime(p)]
    assert selected == independent
    failures = [p for p in selected if all(q % 3 == 1 for q, _ in factor((p+3)//4))]
    assert (len(selected), len(failures)) == (273, 186)
    assert prime(118801) and 118801 % 840 in RESIDUES
    pairs = [pair(p, t) for p in failures for t in range(16)]
    pairs += [pair(118801, t) for t in range(15)]
    assert len(pairs) == 2991
    bykey = {(r['p'], r['t']): r for r in pairs}
    trap = bykey[1201, 2]
    assert trap['x'] == 303 and trap['a'] == 11
    assert trap['D'] == [1, 2, 3, 6] and trap['R'] == [1, 2, 3, 4, 6, 7, 8]
    assert trap['H'] == list(range(1, 11)) and not trap['A'] and not trap['B']
    assert all(not bykey[118801, t]['A'] and not bykey[118801, t]['B'] for t in range(14))
    assert bykey[118801, 14]['x'] == 29715 and bykey[118801, 14]['A']
    certificate(118801, 29715, 59834124, 5077395546660)
    switched, comparisons = [], []
    for p in SEVEN:
        found = None
        for g in range(1, 17):
            for k in range(1, 17):
                r = switch(p, g, k)
                switched.append(r)
                if r['witness']:
                    found = r
                    break
            if found:
                break
        available = [{'t': r['t'], 'x': r['x'], **r['normalized_A']}
                     for r in pairs if r['p'] == p and r['A']]
        comparisons.append({'p': p, 'first_switch': found,
                            'normalized_A': available})
    # Exactly two cross-shift guesses, with smallest (p,t) counterexamples.
    c1, c2, antecedents1, antecedents2 = [], [], 0, 0
    for p in failures + [118801]:
        T = 16 if p != 118801 else 15
        for t in range(T-1):
            r, s = bykey[p, t], bykey[p, t+1]
            if r['obstruction'] and r['obstruction']['kind'] != 'quadratic':
                antecedents1 += 1
                if not s['A'] and not s['B']:
                    c1.append({'p': p, 't': t, 'next_t': t+1})
        prime_rows = [bykey[p, t] for t in range(T) if prime(bykey[p, t]['a'])]
        for r, s in zip(prime_rows, prime_rows[1:]):
            if (-1) % r['a'] in r['H'] and (-1) % s['a'] in s['H']:
                antecedents2 += 1
                if not any([r['A'], r['B'], s['A'], s['B']]):
                    c2.append({'p': p, 't': r['t'], 'next_t': s['t']})
    kinds = Counter('both' if r['A'] and r['B'] else 'A_only' if r['A'] else 'B_only' if r['B'] else 'neither' for r in pairs)
    obstructions = Counter(r['obstruction']['kind'] for r in pairs if r['obstruction'])
    sats = [r for r in pairs if r['saturation']]
    firsts = [next(r['t'] for r in pairs if r['p'] == p and (r['A'] or r['B'])) for p in failures]
    stats = {'result': 'PASS', 'selected_primes': len(selected), 'x0_failures': len(failures),
             'pairs': len(pairs), 'branch_status': dict(kinds), 'obstructions': dict(obstructions),
             'factor_pair_disagreements': 0, 'certificates_checked_compact': sum(r['A_count']+r['B_count'] for r in pairs),
             'certificates_checked_factor_pairs': sum(sum(r['factor_pairs'].values()) for r in pairs),
             'prime_defect_minus_one_in_H': len(sats),
             'prime_defect_A_failures_with_deficiency': sum(not r['A'] for r in sats),
             'full_failures_with_deficiency': sum(not r['A'] and not r['B'] for r in sats),
             'first_offset_histogram_186': dict(sorted(Counter(firsts).items())),
             '118801_first_offset': 14,
             'switched_candidates': len(switched), 'switched_solved': sum(bool(r['first_switch']) for r in comparisons),
             'switched_first_g_k': [[r['p'], r['first_switch']['g'], r['first_switch']['k']] for r in comparisons if r['first_switch']],
             'cross_shift_candidates': [
                 {'id': 'C1', 'antecedents': antecedents1, 'counterexample_count': len(c1), 'smallest': c1[0] if c1 else None},
                 {'id': 'C2', 'antecedents': antecedents2, 'counterexample_count': len(c2), 'smallest': c2[0] if c2 else None}]}
    return {'pairs.jsonl': pairs, 'switches.jsonl': switched,
            'switch_comparison.json': comparisons, 'summary.json': stats}


def encode(name, obj):
    if name.endswith('.jsonl'):
        return ''.join(json.dumps(r, sort_keys=True, separators=(',', ':'))+'\n' for r in obj)
    return json.dumps(obj, sort_keys=True, indent=2)+'\n'


def main():
    assert __debug__, 'Assertions required: do not use -O'
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--out', type=Path)
    group.add_argument('--check', type=Path)
    args = parser.parse_args()
    directory = args.out or args.check
    if directory:
        assert directory.is_absolute(), 'Use an absolute output/check path'
    started = perf_counter_ns()
    data = compute()
    hashes = {name: hashlib.sha256(encode(name, obj).encode()).hexdigest() for name, obj in data.items()}
    if args.out:
        args.out.mkdir(parents=True, exist_ok=True)
        for name, obj in data.items():
            path = args.out/name
            assert not path.exists(), ('Refusing overwrite', path)
            path.write_text(encode(name, obj))
    if args.check:
        for name, obj in data.items():
            assert (args.check/name).read_text() == encode(name, obj), ('Record mismatch', name)
    environment = {'python': sys.version, 'platform': platform.platform(), 'architecture': platform.machine(),
                   'runtime_ns': perf_counter_ns()-started,
                   'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   'artifact_sha256': hashes, 'check_mode': bool(args.check)}
    if args.out:
        (args.out/'environment.json').write_text(json.dumps(environment, indent=2)+'\n')
    print(json.dumps(data['summary.json'], indent=2))
    print(json.dumps(environment, indent=2))


if __name__ == '__main__':
    main()
