# exerise4.py
# Improvement of the computer_move() function.


# Glgobal constants
X = "X"
O = "O"
EMPTY = " "
TIE = "Tie"
NUM_SQUARES = 9
# Squares from the best to the worth.
BEST_MOVES = (4, 2, 8, 6, 0, 1, 3, 5, 7)
# Ways to win from the best to the worth.
WAYS_TO_WIN = (
		(0, 4, 8),		# 0
		(2, 4, 6),		# 1
		(0, 1, 2),		# 2
		(3, 4, 5),		# 3
		(6, 7, 8),		# 4
		(0, 3, 6),		# 5
		(1, 4, 7),		# 6
		(2, 5, 8)		# 7
)


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
	''' Asks you to enter the number from 
	a range from low to (high-1) inclusive. 

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
	
	# Winner is not defined.
	game = False			
	for row in WAYS_TO_WIN:
		if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
			winner = board[row[0]]
			# Winner is defined.
			game = True		
			break

	# The game is a tie.
	if EMPTY not in board and not game:
		winner = TIE
	# The game is not ended yet.
	elif not game:
		winner = None

	return winner


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


def is_empty(board):
	''' Checking if the board is empty. '''
	empty = True
	legal = legal_moves(board)
	if len(legal) != NUM_SQUARES:
		empty = False

	return empty


def calc_move(board, computer, human):
	''' Returns move to win if it is for the computer opponent
	else returns None.

	Defines the move for winning for the computer opponent.
	Helper function for computer_move() function.

	'''
	legal = legal_moves(board)
	# For error checking.
	move = None

	# First turn calculating for the computer
	if is_empty(board) and X == computer:
		move = BEST_MOVES[0]

	# Process the situations when computer begins playing as the second player
	elif (O == computer and len(legal) == NUM_SQUARES-1 and 
			board[BEST_MOVES[0]] == human):
		if board[BEST_MOVES[0]] == human:
			move = BEST_MOVES[1]
		else:
			move = BEST_MOVES[0]
	
	# Improvement of the strategy of the computer opponent.
	elif (O == computer and len(legal) == NUM_SQUARES-1 and 
			(human == board[BEST_MOVES[1]] or human == board[BEST_MOVES[2]] or 
			human == board[BEST_MOVES[3]] or human == board[BEST_MOVES[4]])):
		# Case #1
		if human == board[BEST_MOVES[1]]:
			move = BEST_MOVES[3]
		# Case #2
		elif human == board[BEST_MOVES[2]]:
			move = BEST_MOVES[4]
		# Case #3
		elif human == board[BEST_MOVES[3]]:
			move = BEST_MOVES[1]
		# Case #4
		elif human == board[BEST_MOVES[4]]:
			move = BEST_MOVES[2]

	# Second and more turn calculating for the computer
	else:
		for row in WAYS_TO_WIN:
			if (board[row[0]] == board[row[1]] == EMPTY and board[row[2]] == computer):
				move = row[0]
				break
			elif (board[row[0]] == board[row[2]] == EMPTY and board[row[1]] == computer):
				move = row[0]
				break
			elif (board[row[1]] == board[row[2]] == EMPTY and board[row[0]] == computer):
				move = row[2]
				break

	return move


def computer_move(board, computer, human):
	''' Makes a move for the computer opponent. '''
	
	# Create a working copy of the board because
	# the function will change some values in the list.
	board = board[:]
	legal = legal_moves(board)
	# For error checking.
	comp_move = None
	
	# Pre-choosing message of the computer opponent.
	print("I will choose the move", end=" ")

	winner_found = False
	for move in legal:
		board[move] = computer
		# If the computer could win with next move, choose this move.
		if winner(board) == computer:
			comp_move = move
			winner_found = True
			break
		# After checking, we will cancel the changes made.
		board[move] = EMPTY

	if not winner_found:
		for move in legal:
			board[move] = human
			# If the human could win with next move, block this move.
			if winner(board) == human:
				comp_move = move
				winner_found = True
				break			
			# After checking, we will cancel the changes made.
			board[move] = EMPTY

	# Since neither side can win on the next move, 
	# let's choose a move from the available squares for the computer to win.
	if not winner_found:
		comp_move = calc_move(board, computer, human)
		if comp_move != None:
			winner_found = True

	# As a last resort, use the "best" possible move.
	if not winner_found:
		for move in BEST_MOVES:
			if move in legal:
				comp_move = move
				winner_found = True
				break

	print(comp_move)

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
		print("As I predicted, the victory once again remained with me.\n" +
			"Here is another argument in favor of the fact that computers", 
			"are superior to people in absolutely everything.")
	elif the_winner == human:
		print("Oh no, it can\'t be!", 
			"Have you somehow managed to outsmart me, you pitiful human being?\n" +
			"I swear I\'m a computer, I\'ll never let that happen again!")
	elif TIE == the_winner:
		print("You are incredibly lucky, my friend, you managed to bring the game to a draw.\n" +
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

	# Define the winner and give congratulations.
	the_winner = winner(board)
	congrat_winner(the_winner, computer, human)


# Program launch (global scope only).
main()
input("\n\nPress the key <Enter> to exit.")
