#!/usr/bin/env python3
"""Self-contained flagship reproduction of E-001."""
from math import isqrt

LIMIT = 100_000
RESIDUES = {1, 121, 169, 289, 361, 529}


def sieve(limit):
    prime = bytearray(b"\x01") * (limit + 1)
    prime[:2] = b"\x00\x00"
    for q in range(2, isqrt(limit) + 1):
        if prime[q]:
            prime[q * q : limit + 1 : q] = b"\x00" * ((limit - q * q) // q + 1)
    return prime


def factor(n, prime):
    out = []
    for q in range(2, isqrt(n) + 1):
        if prime[q] and n % q == 0:
            exponent = 0
            while n % q == 0:
                n //= q
                exponent += 1
            out.append((q, exponent))
    if n > 1:
        out.append((n, 1))
    return out


def divisors_squared(factors):
    divisors = [1]
    for q, exponent in factors:
        old = list(divisors)
        divisors = old + [d * q**power for d in old for power in range(1, 2 * exponent + 1)]
    return divisors


def certificate_valid(p, x, y, z):
    return min(p, x, y, z) > 0 and 4 * x * y * z == p * (x * y + x * z + y * z)


def main():
    prime = sieve(LIMIT)
    selected = [p for p in range(2, LIMIT + 1) if prime[p] and p % 840 in RESIDUES]
    successes = []
    failures = []
    disagreements = []

    for p in selected:
        x = (p + 3) // 4
        factors = factor(x, prime)
        q = next((r for r, _ in factors if r % 3 == 2), None)
        classifier = q is not None
        b = p * x
        completions = []
        for d in divisors_squared(factor(b, prime)):
            if d > b or b * b % d:
                continue
            e = b * b // d
            if (b + d) % 3 == 0 and (b + e) % 3 == 0:
                y, z = (b + d) // 3, (b + e) // 3
                if x <= y <= z and certificate_valid(p, x, y, z):
                    completions.append((d, y, z))
        exhaustive = bool(completions)
        if classifier != exhaustive:
            disagreements.append((p, classifier, exhaustive))
        if classifier:
            e = b * b // q
            y, z = (b + q) // 3, (b + e) // 3
            assert certificate_valid(p, x, y, z)
            successes.append((p, x, q, y, z))
        else:
            failures.append((p, x, factors))

    assert len(selected) == 273
    assert len(successes) == 87
    assert len(failures) == 186
    assert not disagreements
    assert successes[0] == (1009, 253, 11, 85096, 1974822872)
    assert failures[1] == (1201, 301, [(7, 1), (43, 1)])
    print("PASS selected=273 successes=87 failures=186 disagreements=0")


if __name__ == "__main__":
    main()
