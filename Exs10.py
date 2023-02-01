n = int(input('Введите число монет: '))
count = 0
for i in range(n):
    value = int(input())
    if value > 0:
        count += 1
if count > n // 2:
    print(n - count)
else:
    print(count)
