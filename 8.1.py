def add_everything_up(a, b):
    try:
        return round(a + b, 3)
    except:
        if isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            (isinstance(a, (int, float)) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, (int, float)))
            return str(a) + str(b)

# Пример результата выполнения программы:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print('Свой вариант:')
print(add_everything_up('яблоко', 'строка'))