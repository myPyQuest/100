s = input("put here your string > ")

reverse = ""

for i in range(len(s) - 1, -1, -1):
	reverse += s[i]

print("reverse string of yours is: " + reverse)