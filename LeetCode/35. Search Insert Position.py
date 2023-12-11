# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


nums = [1,3,5,6]
target = 2


# just binary
def Search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left # returning left cause we need to find index where number would be if not in given array

    

nums = list(map(int, input().split()))
target = int(input())

result = Search(nums, target)
print(result)