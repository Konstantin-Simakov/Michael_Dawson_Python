# exercise4.py -- Chapter 4
# The computer picks some word and a player try to guess it

import random			# For random.randrange()

# Set of 'ranodm' words that have to be guessed by the player
WORDS = ("purple", "jumble", "easy", "difficult", "answer", "xylophone")	# Total: 6 words
# According to these words set of prompts
PROMPTS = (
		"\"That is a color intermediate between red and blue.\"", 			# 1st prompt
		"\"That is an untidy collection or pile of things.\"", 				# 2nd prompt
		"\"That was achieved without great effort.\"",						# 3rd prompt
		"\"That was achieved with great effort.\"",							# 4th prompt
		"\"This is a thing said, written, or done to deal with or as\n" \
		   + "a reaction to a question, statement, or situation.\"",		# 5th prompt
		"\"This is a musical instrument.\""									# 6th prompt
)
# The max number of attempts to guess a letter in a word
ATTEMPTS = 5

# Pick one word randomly from the sequence by the 'WORDS' index
index = random.randrange(len(WORDS))
word = WORDS[index]

# Create a variable to uses later to see if the guess is correct
correct = word

# Create a start unknown word
guess = ""
for i in range(len(word)):
	guess += "_"

# Start the game
print(
"""
			Welcome to the game \'Guess the word\'!
		Unscramble the letters to guess a word.
	(Press the key <Enter> without input your version to exit.)
"""
)
# Output the prompt
print("\nGuessed word:", guess)
print("\nPrompt for guessing:")
print(PROMPTS[index])

# 'Word' algorithm realization.
# Enter a letter from the word
print("\nTry to guess a letter from the word (up to", 
	ATTEMPTS, "attempts for a letter):", end=" ")
letter = input()
# Current number of attempts
attempt = 0
while letter != "":
	if letter not in word:
		print("No")
		
		attempt += 1
		if ATTEMPTS == attempt:
			break
		
		print(guess)
		letter = input("Enter a letter from the guessing word: ")
		continue
	
	attempt = 0
	print("Yes")
	# Search for a letter contained in a word
	for i in range(len(word)):
		if word[i] == letter:
			position = i
			break

	# Write the given letter to the desired variable 
	# at the given position
	guess = guess[:position] + letter + guess[(position + 1):]
	print(guess)
	if guess == correct:
		break

	# From the updated word, delete the given letter 
	# at the same position
	word = word[:position] + "_" + word[(position + 1):]

	# Enter a next letter from the word
	letter = input("Enter a next letter from the guessing word: ")

# Output results
if "" == letter:
	print("You lose because you refused to guess the word.")
elif guess == correct:
	print("You win because you guessed the word.")
elif ATTEMPTS == attempt:
	print("You lose because you didn\'t guess a letter for", ATTEMPTS, "attempts in a row.")
else:
	print("Error: \'word\' algorithm realization")

input("\n\nPress the key <Enter> to exit.")
