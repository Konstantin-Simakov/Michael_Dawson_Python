# exercise2.py
# 
# Write a character creation program for a role-playing game. 
# The player must receive a pool of 30 points that they can spend on four attributes: 
# Strength, Health, Wisdom and Dexterity. 
# The player must be able to spend points from the pool on any attribute, 
# as well as return them to the pool.
# 

# Constants
MAX_POOL = 30

# Initial varaibles.
person = {"Strength": 0, "Health": 0, "Wisdom": 0, "Dexterity": 0}
pool = MAX_POOL

print("Welcome to \'Creator of Roler Person\'!")

choice = None
while choice != 0:
	# Output of results
	print("\nYour person has follow attributes:\n")
	for attribute in person.keys():
		print("\t\t", end="")
		print(attribute, "-", person[attribute])
	print("\n\t\tPool has", pool, "points.")

	# Menu
	print(
		"""
What action do you want to choose?\n
\t\t0 - Exit
\t\t1 - Add points to attributes
\t\t2 - Withdraw points from attributes

		""")
	# Choice of action
	choice = int(input("Your action: "))

	# 0 - Exit
	if 0 == choice:
		break

	# 1 - Add points from pool to attributes
	elif 1 == choice:
		strength = int(input("\nHow many points do you want to add for \'Strength\'? "))
		health = int(input("How many points do you want to add for \'Health\'? "))
		wisdom = int(input("How many points do you want to add for \'Wisdom\'? "))
		dexterity = int(input("How many points do you want to add for \'Dexterity\'? "))
		
		# Input validation
		while (strength + health + wisdom + dexterity > pool or
				strength < 0 or
				health < 0 or
				wisdom < 0 or
				dexterity < 0):
			print("Incorrect input. Try again.")
			strength = int(input("How many points do you want to add for \'Strength\'? "))
			health = int(input("How many points do you want to add for \'Health\'? "))
			wisdom = int(input("How many points do you want to add for \'Wisdom\'? "))
			dexterity = int(input("How many points do you want to add for \'Dexterity\'? "))

		person["Strength"] += strength
		person["Health"] += health
		person["Wisdom"] += wisdom
		person["Dexterity"] += dexterity

		pool -= strength + health + wisdom + dexterity

	# 2 - Withdraw points from attributes to pool
	elif 2 == choice:
		strength = int(input("How many points do you want to withdraw from \'Strength\'? "))
		health = int(input("How many points do you want to withdraw from \'Health\'? "))
		wisdom = int(input("How many points do you want to withdraw from \'Wisdom\'? "))
		dexterity = int(input("How many points do you want to withdraw from \'Dexterity\'? "))

		# Input validation
		if strength > person["Strength"] or strength < 0:
			strength = person["Strength"]
		if health > person["Health"] or health < 0:
			health = person["Health"]
		if wisdom > person["Wisdom"] or wisdom < 0:
			wisdom = person["Wisdom"]
		if dexterity > person["Dexterity"] or dexterity < 0:
			dexterity = person["Dexterity"]

		person["Strength"] -= strength
		person["Health"] -= health
		person["Wisdom"] -= wisdom
		person["Dexterity"] -= dexterity
		
		pool += strength + health + wisdom + dexterity

	# Invalid choice
	else:
		print("Invalid choice. Choose 0, 1 or 2.")

input("\n\nPress the key <Enter> to exit.")
