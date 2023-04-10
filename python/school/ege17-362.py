#!/usr/bin/env python3
# Егэ №17-362 (№6096)

with open('ege17-362.txt', 'r') as file1:
    l = [list(i.strip()) for i in file1]
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZF'
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] in alpha:
            l[i][j] = 10 + alpha.find(l[i][j])
        l[i][j] = int(l[i][j])
