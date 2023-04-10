#!/usr/bin/env python3
import random


# №8
def count_div(number):
   div = 0
   for i in range(2, number // 2):
       if not number % i:
           div += 1
   return div

list1 = []
for i in range(10000):
   list1.append(random.randint(100, 999))

list1 = sorted(list1, key=lambda number: count_div(number))
print(list1)


# №9
list1 = []
for i in range(100):
   list1.append(random.randint(0, 1000))

min1, min2, min3 = (1000, 1000, 1000)

for i in list1:
   if min3 > i:
       if min2 > i:
           if min1 > i:
               min1 = i
           else:
               min2 = i
       else:
           min3 = i
print(list1)
print(min1, min2, min3)
