def get_matrix(n, m, value):

    matrix = []                                 # Создаём пустой список для матрицы

    for i in range(n):                          # Внешний цикл для строк

        row = []                                # Добавляем пустой список для новой строки

        for j in range(m):                      # Внутренний цикл для столбцов

            row.append(value)                   # Заполняем строку значением value

        matrix.append(row)

    return matrix

result = get_matrix(3, 4, 5)

result1 = get_matrix(-1, 4, 5)      # Выдача результата с аргументами <=0

result2 = get_matrix(3, 0, 5)
result3 = get_matrix(0, 4, 5)
result4 = get_matrix(3, 4, 0)

print(result)                                   # Вывод на консоль

print(result1)
print(result2)
print(result3)
print(result4)
