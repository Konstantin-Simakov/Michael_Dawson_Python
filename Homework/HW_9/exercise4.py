# exercise4.py
# 
# A simple object-oriented game in which 
# the player can change their location 
# by moving to one of the places closest to the current one.
# 

# For sys.exit()
import sys
# For games.ask_number()
import games


SPACE = " "
QUIT = "quit"


class Board():
	""" A board for a player. """
	# size means a number of cells on the one of sides on the board.
	def __init__(self, size, player):
		self.size = size

		# Create an empty board.
		self.board = []
		for _ in range(self.size**2):
			self.board.append(SPACE)

		self.board[player.location] = player.piece

	def __str__(self):
		res = "\n"
		for i in range(self.size):
			res += "\t\t"
			for j in range(self.size):
				res += "-----"
			res += "\n"

			res += "\t\t"
			for j in range(self.size):
				res += "|" + self.board[i * self.size + j].center(4)
			res += "|\n"
		
		res += "\t\t"
		for j in range(self.size):
			res += "-----"
		res += "\n\n"

		return res

	def change_location(self, player, position):
		position = player.make_move(position, self.size)

		self.board[position] = player.piece
		self.board[player.location] = SPACE
		player.location = position


class Player():
	""" The player is like a piece on the board 
		(asterisk by default). 
	"""
	def __init__(self, location=0, piece="*"):
		self.piece = piece
		self.location = location

	# size means a number of cells on the one of sides on the board.
	def __legal_moves(self, size):
		legals = []

		# 1. When we can make only 2 moves.
		# Upper left corner:
		if 0 == self.location:
			legals = [self.location + 1, self.location + size]
		# Upper right corner:
		elif (size - 1) == self.location:
			legals = [self.location - 1, self.location + size]
		# Lower left corner:
		elif (size**2 - size) == self.location:
			legals = [self.location + 1, self.location - size]
		# Lower right corner:
		elif (size**2 - 1) == self.location:
			legals = [self.location - 1, self.location - size]

		# 2. When we can make 3 moves.
		# Upper side: [1; size - 2] with step=1.
		elif self.location in range(1, size - 1):
			legals = [self.location + 1, self.location - 1, self.location + size]
		# Lower side: [size**2 - (size-1); size**2 - 2] with step=1.
		elif self.location in range(size**2 - (size-1), size**2 - 1):
			legals = [self.location + 1, self.location - 1, self.location - size]
		# Left side: [size; size**2 - 2*size] with step=size.
		elif self.location in range(size, size**2 - 2*size + 1, size):
			legals = [self.location + 1, self.location + size, self.location - size]
		# Right side: [2*size - 1; size**2 - size - 1] with step=size.
		elif self.location in range(2*size - 1, size**2 - size, size):
			legals = [self.location - 1, self.location + size, self.location - size]

		# 3. When we can make 4 moves.
		else:
			legals = [self.location + 1, self.location - 1, self.location + size, self.location - size]

		return legals

	def make_move(self, position, size):
		legal_moves = self.__legal_moves(size)
		while position not in legal_moves:
			position = input("You cannot move to this position. Your move: ")
			if QUIT == position:
				input("\n\nPress the key <Enter> to exit.")
				sys.exit()

			position = int(position)

		return position


def display_instruct(size):
	""" Display instrucions of the game. """
	print("This is a board on which you can make moves with numbers from 0 to", size**2 - 1, 
			"as specified below.")
	res = "\n"
	for i in range(size):
		res += "\t\t"
		for j in range(size):
			res += "-----"
		res += "\n"

		res += "\t\t"
		for j in range(size):
			res += "|" + str(i*size + j).center(4)
		res += "|\n"
	
	res += "\t\t"	
	for j in range(size):
		res += "-----"
	res += "\n\n"
	
	print(res)


def main():
	# Greeting and instructions.
	print("\tWelcome to the \'Robot\' game.\n\n")
	size = games.ask_number("Enter a size of one side of the game board (2 - 10): ", 2, 10+1)
	display_instruct(size)

	# Start the game.
	start_pos = games.ask_number("Enter a start location of your piece (0 - " + str(size**2 - 1) + "): ", 
			0, size**2)
	player = Player(start_pos)
	board = Board(size, player)
	print(board)

	print("\nYou may enter", QUIT, "to finish the game.\n")
	next_pos = None
	next_pos = input("Enter the next position you want to be in (0 - " + str(size**2 - 1) + "): ")
	while next_pos != QUIT:
		next_pos = int(next_pos)
		board.change_location(player, next_pos)
		print(board)

		next_pos = input("Enter the next position you want to be in (0 - " + str(size**2 - 1) + "): ")


# Main part.
main()
input("\n\nPress the key <Enter> to exit.")
