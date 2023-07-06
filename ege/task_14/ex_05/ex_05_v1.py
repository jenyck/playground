#!/usr/bin/env python3

for n in range(2, 1000):
    if 338 % n == 2 and n**2 <= 338 < n**3:
        print(n)
