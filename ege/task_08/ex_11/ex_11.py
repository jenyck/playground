#!/usr/bin/env python3
from itertools import product

count = 1
for x in product('АОУ', repeat=5):
    s = ''.join(x)
    if s == 'ОУОУА':
        start = count
    if s == 'УАУАУ':
        end = count
    count += 1

print(end - start + 1)
