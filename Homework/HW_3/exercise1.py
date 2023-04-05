# exercise1.py
# 
# The program is a simulator of a pie festival.
# It displays 1 of 5 different pies that are choiced by a random way
# when the program is being launched.
# 

import random

print("\tWelcome to \'Simulator of Pie Festival\'!\n")
print("I will give you a pie randomly because we have Pie Festival!")
print("You may get the next pie: apple, raspberry, cherry, blueberry, cottage cheese.");

pie = random.randint(1, 5)
if 1 == pie:
	name = "apple"
elif 2 == pie:
	name = "raspberry"
elif 3 == pie:
	name = "cherry"
elif 4 == pie:
	name = "blueberry"
elif 5 == pie:
	name = "cottage cheese"
else:				# For error detecting.
	name = "none"

print("\nCongratulations!")
print("You got a pie with", name, end="!\n")

input("\n\nPress the key <Enter> to exit.")
