# exercise1.py
# 
# Improvement the critter_caretaker.py program.
# Virtual pet that user takes care about.
# 


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
		elif 5 <= unhappiness <= 10:
			m = "good"
		elif 11 <= unhappiness <= 15:
			m = "satisfactorily"
		else:
			m = "awful"

		return m

	def talk(self):
		print("My name is", self.name, "and I feel", self.mood, "now.\n")
		self.__pass_time()

	def eat(self):
		print("How many kg of food do you want to give your critter?")
		print("(The recommended amount is 3 kg or more.)")
		food = int(input("Your amount of food: "))
		
		self.hunger -= food
		if self.hunger < 0:
			self.hunger = 0

		print("Ufff... Thanks!")
		self.__pass_time()

	def play(self):
		print("How many hours do you want to play with your critter?")
		print("(The recommended amount is 3 hours or more.)")
		fun = int(input("Your amount of time: "))
		
		self.boredom -= fun
		if self.boredom < 0:
			self.boredom = 0

		print("Uiiii!")
		self.__pass_time()


# Main part
def main():
	crit_name = input("How will you name your critter? ")
	crit = Critter(crit_name)

	choice = None
	while choice != "0":
		print(
		"""
		Critter Caretaker
		0 - Quit
		1 - Find out about the critter\'s feeling
		2 - Feed the critter
		3 - Play with the critter
		""")
		choice = input("Your choice: ")
		print()

		# Quit.
		if "0" == choice:
			print("Bye.")
		
		# Find out about critter's feeling.
		elif "1" == choice:
			crit.talk()
		
		# Feed the critter.
		elif "2" == choice:
			crit.eat()
		
		# Play with the critter.
		elif "3" == choice:
			crit.play()

		# Unknown user input.
		else:
			print("Sorry, there is no item", choice, "in the menu.")


# Start the program.
main()
input("\n\nPress the key <Enter> to exit.")
