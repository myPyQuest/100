""" Change Return Program.
    The user enters a cost and then the amount of money given.
    The program will figure out the change and the number of quarters,
    dimes, nickels, pennies needed for the change.
"""

# cost = float(input('цена > '))
# given = float(input('ваши > '))

cost = 22.14
given = 25

print('цена %.2f' % cost)
print('ваши %.2f' % given)

pound, quarter, dime, nickel, penny = 0, 0, 0, 0, 0

change = given - cost

print('сдача %.2f' % change)

pound = int(change)

change_in_pe = int((change - pound) * 100)

quarter = change_in_pe // 25

dime = (change_in_pe % 25) // 10

nickel = ((change_in_pe % 25) % 10) // 5

penny = ((change_in_pe % 25) % 10) % 5

print(pound, 'pounds')
# print('left = %.2f' % (change - pound))
print(quarter, 'quarters')
# print('left =', change_in_pe % 25)
print(dime, 'dimes')
# print('left =', (change_in_pe % 25) % 10)
print(nickel, 'nickels')
# print('left =', ((change_in_pe % 25) % 10) % 5)
print(penny, 'pennies')