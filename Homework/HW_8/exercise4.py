# exercise4.py
# 
# List of virtual pets in the zoo farm 
# that the user cares about.
# 

import random		# For random.randint()
import sys			# For sys.exit()


AWFUL = 16			# Level of unhappiness named 'awful'.


class Critter(object):
	'''Virtual pet.'''

	def __init__(self, name, hunger=0, boredom=0):
		self.name = name
		self.hunger = hunger
		self.boredom = boredom

	def __pass_time(self):
		self.hunger += 1
		self.boredom += 1

	@property
	def mood(self):
		unhappiness = self.hunger + self.boredom
		if unhappiness < 5:
			m = "great"
		elif AWFUL - 11 <= unhappiness <= AWFUL - 6:
			m = "good"
		elif AWFUL - 6 <= unhappiness <= AWFUL - 1:
			m = "satisfactorily"
		else:
			m = "awful"

		return m

	def talk(self):
		print("My name is", self.name, "and I feel", self.mood, "now.\n")
		
		self.__pass_time()

	def eat(self, food=4):
		print("Ufff... Thanks!")
		
		self.hunger -= food
		if self.hunger < 0:
			self.hunger = 0

		self.__pass_time()

	def play(self, fun=4):
		print("Uiiii!")
		
		self.boredom -= fun
		if self.boredom < 0:
			self.boredom = 0

		self.__pass_time()


# Main part
def main():
	critters = []
	print("Enter names of critters (empty line to finish input).\n")
	
	crit_name = input("How will you name your critter? ")
	while crit_name != "":
		# Random level of hunger and boredom for a critter.
		crit_hunger = random.randint(0, AWFUL // 2)
		crit_boredom = random.randint(0, AWFUL // 2)
		critters.append(Critter(crit_name, crit_hunger, crit_boredom))
		
		crit_name = input("How will you name your next critter? ")
	
	if len(critters) != 0:
		print("\nYou have", len(critters), "critters in your zoo farm.\n")
	else:
		input("\n\nPress the key <Enter> to exit.")
		sys.exit()

	choice = None
	while choice != "0":
		print(
		"""
		Critter Caretaker
		0 - Quit
		1 - Find out about feelings of critters
		2 - Feed critters
		3 - Play with critters
		""")
		choice = input("Your choice: ")
		print()

		# Quit.
		if "0" == choice:
			print("Bye.")
		
		# Find out about critter's feeling.
		elif "1" == choice:
			for crit in critters:
				crit.talk()
		
		# Feed the critter.
		elif "2" == choice:
			for crit in critters:
				crit.eat()
		
		# Play with the critter.
		elif "3" == choice:
			for crit in critters:
				crit.play()

		# Unknown user input.
		else:
			print("Sorry, there is no item", choice, "in the menu.")


# Start the program.
main()
input("\n\nPress the key <Enter> to exit.")
