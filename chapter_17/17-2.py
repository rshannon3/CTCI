"""
17 .2 Shuffle: Write a method to shuffle a deck of cards. It must be a perfect shuffle-in other words, each
of the 52! permutations of the deck has to be equally likely. Assume that you are given a random
number generator which is perfect.
Hints: #483, #579, #634
"""
import random

def shuffle(cards):
	rand_range = len(cards)-1
	ret = []
	while rand_range > -1:
		i = random.randint(0,rand_range)
		ret.append(cards.pop(i))
		rand_range -= 1
	return ret


cards = list(range(0,52))
print(shuffle(cards))
