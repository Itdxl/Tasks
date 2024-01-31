# 1 acceptable but not for interviews
def lengthOfLastWord(s):
    words = s.split()
    result = (len(words[-1]))
    return result

s = 'Hello world'
# result = lengthOfLastWord(s)
# print(result)

s2 = 'aa'
# 2
def length2(s):
    counter = 0
    i = len(s) - 1
    while i >=0:
        if s[i] == ' ':
            if counter > 0:
                return counter
        else:
            counter +=1
        i -=1
    return counter # in case if no spaces in string



result = length2(s2)
print(result)