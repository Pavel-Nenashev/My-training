import math

class Figure:
    sides_count = 0
    filled = False

    def __init__(self, colour, *sides):
        # Атрибуты класса Figure
        self.__colour = list(colour)              # Задаем цвет фигуры как список цветов в формате RGB
        if len(sides) != self.sides_count:        # Задаем стороны фигуры в соответствии с условием:
            self.__sides =[1] * self.sides_count  # self.__sides равно список сторон, если сторон не ровно
        else:                                     # sides_count, то создаем массив с единичными сторонами
            self.__sides = list(sides)            # и в том количестве, которое требует фигура.

    def get_colour(self):                         # Метод get_color, возвращает список RGB цветов.
        return self.__colour

    def __is_valid_colour(self, r, g, b):                      # Метод __is_valid_color - служебный, принимает
        for colour in [r, g, b]:                               # параметры r, g, b, который проверяет корректность
            if 0 <= colour <= 255 and isinstance(colour, int): # переданных значений перед установкой нового цвета.
                return True
            else:
                return False

    def set_colour(self, r, g, b):                # Метод set_color принимает параметры r, g, b - числа и изменяет
        if self.__is_valid_colour(r, g, b):       # атрибут __color на соответствующие значения, предварительно
            self.__colour = [r, g, b]             # проверив их на корректность.

    def __is_valid_sides(self, *sides):           # Метод __is_valid_sides - служебный, принимает неограниченное
        for side in sides:                                                                  # количество сторон.
            if side > 0 and len(sides) == self.sides_count and isinstance(side, int):
                return True
            else:                                 # Возвращает True если все стороны целые положительные числа и
                return False                      # количество новых сторон совпадает с текущим, False - во всех
                                                  # остальных случаях.
    def get_sides(self):                          # Метод get_sides возвращает значения атрибута __sides.
        return self.__sides

    def __len__(self):                            # Метод __len__ возвращает периметр фигуры.
        return sum(self.__sides)

    def set_sides(self, *new_sides):              # Метод set_sides принимает новые стороны. Если их количество
        if len(new_sides) != self.sides_count:    # не равно sides_count, то не изменяет, в противном случае - меняет.
            self.__sides = self.__sides
        else:
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self,colour, __radius):
        super().__init__(colour)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):                                   # Метод get_square возвращает площадь круга
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, colour, *sides):
        super().__init__(colour,*sides)

    def get_square(self):                                   # Метод get_square возвращает площадь треугольника
        a, b, c = self.get_sides()
        p = (a + b + c) / 2                                 # Полупериметр
        return math.sqrt(p * (p - a) * (p - b) * (p - c))   # Формула Герона

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        if len(sides) == 1:                                 # Переопределяем стороны куба как 12
            self.__sides = [sides[0]] * self.sides_count    # одинаковых сторон

    def get_sides(self):                                    # Устанавливаем стороны
        return self.__sides

    def get_volume(self):                                   # Возвращает объем куба
        return self.__sides[0] * self.__sides[0] * self.__sides[0]

'''Примеры выполняемого кода:'''    # Закомментированные варианты с отступом(табуляцией) - свои варианты

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
#   triangle1 = Triangle((200, 200, 100),3, 4, 5)

# Проверка на изменение цветов:
circle1.set_colour(55, 66, 77) # Изменится
print(circle1.get_colour())
cube1.set_colour(300, 70, 15) # Не изменится
print(cube1.get_colour())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка площади треугольника
#   print(triangle1.get_square())
