# exercise3.py
# Improvement of the 'Blackjack' game by adding betting functionality.

# For sys.exit()
import sys
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

	# The number of total scores in a hand.
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
	def __init__(self, name, fund):
		super().__init__(name)
		self.fund = fund
		self.bet = 0
		# If a player immediately has a blackjack, 
		# then he can end the game right away or wait until it ends.
		self.game_end = False

	def place_bet(self):
		print(self.name, "\'s fund is $", self.fund, ".", sep="")

		# Get how much money the player wants to bet.
		bet = games.ask_number("Your bet (1 - " + str(self.fund) + "): $", 
				low=1, high=(self.fund + 1))
		self.bet = bet

	def clear(self):
		# The player returns to the beginning state of the game.
		super().clear()
		self.game_end = False

	def is_hitting(self):
		if self.total != 21:
			response = games.ask_yes_no("\n" + self.name + ", will you take more cards? (y/n) ")
			hit = "y" == response
		else:
			print(self.name, "has Blackjack.")
			hit = False
		
		return hit

	def bust(self):
		print(self.name, "busts.")
		self.lose()

	def lose(self):
		print(self.name, " loses $", self.bet, ".", sep="")
		self.fund -= self.bet

	# factor effects to the size of winnings.
	def win(self, factor):
		winnings = int(self.bet * factor)

		print(self.name, " wins $", winnings, ".", sep="")
		self.fund += winnings

		self.game_end = True

	def push(self):
		print(self.name, "pushes and sticks to his bet.")


class BJ_Dealer(BJ_Hand):
	""" The dealer in 'Blackjack' game. """
	def is_hitting(self):
		hit = self.total < 17
		if 21 == hit:
			print("Dealer has Blackjack.")

		return hit

	def bust(self):
		print(self.name, "busts.")

	def flip_first_card(self):
		first_card = self.cards[0]
		first_card.flip()


class BJ_Game(object):
	""" The 'Blackjack' game. """
	MAX_DECKS = 8

	def __init__(self, players):
		self.players = players
		self.dealer = BJ_Dealer("Delear")
		
		self.deck = BJ_Deck()
		self.deck.populate()
		self.deck.shuffle()

		self.decks = 0

	@property
	def still_playing(self):
		sp = []
		for player in self.players:
			if not player.is_busted():
				sp.append(player)

		return sp

	def __remove_bankrupts(self, players):
		for player in players:
			if 0 == player.fund:
				print(player.name.title(), "has no more money and leaves the gaming table.\n")
				players.remove(player)

		return players

	def __additional_cards(self, player):
		while not player.is_busted() and player.is_hitting():
			self.deck.deal([player])
			print(player)
			if player.is_busted():
				player.bust()

	def play(self):
		# If only 1 player is left and he has blackjack.
		# At the beginning of the next round, there is no such player.
		only_one_and_bj = False

		# Check if any players have no money left before the next round and remove them.
		self.players = self.__remove_bankrupts(self.players)
		# Check if there is at least 1 player in the game.
		if not self.players:
			print("No one player has money. The game is over.")
			input("\n\nPress the key <Enter> to exit.")
			sys.exit()

		# The remaining players place their bets.
		for player in self.players:
			player.place_bet()
		print()

		# Checks how many cards in the deck.
		# If the number of players multiplied by 5 is less, clear the deck, populate and shuffle it. 
		if (len(self.deck.cards) < len(self.players) * 5 and
				self.decks < BJ_Game.MAX_DECKS):
			self.decks += 1
			print("Populate and shuffle the deck...")
			self.deck.populate()
			self.deck.shuffle()

		# Everyone is dealt 2 cards.
		self.deck.deal(self.players + [self.dealer], per_hand=2)

		# The first card dealt to the dealer is turned face down.
		self.dealer.flip_first_card()

		for player in self.players:
			print(player)
		print(self.dealer)

		for player in self.players:
			self.__additional_cards(player)
			if 21 == player.total:
				answer = games.ask_yes_no("Do you want to collect your winnings immediately " + 
						"or wait until the end of the game? (y/n): ")
				if "y" == answer:
					# The player wins with a factor of 1 
					# because he took the winnings immediately.
					player.win(1)

					# If only 1 player is left and he has blackjack, 
					# end the game round with initial values 
					# for the remaining player and the dealer
					# before the next round.
					if len(self.players) == 1:
						only_one_and_bj = True
						# Or replace with:
						# 
						# player.clear()
						# self.dealer.clear()
						# return

		if not only_one_and_bj:
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
						if not player.game_end:
							# The player wins with factor 1.5
							# because he waited for the end of the game.
							player.win(1.5)
				else:
					# We compare the total points of the dealer
					# and the players remaining in the game.
					for player in self.still_playing:
						if not player.game_end:
							if player.total > self.dealer.total:
								# The player wins with factor 1.5
								# because he waited for the end of the game.
								player.win(1.5)
							elif player.total < self.dealer.total:
								player.lose()
							else:
								player.push()

		# Delete all cards and 
		# set all value to initial state before the next game round.
		for player in self.players:
			player.clear()
		self.dealer.clear()


def main():
	print("\t\tWelcome to the Blackjack gaming table!")
	players = []
	number = games.ask_number("How many players total? (1 - 7): ", low=1, high=(7+1))
	for _ in range(number):
		name = input("Enter player name: ")
		fund = int(input("Enter player fund: $"))
		print()

		player = BJ_Player(name, fund)
		players.append(player)

	game = BJ_Game(players)
	again = None
	while again != "n":
		game.play()
		again = games.ask_yes_no("\nWould you like to play again? (y/n): ")


# Main part.
main()
input("\n\nPress the key <Enter> to exit.")
