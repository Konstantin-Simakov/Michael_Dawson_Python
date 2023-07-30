# exercise3.py
# 
# Virtual pet that user takes care about.
# With the secret item in the menu that displays 
# values of all object attributes without according prompt.
# 


class Critter(object):
	'''Virtual pet.'''

	def __init__(self, name, hunger=0, boredom=0):
		self.name = name
		self.hunger = hunger
		self.boredom = boredom

	def __str__(self):
		res = "Critter\'s name: " + self.name + "\n"
		res += "Its hunger level: " + str(self.hunger) + "\n"
		res += "Its boredom level: " + str(self.boredom) + "\n"

		return res

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
		choice = input("Your choice: ").lower()
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

		# Secret code to display the object content. 
		elif "status" == choice:
			print("You entered the secret code!\n")
			print(crit)

		# Unknown user input.
		else:
			print("Sorry, there is no item", choice, "in the menu.")


# Start the program.
main()
input("\n\nPress the key <Enter> to exit.")
