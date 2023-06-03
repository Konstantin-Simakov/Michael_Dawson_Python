# exercise2.py
# Improvement of the guess_my_number.py with aks_number() function using.

import random

# Range limits
LOW = 1
HIGH = 100

def ask_number(question="Some question... ", 
			   low=LOW, high=HIGH+1, step=1):
	''' Asks you to enter the number from a 
		range from low to (high-1) inclusive. 

	'''
	response = None
	while response not in range(low, high, step):
		response = int(input(question))

	return response


# Global scope

print("\tWelcome to \'Guess My Number\'!")
print("\nI\'m thinking of a number between", LOW, "and", HIGH, end=".\n")
print("Try to guess it in as few attempts as possible.")

# Set the initial values
the_number = random.randint(LOW, HIGH)
guess = ask_number(question="Take a guess: ")
tries = 1

# Guessing loop
while guess != the_number:
	if the_number < guess:
		print("Lower...")
	else:
		print("Higher...")
	guess = ask_number("Take a guess: ")
	tries += 1

print("You guessed it! The number was", the_number)
print("And it only took you", tries, "tries!\n")

input("\n\nPress the key <Enter> to exit.")
