a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
c = int(input('Введите 3 число: '))


if a <= b:
    if a <= c:
        mn = a
if b <= a:
    if b <= c:
        mn = b
if c <= a:
    if c <= b:
        mn = c


print(f'Минимальное число: {mn}')
