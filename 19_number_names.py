""" **Number Names**
    Show how to spell out a number in English. You can use a preexisting
    implementation or roll your own, but you should support inputs up to
    at least one million (or the maximum value of your language's
    default bounded integer type, if that's less).
    ##################################################################
    *Optional: Support for inputs other than positive integers
    (like zero, negative integers, and floating-point numbers).*
"""

units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

places = ['', 'first', 'second', 'third', ]
teenPlaces = ['tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth']
tensPlaces = ['', 'tenth', 'twentieth', 'thirtieth', 'fortieth', 'fifthieth', 'sixthieth', 'seventieth', 'eightieth', 'ninetieth']


def num_to_array(num):
    num_array = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    num_array[0] = num/100000000 % 10  # Hundred Millions place
    num_array[1] = num/10000000 % 10   # Ten Millions place
    num_array[2] = num/1000000 % 10    # Millions place
    num_array[3] = num/100000 % 10     # Hundred-thousands place
    num_array[4] = num/10000 % 10      # Ten-thousands place
    num_array[5] = num/1000 % 10       # Thousands place
    num_array[6] = num/100 % 10        # Hundreds place
    num_array[7] = num/10 % 10         # Tens place
    num_array[8] = num/1 % 10          # Ones place
    return num_array


def has_trailing_zeros(num_array):
    if num_array[6] != 0:
        return num_array[7] == 0 and num_array[8] == 0
    elif num_array[3] != 0 or num_array[4] != 0 or num_array[5] != 0:
        return num_array[6] == 0 and num_array[7] == 0 and num_array[8] == 0
    elif num_array[0] != 0 or num_array[1] != 0 or num_array[2] != 0:
        return num_array[3] == 0 and num_array[4] == 0 and num_array[5] == 0 and num_array[6] == 0 and num_array[7] == 0\
               and num_array[8] == 0


def num_to_words(num):
    num_array = num_to_array(num)
    word = ''
    if num == 0:
        word = 'zero'
    if 1 <= num <= 9:
        word = units[num]
    if 10 <= num <= 19:
        word = teens[num % 10]
    if 20 <= num <= 99:
        word += tens[num/10]
        if num_array[8] != 0:
            word += ' ' + units[num % 10]

    if 100 <= num <= 999:
        word += units[num_array[6]] + ' hundred '
        if not has_trailing_zeros(num_array):
            word += num_to_words(num_array[7]*10+num_array[8])

    if 1000 <= num <= 999999:
        word += num_to_words(num_array[3]*100+num_array[4]*10+num_array[5]) + ' thousand '
        if not has_trailing_zeros(num_array):
            word += num_to_words(num_array[6]*100+num_array[7]*10+num_array[8])

    if 1000000 <= num <= 999999999:
        word += num_to_words(num_array[0]*100+num_array[1]*10+num_array[2]) + ' million '
        if not has_trailing_zeros(num_array):
            word += num_to_words(num_array[3]*100000+num_array[4]*10000+num_array[5]*1000+num_array[6]*100+num_array[7]*10+num_array[8])

    word = ' '.join(word.split())
    return word


def num_to_place(num):
    num_array = num_to_array(num)
    place = ''
    if (num == 0):
        place = 'zeroth'
    if 1 <= num <= 9:
        place = places[num]
    if 10 <= num <= 19:
        place = teenPlaces[num % 10]
    if 20 <= num <= 9:
        if num_array[8] == 0:
            place += tensPlaces[num/10]
        else:
            place += tens[num/10] + ' ' + places[num % 10]

    if 100 <= num <= 999:
        if has_trailing_zeros(num_array):
            place += units[num_array[6]] + ' hundredth'
        else:
            place += units[num_array[6]] + ' hundred ' + num_to_place(num_array[7]*10+num_array[8])

    if 1000 <= num <= 999999:
        if has_trailing_zeros(num_array):
            place += num_to_words(num_array[3]*100 + num_array[4]*10 + num_array[5]) + ' thousandth'
        else:
            place += num_to_words(num_array[3]*100+num_array[4]*10+num_array[5]) + ' thousand '
            if not has_trailing_zeros(num_array):
                place += num_to_place(num_array[6]*100+num_array[7]*10+num_array[8])

    if 1000000 <= num <= 999999999:
        if has_trailing_zeros(num_array):
            place += num_to_words(num_array[0]*100 + num_array[1]*10 + num_array[2]) + ' millionth'
        else:
            place += num_to_words(num_array[0]*100+num_array[1]*10+num_array[2]) + ' million '
            if not has_trailing_zeros(num_array):
                place += num_to_place(num_array[3]*100000+num_array[4]*10000+num_array[5]*1000+num_array[6]*100+num_array[7]*10+num_array[8])
    place = ' '.join(place.split())
    return place


def main(num):
    number = input('Please enter a number: ')
    print('Word:\t%s' % num_to_words(number))
    print('Place:\t%s' % num_to_place(number))


main()