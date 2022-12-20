# exercise3.py -- Chapter 3
#
# The computer chooses a random number between 1 and 100.
# The player attempts to guess within a limited number of tries (5 tries) 
# and the computer tells the player if the guess is too high, too low, or correct.
#

import random

LOWER = 1 			# Lower range limit
UPPER = 100			# Upper range limit
MAX_TRIES = 8

print("\tWelcome to \'Guess My Number\'!")
print("\nI\'m thinking of a number between", LOWER, "and", UPPER, end=".\n")
print("Try to guess it in", MAX_TRIES, "attempts.")

# Set the initial values
the_number = random.randrange(UPPER) + LOWER
guess = int(input("Take a guess: "))
tries = 1

# Guessing loop
while  guess != the_number and tries < MAX_TRIES:
	if the_number < guess:
		print("Lower...")
	else:
		print("Higher...")

	guess = int(input("Take a guess: "))
	tries += 1

if tries < MAX_TRIES:
	print("You guessed it! The number was", the_number)
	print("And it only took you", tries, "tries!\n")
else:
	print("You lost!")
	print("You failed in", MAX_TRIES, "attempts.")

input("\n\nPress the key <Enter> to exit.")
