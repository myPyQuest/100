""" #20 **Coin Flip Simulation**
    Write some code that simulates flipping a single coin however
    many times the user decides. The code should record the outcomes
    and count the number of tails and heads.
"""
import random


def coin_flip():
    head, tail, yes, result = 0, 0, True, None
    while yes:
        result = random.randint(0, 1)
        print(result)
        if result == 0:
            head += 1
            print('орел =', head)
        else:
            tail += 1
            print('решка =', tail)
        y = input('Again? (Y/N) ')
        if y.lower() is 'n':
            yes = False
        else:
            yes = True


coin_flip()