""" Prime Factorization
Have the user enter a number and find all
Prime Factors (if there are any) and display them."""


def is_prime(n):
    if n % 2 == 0:
        # print(str(n) + ' % 2 False')
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            # print(str(n), ' % ', str(i), ' False')
            return False
    return True

num = int(input('Lets try > '))

factors = [1]

if num % 2 == 0:
    factors.append(2)

for i in range(3, int(num / 2) + 1):
    if num % i == 0:
        if is_prime(i):
            factors.append(i)
if len(factors) == 1:
    print('There\'s one factor:', factors, '.')
elif len(factors) > 1:
    print('There\'re such factors:', factors, '.')
else:
    print('There\'s no any factors.')

factors = []