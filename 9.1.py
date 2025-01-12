def apply_all_func(int_list, *function):
    result = {}

    for func in function:
        result[func.__name__] = func(int_list)

    return result

    # Пример результата выполнения программы
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))