# А - плата за месяц, B кол-во МБ выданных на это
# Если выше лимита то плата за MБ = С
# D сколько планирует потратить МБ
#



def Count(A, B, C, D):
    if D <= B:
        return A
    if D > B:
        result = A + C*(D-B)
        return result



input_str = input()
A, B, C, D = map(int, input_str.split())

result = Count(A, B, C, D)
print(result)