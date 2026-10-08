n = int(input())
num = int(input())

total_sum = num
if num > 0:
    p_count = 1
else:
    p_count = 0
    
max_value = num

for k in range(n - 1):
    num = int(input())

    total_sum += num

    if num > 0:
        p_count += 1

    if num > max_value:
        max_value = num


print(f'Сумма: {total_sum}')
print(f'Кол-во положительных: {p_count}')
print(f'Максимальное значение: {max_value}')
