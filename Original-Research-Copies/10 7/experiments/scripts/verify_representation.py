#!/usr/bin/env python3
"""Exact verification utilities for Erdos-Straus representations.

This script never uses floating-point arithmetic. A successful finite search
is evidence for the stated range only and is not a proof of the conjecture.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Certificate:
    n: int
    x: int
    y: int
    z: int

    def valid(self) -> bool:
        if min(self.n, self.x, self.y, self.z) <= 0:
            return False
        return 4 * self.x * self.y * self.z == self.n * (
            self.x * self.y + self.x * self.z + self.y * self.z
        )

    def exact_value(self) -> Fraction:
        return Fraction(1, self.x) + Fraction(1, self.y) + Fraction(1, self.z)


def find_certificate(n: int, x_limit: int, denominator_limit: int) -> Certificate | None:
    if n < 2:
        raise ValueError("n must be at least 2")
    for x in range(1, x_limit + 1):
        residual = Fraction(4, n) - Fraction(1, x)
        if residual <= 0:
            continue
        for y in range(x, denominator_limit + 1):
            remainder = residual - Fraction(1, y)
            if remainder <= 0:
                continue
            if remainder.numerator == 1:
                z = remainder.denominator
                if z >= y:
                    candidate = Certificate(n, x, y, z)
                    if candidate.valid() and candidate.exact_value() == Fraction(4, n):
                        return candidate
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=2)
    parser.add_argument("--end", type=int, default=100)
    parser.add_argument("--x-limit", type=int, default=1000)
    parser.add_argument("--denominator-limit", type=int, default=10000)
    args = parser.parse_args()

    if args.start < 2 or args.end < args.start:
        parser.error("require 2 <= start <= end")

    found = 0
    failures: list[int] = []
    for n in range(args.start, args.end + 1):
        certificate = find_certificate(n, args.x_limit, args.denominator_limit)
        if certificate is None:
            failures.append(n)
        else:
            found += 1
            print(f"n={n} x={certificate.x} y={certificate.y} z={certificate.z}")

    print(
        f"SUMMARY start={args.start} end={args.end} tested={args.end - args.start + 1} "
        f"certificates={found} failures={len(failures)} "
        f"x_limit={args.x_limit} denominator_limit={args.denominator_limit}"
    )
    if failures:
        print("UNRESOLVED_IN_SEARCH_BOUNDS " + " ".join(map(str, failures)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
