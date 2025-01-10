
class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    ''' Метод get_products(self), который считывает всю информацию из файла __file_name,
    закрывает его и возвращает единую строку со всеми товарами из файла __file_name. '''
    def get_products(self):
        file = open(self.__file_name, 'r')
        products_info = file.read()
        file.close()
        return products_info

    ''' Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
    Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле 
    (по полю name И по полю category). Если такой продукт уже есть, то увеличивает общий вес и выводит строку
    'Продукт <название> уже был в магазине, его общий вес теперь равен <вес> .'''
    def add(self, *products):
        existing_products = {}

         # Считываем существующие продукты из файла
        file = open(self.__file_name, 'r')
        for line in file:
            name, weight, category = line.strip().split(', ')
            existing_products[(name, category)] = float(weight)
        file.close()
        #  Добавляем новые продукты
        file = open(self.__file_name, 'a')
        for product in products:
            key = (product.name, product.category)
            if key in existing_products:
                    # Увеличиваем вес существующего продукта
                existing_products[key] += product.weight
                print(
                    f'Продукт {product.name} уже был в магазине, его общий вес теперь'
                    f' равен {existing_products[key]}.')
            else:
                    # Записываем новый продукт
                existing_products[key] = product.weight
                file.write(f'{product}\n')
        file.close()

# Пример результата выполнения программы:

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())