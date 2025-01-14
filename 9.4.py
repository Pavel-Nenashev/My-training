from random import choice

# Задание 1: Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'
comparison = list(map(lambda f, s: f == s, first, second))

# Задание 2: Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')

    return write_everything

# Задание 3: Метод __call__:
class MysticBall:
    def __init__(self, *words):
        self.words = words

    # Случайно выбирает одно из слов
    def __call__(self):
        return choice(self.words)

# Пример результата выполнения программы

# Пример Lambda-функции
print(comparison)

# Пример использования замыкания:
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Пример использования класса MysticBall:
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

# Свои варианты:
print('Свои варианты:')
first = 'Хорошо!'
second = 'Нормуль!!!'
comparison = list(map(lambda f, s: f == s, first, second))
print(comparison)

# Пример использования замыкания:
write('------------', (1, 2, 3), [1, 2 ,3], '123 - это строка')

# Пример использования класса MysticBall:
second_ball = MysticBall('Понедельник', 'Вторник', 'Среда', 'Четверг','Пятница','Выходные')
print(second_ball())
print(second_ball())
