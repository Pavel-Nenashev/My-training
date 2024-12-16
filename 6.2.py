class Vehicle:
    __COLOR_VARIANTS = ['red', 'green', 'blue','black','white']

    def __init__(self, owner, model, color, engine_power):
            self.owner = owner
            self.__model = model
            self.__engine_power = engine_power
            self.__color = color

    def get_model(self,__model):
        return f'Модель: {self.__model}'

    def get_horsepower(self, __engine_power):
        return f'Мощность: {self.__engine_power}'

    def get_color (self, __color ):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'Марка: {self.__model}, мощность: {self.__engine_power}, цвет: {self.__color}, владелец: {self.owner} ')
        return

    def set_color(self, new_color):
        self.new_color = new_color
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass

'''Примеры выполняемого кода:'''    # Закомментированные варианты с отступом(табуляцией)
                                    # Свои варианты - все работает!!!
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
#    vehicle2 = Sedan('Доктор Хаус', 'БМВ М5', 'Silver', 350)
#    vehicle3 = Sedan('Руссо туристо', 'Лада Веста', 'white', 150)

# Изначальные свойства
vehicle1.print_info()
#    vehicle2.print_info()
#    vehicle3.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

#    vehicle2.set_color('Green')
#    vehicle2.owner = 'Илья Муромец'
#    vehicle2.print_info()
#
#    vehicle3.print_info()
#    vehicle3.set_color('Индиго')