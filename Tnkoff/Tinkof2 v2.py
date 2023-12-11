
def Count(A):
    count = 0
    p = 1
    while p < A:
        count += 1
        p *= 2
    return count

input_str = input()
A = int(input_str)

result = Count(A)
print(result)
