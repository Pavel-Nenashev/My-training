numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
n = len(numbers)

primes = []
not_primes = []

for i in range(n):                  # перебираем список
    print(numbers[i])

for i in range(2, n+1):             # так как 1 не простое и не составное число - исключаем его из поиска

    for j in primes:                # ищем простые числа
        if i % j == 0:
            not_primes.append(i)
            break
    else:
        primes.append(i)

print ("Praimes:",primes)
print ("Not Praimes:",not_primes)