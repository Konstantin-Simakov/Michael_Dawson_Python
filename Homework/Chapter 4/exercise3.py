# exercise3.py -- Chapter 4
# 
# The computer picks a random word and then "jumbles" it.
# The player has to guess the original word.
# If player cannot to guess the original word he gets the prompt.
# 

import random

# Create a sequence of words from which the computer chooses.
# Also creat a sequence of prompts for each word separately 
# if the player has no assumptions about the word.
WORDS = ("purple", "jumble", "easy", "difficult", "answer", "xylophone")	# Total: 6 words
PROMPTS = (
		"\"That is a color intermediate between red and blue.\"", 			# 1st prompt
		"\"That is an untidy collection or pile of things.\"", 				# 2nd prompt
		"\"That was achieved without great effort.\"",						# 3rd prompt
		"\"That was achieved with great effort.\"",							# 4th prompt
		"\"This is a thing said, written, or done to deal with or as a\n" \
		   + "reaction to a question, statement, or situation.\"",			# 5th prompt
		"\"This is a musical instrument.\""									# 6th prompt
)

TOTAL_SCORES = 100			# The total number of scores the user starts playing with.
WITHOUT_PROMPT = 10			# The number of scores lost when a guess fails without prompt for player.
WITH_PROMPT = 20			# The number of scores lost when a guess fails with prompt for player.

# Pick one word randomly from the sequence
index = random.randrange(len(WORDS))
word = WORDS[index]

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
	(Put your scores down to 0 or lower or enter <Ctrl+C> to exit.)
"""
)
print("The jumble is:", jumble)

scores = TOTAL_SCORES
print("You have", scores, "scores at the start of the game.")

guess = input("\nTry to guesss the original word:\n")
while guess != correct and scores > 0:
	if "" == guess:			# Unsuccessful case with prompts 
		scores -= WITH_PROMPT
		if scores <= 0:
			break
		print("You request a prompt, so you lose", WITH_PROMPT, "scores " \
			+ "and you have", scores, "scores left.")
		print(PROMPTS[index])
		guess = input("Try to guess the original word again:\n")
	else:					# Unsuccessful case without prompts
		scores -= WITHOUT_PROMPT
		if scores <= 0:
			break
		print("Sorry, that\'s not it, so you lose", WITHOUT_PROMPT, "scores "\
			+ "and you have", scores, "scores left.")
		guess = input("Try to guess the original word again:\n")

if scores <= 0:
	print("You lose because you have no scores left.")
else:
	print("That\'s it! You guessed it!\n")
print("Thanks for playing.")

input("\n\nPress the key <Enter> to exit.")
