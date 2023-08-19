# playing_cards_3.py
# 
# Demonstrates inheritance of classes 
# in the part of re-definition of methods.
# 


class Card(object):
	""" One playing card. """
	RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
	SUITS = ("c", "d", "h", "s")

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		return self.rank + self.suit


class Unprintable_Card(Card):
	""" A card whose value and suit cannot be displayed. """
	def __str__(self):
		return "<cannot be displayed>"


class Positionable_Card(Card):
	""" A card that can be placed face up or face down. """
	def __init__(self, rank, suit, face_up=True):
		super(Positionable_Card, self).__init__(rank, suit)

		self.is_face_up = face_up
	
	def __str__(self):
		if self.is_face_up:
			res = super().__str__()
		else:
			res = "XX"

		return res

	def flip(self):
		self.is_face_up = not self.is_face_up


# Main part
card_1 = Card("A", "c")
card_2 = Unprintable_Card("A", "d")
card_3 = Positionable_Card("A", "h")

print("Print a Card object:")
print(card_1)
print("\nPrint a Unprintable_Card object:")
print(card_2)
print("\nPrint a Positionable_Card object:")
print(card_3)

print("Flip the Positionable_Card object.")
card_3.flip()
print("\nPrint the Positionable_Card object:")
print(card_3)

input("\n\nPress the key <Enter> to exit.")
