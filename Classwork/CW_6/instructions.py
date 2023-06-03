# instructions.py
# Demonstrates how to create functions


def instructions():
	''' Displays instruction for a player on the screen. '''
	print(
		"""
	Welcome to the ring of the greatest intellectual competition of all time.
	Your brain and my processor will clash at the Tic-Tac-Toe board. 
	To make a move, enter a number from 0 to 8. 
	The numbers uniquely correspond to the board's fields - as shown below:
	0 | 1 | 2
	---------
	3 | 4 | 5
	---------
	6 | 7 | 8
	Get ready to fight, you pathetic human. The decisive battle is about to begin.
		"""
	)


# Main part of the program
print("This is the instruction for playing Tic-Tac-Toe:")
instructions()
print("It\'s the same instruction again:")
instructions()
print("I hope the meaning of the game is clear.")

input("\n\nPress the key <Enter> to exit.")
