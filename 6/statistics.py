n = input('Введите целые числа через пробел: ')


numbers = []
for part in n.split():
    numbers.append(int(part))


if len(numbers) == 0:
    print('Нет данных')
else:
    n_count = len(numbers)
    n_sum = sum(numbers)
    n_min = min(numbers)
    n_max = max(numbers)
    n_sr = n_sum / n_count
    print(f'Кол-во: {n_count}')
    print(f'Сумма: {n_sum}')
    print(f'Минимум: {n_min}')
    print(f'Максимум: {n_max}')
    print(f'Среднее: {n_sr:.2f}')
