stringOfNumbers = input("Enter a valid string of commands (if you dont know the syntax, read the docs on the github - github.com/PartehDev/Letlang) $ ")
prevchar = None
value = 0
output = ""
char = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
charlength = 62
for char in stringOfNumbers:
	if prevchar = None:
		if char == 1:
			print("Exiting! Output is none")
			raise TypeError('Exited!')
		if char == 2:
			value += 1
			prevchar = 2
		if char == 3:
			value -= 1
			prevchar = 3
		if char == 4:
			prevchar = 4
		if char == 5:
			output += " Hello, world!"
			prevchar = 5
		if char == 6:
			value *= value
			prevchar = 6
	if prevchar == 2:
		if char == 1:
			print("Exiting! Output is "+output)
			raise TypeError('Exited!')
		if char == 2:
			value += 1
			prevchar = 2
		if char == 3:
			value -= 1
			prevchar = 3
		if char == 4:
			prevchar = 4
		if char == 5:
			output += " Hello, world!"
			prevchar = 5
		if char == 6:
			value *= value
			prevchar = 6
	if prevchar == 3:
		if char == 1:
			print("Exiting! Output is "+output)
			raise TypeError('Exited!')
		if char == 2:
			value += 1
			prevchar = 2
		if char == 3:
			value -= 1
			prevchar = 3
		if char == 4:
			prevchar = 4
		if char == 5:
			output += " Hello, world!"
			prevchar = 5
		if char == 6:
			value *= value
			prevchar = 6
	if prevchar == 4:
		for i in range(char):
			value += 1
	if prevchar == 5:
		if char == 1:
			print("Exiting! Output is "+output)
			raise TypeError('Exited!')
		if char == 2:
			value += 1
			prevchar = 2
		if char == 3:
			value -= 1
			prevchar = 3
		if char == 4:
			prevchar = 4
		if char == 5:
			output += " Hello, world!"
			prevchar = 5
		if char == 6:
			value *= value
			prevchar = 6
	if prevchar == 6:
		if char == 1:
			output += char[value]
			print("Exiting! Output is "+output)
			raise TypeError('Exited!')
		if char == 2:
			value += 1
			prevchar = 2
		if char == 3:
			value -= 1
			prevchar = 3
		if char == 4:
			prevchar = 4
		if char == 5:
			output += " Hello, world!"
			prevchar = 5
		if char == 6:
			value *= value
			prevchar = 6
if value > charlength:
	raise TypeError("Value heigher than the length of the character limit.")
output += char[value]
print(output)
