# https://leetcode.com/problems/3sum/description/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

def ThreeSum(nums):
    answer = []
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-2):
            for k in range(j+1,len(nums)):
                if (nums[i]!=nums[j] and nums[i]!=nums[k] and nums[j]!=nums[k]) and (nums[i] + nums[j] + nums[k] == 0):
                    # return nums[i], nums[j], nums[k]
                    answer.append((nums[i], nums[j], nums[k]))
    return answer

#  если числа 3 а сумма должна быть 0, то сумма двух по модулю равна третьему
# тогда 3 число будем сравнивать с двумя другими?


def Sum3(nums):
    nums.sort()
    answer = []
    # numssort2 = [-4, -2, -1, -1, 0, 3, 5]
    # num_indexes=[ 0,  1,  2,  3, 4, 5, 6]
    # range = nums-2 потому что нам всегда нужно минимум 3 числа в сумме
    for i in range(len(nums)-2):
        if nums[i]> 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = len(nums)-1
        # начинаем подход с 2 указателями
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # сумма дающая 0 является ответом на задачу, мы добавляем ее в ответ
                #  важно запомнить что в варианте ответа числа записаны в определенном порядке
                # индексы [   0   ,     1     ,     2      ]
                variant = [nums[i], nums[left], nums[right]]
                answer.append(variant)
                # но поскольку задание найти все триплеты, надо проверить дальше
                # то есть идти по указателям
                # сравнением с variant[1/2] мы проверяем и исключаем повтор чисел
                while left < right and nums[left] == variant[1]:
                    left += 1
                while left < right and nums[right] == variant[2]:
                    right -= 1
    return answer

nums2 = [-1, 0, -4, 3, -2, 5, -1]
numssort2 = [-4, -2, -1, -1, 0, 3, 5]
# Example 2 Output:

nums = [-1, -1, 0, 1, 2, 4]
# Example 1 Output: [[-1,-1,2],[-1,0,1]]


# print(ThreeSum(nums))
print(Sum3(nums2))
