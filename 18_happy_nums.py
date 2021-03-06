""" **Happy Numbers**
    A happy number is defined by the following process. Starting with any positive integer,
    replace the number by the sum of the squares of its digits, and repeat the process until
    the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not
    include 1. Those numbers for which this process ends in 1 are happy numbers, while those
    that do not end in 1 are unhappy numbers. Display an example of your output here.
    Find first 8 happy numbers.
"""


numbers_found = 1
happy_numbers = [1]
i = 2
while numbers_found != 8:
    j = i
    string_number = str(i)
    sum_of_squares = 0
    memory = []
    memory.append(i)
    while True:
        for k in string_number:
            sum_of_squares += int(k) ** 2
        if sum_of_squares in memory:
            break
        if sum_of_squares == 1:
            happy_numbers.append(i)
            numbers_found += 1
            break
        memory.append(sum_of_squares)
        string_number = str(sum_of_squares)
        sum_of_squares = 0
    i += 1

print(happy_numbers)


#
# def get_digits(number):
#     digits = []
#     while number:
#         digits.append(number % 10)
#         number //= 10
#     digits.reverse()
#     return digits
#
#
# def is_happy_number(number):
#     previous_numbers = []
#     while True:
#         digits = get_digits(number)
#         sum_of_squared_digits = sum(list(map(lambda x: x ** 2, digits)))
#         if sum_of_squared_digits == 1:
#             return True
#         elif sum_of_squared_digits in previous_numbers:
#             return False
#         else:
#             number = sum_of_squared_digits
#             previous_numbers.append(number)
#
#
# def print_happy_number(number):
#     happy_numbers = []
#     count = 0
#     while count < 8:
#         if is_happy_number(number):
#             happy_numbers.append(number)
#             count += 1
#         number += 1
#     return happy_numbers
#
#
# print(print_happy_number(int(input())))