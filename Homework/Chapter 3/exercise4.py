# exercise4.py -- Chapter 3
# Guesses a user-specified number using a binary search strategy.

# Set the working range 
MIN = 1
MAX = 100

print("Computer will guess your number between", MIN, "and", MAX)

# Set the initial values
minimum = MIN - 1
maximum = MAX + 1
number = (minimum + maximum) // 2

print("Is it", number, "your guessed number? [Yes/Higher/Lower]")
answer = input()
# Target loop
while answer != "Yes":
	if "Higher" == answer:
		minimum = number
	elif "Lower" == answer:
		maximum = number
	else:
		print("Invalid input. Enter only Yes/Higher/Lower.")
		answer = input()
		continue

	if maximum - minimum == 2:
		number = (minimum + maximum) // 2
		break
	elif maximum - minimum == 1:
		number = maximum
		break

	number = (minimum + maximum) // 2
	print("Is it", number, "your guessed number? [Yes/Higher/Lower]")
	answer = input()

# Output results
print("Yes, I knew it! Your number is", number, end="!\n")

input("\n\nPress the key <Enter> to exit.")
