#!/usr/bin/env python3
from itertools import product

count = 0
for x in product('ЛТ', 'ЛЕТО', 'ЛЕТО', 'ЛЕТО'):
    s = ''.join(x)
    count += 1

print(count)
