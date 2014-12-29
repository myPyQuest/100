""" Binary to Decimal and Back Converter.
    Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
"""


def bin2dec(num):
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

    return binary[::-1]







# print(dec2bin(8))
print(bin2dec(1000))