# random_access.py
# Demonstrates string indexation

import random

word = "Hello"
print("There is the next word in \'word\' variable:", word)

high = len(word)
low = -len(word)
for _ in range(10):
	index = random.randrange(low, high)
	print("word[", index, "]\t", word[index])

input("\n\nPress the key <Enter> to exit.")
