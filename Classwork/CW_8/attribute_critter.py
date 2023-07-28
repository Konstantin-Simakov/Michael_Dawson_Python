# attribute_critter.py
# Demonstrates creating attributes of an instance and access to them.

class Critter(object):
	'''Virtual pet.'''

	def __init__(self, name):
		print("The new critter has been born!")
		self.name = name

	def __str__(self):
		ret_val = "An object of the Critter class.\n";
		ret_val += "name: " + self.name + "\n"

		return ret_val

	def talk(self):
		print("Hello. My name is", self.name, "\n")


# Main part
crit_1 = Critter("Bobik")
crit_1.talk()
crit_2 = Critter("Murzik")
crit_2.talk()

print("Output of the crit_1 object on the screen:")
print(crit_1)
print("Output of the crit_2 object on the screen:")
print(crit_2)

print("Direct access to the crit_1.name attribute:")
print(crit_1.name, "\n")

crit_1.name = "Gafgaf"
print("Direct access to the crit_1.name attribute:")
print(crit_1.name, "\n")

print("Direct access to the crit_2.name attribute:")
print(crit_2.name, "\n")


input("\n\nPress the key <Enter> to exit.")
