# index_checking.py
# Demonstrates index working

import random

word = "Hello"
print("There is the next word in \'word\' variable:", word)

high = len(word)
low = -len(word)
for index in range(high):
	print("word[", end="") 
	print(index, end="")
	print("] =", word[index])
print()

for index in range(low, 0):
	print("word[", end="") 
	print(index, end="")
	print("] =", word[index])

input("\n\nPress the key <Enter> to exit.")
