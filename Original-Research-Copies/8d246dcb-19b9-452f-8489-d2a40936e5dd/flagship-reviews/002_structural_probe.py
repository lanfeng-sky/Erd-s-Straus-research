#!/usr/bin/env python3
"""R-002/I-002 exact diagnostic; standard library, no file writes or network.
Run this mounted file directly. Deliberately independent of H-001 helpers.
Scope: selected primes <=100000; x=x0+t, 0<=t<=63, stopping at first hit.
Also probes prime-defect and square-root windows; those are limited searches.
"""
from math import isqrt, prod, gcd
from collections import Counter
import json, platform, sys
from time import perf_counter

RESIDUES = {1, 121, 169, 289, 361, 529}

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))

def factor(n):
    original = n
    out = []
    q = 2
    while q*q <= n:
        e = 0
        while n % q == 0:
            n //= q
            e += 1
        if e:
            out.append((q, e))
        q = 3 if q == 2 else q + 2
    if n > 1:
        out.append((n, 1))
    assert prod(q**e for q,e in out) == original
    assert all(prime(q) and e > 0 for q,e in out)
    return out

def divisors(fs, scale=1):
    out = [1]
    for q,e in fs:
        out = [d*q**j for d in out for j in range(scale*e+1)]
    assert len(out) == len(set(out)) == prod(scale*e+1 for _,e in fs)
    return sorted(out)

def cert(p,x,y,z):
    assert min(p,x,y,z) > 0
    assert 4*x*y*z == p*(x*y+x*z+y*z)

def compact(p,x):
    a = 4*x-p
    assert p%4 == 1 and p//4 < x < p and gcd(a,p*x) == 1
    fx = factor(x)
    ds = divisors(fx,2)
    A = next((d for d in ds if (d+x)%a == 0),None)
    B = next((d for d in ds if (4*d+1)%a == 0),None)
    for kind,d in [('A',A),('B',B)]:
        if d is None:
            continue
        if kind == 'A':
            num1, num2 = p*(x+d), p*(x+x*x//d)
        else:
            num1, num2 = p*(x+p*d), p*x+x*x//d
        assert num1%a == num2%a == 0
        cert(p,x,num1//a,num2//a)
    return A,B,fx

def exhaustive(p,x):
    a,b = 4*x-p,p*x
    hits = []
    # Independently factor b rather than importing the compact x factorization.
    for d in divisors(factor(b),2):
        if d>b:
            break
        e = b*b//d
        if (b+d)%a == (b+e)%a == 0:
            y,z = (b+d)//a,(b+e)//a
            cert(p,x,y,z)
            hits.append((y,z))
    return hits

def group(a,fx):
    H={1}
    todo=[1]
    while todo:
        u=todo.pop()
        for q,_ in fx:
            v=u*q%a
            if v not in H:
                H.add(v)
                todo.append(v)
    return H

def obstruction(p,x,fx):
    a=4*x-p
    blockers=[ell for ell,_ in factor(a) if ell%4==3 and all(pow(q%ell,(ell-1)//2,ell)==1 for q,_ in fx)]
    H=group(a,fx)
    if (-1)%a not in H and (-p)%a not in H:
        return 'quadratic' if blockers else 'subgroup_other'
    return 'bounded_exponent'

def main():
    start=perf_counter()
    P=[p for p in range(2,100001) if p%840 in RESIDUES and prime(p)]
    successes=[]; failures=[]
    for p in P:
        x=(p+3)//4
        fx=factor(x)
        works=any(q%3==2 for q,e in fx)
        assert works == bool(exhaustive(p,x))
        if works: successes.append(p)
        else: failures.append(p)
    assert (len(P),len(successes),len(failures)) == (273,87,186)
    print('independent_x0',len(P),len(successes),len(failures))
    counts=Counter(); first=[]; survivors=[]; pairs=0; first_obstruction={}
    for p in failures:
        x0=(p+3)//4
        for t in range(64):
            x=x0+t
            if x>3*p//4: break
            A,B,fx=compact(p,x)
            hits=exhaustive(p,x)
            assert (A is not None or B is not None) == bool(hits)
            pairs+=1
            if hits:
                first.append((p,t,4*x-p, 'both' if A is not None and B is not None else 'A' if A is not None else 'B'))
                break
            k=obstruction(p,x,fx)
            counts[k]+=1
            first_obstruction.setdefault(k,(p,x,4*x-p,fx))
        else:
            survivors.append(p)
    print('offset_window',json.dumps({'pairs':pairs,'solved':len(first),'survivors':survivors,'max_offset':max(r[1] for r in first),'first_hit_types':dict(Counter(r[3] for r in first)),'failed_pair_obstructions':dict(counts),'first_obstruction_examples':first_obstruction,'largest_offsets':sorted(first,key=lambda r:r[1],reverse=True)[:12]}))
    for p,x in [(1201,303)]:
        A,B,fx=compact(p,x); a=4*x-p
        D={d%a for d in divisors(fx)}
        R={u*pow(v,-1,a)%a for u in D for v in D}
        print('subgroup_trap',json.dumps({'p':p,'x':x,'a':a,'D':sorted(D),'R':sorted(R),'H':sorted(group(a,fx)),'targets':[(-1)%a,(-p)%a]}))
        assert A is B is None
    # Falsify two sharper guesses: square-root window and prime-only defects.
    sqrt_fail=[]; prime64_fail=[]
    for p in failures:
        x0=(p+3)//4
        if not any(any(d is not None for d in compact(p,x0+t)[:2]) for t in range(max(0,(isqrt(p)-3)//4+1))):
            sqrt_fail.append(p)
        if not any(any(d is not None for d in compact(p,x0+t)[:2]) for t in range(64) if prime(3+4*t)):
            prime64_fail.append(p)
    print('restricted_tests',json.dumps({'sqrt_defect_failure_count':len(sqrt_fail),'sqrt_defect_failures':sqrt_fail,'prime_defect_64_failure_count':len(prime64_fail),'prime_defect_64_failures':prime64_fail}))
    print('environment',sys.version.split()[0],platform.system(),platform.machine(),'seconds',round(perf_counter()-start,6))

if __name__ == '__main__':
    main()
