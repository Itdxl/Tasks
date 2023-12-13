# https://leetcode.com/problems/4sum/description/
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

#  https://leetcode.com/problems/4sum/solutions/737096/sum-megapost-python3-solution-with-a-detailed-explanation/
# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

#  [1, -2, -3, -1, 4, 6, 2, 2]

# [-3, -2, -1, 1, 2, 2, 4, 6]

def FourSum(nums, target):
    nums.sort()
    answer = []
    for i in range(len(nums)-3):
        # if i > 0 and nums[i] == nums[i-1]:
        #     continue
        for k in range(i + 1, len(nums)-2):
            # if k > 0 and nums[k] == nums[k-1]:
            #     continue
            # правый сдвинут на два так как нужны 2 числа и это i и k
            # left = k + 1 так как по цикллу мы смещаем k и автоматически сдвинется left
            left = k + 1 
            right = len(nums) - 1
            while left < right:
                sum =  nums[i] + nums[k] + nums[left] + nums[right]
                if sum < target:
                    left +=1
                elif sum > target:
                    right -=1
                else:
                    variant = [nums[i], nums[k], nums[left], nums[right]]
                    if variant not in answer:
                        answer.append(variant)
                    while left < right and nums[left] == variant[2]:
                        left += 1
                    while left < right and nums[right] == variant[3]:
                        right -= 1
    return answer

nums = [-3, -2, -1, 1, 2, 2, 4, 6]
target = 0

nums2 = [2, 2, 2, 2, 2]
target2 = 8
print(FourSum(nums, target))
print(FourSum(nums2, target2))