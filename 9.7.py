def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 2:
            print("Не простое и не составное")  # 0 и 1 не являются не простыми, не составными числами
            return result
        # Проверяем, является ли число простым
        # Запускаем цикл от 2 до квадратного корня из result для проверки делимости. Если число делится
        # на любое из этих чисел без остатка, оно составное.
        for i in range(2, int(result**0.5) + 1):
            if result % i == 0:
                print("Составное")
                return result
        print("Простое")
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

# Пример результата выполнения программы
result = sum_three(2, 3, 6)
print(result)