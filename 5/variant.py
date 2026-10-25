text = input('Введите строку: ')


words = text.split()
count = 0


for word in words:
    c_word = word.strip('.,!?;:').lower()
    if not c_word:
        continue
    if len(c_word) >= 5:
        print(c_word)
        count += 1
if count == 0:
    print('Нет совпадений')
print(f'Кол-во: {count}')
