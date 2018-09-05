"""
1.5
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
"""
import sys

def one_away(s1, s2):
	if abs(len(s1) - len(s2)) > 1:
		return False
	else:
		strike = False
		for letter in s1:
			if letter not in s2:
				if strike:
					return False
				else:
					strike = True
	return True

if len(sys.argv) != 3:
	print("Usage: python 1-5.py string1 string2")
	print("*****Problem Description*****\nOne Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are on edit (or zero edits) away.")
else:
	print(sys.argv[1] + ", " + sys.argv[2] + " -> " + str(one_away(sys.argv[1], sys.argv[2])))
