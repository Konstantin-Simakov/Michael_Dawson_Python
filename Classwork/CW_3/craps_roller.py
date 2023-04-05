# craps_roller.py
# Demonstrates random numbers generation

# Importing the module, not a library -- ...see point notation for module...
import random

# Create random numbers from the range 1-6
dice1 = random.randint(1, 6)
dice2 = random.randrange(6) + 1
total = dice1 + dice2
print("Your roll resulted in", dice1, "and", dice2, "points, for a total", 
	total, "points.")
input("\n\nPress the key [Enter] to exit.")
