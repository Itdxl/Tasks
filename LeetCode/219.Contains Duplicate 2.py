# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such
# that nums[i] == nums[j] and abs(i - j) <= k.

nums1 = [1,2,3,1]
k1 = 3

nums2 = [-1, -1]
k2 = 1


def containsNearbyDuplicate(nums, k):
    ordered = sorted(nums)
    left = 0
    right = len(nums) - 1
    while left <= right:
        if (nums[left] + nums[right]) == k and abs(nums[left] - nums[right]):
            return True
        elif nums[left] + nums[right] > k:
            right -=1
        else:
            left +=1
    return False

result = containsNearbyDuplicate(nums2, k2)
print(result)
