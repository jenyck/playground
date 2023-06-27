#!/usr/bin/env python3

# read input
with open('17-362.txt', 'r') as file1:
    l = [list(i.strip()) for i in file1]

# translate letters to decimal numbers
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZF'
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] in alpha:
            l[i][j] = 10 + alpha.find(l[i][j])
        l[i][j] = int(l[i][j])

# from random base to decimal
pairs = 0
max_sum = 0
base = []
for i in range(len(l)):
    a = 0
    base.append(max(l[i]) + 1)
    for j in range(len(l[i])):
        a += l[i][j] * base[i]**(len(l[i]) - j - 1)
    l[i] = a
    if i > 0 and abs(base[i] - base[i-1]) <= 2:
        pairs += 1
        if max_sum < l[i] + l[i-1]:
            max_sum = l[i] + l[i-1]

print(pairs, max_sum)
