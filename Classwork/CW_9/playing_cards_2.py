# playing_cards_2.py
# Demonstrates extending a class through inheritance.


class Card(object):
	""" One playing card. """
	RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
	SUITS = ("c", "d", "h", "s")

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		res = self.rank + self.suit

		return res


class Hand(object):
	""" 'Hand': a set of cards in the hands of one player.  """
	def __init__(self):
		self.cards = []

	def __str__(self):
		if self.cards:
			res = "\n"
			for i in range(len(self.cards)):
				res += str(self.cards[i]) + "\t"
				if i % len(Card.RANKS) == (len(Card.RANKS) - 1):
					res += "\n"
		else:
			res = "<empty>"

		return res

	def clear(self):
		self.cards = []

	def add(self, card):
		self.cards.append(card)

	def give(self, card, other_hand):
		self.cards.remove(card)
		other_hand.add(card)


class Deck(Hand):
	""" A deck of playing cards. """
	
	def populate(self):
		self.cards = []
		for suit in Card.SUITS:
			for rank in Card.RANKS:
				self.add(Card(rank, suit))

	def shuffle(self):
		import random
		random.shuffle(self.cards)

	def deal(self, hands, per_hand=1):
		for _ in range(per_hand):
			for hand in hands:
				if self.cards:
					top_card = self.cards[0]
					self.give(top_card, hand)
				else:
					print("Cannot deal: cards ended!")


# Main part
deck_1 = Deck()
print("Create a new deck.")
print("Here is it:")
print(deck_1)

deck_1.populate()
print("\n\nThere are cards in the deck.")
print("Here it is now:")
print(deck_1)

deck_1.shuffle()
print("\n\nThe deck is shuffled.")
print("Here is it now:")
print(deck_1)

my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]
deck_1.deal(hands, per_hand=5)
print("\nYou and I were dealt 5 cards each.")
print("My hand:")
print(my_hand)
print("Your hand:")
print(your_hand)
print("Remain in the deck:")
print(deck_1)

deck_1.clear()
print("\n\nThe deck is cleared.")
print("Here is it now:", deck_1)

input("\n\nPress the key <Enter> to exit.")
