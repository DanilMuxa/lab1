first_room = input('Введите название первой аудитории: ')
second_room = input('Введите название второй аудитории: ')

print(f'''Исходные значения:
первая {first_room}
вторая {second_room}''')


empty_room = first_room
first_room = second_room
second_room = empty_room

print(f'''Результат обмена:
первая {first_room}
вторая {second_room}''')
