# n = int(input())
# dots = [tuple(map(int, input().split())) for _ in range(n)]
n = 8
dots = [(0, 0), (1, 1), (0, 2), (5, 0), (5, 2), (0, 4), (3, 0), (3, 4)]

setd = set(dots)

answer = 0
for i in range(n):
    for j in range(i+1, n):
        formula = abs(dots[i][0] - dots[j][0]) * abs(dots[i][1] - dots[j][1])
        if formula > answer:
            # нужно проверить, что координаты которые мы нашли есть
            # в введенных.
            if (dots[i][0], dots[j][1]) in setd and (dots[j][0], dots[i][1]) in setd:
                answer = formula
print(answer)
