# word_jumble.py
# 
# The computer picks a random word and then "jumbles" it.
# The player has to guess the original word.
# 

import random

# Create a sequence of words from which the computer chooses.
WORDS = ("purple", "jumble", "easy", "difficult", "answer", "xylophone")

# Pick one word randomly from the sequence
word = random.choice(WORDS)

# Create a variable to uses later to see if the guess is correct
correct = word

# Create a jumbled version of the original word
jumble = ""
while word:
	position = random.randrange(len(word))
	jumble += word[position]
	word = word[:position] + word[(position + 1):]

# Start the game
print(
"""
			Welcome to the game \'World Jumble\'!
		Unscramble the letters to guess a word.
	(Press the key <Enter> without input your version to exit.)
"""
)
print("The jumble is:", jumble)

guess = input("\nTry to guesss the original word (empty line to quit): ")
while guess != correct and guess != "":
	print("Sorry, that\'s not it.")
	guess = input("Try to guess the original word again: ")

if guess == correct:
	print("That\'s it! You guessed it!\n")

print("Thanks for playing.")
input("\n\nPress the key <Enter> to exit.")
