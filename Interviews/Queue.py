class Queue:

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
    # all difference between Queue and Queue: pop() or pop(0)
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError('queue is empty')


queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())