immutable_var = tuple([ 1,2,"Hello",True])
print(immutable_var)
print(immutable_var[0])
print(immutable_var[2])

#immutable_var[0]= 10       При попытке изменить элемент кортежа выдает ошибку:
#print(immutable_var[0])    "объект "кортеж" не поддерживает назначение элементов",
#                           так как кортеж является неизменяемой коллекцией элементов

mutable_list = [1,2,"Hello",True]
print(mutable_list)
print(mutable_list[0])      #Вывод 1-го элемента списка
mutable_list[0] = "String"  #Замена первого элемента списка (1 меняется на Sting)
print(mutable_list[0])      #Вывод 1-го элемента измененного списка
print(mutable_list)         #Вывод измененного списка
