#!/usr/bin/env python3
from itertools import permutations

count = 0
for x in set(permutations('АССАСИН')):
    count += 1

print(count)
