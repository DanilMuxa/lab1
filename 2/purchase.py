price = int(input('Введите цену тетради в рублях: '))
count = int(input('Введите кол-во тетрадей: '))
paid = int(input('Введите сколько оплачено в рублях: '))

cost = price * count
change = paid - cost

print(f'''Стоимость: {cost}
Сдача: {change}''')
