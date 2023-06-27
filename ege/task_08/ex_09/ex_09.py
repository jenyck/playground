#!/usr/bin/env python3
from itertools import product

count = 0
for x in product('01234567', repeat=4):
    s = ''.join(x)
    if s[0] != '0' and s[-1] in '04':
        count += 1

print(count)
