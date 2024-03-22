
def count(N, M):
    answer = 0
    x = N * M
    while x > 1:
        if x % 2 == 0:
            x = x / 2
            answer += 1
        else:
            return answer
    return answer



N, M = map(int, input().split())
result = count(N, M)
print(result)
