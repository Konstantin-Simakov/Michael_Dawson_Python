# mood_computer.py
# Demonstrates using elif constructions

import random

print("I feel your energy. None of your feelings are hidden from my screen.")
print("So, your mood...")
mood = random.randint(1, 3)
if 1 == mood:
	# Happy
	print(
	"""
	 -----------
	 |         |
	 | 0     0 |
	 |    <    |
	 |         |
	 | .     . |
	 |  `...`  |
	 -----------
	"""
)
elif 2 == mood:
	# So-so
	print(
	"""
	 -----------
	 |         |
	 | 0     0 |
	 |    <    |
	 |         |
	 |  -----  |
	 |         |
	 -----------
	"""
)
elif 3 == mood:
	# Awful
	print(
	"""
	 -----------
	 |         |
	 | 0     0 |
	 |    <    |
	 |         |
	 |  . ' .  |
	 | '     ' |
	 -----------
	 """
)
else:
	print("There is no such mood (you are probably completely crazy).")
print("...But that\'s just today.")

input("\n\nPress the key [Enter] to exit.")
