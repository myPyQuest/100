""" **Factorial Finder**
    The Factorial of a positive integer, n, is defined as the product of the sequence
    n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1.
    Solve this using both loops and recursion.
"""
import sys


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


def factoloop(n):
    result = 1
    if n < 2:
        return 1
    else:
        while n > 1:
            result *= n
            n -= 1
        return result

num = int(input("Enter a number: "))

if num < 0 or num >= 1000:
    print("Error; num must be a positive or less than 1000")
    sys.exit()

print('fact', num, '=>', fact(num))
print('factoloop', num, '=>', factoloop(num))