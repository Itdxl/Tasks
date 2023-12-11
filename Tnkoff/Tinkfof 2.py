# Мы разре


def Count(A):
    count = 0
    if A == 1:
        return 0
    while A > 1:
        if A % 2 == 0:
            A = A // 2
            count += 1
        else:
            A = A - 1
            count += 1
    return count


input_str = input()
A = int(input_str)

result = Count(A)
print(result)
