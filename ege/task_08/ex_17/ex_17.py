#!/usr/bin/env python3
from functools import lru_cache

@lru_cache(None)
def f(l, prev, curr):
    if l == 16: return curr != 'S'
    if curr == 'S':
        return sum(f(l + 1, curr, new) for new in 'CONT' if new != prev)
    else:
        return sum(f(l + 1, curr, new) for new in 'CONST' if new != curr)

print(sum(f(1, '', new) for new in 'CONT'))
