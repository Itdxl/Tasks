# n кол-во сотрудников t через сколько минут один уйдет
#  
# 5  5
# 1  4  9  16  25
# 2

def Count(n, t, floors, leaver):
    max_time = floors[-1] # last floor
    first = floors[0]
    start = floors[leaver-1]
    # if t < n and (start - first > t) and (max_time - start > t): # comparing with max_time is wrong 
    if (start - first > t) and (max_time - start > t): 
        to_top = (max_time - start)
        to_bottom = (start - first)
        if to_top > to_bottom:
            result = to_bottom + (max_time - first)
            return result
        if to_top < to_bottom:
            result = to_top + (max_time - first)
            return result
    else:
        result = max_time - first
        return result


n, t = map(int, input().split())
floors = list(map(int, input().split()))
leaver = int(input())

result = Count(n, t, floors, leaver)
print(result)
# result = Count(5, 5, floors, leaver)