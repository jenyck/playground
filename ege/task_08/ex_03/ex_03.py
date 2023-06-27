#!/usr/bin/env python3
from itertools import product

count = 0
for char_tuple in product('ЛЕТО', repeat=4):
    s = ''.join(char_tuple)
    if s.count('Е') >= 1:
        count += 1

print(count)
