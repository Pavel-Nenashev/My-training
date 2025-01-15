def all_variants(text):
    '''
    length = len(text)
    # Проходим по всем возможным начальным индексам
    for start in range(length):
        # Проходим по всем возможным конечным индексам
        for end in range(start + 1, length + 1):
            # Возвращаем подпоследовательность
            yield text[start:end]
     ''' 
      # Исправлено
    n = len(text)                                  # Получаем длину исходной строки.
    for length in range(1, n + 1):                 # Перебираем все возможные длины подстрок от 1 до полной длины строки.
        for start in range(n - length + 1):        # Для каждой длины перебираем все возможные стартовые позиции подстроки.
            substring = text[start:start + length] # Извлекаем подстроку заданной длины начиная с позиции `start`.
            yield substring                        # Возвращаем подстроку с помощью оператора `yield`.       

# Пример выполнения программы
a = all_variants("abc")
for i in a:
    print(i)
# Свой вариант
# b = all_variants("Urban")
# for k in b:
#     print(k)
