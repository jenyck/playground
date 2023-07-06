#!/usr/bin/env python3
from functools import lru_cache

@lru_cache(None)
def f(l, digits, ca):
    if l == 8: return len(digits) == 6 and ca <= 2

    count = 0
    for i in '0123456789abc':
        count += f(l+1, digits | {i} , ca + (i == 'a'))
    
    return count

print(sum(f(1, frozenset([i]), i == 'a') for i in '123456789abc'))
