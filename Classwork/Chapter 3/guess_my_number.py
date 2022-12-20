# guess_my_number.py
#
# The computer picks a random number between 1 and 100.
# The player tries to guess it and the computer lets
# the player knwo if the guess is too high, too low
# or right on the money.
#

import random

print("\tWelcome to \'Guess My Number\'!")
print("\nI\'m thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")

# Set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# Guessing loop
while guess != the_number:
	if the_number < guess:
		print("Lower...")
	else:
		print("Higher...")
	
	guess = int(input("Take a guess: "))
	tries += 1

print("You guessed it! The number was", the_number)
print("And it only took you", tries, "tries!\n")

input("\n\nPress the key <Enter> to exit.")
