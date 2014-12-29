s = input("> ")
splited = s.split()
l = len(splited)
if l == 1:
	print("there'is " + str(l) + " word in such string.")
elif l == 0:
	print("there's nothing.")
else:
	print("there're " + str(l) + " words in such string.")