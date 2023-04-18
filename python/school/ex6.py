#!/usr/bin/env python3
import random

list1 = [random.randint(0,10000000000) for i in range(10)]

even = []
for i in list1:
    if not i % 2:
        even.append(i)
odd = []
for i in list1:
    if i % 2:
        odd.append(i)

list2 = []
for i in range(0, min(len(odd), len(even))):
    list2.append(even.pop())
    list2.append(odd.pop())
print(list2)
