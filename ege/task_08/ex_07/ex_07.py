#!/usr/bin/env python3
from itertools import permutations

count = 0
unnecessary = ['ОУ', 'УО', 'КЛ', 'ЛК', 'КН', 'НК', 'ЛН', 'НЛ']

for x in permutations('КОЛУН'):
    s = ''.join(x)
    if all(sub not in s for sub in unnecessary):
        count += 1

print(count)
