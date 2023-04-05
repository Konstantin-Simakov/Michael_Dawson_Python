# exercise1.py
# Displays the list of words in random order

import random		# For choice() function

# Create initial list of words with two same words
words = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Main part of program
for _ in range(len(words)):
	word = random.choice(words)
	words.remove(word)
	print(word)

input("\n\nEnter the key <Enter> to exit.")
