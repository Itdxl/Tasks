

# def plus(a, b):
#     return a + b

# def plus3(**args, c):
#     return plus(*)

# assert plus(1,2) == 3


# def plus(*args):
#     result = 0
#     for arg in args:
#         plus(arg, result)
#     return result

# # print(plus(1, 2, 3))

# data = map(abs, [1, 4, 2, 3 ])

# print(4 in data) # True
# print(3 in data) # True
# print(1 in data) # False так, как map уже прошел по списку и к 1 не вернется

# Замыкание
# def f():
#     num = 10
#     def g():
#         return num
#     num = 20
#     return g 
# func = f()
# print(func())
# print(func())

# str = 'sdasda'

# print(type(str))


# решить 150 и 224

# tokens = ["2","1","+","3","*"]
# n = len(tokens) - 1
# print(tokens[0])
# for i in range(0, n):
#     tokens[i]
#     print(tokens)


# import array

# # Создание массива значений типа float
# float_array = array.array('d', [1.0, 2.0, 3.0, 4.0, 5.0])

# # Создание кортежа значений типа float
# float_tuple = (1.0, 2.0, 3.0, 4.0, 5.0)

# # Получение размера в памяти каждой структуры данных
# size_of_float_array = float_array.__sizeof__()
# size_of_float_tuple = float_tuple.__sizeof__()

# print("Размер массива float:", size_of_float_array, "байт")
# print("Размер кортежа float:", size_of_float_tuple, "байт")


import json

# Пример строки JSON
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Преобразование строки JSON в объект Python
python_object = json.loads(json_string)

# Вывод объекта Python
print("Python объект после преобразования из JSON:", python_object)
print("Тип объекта:", type(python_object))

# Преобразование объекта Python обратно в строку JSON
new_json_string = json.dumps(python_object)

# Вывод новой строки JSON
print("Строка JSON после преобразования из объекта Python:", new_json_string)
print("Тип строки:", type(new_json_string))
