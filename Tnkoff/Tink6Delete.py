def is_enough_a_pair(nums):
    wrong_pos = []
    for index, value in enumerate(nums):
        if (index + 1) % 2 != value % 2:
            wrong_pos.append(index+1)
        if len(wrong_pos) > 2:
            return -1, -1
    if len(wrong_pos) > 0:
        if len(wrong_pos) == 2 and wrong_pos[0] % 2 != wrong_pos[1] % 2:
            return wrong_pos
        return -1, -1
    if len(nums) > 2:
        return 1, 3
    return -1, -1
 
 
 
n = int(input())
nums = list(map(int, input().split()))
 
# print(*is_enough_a_pair(nums))

# nums = [1, 2, 3, 4]
# for i,y in enumerate(nums):
#     print (i, y)
    



