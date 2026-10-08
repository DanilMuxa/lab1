x = int(input("Введите число от 0 до 100: "))


if x < 0 or x > 100:
    print("Ошибка диапазона")
else:
    if x <= 24:
        print("Мало")
    if 24 <= x and x <= 74:
        print("Достаточно")
    if 75 <= x:
        print("Много")
