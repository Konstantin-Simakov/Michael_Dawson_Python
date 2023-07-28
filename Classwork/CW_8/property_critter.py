# property_critter.py
# Demonstrates properties.

class Critter(object):
	'''Virtual pet.'''

	def __init__(self, name):
		print("The new critter has been born.")
		self.__name = name

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, new_name):
		if "" == new_name:
			print("The name of a critter couldn\'t be an emtpy string.")
		else:
			self.__name = new_name
			print("The name has been changed successfully.")

	def talk(self):
		print("\nHello, my name is", self.name)


# Main part
crit = Critter("Bobik")
crit.talk()
print("My critter\'s name is", end=" ")
print(crit.name)

print("\nI try to change the critter\'s name to Murzik...")
crit.name = "Murzik"
print("My critter\'s name is", crit.name)

print("\nI try to change the critter\'s name to empty string...")
crit.name = ""
print("My critter\'s name is", crit.name)

input("\n\nPress the key <Enter> to exit.")
