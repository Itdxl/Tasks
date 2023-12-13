# # на вход дается массив данных в котором числа от одного до N, перемешаны, 1 число удалено
# # найти удаленное число. Числа изначально шли по порядку и включали все числа от 1 до N

def Search(array):
    expected = 1
    for number in array:
        if number != expected:
            return expected
        expected +=1
     

array = list(map(int, input().split()))

result = Search(array)
print(result)


def Search2(array):
    for i in range(len(array) - 1):
        if array[i] + 1 != array[i + 1]:
            return array[i] + 1
        
array = list(map(int, input().split()))

result = Search2(array)
print(result)


def Search3(array):
    len_second = len(array)
    len_first = len_second + 1

    summ_first = len_first * (len_first+1) / 2   # S = (n * (n+1)) / 2
    return int(summ_first - sum(array))

        
array = list(map(int, input().split()))

result = Search3(array)
print(result)



