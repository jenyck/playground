#!/usr/bin/env python3

from functools import lru_cache

@lru_cache(maxsize=None)
def f1(n):
    if n < 10:
        return n
    if 10 <= n < 1000:
        return f1(n // 10) + f1(n % 10)
    else:
        return f1(n // 1000) - f1(n % 1000)

count = 0
for i in range(1000000):
    if not f1(i):
        count += 1

print(count)
