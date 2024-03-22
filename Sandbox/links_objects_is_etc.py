# charles = {'name': 'Charles L. Dodgson', 'born': 1832}
# lewis = charles
# print(lewis is charles)
# print(id(charles), id(lewis))
# lewis['balance'] = 950
# print(charles)

# alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
# print(alex == charles)
# print(alex is not charles)


# print(id(alex)), print(id(charles))


# l1 = [3, [55, 44], (7, 8, 9)]
# l2 = list(l1)
# # l2 копия объекта l1, они будут равны, но ссылаться будут на один объект.

# l3 = l1[:]
# print(id(l1))
# print(id(l2))
# print(id(l3))

# l1 = [3, [66, 55, 44], (7, 8, 9)]
# l2 = list(l1) 
# l1.append(100) 
# l1[1].remove(55)
# print('l1:', l1)
# print('l2:', l2)
# l2[1] += [33, 22] 
# l2[2] += (10, 11) 
# print('l1:', l1)
# print('l2:', l2)


# import copy

# original_list = [[1, 2, 3], [4, 5, 6]]
# copied_list = copy.deepcopy(original_list)
# print(id(original_list))
# print(id(copied_list))


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# # Создаем два узла
# node1 = Node(1)
# node2 = Node(2)

# # Связываем их друг с другом
# node1.next = node2
# node2.next = node1 
