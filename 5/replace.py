text = input('Введите текст: ')


r_count = text.count(':')
new_text = text.replace(':', '-')


print(f'Количество замен: {r_count}')
print(f'Новая строка: {new_text}')
