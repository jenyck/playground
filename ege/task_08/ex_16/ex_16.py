#!/usr/bin/env python3
from itertools import product

count = 0
for x in product('70ЧН', repeat=10):
    s = ''.join(x)
    if s[0] != '0' and s.count('7') == 5 \
            and '77' not in s and 'Н7' not in s and '7Н' not in s:
        count += 3**(s.count('Ч') + s.count('Н'))

print(count)
