def  custom_write(file_name, strings: list):
    # Записывает в файл file_name все строки из списка strings, каждая на новой строке.
    # Возвращает словарь strings_positions, где ключом будет кортеж
    # (<номер строки>, <байт начала строки>), а значением - записываемая строка.
    # Для получения номера байта начала строки используйте метод tell() перед записью.
    string_positions = dict()
    new_file = open(file_name, 'w', encoding='UTF-8')
    i = 1
    for record in strings:
        index = (i, new_file.tell())
        new_file.write(f'{record}\n')
        string_positions[index] = record
        i += 1
    new_file.close()
    return string_positions

    '''Примеры выполняемого кода:'''

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)