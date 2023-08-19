# games.py
# Demonstrates how to create a module.


class Player(object):
	""" Game participant. """
	def __init__(self, name, score=0):
		self.name = name
		self.score = score

	def __str__(self):
		res = self.name + ":\t" + str(self.score)

		return res


def ask_yes_no(question):
	""" Makes a question with answer 'yes' or 'no'. """
	response = None
	while response not in ("y", "n"):
		response = input(question).lower()

	return response


def ask_number(question, low, high):
	""" Asks to enter a number from a given range. """
	response = None
	while response not in range(low, high):
		response = int(input(question))

	return response


if __name__ == "__main__":
	print("You ran this module directly instead of importing it.")
	input("\n\nPress the key <Enter> to exit.")
