calls = 0
def count_calls():                                          #Функция подсчитывающая вызовы
    global calls                                            #остальных функций
    calls +=1

def string_info(string):                                    #Функция с аргументом в виде строки, которая
    count_calls()                                           #возвращает кортеж из длины этой строки,
    length_of_string = len(string)                          # строку в верхнем регистре, строку в нижнем регистре.
    modified_string = (length_of_string, string.lower(), string.upper())
    return modified_string

def is_contains(string, list_to_search):                    #Функция is_contains принимает два аргумента: строку
    count_calls()                                           #string и список list_to_search и возвращает True,
    a = False                                               #если строка находится в этом списке,
    for i in range (len(list_to_search)):                   #False - если отсутствует
        if string.lower() == list_to_search[i].lower():
            a = True
        elif string.lower() != list_to_search[i].lower():
            continue
    return a
                                                            #Вывод на экран (в консоль)
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(string_info('Hello world'))
print(is_contains('How are you?',['Just do it', 'how are You?']))
print(is_contains('How are you?',['Just do it', 'How are you doing?, Who is on duty today?']))

print(calls)