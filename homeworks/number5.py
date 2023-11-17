words = input('Введите предложение: ').split()
count = 0
for word in words:
    if word.lower() == 'кот':
        if word == word.upper() or word == word.lower() or word == word.capitalize():
            count += 1
print(f'кот/Кот/КОТ встречается в предложении {count} раз(а)')

