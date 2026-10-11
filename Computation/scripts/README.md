# Verification Scripts

`verify_representation.py` performs bounded exact-integer verification.

Example:

```text
python3 verify_representation.py --start 2 --end 100 --x-limit 1000 --denominator-limit 10000
```

The script checks the division-free identity

```text
4*x*y*z = n*(x*y + x*z + y*z)
```

and exact rational equality. It does not use floating-point arithmetic. The search bounds are finite and must be recorded in the corresponding experiment report. A successful run does not prove the conjecture.