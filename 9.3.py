first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка, которая высчитывает разницу длин строк из списков first и second,
# если их длины не равны с использованием функции zip.
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка, которая содержит результаты сравнения длин строк в одинаковых позициях
# из списков first и second без использования функции zip с применением функций range и len
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Пример результата выполнения программы
print(list(first_result))
print(list(second_result))