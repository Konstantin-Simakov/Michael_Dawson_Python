# cards.py
# 
# Python module.
# The collection of base classes for a card game.
# 


class Card(object):
	""" A playing card. """
	RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
	SUITS = ("c", "d", "h", "s")

	def __init__(self, rank, suit, face_up=True):
		self.rank = rank
		self.suit = suit
		self.is_face_up = face_up

	def __str__(self):
		if self.is_face_up:
			res = self.rank + self.suit
		else:
			res = "XX"

		return res

	def flip(self):
		self.is_face_up = not self.is_face_up


class Hand(object):
	""" 'Hand': a collection of cards in the hand of a player. """
	def __init__(self):
		self.cards = []

	def __str__(self):
		if self.cards:
			res = ""
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
					print("Cannot deal anymore: cards ended!")


if __name__ == "__main__":
	print("This is a module that consists of cards for card games.")
	input("\n\nPress the key <Enter> to exit.")
