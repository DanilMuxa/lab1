n = input('Введите целые числа через пробел: ')


numbers = []
for part in n.split():
    numbers.append(int(part))


t_numbers = []
for number in numbers:
    if number < 0:
        t_numbers.append(-number)
    else:
        t_numbers.append(number)
print(f'Исходный список: {numbers}')
print(f'Новый список: {t_numbers}')
