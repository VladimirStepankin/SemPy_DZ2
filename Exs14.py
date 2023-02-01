n = int(input('Введите число N: '))
volue = 0
while 2**volue < n:
    print(2**volue, end=' ')
    volue += 1
