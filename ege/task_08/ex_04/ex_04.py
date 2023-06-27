#!/usr/bin/env python3
from itertools import product

count = 0
for char_tuple in product('ЖИРАФ', repeat=5):
    s = ''.join(char_tuple)
    if s.count('Ж') == 1 and s[0] != 'Ф' and s[-1] != 'Р':
        count += 1

print(count)
