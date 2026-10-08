order_name = input('Название заказа: ')
buyer_name = input('Имя заказчика: ')
ball_name = input('Название первой позиции: ')
ball_amount = int(input('Количество первой позиции: '))
ball_cost = float(input('Цена за единицу первой позиции, руб.: '))
rope_name = input('Название второй позиции: ')
rope_amount = int(input('Количество второй позиции: '))
rope_cost = float(input('Цена за единицу второй позиции, руб.: '))
shipping_price = float(input('Стоимость доставки, руб.: '))
prepaid_sum = float(input('Внесённая сумма, руб.: '))


ball_sum = ball_amount * ball_cost
rope_sum = rope_amount * rope_cost
goods_sum = ball_sum + rope_sum
order_sum = goods_sum + shipping_price
units_total = ball_amount + rope_amount
refund = prepaid_sum - order_sum


print('-------------------------------------------------------------------')
print(f'Заказ: {order_name}')
print(f'Заказчик: {buyer_name}')
print('Позиция | Кол-во | Цена | Стоимость')
print(f'{ball_name} | {ball_amount} | {ball_cost:.2f} | {ball_sum:.2f}')
print(f'{rope_name} | {rope_amount} | {rope_cost:.2f} | {rope_sum:.2f}')
print(f'Товары без доставки:      {goods_sum:.2f} руб.')
print(f'Доставка:                 {shipping_price:.2f} руб.')
print(f'Итого к оплате:           {order_sum:.2f} руб.')
print(f'Всего единиц товара:      {units_total}')
print(f'Внесено:                  {prepaid_sum:.2f} руб.')
print(f'Сдача:                    {refund:.2f} руб.')
print('-------------------------------------------------------------------')
