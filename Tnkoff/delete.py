tuple = (1, 2 , ['a', 'b'])

sth = ['c','c', 'c', 'c','c','c','c', 'c', 'c','c','c','c', 'c', 'c','c','c','c', 'c', 'c','c','c','c', 'c', 'c','c','c']

for i in sth:
    tuple[2].append(i)
print(tuple)