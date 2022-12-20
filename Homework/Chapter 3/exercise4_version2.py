# exercise4_version2.py -- Chapter 3
# Guesses a user-specified number using a sequential search strategy.

MIN = 1
MAX = 5

print("Computer will guess your number between", MIN, "and", MAX)

# Set the initial values
number = MIN
print("Is", number, "your guessed number? [Yes/no]")
answer = input()

# Target loop
while answer != "Yes":
	if answer != "no":
		print("Invalid input. Enter only Yes/no.")
		answer = input()
		continue
	number += 1
	print("Is", number, "your guessed number? [Yes/no]")
	answer = input()


	if MAX - number == 1 and answer != "Yes":
		number += 1
		break

# Output results
print("Yes, I knew it! Your number is", number, end="!\n")
input("\n\nPress the key <Enter> to exit.")
