# KI-001 — Compressed proof reference

> COMPRESSED HISTORICAL RECORD. See `flagship/historical_compression.md` for the retained proof mechanism. Ask the user before restoring the original proof.

For p=24k+1 prime, x0=6k+1 and b=p*x0. After subtracting 1/x0, a completion satisfies 3yz=b(y+z). Set d=3y-b and e=3z-b. Then d,e>0, de=b^2 and d=e=2 mod 3. Since p and x0 are 1 mod 3, absence of a prime factor q=2 mod 3 in x0 makes every divisor of b^2 equal to 1 mod 3, impossible.

Conversely q|x0 with q=2 mod 3 gives e=b^2/q and

    y=(b+q)/3,
    z=(b+e)/3.

These are positive integers and satisfy

    4*x0*y*z=p*(x0*y+x0*z+y*z).

This is a fixed-x theorem only.