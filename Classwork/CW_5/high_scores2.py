# high_scores2.py
# Demonstrates nested sequences

scores = []
choice = None

# Main part of program
while choice != "0":
	print(
		"""
\tHigh Scores 2.0
\t0 - exit
\t1 - show scores
\t2 - add a score
		"""
	)
	choice = input("Your choice: ")
	print()

	# Exit
	if "0" == choice:
		print("Goodbye!")

	# Display high-score table
	elif "1" == choice:
		print("High Scores:")
		print("NAME\tSCORE")
		for entry in scores:
			score, name = entry
			print(name, "\t", score)

	# Add a score
	elif "2" == choice:
		name = input("Put down the player\'s name: ")
		score = int(input("Put down his score: "))
		entry = (score, name)
		scores.append(entry)
		scores.sort(reverse=True)
		scores = scores[:5]			# Keep only top 5 scores

	# Some unknown choice
	else:
		print("Sorry, but", choice, "isn\'t a valid choice.")

input("\n\nPress the key <Enter> to exit.")
