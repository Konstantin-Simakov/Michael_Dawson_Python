# exercise2.py
#
# This program "tosses" a coin 100 times 
# and reports how many times heads and how many times tails.
#

import random

# HEAD must be less than TAIL and differ between them by 1.
# Let 1 correspond to head, and 2 to tail.
HEAD = 1
TAIL = HEAD + 1
TRIES = 100		# Total number of tries

print("I toss a coin", TRIES, "times")
print("and report you how many times heads and tails.")

heads = 0		# The number of heads dropped
tails = 0 		# The number of tails dropped
while heads+tails != TRIES:
	coin = random.randint(HEAD, TAIL)
	# print("Toss #", heads+tails, end=": ")
	if HEAD == coin:
		# print("head")
		heads += 1
	else:
		# print("tail")
		tails += 1

print("\nHeads are dropped", heads, "times.")
print("Tails are dropped", tails, "times.")
input("\n\nPress the key <Enter> to exit.")
