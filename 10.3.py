import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock =threading.Lock()

    def deposit(self):
        for _ in range(100):                                      # 100 транзакций
            amount = random.randint(50, 500)                # Генерируем случайную сумму для пополнения
            self.balance += amount                                # Пополняем баланс
            print(f'Пополнение: {amount}. Баланс: {self.balance}')
            # Если баланс больше или равен 500 и замок lock заблокирован,
            # то разблокируем его методом release.
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)                                     # Ожидание в 0.001 секунды имитирует скорость
                                                                  # выполнения пополнения

    def take(self):
        for _ in range(100):                                       # 100 транзакций
            amount = random.randint(50, 500)                 # Генерируем случайную сумму снятия
            print(f'Запрос на {amount}')                           # Выдаем сообщение: 'Запрос на снятие'
            # Условие для снятия средств:
            # если сумма снятия меньше или равна текущему балансу, то произвести
            # снятие и вывести строку f"Снятие: {сумма}. Баланс: {баланс}"
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            # Иначе:
            # Если сумма снятия оказалось больше баланса, то вывести строку: "Запрос отклонён,
            # недостаточно средств" и заблокировать поток методом acquire.
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)                                   # Ожидание в 0.001 секунды имитирует скорость
                                                                # выполнения снятия
# Создаем объект класса Bank
bk = Bank()

# Создаем потоки для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запускаем потоки
th1.start()
th2.start()

# Ожидаем завершения потоков
th1.join()
th2.join()

# Выводим итоговый баланс
print(f'Итоговый баланс: {bk.balance}')