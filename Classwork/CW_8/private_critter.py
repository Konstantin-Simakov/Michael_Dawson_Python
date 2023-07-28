# private_critter.py
# Demonstrates private attributes and methods.

class Critter(object):
	'''Virtaul pet.'''

	def __init__(self, name, mood):
		print("The new critter has been born!")
		
		self.name = name		# Public attribute
		self.__mood = mood		# Private attribute

	def talk(self):
		print("\nMy name is", self.name)
		print("Now I fell", self.__mood, "\n")

	def __private_method(self):
		print("It is a private method.")

	def public_method(self):
		print("It is a public method.")
		self.__private_method()


# Main part
crit = Critter(name="Bobik", mood="great")

crit.talk()
crit.public_method()

input("\n\nPress the key <Enter> to exit.")
