def change_list(numbers = None, string = None):
    if numbers == None:
        numbers = [1, 2, 3]
        numbers.append(string)
    else:
        numbers.append(string)
    
    return numbers

numbers = [1, 100, 1000]
string = 'sth'

result = change_list(numbers, string)
print(result)



from abc import ABC, abstractmethod

class MyInterface(ABC):
    @abstractmethod
    def do_something(self):
        pass