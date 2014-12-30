""" **Unit Converter (temp, currency, volume, mass and more)**
    Converts various units between one another. The user enters the type of unit being entered,
    the type of unit they want to convert to and then the value. The program will then make the conversion.
"""

print('''
1. temp
2. currency
3. volume
4. mass ''')

type_of_value = input("choose what you want to convert: ")

if type_of_value == '1' or type_of_value == 'temp':
    print("""
    1. C
    2. F
    3. K
    """)

    t_in = input('from: ')

    if t_in == '1' or t_in.lower() == 'c':
        t_out = input('to: ')

        if t_out == '1' or t_out.lower() == 'c':
            t_val = int(input("How much (C): "))
            print(t_val * 1, 'C')
        elif t_out == '2' or t_out.lower() == 'f':
            t_val = int(input("How much (C): "))
            print(t_val * 9 / 5 + 32, 'F')
        elif t_out == '3' or t_out.lower() == 'k':
            t_val = int(input("How much (C): "))
            print(t_val + 273.15, 'K')

# elif type_of_value == '2' or type_of_value == 'currency':
#     pass
# elif type_of_value == '3' or type_of_value == 'volume':
#     pass
# elif type_of_value == '4' or type_of_value == 'mass':
#     pass
else:
    print('No such types')