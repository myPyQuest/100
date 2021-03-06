""" **Unit Converter (temp, currency, volume, mass and more)**
    Converts various units between one another. The user enters the type of unit being entered,
    the type of unit they want to convert to and then the value. The program will then make the conversion.
"""


def temp_cf(begin, t):
    # convert C to F and back
    if str(begin).lower() == 'c':
        t_f = t * 9 / 5 + 32
        return t_f
    elif str(begin).lower() == 'f':
        t_c = (t - 32) * 5 / 9
        return t_c
    else: print("Error input")


def temp_ck(begin, t):
    # convert C to K & back
    if str(begin).lower() == 'c':
        t_k = t + 273.15
        return t_k
    elif str(begin).lower() == 'k':
        t_c = t - 273.15
        return t_c
    else: print("Error input")


def temp_kf(begin, t):
    # convert K to F & back
    if str(begin).lower() == 'k':
        t_f = (t - 273.15) * 9 / 5 + 32
        return t_f
    elif str(begin).lower() == 'f':
        t_k = ((t - 32) * 5 / 9) + 273.15
        return t_k


def exchange_us_eu(start, cur):
    pass


# def exchange_...LONG LONG SUCKS


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
        start = 'c'
        t_out = input('to: ').lower()

        if t_out == '1' or t_out == 'c':
            t_val = int(input("How much (C): "))
            print(t_val)
        elif t_out == '2' or t_out == 'f':
            t_val = int(input("How much (C): "))
            print(temp_cf(start, t_val))
        elif t_out == '3' or t_out == 'k':
            t_val = int(input("How much (C): "))
            print(temp_ck(start, t_val))
    elif t_in == '2' or t_in.lower() == 'f':
        start = 'f'
        t_out = input('to: ').lower()

        if t_out == '1' or t_out == 'c':
            t_val = int(input("How much (F): "))
            print(temp_cf(start, t_val))
        elif t_out == '2' or t_out == 'f':
            t_val = int(input("How much (F): "))
            print(t_val)
        elif t_out == '3' or t_out == 'k':
            t_val = int(input("How much (F): "))
            print(temp_kf(start, t_val))
    elif t_in == '3' or t_in.lower() == 'k':
        start = 'k'
        t_out = input('to: ').lower()

        if t_out == '1' or t_out == 'c':
            t_val = int(input("How much (K): "))
            print(temp_ck(start, t_val))
        elif t_out == '2' or t_out == 'f':
            t_val = int(input("How much (K): "))
            print(temp_kf(start, t_val))
        elif t_out == '3' or t_out == 'k':
            t_val = int(input("How much (K): "))
            print(t_val)


elif type_of_value == '2' or type_of_value == 'currency':
    print("""
1. US
2. EU
3. RU
4. HR
""")

    cur_in = input("What's currency you want to convert? > ").lower()
    cur_out = input("In what currency? > ").lower()

    if cur_in == '1' or cur_in == 'us':
        cur = 'us'

    elif cur_in == '2' or cur_in == 'eu':
        cur = 'eu'
    elif cur_in == '3' or cur_in == 'ru':
        cur = 'ru'
    elif cur_in == '4' or cur_in == 'hr':
        cur = 'hr'

# elif type_of_value == '3' or type_of_value == 'volume':
#     pass
# elif type_of_value == '4' or type_of_value == 'mass':
#     pass
else:
    print('No such types')
