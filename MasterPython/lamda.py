fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
# sorting by last symbol. Lambda is reversing, sorted comparing and returning.
result = sorted(fruits, key=lambda word: word[::-1])
print(result)
# Lambda, considering its simplicity, can't contain any operators like with/try and even =
# 


numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, numbers))

print(squared)