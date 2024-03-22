# N = int(input())
# numbers = list(map(int, input().split()))

N = 6
numbers = [1, 2, 1, 3, 1, 3]


def find(N, numbers):
    max, min = 0, 0
    for i in range(N):
    # for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[max]:
            max = i
        if numbers[i] < numbers[min]:
            min = i
    return min+1, max+1


result = find(N, numbers)
print(result)
