"""
10.2 Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to
each other.
Hints: #717, #182, #263, #342
"""
import sys


def anagram_sort(s):
	alph = {}
	for word in s:
		sorted = list(word)
		sorted.sort()
		sorted = str(sorted)
		if sorted in alph:
			alph[sorted].append(word)
		else:
			alph[sorted] = [word]
	ret = []
	#print(alph)
	for key,value in alph.items():
		for item in value:
			ret.append(item)
	return ret




words = ["car", "rac", "something", "nothing", "arc"]
print(words)
print("Sorted by anagrams:")
print(anagram_sort(words))
