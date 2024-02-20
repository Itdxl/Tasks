# Декоратор - механизм, позволяющий изменить поведение функции или метода.
# Позволяют изменить работу функции целиком или только ее логику.


def my_decor(func):
    def wrapper(*args, **kwargs):
        print('before func')
        func(*args, **kwargs)
        print('after func')

    return wrapper

@my_decor
def my_funct():
    print('inside func')

my_funct()

