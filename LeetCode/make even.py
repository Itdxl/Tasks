# Дан массив разных чисел, нужно привести все числа к четным,
# с помощью добавления единицы к числу и к его соседу
# Нам достаточно понять сколько нечетных чисел в массиве,
# то есть если общая сумма чисел четная то можно решить и идем дальше

def function(nums: list) -> int:
    count = 0

    if sum(nums) % 2 != 0:
        return 'impossible'
    else:
        for i in range(len(nums)):
            a = i + 1
            if nums[i] % 2 != 0:
                nums[i] += 1
                nums[a] += 1
                count += 1
            i += 1
        return count


nums = [4, 5, 6, 7]
nums2 = [3, 2, 2, 2]
nums3 = [0, 1, 0, 0, 1, 0]
nums4 = [4, 3, 4, 4, 3]

nums5 = [0, 0, 0, 0, 0, 0]
nums6 = []
print(function(nums6))
