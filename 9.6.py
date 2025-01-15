def all_variants(text):
    length = len(text)
    # Проходим по всем возможным начальным индексам
    for start in range(length):
        # Проходим по всем возможным конечным индексам
        for end in range(start + 1, length + 1):
            # Возвращаем подпоследовательность
            yield text[start:end]

# Пример выполнения программы
a = all_variants("abc")
for i in a:
    print(i)
# Свой вариант
# b = all_variants("Urban")
# for k in b:
#     print(k)