def repeatedCharacter(s: str) -> str:
        dict = []
        for simb in s:
                if simb in dict:
                        return simb
                else:
                    dict.append(simb)
        return None

s = 'abbcda'
result = repeatedCharacter(s)
print(result)