# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


target = 14

def Search(target):
    left = 0
    right = target
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == target:
            return mid
        elif mid * mid > target:
            right = mid - 1
        else:
            left = mid + 1
    return right 

result = Search(target)
print(result)