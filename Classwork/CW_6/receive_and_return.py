# receive_and_return.py
# Demonstrates parameters and return values


def display(message):
	print(message)


def give_me_five():
	five = 5

	return five


def ask_yes_no(question):
	''' Asks a question with answer 'Y' or 'n'. '''
	
	response = None
	while response not in ("y", "n"):
		response = input(question).lower()

	return response


# Main part of the program
display("Message for you.\n")

number = give_me_five()
print("There is that the function give_me_five() returns:", number)

answer = ask_yes_no("\nPlease enter \'y\' or \'n\': ")
print("Thank you for entering", answer)

input("\n\nPress the key <Enter> to exit.")
