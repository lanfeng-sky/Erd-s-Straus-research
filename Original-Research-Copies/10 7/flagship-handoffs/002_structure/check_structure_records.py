#!/usr/bin/env python3
"""Independent record audit, no generator imports. Direct divisor scanning.
Usage: python3 THIS_FILE ABSOLUTE_RECORD_DIRECTORY. Read-only; no -O.
"""
import json
import sys
import hashlib
from pathlib import Path
from math import isqrt, prod, gcd
from collections import Counter
from time import perf_counter_ns
import platform


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def scan_divisors(n):
    out = set()
    for d in range(1, isqrt(n)+1):
        if n % d == 0:
            out.update((d, n//d))
    return sorted(out)


def cert(p, x, y, z):
    assert all(type(v) is int and v > 0 for v in (p, x, y, z))
    assert 4*x*y*z == p*(x*y+x*z+y*z)


def factor_record(n, fs):
    assert len(fs) == len({q for q, _ in fs})
    assert all(prime(q) and e > 0 for q, e in fs)
    assert prod(q**e for q, e in fs) == n


def check(root):
    rows = [json.loads(s) for s in (root/'pairs.jsonl').read_text().splitlines()]
    keys = {(r['p'], r['t']) for r in rows}
    assert len(keys) == len(rows) == 2991
    selected = [p for p in range(2, 100001) if p % 840 in {1,121,169,289,361,529} and prime(p)]
    # Independent x0 test: a divisor 2 mod 3 iff a prime divisor 2 mod 3.
    failed = [p for p in selected if not any(d % 3 == 2 for d in scan_divisors((p+3)//4))]
    assert len(selected) == 273 and len(failed) == 186
    assert keys == {(p,t) for p in failed for t in range(16)} | {(118801,t) for t in range(15)}
    counts, obs, checked = Counter(), Counter(), 0
    for r in rows:
        p,t,x,a = (r[k] for k in ('p','t','x','a'))
        assert prime(p) and x == (p+3)//4+t and a == 4*x-p and gcd(a,p*x)==1
        factor_record(x, r['factor_x'])
        cs = scan_divisors(x*x)  # Complete: every pair straddles sqrt(x^2)=x.
        aa = [c for c in cs if (c+x)%a == 0]
        bb = [c for c in cs if (4*c+1)%a == 0]
        assert len(aa)==r['A_count'] and len(bb)==r['B_count']
        assert len(cs)==r['c_count'] and sorted({c%a for c in cs})==r['c_residues']
        for branch, candidates in [('A',aa),('B',bb)]:
            w=r[branch]
            assert bool(w)==bool(candidates)
            if w:
                c,E,y,z=(w[k] for k in ('c','E','y','z'))
                assert c==candidates[0] and c*E==x*x
                assert a*y == (p*(x+c) if branch=='A' else p*(x+p*c))
                assert a*z == (p*(x+E) if branch=='A' else p*x+E)
                cert(p,x,y,z)
                checked+=1
            assert bool(candidates)==bool(r['factor_pairs'].get(branch,0))
        D={d%a for d in scan_divisors(x)}
        R={u*pow(v,-1,a)%a for u in D for v in D}
        H={1}
        # Independent group construction using complete powers of each generator.
        for q,_ in r['factor_x']:
            powers={1}; v=q%a
            while v!=1:
                assert v not in powers
                powers.add(v); v=v*q%a
            H={u*v%a for u in H for v in powers}
        assert sorted(D)==r['D'] and sorted(R)==r['R'] and sorted(H)==r['H']
        ta,tb=(-1)%a,(-p)%a
        assert r['targets']==[ta,tb] and bool(aa)==(ta in R) and bool(bb)==(tb in R)
        kind='both' if aa and bb else 'A_only' if aa else 'B_only' if bb else 'neither'
        counts[kind]+=1
        if kind=='neither':
            # Scan ALL prime divisors of a, independent of factoring a.
            ls=[l for l in scan_divisors(a) if prime(l) and l%4==3 and
                all(pow(q,(l-1)//2,l)==1 for q,_ in r['factor_x'])]
            k='quadratic' if ls else 'subgroup_other' if ta not in H and tb not in H else 'bounded_exponent'
            assert r['obstruction']['kind']==k
            if ls:
                assert r['obstruction']['ell']==min(ls)
            obs[k]+=1
        else:
            assert r['obstruction'] is None
        sat=r['saturation']
        assert bool(sat)==(prime(a) and a%4==3 and ta in H)
        if sat:
            h=len(H)
            assert sat['h']==h and h%2==0 and (h//2)%2==1
            checks=[]
            for d in scan_divisors(h):
                if d%2==0: continue
                K=sorted(u for u in H if pow(u,d,a)==1)
                N=sum(e for q,e in r['factor_x'] if q%a not in K)
                checks.append({'r':d,'K':K,'N':N,'threshold':h//(2*d)})
            assert checks==sat['all_odd_subgroups']
            deficient=[v for v in checks if v['N']<v['threshold']]
            assert deficient==sat['deficient'] and (bool(aa) or deficient)
            stab=sorted(u for u in H if {u*d%a for d in D}==D)
            assert stab==sat['stabilizer']
        if aa:
            v=r['normalized_A']; g,k,u,w=(v[s] for s in ('g','k','u','v'))
            assert gcd(u,w)==1 and g*u*w==x and k*a==u+w
            assert v['d']==4*g*k*u-1 and v['e']==4*g*k*w-1
            assert v['d']*v['e']==4*g*k*k*p+1
            cert(p,x,p*g*k*u,p*g*k*w)
    switches=[json.loads(s) for s in (root/'switches.jsonl').read_text().splitlines()]
    assert len(switches)<=1792
    for r in switches:
        p,g,k,N,m=(r[s] for s in ('p','g','k','N','modulus'))
        assert 1<=g<=16 and 1<=k<=16 and N==4*g*k*k*p+1 and m==4*g*k
        factor_record(N,r['factor_N'])
        small=[d for d in scan_divisors(N) if d*d<=N]
        hits=[d for d in small if d%m==m-1]
        assert r['small_divisor_count']==len(small) and bool(r['witness'])==bool(hits)
        if hits:
            w=r['witness']; d,e,u,v,x,y,z=(w[s] for s in ('d','e','u','v','x','y','z'))
            assert d==hits[0] and d*e==N and e%m==m-1
            assert m*u==d+1 and m*v==e+1 and x==g*u*v and y==p*g*k*u and z==p*g*k*v
            cert(p,x,y,z)
    comp=json.loads((root/'switch_comparison.json').read_text())
    assert [r['p'] for r in comp]==[20521,31081,39841,51361,58321,66889,88729]
    for r in comp:
        tested=[s for s in switches if s['p']==r['p']]
        assert tested==sorted(tested,key=lambda s:(s['g'],s['k']))
        last=tested[-1]
        assert last['witness'] and r['first_switch']==last and all(not s['witness'] for s in tested[:-1])
        assert [(s['g'],s['k']) for s in tested]==[(g,k) for g in range(1,17) for k in range(1,17) if (g,k)<=(last['g'],last['k'])]
        available=[{'t':s['t'],'x':s['x'],**s['normalized_A']} for s in rows if s['p']==r['p'] and s['A']]
        assert available==r['normalized_A']
    summary=json.loads((root/'summary.json').read_text())
    assert dict(counts)==summary['branch_status'] and dict(obs)==summary['obstructions']
    env=json.loads((root/'environment.json').read_text())
    for name,h in env['artifact_sha256'].items():
        assert hashlib.sha256((root/name).read_bytes()).hexdigest()==h
    if (root/'audit_structure.py').exists():
        assert hashlib.sha256((root/'audit_structure.py').read_bytes()).hexdigest()==env['source_sha256']
    return {'result':'PASS', 'pairs':len(rows), 'saved_branch_certificates_checked':checked,
            'switch_candidates_directly_scanned':len(switches), 'branch_status':dict(counts), 'obstructions':dict(obs)}


if __name__=='__main__':
    assert __debug__
    root=Path(sys.argv[1]); assert root.is_absolute()
    start=perf_counter_ns()
    result=check(root)
    result.update(runtime_ns=perf_counter_ns()-start,python=sys.version,architecture=platform.machine(),
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    print(json.dumps(result,indent=2))
