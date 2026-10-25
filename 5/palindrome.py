text = input('Введите текст для проверки: ')


c_text = text.lower().replace(' ', '')


if len(c_text) == 0:
    print('Нет текста')
elif c_text == c_text[::-1]:
    print('Палиндром')
else:
    print('Не палиндром')
