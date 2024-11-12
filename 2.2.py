first = int(input("Введите первое случайное целое число: "))
second = int(input("Введите второе случайное целое число: "))
third = int(input("Введите третье случайное целое число: "))

if first == second and first == third:
    print(3)
elif first == second or first == third and first == third or second == third:
    print(2)
elif second != third and first != third:
    print(0)