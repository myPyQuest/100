""" Calculator.
    A simple calculator to do basic operators. Make it a scientific calculator for added complexity.
"""

print("""
    Ex. 5 + 8;
    operators can be: +, -, /, *, **, %, //
""")

num1, operator, num2 = int(input("first number > ")), input("operator > "), int(input("second number > "))


if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '/':
    print(num1 / num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '**':
    print(num1 ** num2)
elif operator == '%':
    print(num1 % num2)
elif operator == '//':
    print(num1 // num2)
else:
    print('Invalid operator')