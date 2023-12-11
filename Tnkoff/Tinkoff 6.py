

def Count(n, heights):
    left = 0
    right = n-1
    result = []
    if n == 2:
        if heights[left] % 2 == 0 and heights[right] % 2 == 1:
            return heights[right], heights[left]
        else:
            return ('here', -1, -1)
    if n > 2 and sum(heights) % 2 != 0:
        return -1, -1
    
    else:
        i = 1
        # нужен определяющий четность фактор и счетчик
        for height in heights:
            if i % 2 != 0:
                if heights[height] % 2 != 0:
                    i+=1
                    continue
                if heights[height] % 2 == 0:
                    result.append(heights[height])
                    i+=1
            if i % 2 == 0:
                if heights[height] % 2 == 0:
                    i+=1
                    continue
                if heights[height] % 2 != 0:
                    result.append(heights[height])
    return reversed(result)


n = int(input())
heights = list(map(int, input().split()))

result = Count(n, heights )
print(result)


# 4
# 2  1  3  6

# 3
# 1 2 3 4




# left = 0
#     right = n-1
#     while left < right:
#         if heights[left] % 2 == 0 and heights[right] % 2 != 0:  # thats wrong, task not about this at all