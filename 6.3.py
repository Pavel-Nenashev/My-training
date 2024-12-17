import random

class Animal:
    live = True
    sound = None                                        # звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0                               # степень опасности существа

    def __init__(self, speed, _cords = [0, 0, 0]):
        self.speed = speed                              # скорость передвижения существа
        self._cords = _cords                            # координаты в пространстве

    def move(self, dx, dy, dz):                         # dx изменение координаты x в _cords
        if (self.speed * dz) < 0 :                      # dy изменение координаты y в _cords
            print(f"It's too deep, i can't dive :(")    # dz изменение координаты z в _cords
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        return print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0" )

class Bird(Animal):
    beak = True                                          # наличие клюва

    def lay_eggs(self):
        print(f"Here are (is) {random.randint(1, 4)} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= int(abs(dz) * self.speed / 2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    pass

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    def __init__(self, speed):
        self.sound = "Click-click-click"
        super().__init__(speed)

    def speak(self):
        return print(f'{self.sound}')

# print(Duckbill.mro())                                 # проверка порядка наследования

'''Пример выполняемого кода:'''
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()