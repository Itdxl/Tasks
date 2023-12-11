

def Count(n, k, numbers):
    result = []
    for number in numbers:
        i = 1
        variants = []
        while number:
            dif = ((9 - number%10) * i)
            result.append(dif)
            number //= 10
            i *= 10
    result = sorted(result)
    result_sum = sum(result[-k:])
    return result_sum


n, k = map(int, input().split())
numbers = list(map(int, input().split()))

result = Count(n, k, numbers)
print(result)