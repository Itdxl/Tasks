import collections

# namedtuple - a type of container dictionary 
# Класс из коллекции collections, который используется для построения классов,
# содержащих только атрибуты, никаких методов.
# Похож на класс, но не совсем, выглядит по принципу словаря, key:value
Card = collections.namedtuple('Card', ['rank', 'suit'])

some_card = Card('king', 'hearts')
# print(some_card) => Card(rank='king', suit='hearts')


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
    

deck = FrenchDeck()
deck2 = FrenchDeck()

card = deck[-1]
print(card)

# deck = deck.__len__()
# print(deck)

# deck2 =len(deck2) Пример, что для пользователя упрощен интерфейс взаимодействия
# print(deck2)  Так как в классе определен метод __len__, то мы мобращаясь к экземпляру используем len()

# В случае если происхожит обрещеие к встроенному классу, то у него есть полу ob_size(размер объекта),
#  поэтому вызов len() для экземпляра встроенного типа будет гораздо быстрее, так как вернется значение поля ob_size