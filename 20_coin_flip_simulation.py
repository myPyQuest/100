""" #20 **Coin Flip Simulation**
    Write some code that simulates flipping a single coin however
    many times the user decides. The code should record the outcomes
    and count the number of tails and heads.
"""
import random


def coin_flip(n):
    n1 = n
    head, tail, yes, result = 0, 0, True, None
    while n:
        result = random.randint(0, 1)
        print(result)
        if result == 0:
            head += 1
            # print('орел =', head)
        else:
            tail += 1
            # print('решка =', tail)
        n -= 1
    print('Бросков:', n1, 'раз')
    print('Орел выпал', head, 'раз')
    print('Решка выпала', tail, 'раз')


n = int(input('Сколько раз будем бросать монету?: '))
coin_flip(n)