#!/usr/bin/env python3
from itertools import permutations 

count = 0
unnecessary = ['ЬЕ', 'ЬА', 'ЬР']
for x in permutations('ПЕСКАРЬ'):
    s = ''.join(x)
    if s[0] != 'Ь' and all(sub not in s for sub in unnecessary):
        count += 1

print(count)
