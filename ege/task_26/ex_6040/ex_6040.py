#!/usr/bin/env python3

pipes = []
with open('26-100.txt') as file1:
    n, distance = map(int, file1.readline().split())
    for i in range(n):
        pipes.append(int(file1.readline()))
    
pipes.sort()
pipes = pipes[pipes.index(pipes[-distance-1]):]
pipes = pipes[:distance]

print(pipes[0], pipes[-1])
