# Оператор global указывает, что мы изменяем глобальную переменную.
# Оператор nonlocal позволяет изменять значение переменных, определенных во внешней функции.
# Замыкание состоит из внешней и внутренеей функции. 
# Внутрення функция имеет доступ к еременным внешней функции даже после заврешения работы последней.
# Так как замыкание сохраняет сссылки на переменные, а не значение.
# Вывод: замыкание это концепт программирования, позволяющий создавать функции и давать им доступ к переменным
# вне их зоны видимости. Полезен при ограничении доступа, работе с файлами, сетевыми протоколами.


# 1
def outer():
    n = 5
    def inner():
        # Здесь мы создаем переменную заново
        # Можно указать что она глобальная, тогда 
        # global n
        n = 25
        print(n)
    inner()
    print(n)

outer()

# 2
def outer(x):
    def inner(y):
        return x + y
    return inner

closure = outer(100)
print(closure(20))  
# 3
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3

# 4

def defender(password):
    def checker():
        if password == 'expected':
            print('Correct password')
        else:
            print('Denied')
        
    return checker
check = defender('expected')
check()