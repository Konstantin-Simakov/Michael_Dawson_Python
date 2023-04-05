# high_scores.py
# Demonstrates list methods

# Seeds
scores = []
choice = None

# Main part of program
while choice != "0":
	print(
		"""
\tHigh Scores

\t0 - exit
\t1 - show scores
\t2 - add a score
\t3 - remove a score
\t4 - sort scores
		"""
	)
	choice = input("Your choice: ")
	print()

	# Exit
	if "0" == choice:
		print("Goodbye!")

	# List high-score table
	elif "1" == choice:
		print("High socres:")
		for score in scores:
			print(score)

	# Add a score
	elif "2" == choice:
		score = int(input("What score did you get? "))
		scores.append(score)

	# Remove a score
	elif "3" == choice:
		score = int(input("Which score would you like to remove? "))
		if score in scores:
			scores.remove(score)
		else:
			print(score, "isn\'t in the high scores list.")

	# Sort scores
	elif "4" == choice:
		scores.sort(reverse=True)

	# Unknown choice
	else:
		print("Sorry, but", choice, "isn\'t a valid choice.")

input("\n\nPress the key <Enter> to exit.")
