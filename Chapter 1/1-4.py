"""
1.4
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
"""
import sys

def palindrome_permutation(s):
	s = s.replace(" ", "")
	letter_count = {}
	for letter in s:
		if letter not in letter_count:
			letter_count[letter] = 1
		else:
			letter_count[letter] = letter_count[letter] + 1
	middle_letter = False
	for letter, count in letter_count.items():
		if count % 2 != 0:
			if len(s) % 2 == 0:
				return False
			else:
				if middle_letter:
					return False
				else:
					middle_letter = True
	return True




if len(sys.argv) != 2:
	print("Usage: python 1-4.py string")
	print("*****Problem Description*****\nPalindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. ")
else:
	print(palindrome_permutation(str(sys.argv[1])))
