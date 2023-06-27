#!/usr/bin/env python3
from itertools import product

count = 0
for x in product('ЛЕТО', repeat=4):
    s = ''.join(x)
    if s[0] in 'ЛТ':
        count += 1

print(count)
