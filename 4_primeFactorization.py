""" Prime Factorization
Have the user enter a number and find all
Prime Factors (if there are any) and display them."""


def is_prime(n):
    if n % 2 == 0:
        print(str(n) + ' % 2 False')
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            print(str(n), ' % ', str(i), ' False')
            return False
    return True

num = int(input('Lets try > '))

print(is_prime(num))