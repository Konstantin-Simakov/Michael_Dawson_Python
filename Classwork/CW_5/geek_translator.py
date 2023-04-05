# geek_translator.py
# Demonstrates using dictionaries

geek = {"404": "clueless. From the web error message 404, meaning page not found.", 
		"Googling": "searching the Internet for background information on a person.", 
		"Keyboard Plaque": "the collection of debris found in computer keyboards.", 
		"Link Rot": "the process by which web page links become obsolete.", 
		"Percussive Maintenance": "the act of striking an electronic device to make it work.", 
		"Uninstalled": "being fired. Especially popular during the dot-bomb era."}

choice = None
while choice != "0":
	print(
	"""
	Geek Translator

	0 - Quit
	1 - Look up a Geek Term
	2 - Add a Geek Term
	3 - Redefine a Geek Term
	4 - Delete a Geek Term

	"""
	)
	choice = input("Choice: ")
	print()

	# Exit
	if "0" == choice:
		print("Goodbye!")

	# Look up a definition
	elif "1" == choice:
		term = input("What term do you want me to translate? ")
		if term in geek:
			definition = geek[term]
			print("\n", term, "means", definition)
		else:
			print("\nSorry, I don\'t know", term)

	# Add a term-definition pair
	elif "2" == choice:
		term = input("What term do you want me to add? ")
		if term not in geek:
			definition = input("What\'s the definition? ")
			geek[term] = definition
			print("\n", term, "has been added.")
		else:
			print("\nThat term already exists! Try redefining it.")

	# Redefine an existing term
	elif "3" == choice:
		term = input("What term would you like to redefine? ")
		if term in geek:
			definition = input("What\'s the new definition? ")
			geek[term] = definition
			print("\n", term, "has been redefined.")
		else:
			print("That term doesn\'t exist. Try adding it.")

	# Delete a term-definition pair
	elif "4" == choice:
		term = input("What term would you like to delete? ")
		if term in geek:
			del geek[term]
			print("\nOkay, I deleted", term)
		else:
			print("\nI can\'t do that!", term, "doesn\'t exist in the dictionary.")

	# Some unkown choice
	else:
		print("\nSorry, but", choice, "isn\'t a valid choice.")

input("\n\nPress the key <Enter> to exit.")
