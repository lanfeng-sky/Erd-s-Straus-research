# KI-001 Review Snapshot

Status submitted by main model: `proved`.

For every prime p congruent to 1 modulo 24, let

    x = (p + 3) / 4
    b = p*x.

A positive integral completion

    4/p = 1/x + 1/y + 1/z

at this fixed x exists if and only if x has a prime divisor q congruent to 2 modulo 3.

## Necessity

Write p = 24*k + 1. Then x = 6*k + 1 and b is congruent to 1 modulo 3. The remainder after 1/x is 3/b, so a completion satisfies

    3*y*z = b*(y + z).

Set

    d = 3*y - b
    e = 3*z - b.

Both are positive and direct expansion gives d*e = b^2. Also d and e are congruent to 2 modulo 3. If x had no prime divisor congruent to 2 modulo 3, every prime divisor of b would be congruent to 1 modulo 3 because p is congruent to 1 modulo 3. Every divisor of b^2 would then be congruent to 1 modulo 3, contradicting the existence of d.

## Sufficiency

Choose a prime q dividing x with q congruent to 2 modulo 3, and define

    e = b^2/q
    y = (b + q)/3
    z = (b + e)/3.

The values are positive integers. Since q <= x <= b, q <= e and y <= z. Expanding gives

    9*y*z = (b + q)*(b + e)
            = b*(2*b + q + e)
            = 3*b*(y + z).

Thus 3*y*z = b*(y + z). Since b = p*x and 4*x - p = 3, this is equivalent to

    4*x*y*z = p*(x*y + x*z + y*z).

## Completeness at Fixed x

Every completion can be ordered y <= z. Then d <= e, so d <= b because d*e = b^2. Conversely, every factor pair d*e = b^2 with 1 <= d <= b and both b+d and b+e divisible by 3 reconstructs a positive ordered completion.

Exact bounds are

    b/3 < y <= 2*b/3
    z <= (b + b^2)/3.

This proves completeness only at x = (p+3)/4. It does not prove the full Erdos-Straus conjecture, and failure at this x is not a counterexample.