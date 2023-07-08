# exercise2.py
# 
# Improvement the 'Quiz' game.
# With list of records in the file: name, score - for every player.
# Using the pikling of data to file.
# 

# For pickling of data. 
import pickle
# For sys.exit() function.
import sys


def open_file(file_name, mode):
	''' Opens the file. '''
	try:
		the_file = open(file_name, mode, encoding="utf-8")
	except IOError as err_message:
		print("Couldn\'t open the file", file_name)
		the_file = 0

	return the_file


def next_line(the_file):
	''' Returns the following line of a game file in formatting form. '''
	line = the_file.readline()
	line = line.replace("/", "\n")

	return line


def next_block(the_file):
	''' Returns the following block of data from a game file. '''
	category = next_line(the_file)
	question = next_line(the_file)
	
	answers = []
	for i in range(4):
		answers.append(next_line(the_file))

	correct = next_line(the_file)
	rating = next_line(the_file)
	if correct and rating:
		correct = correct[0:len(correct) - 1]
		rating = rating[0:len(rating) - 1]
	
	explanation = next_line(the_file)

	return category, question, answers, correct, rating, explanation


def welcome(title):
	''' Greets the player and informs the game theme. '''
	print("\t\tWelcome to the game \'Quiz\'!\n")
	print("\t\t", end="")
	print(title, "\n")


def main():
	trivia_file = open_file("exercise1.txt", "r")
	title = next_line(trivia_file)
	welcome(title)

	# Output of the invormation about a previous winner 
	# in the game from the file if it exists.
	file_name = "exercise2.dat"
	scores_file = open_file(file_name, "rb")
	if scores_file:		
		name = pickle.load(scores_file)
		score = pickle.load(scores_file)
		print(name, "with", score, "scores is the previous winner.")
		scores_file.close()

	# Getting a name of a current player.
	name = input("\nEnter your name: ")
	while not name:
		name = input("Incorrect input. Try again: ")
	print("\n")

	# First block unpacking
	category, question, answers, correct, rating, explanation = next_block(trivia_file)
	score = 0
	while category:
		# Output of the block to screen.
		print(category)
		print(question)
		for i in range(4):
			print("\t", end="")
			print(i + 1, "-", answers[i])

		# Getting an answer
		answer = input("Your answer: ")

		# Checking the asnwer
		if answer == correct:
			print("\nYes!", end = " ")
			score += int(rating)
		else:
			print("\nNo.", end=" ")
		print(explanation)
		print("Score:", score, "\n\n")
		
		# Going to the next block (question).
		category, question, answers, correct, rating, explanation = next_block(trivia_file)

	trivia_file.close()
	print("This was the last question!")
	print("You have", score, "scores.")

	# Putting down of the data in the pickle file.
	scores_file = open_file(file_name, "wb")
	pickle.dump(name, scores_file)
	pickle.dump(score, scores_file)
	scores_file.close()


main()
input("\n\nPress the key <Enter> to exit.")
