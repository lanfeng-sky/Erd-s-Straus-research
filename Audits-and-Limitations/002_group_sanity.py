#!/usr/bin/env python3
"""Finite implementation sanity check, NOT a proof of the Kneser input."""
from itertools import combinations_with_replacement
from math import gcd
from functools import reduce

checks=passed=0
for m in (2,6,10,14,18,22):
    for length in range(1,7):
        for seq in combinations_with_replacement(range(1,m),length):
            if reduce(gcd,seq,m)!=1:
                continue
            checks+=1
            sat=all(sum(s%(m//r)!=0 for s in seq)>=m//(2*r)
                    for r in range(1,m+1,2) if m%r==0)
            if not sat:
                continue
            R={0}
            for s in seq:
                R={(u+v*s)%m for u in R for v in (-1,0,1)}
            assert m//2 in R,(m,seq)
            passed+=1
assert (checks,passed)==(416931,4569)
print('cyclic_saturation_checks',checks,'sufficient_condition_hits',passed,'disagreements',0)
