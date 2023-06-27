#!/usr/bin/env python3
from itertools import product

count = 0
for x in product('КРОТ', repeat=6):
    s = ''.join(x)
    if s.count('О') == 1:
        count += 1

print(count)
