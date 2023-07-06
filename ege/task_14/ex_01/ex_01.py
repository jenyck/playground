#!/usr/bin/env python3

x = 7**103 + 20 * 7**204 - 3 * 7**57 + 97
a = []

while x > 0:
    a = [x % 7] + a
    x = x//7

print(a.count(6))
print(sum(a))
print(a.count(0) - a.count(5))
