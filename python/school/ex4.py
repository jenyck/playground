#!/usr/bin/env python3
# Дан список. Не изменяя его и не используя дополнительные списки, определите,
# какое число в этом списке встречается чаще всего.
# Если таких чисел несколько, выведите любое из них.

num_list = [int(i) for i in input().split()]

max_count = 0

for i in range(len(num_list)):
    number = num_list[i]
    if not number in num_list[:i]:
        tmp_count = num_list.count(number)
        if tmp_count > max_count:
            max_count = number

print(max_count)
