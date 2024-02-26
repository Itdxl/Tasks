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
    