                                                                # Работа со словарем
my_dict = {'Pavel':1981, 'Sergey': 1982, 'Olga': 2005}
print(my_dict)
print(my_dict['Pavel'])
my_dict['Evgenia'] = 1995
print(my_dict['Evgenia'])
my_dict.update({'Fernando':1975, 'Lesli':1985})
print(my_dict)
a = my_dict.pop('Olga')
print(a)
print(my_dict)
                                                                # Работа с множеством
my_set = {1,2,5,1,2,3,25.1,'Кабачок','Повторяющийся элемент','Пример','Повторяющийся элемент', True,(1,2,3,4)}
print(my_set)
my_set.add('Баклажан')
my_set.add(7)
my_set.remove('Повторяющийся элемент')
print(my_set)

