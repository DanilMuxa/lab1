total_sec = int(input('Введите целое количество секунд большее 0: '))


if total_sec < 0:
    print('Ошибка: количество секунд не может быть отрицательным.')
else:
    hours = total_sec // 3600
    minutes = (total_sec % 3600) // 60
    seconds = total_sec % 60
    print(f'{total_sec} с = {hours} ч {minutes} мин {seconds} с')
