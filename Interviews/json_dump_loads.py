import json

# Строка JSON
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Преобразование строки JSON в объект Python
python_object = json.loads(json_string)


print("Python объект после преобразования из JSON:", python_object)
print("Тип объекта:", type(python_object))

# Преобразование объекта Python обратно в строку JSON
new_json_string = json.dumps(python_object)

# Вывод новой строки JSON
print("Строка JSON после преобразования из объекта Python:", new_json_string)
print("Тип строки:", type(new_json_string))
