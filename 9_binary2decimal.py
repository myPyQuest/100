""" Binary to Decimal and Back Converter.
    Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
"""


def bin2dec(num):
    num = str(num)[2:]
    rev = str(num)[::-1]
    n = 0

    for i in range(0, len(rev)):
        n += int(rev[i]) * (2 ** i)

    return n


def dec2bin(num):
    binary = ''

    while num > 0:
        binary += str(num % 2)
        num //= 2
    binary += 'b0'

    return binary[::-1]


number = input('> ')

if number[:2] == '0b':
    print(bin2dec(number))
else:
    print(dec2bin(int(number)))