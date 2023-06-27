#!/usr/bin/env python3
import math

danger_list = []
with open('26-68.txt', 'r') as file1:
    n, t = map(int, file1.readline().split())
    for i in range(n):
        danger_list.append(tuple(map(int, file1.readline().split())))

sum_danger = 0
for i in danger_list:
    sum_danger += i[0]
average = math.ceil(sum_danger / len(danger_list))

viruses = []
superviruses = []
for i in range(len(danger_list)):
    if danger_list[-1][0] >= average:
        superviruses.append(danger_list.pop())
    else:
        viruses.append(danger_list.pop())

viruses = sorted(viruses, key=lambda virus: virus[1], reverse=True)
superviruses = sorted(superviruses, key=lambda virus: virus[1], reverse=True)
#print(viruses, average, superviruses)

count_viruses = 0
t_superviruses = 0
count = 0
while viruses and t > 0 and t > viruses[-1][1]:
    if not count % 2 and t > viruses[-1][1] + superviruses[-1][1]:
        tmp1 = superviruses.pop()[1]
        t -= tmp1
        t_superviruses += tmp1
        count_viruses += 1
        count += 1
        #print(count_viruses, t_superviruses)
    else:
        t -= viruses.pop()[1]
        count_viruses += 1
        count += 1
        #print(count_viruses, t_superviruses)
    #print(viruses, superviruses)

print(count_viruses, t_superviruses)
