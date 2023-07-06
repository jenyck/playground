#!/usr/bin/env python3
from itertools import product

count = 0
for x in product('ТИМАШЕВСК', repeat=5):
    s = ''.join(x)
    for c in 'МВСК': s = s.replace(c, 'Т')
    for c in 'ИЕ': s = s.replace(c, 'А')
    if s.count('А') > s.count('Т') + s.count('Ш') and all(
            sub not in s for sub in ['АШ', 'ША']):
        count += 1

print(count)
