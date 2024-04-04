def sequence(n):
    i = 1
    answer = ''
    while i <= n:
        add = str(i) * i
        answer += add
        i += 1
    return answer

result = sequence(10)
print(result)