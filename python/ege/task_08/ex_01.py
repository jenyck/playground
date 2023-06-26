#!/usr/bin/env python3

'''
Сколько слов длины 4, начинающихся с согласной буквы, можно составить из
букв Л, Е, Т, О? Каждая буква может входить в слово несколько раз. Слова
не обязательно должны быть осмысленными словами русского языка.
'''

from itertools import product

count = 0
for char_tuple in product('ЛЕТО', repeat=4):
    s = ''.join(char_tuple)
    if s[0] in 'ЛТ':
        count += 1

print(count)
