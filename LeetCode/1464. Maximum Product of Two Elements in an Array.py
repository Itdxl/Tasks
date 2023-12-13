# def maxProduct(nums):
#     left = 0
#     right = len(nums) - 1
#     max_a = max_b = 0
#     while left < right:
#         if nums[left] > max_a:
#             max_a = nums[left]
#         if nums[right] > max_b:
#             max_b = nums[right]
#         left +=1
#         right -= 1
#     return (max_a - 1) * (max_b - 1)

# def maxProduct(nums):
#     array = sorted(nums)
#     num1 = array[-1]
#     num_2 = array[-2]
#     return (num1 - 1) * (num_2 - 1)

def maxProduct(nums):
    nums.sort()
    num1 = nums[-1]
    num_2 = nums[-2]
    return (num1 - 1) * (num_2 - 1)




nums = [3,4,5,2]

# nums = list(map(int, input().split()))
result = maxProduct(nums)
print(result)

