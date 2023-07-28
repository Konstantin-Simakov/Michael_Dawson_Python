# classy_critter.py
# Demonstrates attributes of a class and its static methods.

class Critter(object):
	'''Virtual pet.'''
	total = 0

	@staticmethod
	def status():
		print("\nTotal critters now are", Critter.total)

	def __init__(self, name):
		print("The new critter has been born!")
		self.name = name
		
		Critter.total += 1


# Main part
print("I find the attribute value Critter.total of the class:", end=" ")
print(Critter.total)

print("\nCreate critters.")
crit_1 = Critter("critter 1")
crit_2 = Critter("critter 2")
crit_3 = Critter("critter 3")
Critter.status()

print("\nI access for a class attribute through an object:", end=" ")
print(crit_1.total)

input("\n\nPress the key <Enter> to exit.")
