""" **Number Names**
    Show how to spell out a number in English. You can use a preexisting
    implementation or roll your own, but you should support inputs up to
    at least one million (or the maximum value of your language's
    default bounded integer type, if that's less).
    ##################################################################
    *Optional: Support for inputs other than positive integers
    (like zero, negative integers, and floating-point numbers).*
"""


def get_digits(number):
    digits = []
    while number:
        digits.append(number % 10)
        number //= 10
    digits.reverse()
    return digits


def is_happy_number(number):
    previous_numbers = []
    while True:
        digits = get_digits(number)
        sum_of_squared_digits = sum(list(map(lambda x: x ** 2, digits)))
        if sum_of_squared_digits == 1:
            return True
        elif sum_of_squared_digits in previous_numbers:
            return False
        else:
            number = sum_of_squared_digits
            previous_numbers.append(number)


def print_happy_number(number):
    happy_numbers = []
    count = 0
    while count < 8:
        if is_happy_number(number):
            happy_numbers.append(number)
            count += 1
        number += 1
    return happy_numbers


print(print_happy_number(int(input())))