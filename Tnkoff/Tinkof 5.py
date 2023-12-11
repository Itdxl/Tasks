

def Count(l, r):
    counter = 0
    for i in range(1,10):
        x = i
        while x <= r:
            if x >= l:
                counter += 1
            x = x * 10 + i
    return counter


n, k = map(int, input().split())

result = Count(n, k)
print(result)
