def print_params(a = 1, b = 'String', c = True):
    print(a,b,c)

# Проверка
print("Функция с параметрами по умолчанию:")

print_params()
print_params(a = 1, b = 'String', c = True)
print_params(b = 25)
print_params(c = [1,2,3])
print_params(a = False)
print_params(a = 'String', b = True,)

print("Распаковка параметров:")

values_list = [5, True , 'String']
values_dict = {'a': 10, 'b': False, 'c': 'String'}
print_params(**values_dict)
print_params(*values_list)


print("Распаковка + отдельные параметры:")

values_list_2 = [5,'Urban']
print_params(*values_list_2)
print_params(*values_list_2,42)
