num = 0

for i in range(10):
    num += i if i % 2 else -i

print(num)
# Вывод будет число: 5 

# if i % 2 == 0 то оно вычитается
# смысл в сравнении с числом 0. Так как В Python число 0 это ложное
#  А любое число не равное 0 - истинное