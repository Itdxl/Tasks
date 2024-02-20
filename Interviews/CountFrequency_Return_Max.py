
from collections import Counter

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# not optimal, cause anyway needs counter or search by value required
def count_frequency1(nums):
    
    dict = {}
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    value_counter = Counter(dict.values())

    return max(value_counter)

result= count_frequency1(nums)

print(result)



def count_frequency2(nums):
    counter = Counter(nums)
    # counter returns pair: element,amount
    # we need only 
    most_common_element, most_common_count = counter.most_common(1)[0]
    return most_common_count




result= count_frequency2(nums)

print(result)

