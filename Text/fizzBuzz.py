for i in range(1, 101):
	if i % 3 == 0 and i % 5 == 0:
		print(str(i) + " " + "FizzBuzz ( % 3 and 5 )")
	elif i % 3 == 0:
		print(str(i) + " " + "Fizz ( % 3 )")
	elif i % 5 == 0:
		print(str(i) + " " + "Buzz ( % 5 )")
	else:
		print(i)