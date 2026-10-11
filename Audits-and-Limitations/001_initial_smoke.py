"""ES initialization smoke check. Python standard library; no network or file I/O.
Scope: n=1009 and n=1201 only. Search at most 16 first-denominator offsets.
Factor-pair search is cross-checked against a full, independently derived y scan.
A missing certificate at a fixed x is not a counterexample to Erdős–Straus.
"""
from math import isqrt
from time import perf_counter
import platform, sys


def factors(n):
    out = {}
    q = 2
    while q*q <= n:
        while n % q == 0:
            out[q] = out.get(q, 0) + 1
            n //= q
        q += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def pair_cert(n, x):
    a, b = 4*x-n, n*x
    ds = [1]
    for q, e in factors(b).items():
        ds = [d*q**j for d in ds for j in range(2*e+1)]
    for d in sorted(ds):
        if d > b:
            break
        e = b*b//d
        if (d+b) % a or (e+b) % a:
            continue
        y, z = (d+b)//a, (e+b)//a
        if x <= y <= z:
            assert n >= 2 and min(x,y,z) > 0
            assert 4*x*y*z == n*(x*y+x*z+y*z)
            return (n,x,y,z,a,b,d,e)
    return None


def independent_scan(n, x):
    a, b = 4*x-n, n*x
    for y in range(max(x,b//a+1), 2*b//a+1):
        den = a*y-b
        num = b*y
        if num % den == 0:
            z = num//den
            if z >= y:
                assert 4*x*y*z == n*(x*y+x*z+y*z)
                return (n,x,y,z)
    return None


start = perf_counter()
print('Python',sys.version.split()[0], 'architecture',platform.machine(), 'OS',platform.system())
for n in (1009,1201):
    assert all(n % q for q in range(2,isqrt(n)+1))
    x0 = n//4+1
    print('n',n,'residue840',n%840,'x0',x0,'factorization(x0)',factors(x0))
    first = None
    for x in range(x0, min(x0+15,3*n//4)+1):
        c = pair_cert(n,x)
        direct = independent_scan(n,x)
        assert (c is None) == (direct is None)
        if c is None:
            print('  x',x,'no sorted completion; independently checked full y interval')
        else:
            assert c[:4] == direct
            print('  certificate n,x,y,z,a,b,d,e:',c)
            print('  integer identity sides:',4*c[1]*c[2]*c[3],n*(c[1]*c[2]+c[1]*c[3]+c[2]*c[3]))
            first = c
            break
    assert first is not None
print('runtime_seconds',round(perf_counter()-start,6))
