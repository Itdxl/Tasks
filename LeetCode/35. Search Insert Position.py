# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

  

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# just binary
def Search(array, target):
    left = 0
    right = len(array) - 1
    while left < right:
        mid = (left + right) // 2
        item = array[mid]
        if target == item:
            return mid
        if item > target:
            right = mid - 1
        else:
            left = mid + 1
        return None
    

nums = list(map(int, input().split()))
target = int(input())

result = Search(nums, target)
print(result)