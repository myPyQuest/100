""" **Tax Calculator**
    Asks the user to enter a cost and either a country or state tax.
    It then returns the tax plus the total cost with tax.
"""


def total_cost(price, tax):
    return int(price) + int(price) * float(tax) / 100


def main():
    price = int(input("Enter the price of an item: $ "))
    tax = int(input("Enter the tax rate(%): "))
    print("The total cost is %.2f $." % total_cost(price, tax))


if __name__ == '__main__':
    main()