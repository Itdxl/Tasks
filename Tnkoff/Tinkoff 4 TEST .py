# n = 5
# k = 2
# numbers = (1, 2, 1, 3, 5)

n = 3
k = 2
numbers = (88, 9, 9)


diff = []
for elem in numbers:
    i = 1
    while elem:
        diff.append((9 - elem%10)*i)
        elem //= 10
        i *= 10
diff.sort(reverse=True)
#print(diff)
print(sum(diff[:k]))

# n = 1
# k = 1
# numbers = (9)



# n = 1
# k = 10
# numbers = (9999, )

# summ = sum(numbers)
# result = []
# for number in numbers:
#     i = 1
#     variants = [0]
#     while number > 0:
#         last = number % 10
#         if last == 9:
#             break
#         dif = ((9 - last) * i)
#         variants.append(dif)   
#         i *= 10
#         number = number // 10
#     result.append(max(variants))

# result = sorted(result)
# result_sum = sum(result[-k:])
# print (result_sum)





# 2741
# (10-4-1) = 5 * 10
# (10-7-1) = 2 * 100
# (10-2-1)= 7 * 1000
# max(50, 200, 7000)
# variants=[]


# n, k = map(int, input().split())
# numbers = list(map(int, input().split()))


# n = 5
# k = 2
# numbers = (1, 2, 1, 3, 5)



# result = Count(n, k, numbers)
# print(result)