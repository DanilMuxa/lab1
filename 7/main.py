import functions

def main():
    user_num = int(input('Введите целое число: '))
    digit_sum_result = functions.sum_digits(user_num)
    print(f'Сумма цифр модуля: {digit_sum_result}')
    print('-' * 30)

    numbers_input = input('Введите целые числа через пробел для списка: ')
    num_list = []
    for part in numbers_input.split():
        num_list.append(int(part))
    avg_result = functions.average(num_list)
    if avg_result is None:
        print('Среднее: Нет данных')
    else:
        print(f'Среднее значение списка: {avg_result:.2f}')
    print('-' * 30)

    threshold = int(input('Введите неотрицательный порог: '))
    selected_list = functions.select_numbers(num_list, threshold)
    print(f'Отфильтрованный список (модуль > {threshold}): {selected_list}')
    print('-' * 30)

    user_text = input('Введите произвольный текст: ')
    normalized_result = functions.normalize_text(user_text)
    print(f'Нормализованный текст: {normalized_result}')


if __name__ == "__main__":
    main()
