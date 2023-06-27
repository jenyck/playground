#!/usr/bin/env python3
from itertools import product

count = 0
for x in product('ЛЕТО', repeat=4):
    s = ''.join(x)
    if s.count('Е') >= 1:
        count += 1

print(count)
