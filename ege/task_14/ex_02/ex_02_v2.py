#!/usr/bin/env python3

for x in range(18):
    a = 11 * 18**4 + 2 * 18**3 + 5 * 18**2 + 16*18 + 2*x
    if a % 15 == 0:
        print(x, a // 15)
