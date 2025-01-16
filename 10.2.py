import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.days = 0
        self.enemies = 100

    def run(self):
        print(f'{self.name} на нас напали!')
        while self.enemies > 0:
            time.sleep(1) # Задержка на 1 секунду (1 день сражений)
            self.days += 1
            self.enemies -= self.power

            if self.enemies < 0:
                self.enemies = 0
                break
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()
# Окончание сражения
first_knight.join()
second_knight.join()

print("Все битвы закончились!")