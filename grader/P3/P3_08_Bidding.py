class Bid:
    def __init__(self, value, person, order):
        self.value = value
        self.person = person
        self.order = order

    def __lt__(self, rhs):
        if self.value != rhs.value:
            return self.value > rhs.value
        return self.order < rhs.order


dict_bid = {}
n = int(input())

for i in range(n):
    q = input()
    bid = Bid(v, p, b)
    if q == 'B':
        b, p, v = input().split()
        if b in dict_bid:
            dict_bid[b] += [bid]
        else:
            dict_bid[b] = [bid]
    else:
        dict_bid[b].remove(bid)
