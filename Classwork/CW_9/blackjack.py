# blackjack.py
# 
# Standard 'Blackjack' game.
# From 1 to 7 players against the dealer.
# 

import cards
import games


class BJ_Card(cards.Card):
	""" A card for 'Blackjack' game. """
	ACE_VALUE = 1

	@property
	def value(self):
		if self.is_face_up:
			v = BJ_Card.RANKS.index(self.rank) + 1
			if v > 10:
				v = 10
		else:
			v = None

		return v


class BJ_Deck(cards.Deck):
	""" A deck for 'Blackjack' game. """
	def populate(self):
		for suit in BJ_Card.SUITS:
			for rank in BJ_Card.RANKS:
				self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(cards.Hand):
	""" 'Hand': the collection of cards in 'Blackjack' for 1 player. """
	def __init__(self, name):
		super().__init__()
		self.name = name

	def __str__(self):
		res = self.name + ":\t" + super().__str__()
		if self.total:
			res += "(" + str(self.total) + ")"

		return res

	@property
	def total(self):
		# If one of the cards has value equalled None, then the entire property is None.
		is_face_down = False
		for card in self.cards:
			if not card.value:
				res = None
				is_face_down = True

		# We sum up the points, counting each ace as 1 point.
		if not is_face_down:
			res = 0
			for card in self.cards:
				res += card.value
			
			# Determine if the player has an ace in his hand.
			contains_ace = False
			for card in self.cards:
				if BJ_Card.ACE_VALUE == card.value:
					contains_ace = True
			
			# If there is an ace in the hand and the total points do not exceed 11, 
			# we will consider the ace as 11 points.
			if contains_ace and res <= 11:
				# You only need to add 10, since 1 is already included in the total.
				res += (11 - 1)

		return res

	def is_busted(self):
		return self.total > 21


class BJ_Player(BJ_Hand):
	""" A player in 'Blackjack'. """
	def is_hitting(self):
		response = games.ask_yes_no("\n" + self.name + ", will you take more cards? (y/n) ")

		return "y" == response

	def bust(self):
		print(self.name, "busts.")
		self.lose()

	def lose(self):
		print(self.name, "loses.")

	def win(self):
		print(self.name, "wins.")

	def push(self):
		print(self.name, "pushes.")


class BJ_Dealer(BJ_Hand):
	""" The dealer in 'Blackjack' game. """
	def is_hitting(self):
		return self.total < 17

	def bust(self):
		print(self.name, "busts.")

	def flip_first_card(self):
		first_card = self.cards[0]
		first_card.flip()


class BJ_Game(object):
	""" The 'Blackjack' game. """
	def __init__(self, names):
		self.players = []
		for name in names:
			player = BJ_Player(name)
			self.players.append(player)
		self.dealer = BJ_Dealer("Delear")
		
		self.deck = BJ_Deck()
		self.deck.populate()
		self.deck.shuffle()

	@property
	def still_playing(self):
		sp = []
		for player in self.players:
			if not player.is_busted():
				sp.append(player)

		return sp

	def __additional_cards(self, player):
		while not player.is_busted() and player.is_hitting():
			self.deck.deal([player])
			print(player)
			if player.is_busted():
				player.bust()

	def play(self):
		# Everyone is dealt 2 cards.
		self.deck.deal(self.players + [self.dealer], per_hand=2)

		# The first card dealt to the dealer is turned face down.
		self.dealer.flip_first_card()

		for player in self.players:
			print(player)
		print(self.dealer)

		for player in self.players:
			self.__additional_cards(player)
		# The dealer's first card is turned face up.
		self.dealer.flip_first_card()

		if not self.still_playing:
			# All players are busted, we will only show the dealer's hand.
			print(self.dealer)
		else:
			# Deal additional cards to dealer.
			print(self.dealer)
			self.__additional_cards(self.dealer)

			if self.dealer.is_busted():
				# Everyone who is still in the game wins.
				for player in self.still_playing:
					player.win()
			else:
				# We compare the total points of the dealer 
				# and the players remaining in the game.
				for player in self.still_playing:

					if player.total > self.dealer.total:
						player.win()
					elif player.total < self.dealer.total:
						player.lose()
					else:
						player.push()

		# Delete all cards.
		for player in self.players:
			player.clear()
		self.dealer.clear()


def main():
	print("\t\tWelcome to the Blackjack gaming table!")
	names = []
	number = games.ask_number("How many players total? (1 - 7): ", low=1, high=(7+1))
	for _ in range(number):
		name = input("Enter player name: ")
		names.append(name)
		print()

	game = BJ_Game(names)
	again = None
	while again != "n":
		game.play()
		again = games.ask_yes_no("\nWould you like to play again? (y/n) ")


# Main part.
main()
input("\n\nPress the key <Enter> to exit.")
