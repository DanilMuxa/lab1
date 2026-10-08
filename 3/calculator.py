n1 = float(input('Введите первое число: '))
op = input('Выберите операцию (+, -, *, /): ').strip()
n2 = float(input('Введите второе число: '))

if op == '+' or op == '-' or op == '*' or op == '/':
    if op == '+':
        r = n1 + n2
        print(f'{r:.2f}')
    if op == '-':
        r = n1 - n2
        print(f'{r:.2f}')
    if op == '*':
        r = n1 * n2
        print(f'{r:.2f}')
    if op == '/':
        if n2 == 0:
            print('Деление на ноль запрещено')
        else:
            r = n1 / n2
            print(f'{r:.2f}')
else:
    print('Неизвестная операция')
