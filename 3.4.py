def single_root_words(root_word, * other_words):

    # Создаем пустой список
    some_words = []

    # Перебираем предпологаемые подходящие слова

    for i in other_words:
    # Составляем новый список same_words только из тех слов списка other_words,
    # которые содержат root_word или наоборот root_word содержит одно из этих слов

        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            some_words.append(i)

    return some_words

    # Примеры выполняемого кода

result1 = single_root_words('rich','richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('Корни', 'Одкоренные', 'корнивища', 'не корнивят')

print(result1)
print(result2)
print(result3)

