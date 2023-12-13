def twoSum(nums, target):
    result = []
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append((nums[i], nums[j]))
    return result

nums = [2, 3, 31, 5, 7, 2, 1, 32]
target = 34
print(twoSum(nums, target))