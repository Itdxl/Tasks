# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time,
# return that integer.

# Так как нам дан отсортированный массив и 25% чисел - одно число, то можно сравнивать первое вхождение и четвертое(25%-ое от длины массива).

def search(nums):
    len_n = len(nums)
    quarter = len_n // 4
    for i in range(0, len_n - quarter):
        if nums[i] == nums[i + quarter]:
            return nums[i] 

# nums = list(map(int, input().split()))

arr = [1,2,2,6,6,6,6,7,10]
print(search(arr))