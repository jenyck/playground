#!/usr/bin/env python3
from itertools import product

count = 0
for char_tuple in product('ЛТ', 'ЛЕТО', 'ЛЕТО', 'ЛЕТО',):
    s = ''.join(char_tuple)
    count += 1

print(count)
