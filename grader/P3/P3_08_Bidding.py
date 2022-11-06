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
