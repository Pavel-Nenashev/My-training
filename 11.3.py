import inspect

# Функция для получения информации об объекте.
def introspection_info(obj):

    # Получение типа объекта
    obj_type = type(obj).__name__

    # Получение атрибутов объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]

    # Получение методов объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    # Определение модуля объекта

    module = inspect.getmodule(obj)
    if module is None:
        module_name = '__main__'
    else:
        module_name = module.__name__

    # Получение других интересных свойств объекта, учитывая его тип,
    # например, длину для последовательностей
    other_info = {}
    if hasattr(obj, '__len__'):
        other_info['length'] = len(obj)
    if isinstance(obj, dict):
        other_info['key_count'] = len(obj)  # количество ключей для словарей

    # Сбор информации в словарь
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module_name,
        'other_info': other_info
    }

    return info

# Пример класса для демонстрации интроспекции.
class MyCustomClass:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello, {self.name}!'

    def change_name(self, new_name):
        self.name = new_name

# Пример результата выполнения программы:

# Использования функции
number_info = introspection_info(42)
print(number_info)

custom_object_info = introspection_info([1,2,3,4,5])
print(custom_object_info)

custom_object_info = introspection_info({'key1': 'value1', 'key2': 'value2'})
print(custom_object_info)

# Использования класса
custom_object_info = introspection_info(MyCustomClass("Urban"))
print(custom_object_info)