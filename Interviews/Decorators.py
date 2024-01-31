def simple_decorator(func):
    def wrapper():
        print("До выполнения функции")
        func()
        print("После выполнения функции")
    return wrapper

def my_function():
    print("Выполнение функции")


decorated_function = simple_decorator(my_function)

@simple_decorator
def my_function():
    print("Выполнение функции")

print(decorated_function())


# декоратор хеширования
cache = dict()
counter = 0

def decor(func):
    def wrapper(*args, **kwargs):
        uniq= hash(*args, **kwargs)
        if uniq in cache:
            return cache[uniq]
        
        a = func(*args, **kwargs)
        cache[uniq] = a
        return a
    return wrapper
