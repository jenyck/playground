#!/usr/bin/env python3
from itertools import permutations

unnecessary = ['АИ', 'ИА', 'АО', 'ОА', 'АУ', 'УА', 'ИО', 'ОИ', 'ИУ', 'УИ',
               'ОУ', 'УО', 'БК', 'КБ', 'БЛ', 'ЛБ', 'БН', 'НБ', 'КЛ', 'ЛК',
               'КН', 'НК', 'ЛН', 'НЛ']
count = 0
for x in permutations('АБИКОЛУН'):
    s = ''.join(x)
    if all(sub not in s for sub in unnecessary):
        count += 1

print(count)
