first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Переменная для первого результата: длины строк из первого списка,
# длина которых не менее 5 символов
first_result = [len(strings) for strings in first_strings if len(strings) >=5]

# Переменная для второго результата: пары слов (кортежи) одинаковой длины
second_result = [(first, second) for first in first_strings for second in second_strings if len(first) == len(second)]

# Переменная для третьего результата: словарь с парами ключ-значение
# (строка-длина строки) для четной длины строки
third_result = {string: len(string) for string in first_strings + second_strings if len(string) % 2 == 0}

# Пример результата выполнения программы
print(first_result)
print(second_result)
print(third_result)
