from time import time

def my_decorator(func):
    def wrapper():
        print('Start')
        start = time()
        func()
        end = time()
        print(f'Time spent for func - {end-start}')

    return wrapper
@my_decorator
def say_hi():
    return tuple(range(10**7))

say_hi()