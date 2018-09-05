"""
1.1
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""
import sys

def is_unique(s):
	seen = {}
	for letter in s:
		if letter not in seen:
			seen[letter] = 1
		else:
			return False
	return True


if len(sys.argv) == 1:
	print("Usage: python 1-1.py string_to_test")
	print("*****Problem Description*****\nIs Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?")
else:
	if is_unique(sys.argv[1]):
		print(sys.argv[1] + " has all unique characters")
	else:
		print(sys.argv[1] + " does not have all unique characters")
