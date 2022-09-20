# craps_roller.py
# Demonstrates random numbers generation

# Importing the module, not a library -- ...see point notation for module...
import random

# Create random numbers from the range 1-6
die1 = random.randint(1, 6)
die2 = random.randrange(6)
total = die1 + die2
print("Your roll resulted in", die1, "and", die2, "points, for a total", total)
input("\n\nPress the key [Enter] to exit.")
