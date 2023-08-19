# playing_cards.py
# Demonstrates combination of objects.


class Card(object):
	''' One playing card. '''
	RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
	SUITS = ("c", "d", "h", "s")

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		res = self.rank + self.suit

		return res


class Hand(object):
	''' "Hand": a set of cards in the hands of one player.  '''
	def __init__(self):
		self.cards = []

	def __str__(self):
		if self.cards:
			res = ""
			for card in self.cards:
				res += str(card) + " "
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


# Main part
card_1 = Card(rank="A", suit="c")
print("Display to the screen the card object:")
print(card_1)

card_2 = Card(rank="2", suit="c")
card_3 = Card(rank="3", suit="c")
card_4 = Card(rank="4", suit="c")
card_5 = Card(rank="5", suit="c")
print("\nDisplay four more cards:")
print(card_2)
print(card_3)
print(card_4)
print(card_5)

my_hand = Hand()
print("\nDisplay cards that I have before the deal:")
print(my_hand)

my_hand.add(card_1)
my_hand.add(card_2)
my_hand.add(card_3)
my_hand.add(card_4)
my_hand.add(card_5)
print("\nDisplay five cards that I have in the hands:")
print(my_hand)

your_hand = Hand()
my_hand.give(card_1, your_hand)
my_hand.give(card_2, your_hand)
print("\nI gave you the first two of my cards.")
print("Now you have in your hand:")
print(your_hand)
print("And in my hand:")
print(my_hand)

my_hand.clear()
print("\nIn my hand after I folded all my cards:")
print(my_hand)

input("\n\nPress the key <Enter> to exit.")
