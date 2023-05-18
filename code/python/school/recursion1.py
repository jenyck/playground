#!/usr/bin/env python3
# 5888
from functools import *
@lru_cache(maxsize=None)
def f2(n):
    if n <= 3:
        return n - 1
    elif n % 2 == 0:
        return f2(n - 2) + n // 2 - f2(n - 4)
    else:
        return f2(n - 1)*n + f2(n - 2)

a = []
for i in range(5000):
    a.append(f2(i))
print(a)
print(a[4952] + 2*a[4958] + a[4964])
