import threading
import random
import time
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None                                              # Изначально стол свободен

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time_to_eat = random.randint(3, 10)                      # Случайное время ожидания от 3 до 10 секунд
        time.sleep(time_to_eat)                                        # Гость "кушает"

class Cafe:
    def __init__(self, *tables):
        self.tables = tables                                           # Список столов
        self.queue = Queue()                                           # Очередь для гостей

    # Метод guest_arrival(self, *guests):
    # Принимает неограниченное количество гостей(объектов класса Guest). Если есть
    # свободный стол, сажает гостя за стол (назначает столу guest), запускает поток гостя
    # и выводит на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>". Если
    # же свободных столов для посадки не осталось, то помещает гостя в очередь queue и
    # выводит сообщение "<имя гостя> в очереди".
    def guest_arrival(self, * guests):
        # Принимаем неограниченное количество гостей
        for guest in guests:
            seated = False                                             # Флаг, чтобы проверить, усажен ли гость
            # Проверяем, есть ли свободный стол
            for table in self.tables:
                # Если стол свободен
                if table.guest is None:
                    table.guest = guest                                # То сажаем гостя за стол(назначаем столу guest)
                    guest.start()                                      # Запускаем поток гостя и выводим сообщение
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    seated = True                                      # Стол занят
                    break                                              # Выходим из цикла

            # Если же свободных столов для посадки не осталось
            if not seated:
                self.queue.put(guest)                                  # То помещаем гостя в очередь и выводим сообщение
                print(f'{guest.name} в очереди')

    # Метод discuss_guests(self):
    # Этот метод имитирует процесс обслуживания гостей.
    # Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
    # Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу -
    # метод is_alive), то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и
    # "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
    # Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему
    # столу присваивается гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя
    # из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
    def discuss_guests(self):
        # Обслуживание происходит пока очередь не пустая (метод empty) или хотя бы один стол занят.
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                # Если за столом есть гость(поток) и гость(поток) закончил приём
                # пищи(поток завершил работу - метод is_alive),
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушел(-шла)')     # Выводим сообщение
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None                                        # Освобождаем текущий стол

                    # Если очередь ещё не пуста (метод empty)
                    if not self.queue.empty():
                        next_guest = self.queue.get()             # Берем следующего из очереди (queue.get()) и
                        table.guest = next_guest                  # присваиваем гостя взятого из очереди текущему столу
                        next_guest.start()                        # Запускаем поток нового гостя и выводим сообщение
                        print(f'{next_guest.name} вышел(-шла) из очереди и сел(-а) за стол номер {table.number}')
            time.sleep(0.5)                                       # Небольшая задержка имитирующая обслуживание

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()