text = input('Введите текст: ')


words = text.split()
normalized = ' '.join(words)
word_count = len(words)


print(f'Исходная длина: {len(text)}')
print(f'Новая длина: {len(normalized)}')
print(f'Нормализованный текст: {normalized}')
print(f'Количество слов: {word_count}')
