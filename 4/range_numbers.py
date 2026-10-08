a = int(input())
b = int(input())


if a <= b:
    x = 1
else:
    x = -1


for k in range(a, b + x, x):
    print(k)
