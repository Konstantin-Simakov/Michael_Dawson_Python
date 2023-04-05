# hangman.py
# 
# The classic game of Hangman. The computer picks a random word
# and the player have to guess it, one letter at a time. If the player
# can't guess the word in time, the little stick figure gets hanged.
# 

# Imports
import random

# Constants
HANGMAN = (

# 1
"""
------
|    |
|
|
|
|
|
|
|
----------
""",

# 2
"""
------
|    |
|    0
|
|
|
|
|
|
----------
""", 

# 3
"""
------
|    |
|    0
|   -+-
|
|
|
|
|
----------
""",

# 4
"""
------
|    |
|    0
|   -+-
|    |
|
|
|
|
----------
""",

# 5
"""
------
|    |
|    0
|   -+-
|    |
|    |
|
|
|
----------
""", 

# 6 
"""
------
|    |
|    0
|   -+-
|    |
|    |
|   | |
|
|
----------
""", 

# 7
"""
------
|    |
|    0
|   -+-
|    |
|    |
|   | |
|   | |
|
----------
""",

# 8
"""
------
|    |
|    0
|  /-+-/
|    |
|    |
|   | |
|   | |
|
----------
"""
)
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")

# Initialize variables
word = random.choice(WORDS)		# The word to be guessed

so_far = "_" * len(word)		# One underscore for each letter in word to be guessed
wrong = 0						# Number of a wrong guesses player has made
used = []						# Letters already used

print("Welcome to \'Hangman\'. Good luck!")

while wrong < MAX_WRONG and so_far != word:
	print(HANGMAN[wrong])
	print("\nYou\'ve used the following letters:\n", used)
	print("So far, the word is:\n", so_far)

	# Enter a letter
	guess = input("\n\nEnter your guess: ")
	guess = guess.upper()
	
	while guess in used:
		print("You\'ve already guessed the letter", guess)
		guess = input("\n\nEnter your guess again: ")
		guess = guess.upper()
	used.append(guess)

	if guess in word:
		print("\nYes!", guess, "is in the word!")

		# Create a new so_far to include guess
		new = ""
		for i in range(len(word)):
			if guess == word[i]:
				new += guess
			else:
				new += so_far[i]
		so_far = new

	else:
		print("\nSorry,", guess, "isn\'t in the word.")
		wrong += 1

if MAX_WRONG == wrong:
	print(HANGMAN[wrong])
	print("\nYou\'ve been hanged.")
else:
	print("\nYou guessed it!")

print("The word was", word)

input("\n\nPress the key <Enter> to exit game.")
