#!/usr/bin/env python3
def two_max(number: str):
    local_max = 0
    for i in (2, len(number) - 2):
        if number[i] > number[i-1] and number[i] > number[i+1]:
            local_max += 1
    return local_max == 2

bn = 0
zl = 0
for i in range(7890123, 7891234):
    str_number = str(i)
    if str_number.count('2') == 2:
        zl += 1
    if two_max(str_number):
        bn += 1

print(zl, ' - нравится Злову\n', bn, ' - нравится Банану', sep='')
