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


def fact_by_loop(n):
    multi = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(n):
            multi *= i
        return multi

num = int(input("Enter a number: "))

if num < 0 or num >= 1000:
    print("Error; num must be a positive or less than 1000")
    sys.exit()
print(num, '=>', fact_by_loop(num))