class Parent1:
    def method(self):
        print("This is a method from Parent1")

class Parent2:
    def method(self):
        print("This is a method from Parent2")

class MyClass(Parent2, Parent1):
    pass


obj = MyClass()
obj.method() # outputs "This is a method from Parent1"
# obj.method2() # outputs "This is a method from Parent2"