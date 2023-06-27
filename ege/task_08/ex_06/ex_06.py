#!/usr/bin/env python3
from itertools import permutations 

count = 0
for x in permutations('КАЛИЙ'):
    s = ''.join(x)
    if s[0] != 'Й' and 'ИА' not in s:
        count += 1

print(count)
