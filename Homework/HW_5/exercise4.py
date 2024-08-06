# exercise3.py
# 
# 'Who is Your Dad?' program that lets the user enter the name of a male
# and produces the name of his father. 
# To make it more interesting, you can "teach" the program about 
# kinship among literary characters, historical figures and modern celebrities.
# Allow the user to add, replace, and delete son-father pairs.
# 

# Initial variables
relations = {}

print("\tWelcome to \'Who is your Dad?\' program!\n")

choice = None
while choice != 0:
	# Menu
	print(
		"""
What action do you want to choose?\n
\t\t0 - Exit
\t\t1 - Show all Son-Dad pairs
\t\t2 - Find Son-Dad pair
\t\t3 - Add Son-Dad pair
\t\t4 - Change Son-Dad pair
\t\t5 - Delete Son-Dad pair\n
		""")
	# Choice of action
	choice = int(input("Your choice: "))

	# 0 - Exit
	if 0 == choice:
		break

	# 1 - Show all Son-Dad pairs
	elif 1 == choice:
		if relations:
			for son, dad in relations.items():
				print("Son:", son, end=", ")
				print("his dad:", dad)
		else:
			print("There are no Son-Dad pairs.")
	
	# 2 - Find Son-Dad pair
	elif 2 == choice:
		son = input("Enter name of son: ").title()
		if son in relations:
			print("Son:", son, end=", ")
			print("his dad:", relations[son])
		else:
			print("There is no such Son-Dad pair. Try to add it.")

	# 3 - Add a Son-Dad pair
	elif 3 == choice:
		son = input("Enter name of son: ").title()
		while not son:
			son = input()

		if son not in relations:
			dad = input("Enter name of his dad: ").title()
			while not dad:
				dad = input()
				
			relations[son] = dad
			print("The Son-Dad pair has been added.")
		else:
			print("This Son-Dad pair already exists. Try to change it.")

	# 4 - Change a Son-Dad pair
	elif 4 == choice:
		son = input("Enter name of son: ").title()
		if son in relations:
			dad = input("Enter name of his dad: ").title()
			while not dad:
				dad = input()
			
			relations[son] = dad
			print("The Son-Dad pair has been changed.")
		else:
			print("This Son-Dad pair doesn\'t exist. Try to add it.")

	# 5 - Delete a Son-Dad pair
	elif 5 == choice:
		son = input("Enter name of son: ").title()
		
		if son in relations:
			print(son, "with his dad,", relations[son], end=", has been deleted.") 
			del relations[son]
		else:
			if not son:
				print("Entered emtpy line. There is nothing to delete.")
			else:
				print("This Son-Dad pair couldn\'t be deleted because it doesn\'t exist.")

	# Invalid choice
	else:
		print("Invalid choice. Please choose 0, 1, 2, 3 or 4.")

input("\n\nPress the key <Enter> to exit.")
