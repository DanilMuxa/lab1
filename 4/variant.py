n = int(input())

count = 0
total_sum = 0

for k in range(n):
    num = int(input())

    if num > 0:
        count += 1
        total_sum += num

print(count)
print(total_sum)
