class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor

        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует.')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Простоквашино', 2)
h4 = House('Санаторий Юбилейный', 7)

# __str__
print(h1)
print(h2)
print(h3)
print(h4)

# __len__
print(len(h1))
print(len(h2))
print(len(h3))
print(len(h4))

# h1.go_to(5)
# h2.go_to(10)
# h3.go_to(0)
# h4.go_to(4)