""" Binary to Decimal and Back Converter.
    Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
"""


def bin2dec(num):
    pass


def dec2bin(num):
    binary = ''

    while num > 0:
        binary += str(num % 2)
        num //= 2

    return binary[::-1]







print(dec2bin(8))