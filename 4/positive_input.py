attempts = 0

while True:
    num = int(input('Введите целое число: '))
    if num > 0:
        break
    attempts += 1


print(f'Квадрат числа: {num**2}')
print(f'Кол-во отклонённых попыток: {attempts}')
