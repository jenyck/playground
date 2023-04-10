#!/usr/bin/env python3
# Определить, симметричен ли заданный во входном файле текст

# creates a file with symmetric random text
import random
with open('text1.txt', 'w') as file1:
    a = ''
    for i in range(1000):
        a += chr(random.randint(4, 127))
        
    file1.write(a)
    for i in a:
        a = i + a
        a = a[:-1]
    file1.write(a)

# creates a file with random text
import random
with open('text2.txt', 'w') as file1:
    a = ''
    for i in range(2000):
        a += chr(random.randint(4, 127))
    file1.write(a)

with open('text1.txt', 'r') as file1:
    text = file1.read()
    
    for i in range((len(text) + 1) // 2):
        if text[i] != text[-i-1]:
            print(text[i], text[-i])
            print('text is not symmetric')
            break
    else:
        print('text is symmetric')

with open('text2.txt', 'r') as file1:
    text = file1.read()
    
    for i in range((len(text) + 1) // 2):
        if text[i] != text[-i-1]:
            print('text is not symmetric')
            break
    else:
        print('text is symmetric')
