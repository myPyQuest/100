""" Mortgage calculator.
    Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate.
    Also figure out how long it will take the user to pay back the loan. For added complexity, add an option
    for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
    # print("Ежемесячный платёж для %.2f %s годовая иппотека %.2f%% процентная ставка - %.2f" % (loan, (month / 12), rate, payment))
"""

month = int(input("введите срок иппотеки в месяцах: "))
rate = float(input("процентная ставка по кредиту: "))
loan = float(input("сумма заёма: "))

monthly_rate = rate / 100 / 12  # per month
payment = (monthly_rate / (1 - (1 + monthly_rate) ** (- month))) * loan

print("Заём:", loan, "грн.")
print("Срок:", month, "месяца(ев)")
print("Процент:", rate, "%")
print("Платёж:", payment, "грн.")