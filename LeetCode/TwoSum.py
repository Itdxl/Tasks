# https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return nums[i], nums[j]
    return None, None


def twoSumB(nums, target):
    result = []
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append((nums[i], nums[j]))
    return result


def twoSumEfficient(nums, target):
    # Важно отсортировать числа, так мы будем идти слева и справа и сравнивать числа беря то левое, то правое
    # То есть если взяли левое и правое и сумма больше, то берем второе левое и правое, потом второе левое и второе правое и тд
    # Если два указателя встретились, значит заданное число найти невозможно
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left< right:
        sum = nums[left] + nums[right]
        if  sum == target:
            return  (nums[left], nums[right])
        # то есть если сумма меньше чем цель, то мы увеличиваем левое
        if sum < target:
            left +=1
        # а если больше то уменьшаем правое
        else:
            right -=1
    return None, None

def twosum_extra_ds(numbers, X):
    # Создаём вспомогательную структуру данных с быстрым поиском элемента.
    previous = set()

    for A in numbers:
        Y = X - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)

    # Если ничего не нашлось в цикле, значит, нужной пары элементов в массиве нет.
    return None, None 




nums = [2, 3, 31, 5, 7, 2, 1, 32]
target = 34
print(twoSum(nums, target))
print(twoSumB(nums, target))
print(twoSumEfficient(nums, target))

