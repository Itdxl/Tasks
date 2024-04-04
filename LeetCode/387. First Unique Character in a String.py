# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

def firstUniqChar(s: str) -> int:
    string = list(s)
    numbers = {}
    for index, letter in enumerate(string):
        if letter in numbers:
            numbers.pop(letter)
        else:
            numbers[letter] = index
            
    return # НЕ ЗАКОНЧЕНА

s = 'loveleetcode'
result = firstUniqChar(s)
print(result)

