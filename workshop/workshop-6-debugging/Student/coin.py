# -*- coding: utf-8 -*-
import math

# find greatest common divisor
# of given inputs a and b


def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


if __name__ == '__main__':
    # na : amount of coin_a
    # nb : amount of coin_b
    # find such a case that T = a*na + b*nb
    # print na, nb if possible, else print IMPOSSIBLE

    print('Input: coin_a coin_b target_value')
    print('Input: ', end='')
    a, b, T = [int(x) for x in input().split(' ')]

    # T cannot be composed by coin_a and coin_b
    # if it cannot be divided by their greatest common divisor
    if(T % gcd(a, b) != 0):
        print("IMPOSSIBLE")

    else:
        na = 0
        yes = False
        while(not yes):
            if (T - a*na) % b == 0:
                nb = (T - a*na)/b
                yes = True
            na += 1

        if(yes):
            print(f"na: {na}, nb: {int(nb)}")
        else:
            print("IMPOSSIBLE")
