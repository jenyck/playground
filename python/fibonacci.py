n1 = 1
n2 = 2
n3 = 0
sum = 2
while True:
    n3 = n1 + n2
    print('Fibonacci:', n3)
    if n3 > 4000000:
        break
    n1 = n2
    n2 = n3
    if not n3 % 2:
        sum += n3
        print(sum)
