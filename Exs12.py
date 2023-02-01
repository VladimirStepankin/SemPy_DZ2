summ = int(input('Введите сумму чисел: '))
prod = int(input('Введите произведение чисел: '))
for i in range(1000):
    j = summ - i
    if i * j == prod:
        print(f'Загаданные числа {i} и {j}')
        exit()
print("нет решения")