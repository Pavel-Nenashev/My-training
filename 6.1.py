'''    Создаем класс Animals (Животные), с атрибутами name (индивидуальное название
    каждого животного), alive = True (живой) и fed = False (накормленность)'''
class Animal:
    alive = True
    fed = False

    def __init__(self, name,):
        self.name = name
    # Метод eat общий для всех животных: Mammal (млекопитающие) и Predator (хищники)
    def eat(self, food):
        # Проверка на cъедобность
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
'''    Создаем класс Plant (Растения) с атрибутами name (индивидуальное название
    каждого растения) и edible = False (съедобность)'''
class Plant:
    edible = False

    def  __init__(self, name):
            self.name = name

'''    Cоздаем класс Flower (цветы) наследующий атрибуты от класса Plant (Растения) '''
class Flower(Plant):
    pass
'''    Cоздаем класс Fruit (фрукты) наследующий атрибуты от класса Plant (Растения) '''
class Fruit(Plant):
    # Т.к. фрукты съедобны, то у класса Fruit атрибут cъедобность edible = True
    edible = True
    pass
'''    Cоздаем класс Mammal (Млекопитающие) наследующий атрибуты от класса Animal (Животные) '''
class Mammal(Animal):
    pass
'''    Cоздаем класс Predator (Хищники) наследующий атрибуты от класса Animal (Животные) '''
class Predator(Animal):
    pass

'''Примеры выполняемого кода:'''
# Создаем объекты классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
# a3 = Mammal('Кот-бегемот')
# a4 = Predator('Тиранозавр-Рекс')

p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
# p3 = Fruit('Баклажан')
# p4 = Flower('Трава-мурава')

# Проверка атрибутов: выводим названия животных и растений
print(a1.name)
print(p1.name)
# print(a3.name)
# print(p3.name)

# Проверка атрибутов: выводим состояние живой-неживой, сытый-голодный
print(a1.alive)
print(a2.fed)

# Проверка метода покушать
a1.eat(p1)
a2.eat(p2)
# a3.eat(p3)
# a4.eat(p3)

# Проверка атрибутов: выводим состояние живой-неживой, сытый-голодный после выполнения метода eat
print(a1.alive)
print(a2.fed)
# print(a3.fed)
# print(a4.fed)
# print(a4.alive)