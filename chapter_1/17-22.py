"""
17.22
"""
import sys

def word_transformer(w1, w2):

	with open('google-10000-english.txt') as f:
		dict = {}
		for word in f:
			dict[word.strip()] = None
		w1 = list(w1)
		w2 = list(w2)
		i = 0
		print("Starting word = " + "".join(w1))
		print("Target word = " + "".join(w2) + "\n")
		while w1 != w2:
			if i >= len(w1):
				print("Could not find a transformation for " + "".join(w1) + " in dictionary. Exiting...")
				exit()
			elif w1[i] == w2[i]:
				i += 1
				continue
			else:
				guess = w1.copy()
				guess[i] = w2[i]
				if "".join(guess) in dict:
					w1 = guess
					i = 0
					print("Transforming word = " + "".join(w1))
					print("Target word = " + "".join(w2) + "\n")
				else:
					i += 1

		print("Words are equal, exiting...")

if len(sys.argv) == 1:
	print("Usage: python 17-22.py w1 w2")
	print("*****Problem Description*****\n")
else:
	if len(sys.argv[1]) != len(sys.argv[2]):
		print("Error, the words are not of equal length")
		exit()
	word_transformer(sys.argv[1], sys.argv[2])
