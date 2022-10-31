class Card:
     def __init__(self, value, suit):
    ???
    def __str__(self):
    ???
    def next1(self):
    ???
    def next2(self):
    ???
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])