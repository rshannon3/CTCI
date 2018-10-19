"""
7.1 Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would
subclass the data structures to implement blackjack.
Hints:#753, #275
"""
from random import shuffle

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __lt__(self, other):
		return self.value < other.value

	def __gt__(self, other):
		return self.value > other.value

	def __eq__(self, other):
		return self.value == other.value and self.suit == other.suit

class Deck:
	suits = ("hearts", "diamonds", "clubs", "spades")
	values = ("2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King", "Ace")
	def __init__(self):
		self.deck = []
		for suit in suits:
			for value in values:
				self.deck.append(Card(suit, value))

	def shuffle(self):
		shuffle(self.deck)

	def draw(self):
		return self.deck.pop(0)

	def insert(self, card):
		self.deck.append(card)
