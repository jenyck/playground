#!/usr/bin/env python3

for n in range(2, 1000):
    x = 338
    a = []
    while x > 0:
        a = [x % n] + a
        x //= n
    if len(a) == 3 and a[-1] == 2:
        print(n)
