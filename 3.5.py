def get_multiplied_digits(number):
    # Переводим число в строку
    str_number = str(number)
    # Определяем индекс первого элемента строки(отделение первой цифры в числе)
    first = int(str_number[0])
    # Находим произведение цифр числа
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    # Последними цифрами в числе может оказаться ноль - заменим его на 1
    elif first > 0:
        return first
    else:
        return 1

    # Примеры выполняемого кода

result1 = get_multiplied_digits(40203)
print(result1)
result2 = get_multiplied_digits(402030)
print(result2)

result3 = get_multiplied_digits(1)
print(result3)
result4 = get_multiplied_digits(123)
print(result4)
result5= get_multiplied_digits(10203)
print(result5)
result6= get_multiplied_digits(12300)
print(result6)
