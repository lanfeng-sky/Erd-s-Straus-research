#!/usr/bin/env python3
"""Bounded falsification and independent switched-factor diagnostics for I-003/004.
Standard library. No network or file writes. Imports only local flagship source.
"""
from pathlib import Path
import importlib.util
from math import isqrt
from collections import Counter
import json
from time import perf_counter

BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('probe', BASE/'002_structural_probe.py')
M=importlib.util.module_from_spec(spec); spec.loader.exec_module(M)

def switched(p,k):
    N=4*k*k*p+1; mod=4*k
    for d in M.divisors(M.factor(N)):
        if d*d>N: break
        e=N//d
        if d%mod != mod-1: continue
        assert e%mod == mod-1
        u,v=(d+1)//mod,(e+1)//mod
        x,y,z=u*v,p*k*u,p*k*v
        assert (u+v)%k==0 and 4*x-p==(u+v)//k
        M.cert(p,x,y,z)
        return {'k':k,'N':N,'d':d,'e':e,'x':x,'y':y,'z':z}
    return None

def saturated(p,a):
    x=(p+a)//4
    fx=M.factor(x); H=M.group(a,fx)
    if (a-1) not in H: return False
    # Here a is prime 3 mod 4; H is cyclic of twice odd order.
    h=len(H)
    for r in range(1,h+1,2):
        if h%r: continue
        outside=sum(e for q,e in fx if pow(q%a,r,a)!=1)
        if outside<h//(2*r): return False
    A,B,_=M.compact(p,x)
    assert A is not None
    return True

def main():
    start=perf_counter()
    P=[p for p in range(2,100001) if p%840 in M.RESIDUES and M.prime(p)]
    F=[p for p in P if all(q%3==1 for q,e in M.factor((p+3)//4))]
    k_hist=Counter(); switch_fail=[]; k1fail=[]; examples={}
    for p in F:
        first=None
        for k in range(1,17):
            w=switched(p,k)
            if k==1 and w is None: k1fail.append(p)
            if w is not None:
                first=w; k_hist[k]+=1; examples.setdefault(k,(p,w)); break
        if first is None: switch_fail.append(p)
    print('switched',json.dumps({'domain':len(F),'k_limit':16,'first_k_histogram':dict(k_hist),'k1_fail_count':len(k1fail),'k1_first_failures':k1fail[:12],'window_failures':switch_fail,'examples':examples}))
    for p in k1fail[:3]:
        print('complementarity_counterexample',p,M.factor((p+3)//4),M.factor(4*p+1))
    satfail=[]; sqrthits=0
    for p in F:
        ok=False
        for a in range(3,isqrt(p)+1,4):
            if M.prime(a) and saturated(p,a):
                ok=True; break
        if ok: sqrthits+=1
        else: satfail.append(p)
    print('saturation_prime_sqrt',json.dumps({'successes':sqrthits,'failure_count':len(satfail),'failures':satfail}))
    # Try to refute the tempting eight-offset rule, stopping at first failure.
    checked=0; bad=None
    for p in range(100001,1000001):
        if p%840 not in M.RESIDUES or not M.prime(p): continue
        checked+=1; x0=(p+3)//4
        if any(any(d is not None for d in M.compact(p,x0+t)[:2]) for t in range(8)):
            continue
        bad=p
        for t in range(8): assert not M.exhaustive(p,x0+t)
        first=None
        for t in range(8,64):
            A,B,_=M.compact(p,x0+t)
            if A is not None or B is not None:
                hits=M.exhaustive(p,x0+t); assert hits
                first=(t,x0+t,*hits[0]); break
        print('eight_offset_counterexample',json.dumps({'p':p,'checked_selected_primes_above_100000':checked,'x0_factorization':M.factor(x0),'first_later_certificate_t_x_y_z':first}))
        break
    if bad is None:
        print('no_eight_offset_counterexample_below_1000000',checked)
    print('seconds',round(perf_counter()-start,6))

if __name__=='__main__': main()
