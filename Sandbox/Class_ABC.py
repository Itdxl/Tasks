from abc import ABC, abstractmethod



class AbsractExample(ABC):

    @abstractmethod
    def move(self):
        pass



class Car(AbsractExample):
    def __init__(self, x):
        self.speed = x
        super().__init__() # probably good practic to add if parent is not ABC
    def move(self):
        return f"Скорость равна {self.speed} "
    

class Plane(AbsractExample):
    def __init__(self, x):
        self.speed = x * 10
    def move(self):
        return f"Скорость равна {self.speed} "
    

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)

person1 = Person('Alice', 25)
person2 = Person.from_birth_year('Bob', 1990)


