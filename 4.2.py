def test_function():

    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

test_function()

# inner_function()

# При попытке вызвать inner_function() вне функции test_function() выдает следующую ошибку:

# Traceback (most recent call last):
#   File "C:\Users\Professional\PycharmProjects\pythonProject\Urban\4.2.py", line 9, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
