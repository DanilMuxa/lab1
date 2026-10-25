n_list = input('Введите целые числа через пробел: ')

numbers = []
for part in n_list.split():
    numbers.append(int(part))


if len(numbers) == 0:
    print('Нет данных')
else:
    max_value = max(numbers)
    max_n = []
    for pos, value in enumerate(numbers):
        if value == max_value:
            max_n.append(pos)
    print(max_n)
