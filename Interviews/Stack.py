class Stack:

    def __init__(self):
        self.items = []
        self.type = None

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        if self.type is None:
            self.type = type(item)
        elif type(item) != self.type:
            raise TypeError(f'expected type is {self.type}')
        return self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('stack is empty')


stack = Stack()
stack.push(1)
stack.push(2)
stack.push('22')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())