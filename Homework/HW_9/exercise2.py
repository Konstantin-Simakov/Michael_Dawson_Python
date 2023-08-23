# exercise2.py
# 
# 'War' game ('GW', 'Game War').
# Every player takes one card from the full deck of 52 cards.
# Winner is who has the biggest rank of his card.
# 

import cards
import games


class GW_Card(cards.Card):
	"""A card for 'War' game."""
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		res = self.rank + self.suit

		return res

	@property
	def value(self):
		v = GW_Card.RANKS.index(self.rank) + 1
		
		# For ace value
		if 1 == v:
			v = 14

		return v
	

class GW_Hand(cards.Hand):
	"""A hand in 'War' game."""
	def __init__(self, name):
		super().__init__()
		self.name = name

	def __str__(self):
		return self.name + ":\t" + super().__str__()

	# Hand needs a value!!!
	@property
	def total(self):
		t = 0
		for card in self.cards:
			t += card.value

		return t


class GW_Player(GW_Hand):
	"""A player in 'War' game."""
	def win(self):
		print(self.name, "won.")


class GW_Deck(cards.Deck):
	"""The deck in the 'War' game."""
	def populate(self):
		for rank in GW_Card.RANKS:
			for suit in GW_Card.SUITS:
				self.cards.append(GW_Card(rank, suit))


class GW_Game(object):
	"""The 'War' game."""
	def __init__(self, names):
		self.players = []
		for name in names:
			player = GW_Player(name)
			self.players.append(player)

		self.deck = GW_Deck()
		self.deck.populate()
		self.deck.shuffle()

	def __winners(self):
		# May be more than one winner.
		winners = []
		
		# Determines the max score.
		max_score = 0
		for player in self.players:
			if max_score < player.total:
				max_score = player.total

		# Determines players who has the max score.
		for player in self.players:
			if max_score == player.total:
				winners.append(player)

		# Displays the winners.
		for winner in winners:
			winner.win()


	def play(self):
		if len(self.deck.cards) < len(self.players):
			self.deck.clear()
			self.deck.populate()
			self.deck.shuffle()

		# Deals 1 card to each player.
		self.deck.deal(self.players)
		
		# Displays info about any player
		for player in self.players:
			print(player)
		
		# Determines and displays winners.
		self.__winners()

		# Delete all cards.
		for player in self.players:
			player.clear()


def main():
	print("\t\tWelcome to the \'War\' card game!\n\n")

	number = games.ask_number("\nHow many players total? (2-52): ", low=2, high=52)
	names = []
	for _ in range(number):
		name = input("Enter player name: ")
		names.append(name)
		print()

	game = GW_Game(names)
	again = None
	while again != "n":
		game.play()
		again = games.ask_yes_no("Would you like to play again? (y/n): ")


# Main part
main()
input("\n\nPress the key <Enter> to exit.")
