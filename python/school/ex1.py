#!/usr/bin/env python3
# В файле содержится текстовая строка. Определить
# частоту повторяемости каждой буквы в тексте и вывести ее.
f1 = open('input.txt', 'r')
f2 = open('output.txt', 'w')

text = f1.read().lower()
for i in 'abcdefghijklmnopqrstuvwxyz':
    f2.write(i + ' = ' + str(text.count(i)) + '\n')

f1.close()
f2.close()
