n = input('Введите целые числа через пробел: ')


numbers = []
for part in n.split():
    numbers.append(int(part))
t_numbers = []
for number in numbers:
    if abs(number) > 5:
        t_numbers.append(number)
sort_n = sorted(t_numbers)


print(f'Результат: {t_numbers}')
print(f'Кол-во: {len(t_numbers)}')
print(f'Сумма: {sum(t_numbers)}')
print(f'Сортированная копия: {sort_n}')
