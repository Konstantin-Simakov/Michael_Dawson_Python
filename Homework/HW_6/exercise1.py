# exerise1.py
# Improvement of the ask_number() function.


# Glgobal constants
X = "X"
O = "O"
EMPTY = " "
TIE = "Tie"
NUM_SQUARES = 9


def display_instruct():
	''' Displays instruction for a plyaer on the screen. '''
	print(
		"""
	Welcome to the ring of the greatest intelligent competitions of all the times.
	Your brain and my processor will fight on the tic-tac-toe board.
	To make a move enter a number from 0 to 8. 
	The numbers uniquely correspond to the board fields as shown below:
	0 | 1 | 2
	---------
	3 | 4 | 5
	---------
	6 | 7 | 8
	Prepare to fight, you pathetic human. The decisive battle is about to begin.
		"""
	)


def ask_yes_no(question):
	''' Makes a question with answer 'Y' or 'n'. '''
	response = None
	while response not in ("y", "n"):
		response = input(question).lower()

	return response


def ask_number(question="Your move. Choose one of the fields (0-8): ", 
			   low=0, high=NUM_SQUARES, step=1):
	''' Asks you to enter the number from a 
		range from low to (high-1) inclusive. 

	'''
	response = None
	while response not in range(low, high, step):
		response = int(input(question))

	return response


def pieces():
	''' Specifies the ownership of the first move. '''
	go_first = ask_yes_no("Do you want to go first? (y/n) ")
	if "y" == go_first:
		print("\nWell, I give you a head start. Play with crosses.")
		human = X
		computer = O
	else:
		print("\nYour luck will destroy you... I\'ll start.")
		computer = X
		human = O

	return computer, human


def new_board():
	''' Creates a new board. '''
	board = []
	for _ in range(NUM_SQUARES):
		board.append(EMPTY)

	return board


def display_board(board):
	''' Displays the board on the screen. '''
	print("\n\t", board[0], "|", board[1], "|", board[2])
	print("\t", "---------")
	print("\t", board[3], "|", board[4], "|", board[5])
	print("\t", "---------")
	print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
	''' Creates the list of allowed moves. '''
	moves = []
	for square in range(NUM_SQUARES):
		if EMPTY == board[square]:
			moves.append(square)

	return moves


def winner(board):
	''' Defines the winner in the game. '''
	WAYS_TO_WIN = (
		(0, 1, 2),
		(3, 4, 5),
		(6, 7, 8),
		(0, 3, 6),
		(1, 4, 7),
		(2, 5, 8),
		(0, 4, 8),
		(2, 4, 6)
	)

	game = False			# Winner is not defined.
	for row in WAYS_TO_WIN:
		if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
			winner = board[row[0]]
			game = True		# Winner is defined.
			break

	if EMPTY not in board:	# The game is a tie.
		winner = TIE
	elif not game:			# The game is not ended yet.
		winner = None

	return winner			# Winner is "X" or "O".


def human_move(board, human):
	''' Gets a human move. '''
	legal = legal_moves(board)
	move = None
	while move not in legal:
		move = ask_number()
		if move not in legal:
			print("\nYou funny human! This field has already taken. Choose another.\n")
	print("OK...")

	return move


def computer_move(board, computer, human):
	''' Makes a move for the computer opponent. '''
	
	# Create a working copy of the board because
	# the function will change some values in the list.
	board = board[:]

	# Squares from the best to the worth.
	BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
	print("I will choose the move", end=" ")

	winner_found = False
	for move in legal_moves(board):
		board[move] = computer
		# If the computer could win with next move, choose this move.
		if winner(board) == computer:
			print(move)
			comp_move = move
			winner_found = True
			break
		
		# After checking, we will cancel the changes made.
		board[move] = EMPTY

	if not winner_found:
		for move in legal_moves(board):
			board[move] = human
			# If the human could win with next move, block this move.
			if winner(board) == human:
				print(move)
				comp_move = move
				winner_found = True
				break
			
			# After checking, we will cancel the changes made.
			board[move] = EMPTY

	# Since neither side can win on the next move, 
	# let's choose the best of the available squares for the computer.
	if not winner_found:
		for move in BEST_MOVES:
			if move in legal_moves(board):
				print(move)
				comp_move = move
				winner_found = True
				break

	return comp_move


def next_turn(turn):
	''' Performs a move turn. '''
	if X == turn:
		move = O
	else:
		move = X

	return move


def congrat_winner(the_winner, computer, human):
	''' Displays results and congratulates the game winner. '''
	if the_winner != TIE:
		print("Three", the_winner, "in a row!\n")
	else:
		print("Tie!\n")

	if the_winner == computer:
		print("As I predicted, the victory once again remained with me.\n" \
			"Here is another argument in favor of the fact that computers", 
			"are superior to people in absolutely everything.")
	elif the_winner == human:
		print("Oh no, it can\'t be!", 
			"Have you somehow managed to outsmart me, you pitiful human being?\n" \
			"I swear I\'m a computer, I\'ll never let that happen again!")
	elif TIE == the_winner:
		print("You are incredibly lucky, my friend, you managed to bring the game to a draw.\n" \
			"Rejoice in today\'s success!", 
			"Tomorrow you are not destined to repeat it.")


def main():
	''' Main program '''
	display_instruct()

	# Initial values
	computer, human = pieces()
	# First move
	turn = X
	board = new_board()
	display_board(board)

	# While the game is not ended
	while not winner(board):
		if turn == human:
			move = human_move(board, human)
			board[move] = human
		else:
			move = computer_move(board, computer, human)
			board[move] = computer

		display_board(board)
		turn = next_turn(turn)

	the_winner = winner(board)
	congrat_winner(the_winner, computer, human)


# Program launch (global scope only).
main()
input("\n\nPress the key <Enter> to exit.")
