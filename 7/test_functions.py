from functions import average, normalize_text, sum_digits, select_numbers

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
print("Базовые проверки пройдены")



assert select_numbers([-5, 0, 2, 5], 2) == [-5, 5]
assert select_numbers([], 2) == []
assert select_numbers([-4, -3, 2, 3], 3) == [-4]
assert select_numbers([6, -6, 2, 6], 5) == [6, -6, 6]
original_list = [-5, 0, 2, 5]
backup_list = original_list.copy()
select_numbers(original_list, 2)
assert original_list == backup_list
print('Все проверки пройдены')
