# exercise4.py
# 
# Improve the program 'Who is your Dad?' (see exercise3.py) so that it was possible, 
# by entering the name of a person, to find out who his grandpa was.
# The program should still use the same dictionary with son-father pairs. 
# Consider how to include several generations in this vocabulary.
# 

# Initial variables
relations = {}

print("\tWelcome to \'Who is your Dad (and Grandpa)?\' program!\n")

choice = None
while choice != 0:
	# Menu
	print(
		"""
What action do you want to choose?\n
\t\t0 - Exit
\t\t1 - Show all Son-Dad-Grandpa trios
\t\t2 - Find Son-Dad-Grandpa trio
\t\t3 - Add Son-Dad-Grandpa trio
\t\t4 - Change Son-Dad-Grandpa trio
\t\t5 - Delete Son-Dad-Grandpa trio\n
		""")
	# Choice of action
	choice = int(input("Your choice: "))

	# 0 - Exit
	if 0 == choice:
		break

	# 1 - Show all Son-Dad-Grandpa trios
	# male_parents is a list of dad's and grandpa's names
	elif 1 == choice:
		if relations:
			for son, male_parents in relations.items():
				print("Son:", son, end=", ")
				if len(male_parents) == 1:
					print("his dad:", male_parents[0])
				else:
					print("his dad:", male_parents[0], end=", ")
					print("his grandpa:", male_parents[1])
		else:
			print("There are no Son-Dad-Grandpa trioes.")
	
	# 2 - Find Son-Dad-Grandpa trio
	elif 2 == choice:
		son = input("Enter name of son: ").title()
		if son in relations:
			print("Son:", son, end=", ")
			if len(relations[son]) == 1:
				print("his dad:", relations[son][0])
			else:
				print("his dad:", relations[son][0], end=", ")
				print("his grandpa:", relations[son][1])
		else:
			print("There is no such Son-Dad-Grandpa trio. Try to add it.")

	# 3 - Add a Son-Dad-Grandpa trio
	elif 3 == choice:
		son = input("Enter name of son: ").title()
		while not son:
			son = input()
		
		if son not in relations:
			# Input for 'dad' is necessary
			dad = input("Enter name of his dad: ").title()
			while not dad:			# Input non-empty string
				dad = input().title()
			# Input for 'grandpa' is optional; you can enter ""
			grandpa = input("Enter name of his grandpa: ").title()
			
			# Creating a list as a value of dictionary
			male_parents = []
			male_parents.append(dad)
			if grandpa:
				male_parents.append(grandpa)
			
			relations[son] = male_parents
			print("The Son-Dad-Grandpa trio has been added.")
		else:
			print("This Son-Dad-Grandpa trio already exists. Try to change it.")

	# 4 - Change a Son-Dad-Grandpa trio
	elif 4 == choice:
		son = input("Enter name of son: ").title()
		if son in relations:
			# Input for 'dad' is necessary
			dad = input("Enter name of his dad: ").title()
			while not dad:			# Input non-empty string
				dad = input().title()
			# Input for 'grandpa' is optional; you can enter ""	
			grandpa = input("Enter name of his grandpa: ").title()
			
			# Creating a list as a value of dictionary
			male_parents = []
			male_parents.append(dad)
			if grandpa:
				male_parents.append(grandpa)
			
			relations[son] = male_parents
			print("The Son-Dad-Grandpa trio has been changed.")
		else:
			print("This Son-Dad-Grandpa trio doesn\'t exist. Try to add it.")

	# 5 - Delete a Son-Dad-Grandpa trio
	elif 5 == choice:
		son = input("Enter name of son: ").title()
		if son in relations:
			if len(relations[son]) == 1:
				print(son, "with his dad,", relations[son][0], end=", has been deleted.")
			else:
				print(son, "with his dad,", relations[son][0], end=", ")
				print("and grandpa,", relations[son][1], end=", has been deleted.")
			del relations[son]		# Deleting an item of the dictionary through the key 'son'
		else:
			if not son:
				print("Entered emtpy line. There is nothing to delete.")
			else:
				print("This Son-Dad-Grandpa trio couldn\'t be deleted because it doesn\'t exist.")

	# Invalid choice
	else:
		print("Invalid choice. Please choose 0, 1, 2, 3 or 4.")

input("\n\nPress the key <Enter> to exit.")
