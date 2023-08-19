# simple_game.py
# Demonstrates module import.

import games, random


print("Welcome to the simplest game!\n")

again = None
while again != "n":
	players = []
	num = games.ask_number(question="How many paritcipants? (2 - 5): ", 
			low=2, high=5)

	for _ in range(num):
		name = input("Player name: ")
		score = random.randint(1, 100)

		player = games.Player(name, score)
		players.append(player)

	print("\nHere is results of the game:")
	for player in players:
		print(player)

	again = games.ask_yes_no("\nWould you like to play again? (y/n): ")

input("\n\nPress the key <Enter> to exit.")
