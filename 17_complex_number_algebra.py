""" **Complex Number Algebra**
    Show addition, multiplication, negation, and inversion of complex numbers in separate functions.
    (Subtraction and division operations can be made with pairs of these operations.)
    Print the results for each operation tested.
"""
from math import sqrt


class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return Number(self.x.r + self.y.r, self.x.im + self.y.im).show()

    def multi(self):
        return Number(self.x.r * self.y.r - self.x.im * self.y.im,
                      self.y.r * self.x.im + self.x.r * self.y.im).show()


class Number:
    def __init__(self, x, y):
        self.r = x
        self.im = y

    def show(self):
        print(self.r, self.im)

    def negation(self):
        self.r = (-self.r)
        self.im = (-self.im)
        return self

    def inversion(self):
        root = sqrt(self.r ** 2 + self.im ** 2)
        self.r /= root
        self.im /= (-root)
        return self

n1 = Number(3, 2)
n2 = Number(1, 1)

n1.negation().show()
n1.inversion().show()

c = Complex(n1, n2)

c.add()

c.multi()