# simple_critter.py
# Demonstrates the simplest class and object.

class Critter(object):
	'''Virtual pet'''

	def talk(self):
		print("Hello. I am a critter, an instance of Critter class.")


# Main part
crit = Critter()
crit.talk()

input("\n\nPress the key <Enter> to exit.")
