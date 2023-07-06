#!/usr/bin/env python3
from itertools import permutations

word = 'ДЕЙКСТРА'
count = 0
for x in permutations(word, r=6):
    s = ''.join(x)
    if any(sub in s for sub in ['ЙД', 'ЙК', 'ЙС', 'ЙТ', 'ЙР']):
        count += 1

print(count)
