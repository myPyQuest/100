""" Find next prime number
    until user say NO
"""


def is_prime(n):
    if n % 2 == 0:
        # print(str(n) + ' % 2 False')
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            # print(str(n), ' % ', str(i), ' False')
            return False
    return True


def generate_prime(current_prime):
    """ return the next prime
        after the current prime
    """

    next_prime = current_prime + 1

    while True:

        if not is_prime(next_prime):
            next_prime += 1
        else:
            break

    return next_prime


def main():     # wrapper function

    current_prime = 2

    while True:
        answer = input('Would you like to see next prime? (Y/N) > ')
        if answer.lower().startswith('y'):
            print(current_prime)
            current_prime = generate_prime(current_prime)
        else:
            break


if __name__ == '__main__':
    main()