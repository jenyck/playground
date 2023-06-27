#!/usr/bin/env python3
from itertools import product

count = 0
for x in product('01234567', repeat=4):
    s = ''.join(x)
    #if s[0] >= s[1] >= s[2] >= s[3]: 
    if all(s[i] >= s[i+1] for i in range(len(s)-1)):
        count += 1

print(count)
