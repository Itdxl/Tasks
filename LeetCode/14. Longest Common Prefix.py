def Seacrh(array):
    first = array[0]
    for i in range(0, len(first)):
        for str in array[1:]:
            if i == len(str) or str[i] != first[i]:
                return first[0:i]  
    return first


# array = list(map(str, input().split()))


# в цикле бежим по каждой строке и по каждой букве
array = ["ab", "a"]

# len_search = len(min(array, key=len))

print(Seacrh(array))