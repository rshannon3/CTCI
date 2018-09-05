"""
1.2
Check Permutation: Given two strings, write a method to determine if one is a permutation of the other.
"""
import sys

def check_permutation(s1, s2):
	return len(s1) == len(s2) and set(s1) == set(s2)


if len(sys.argv) < 3:
	print("Usage: python 1-2.py string1 string2")
	print("*****Problem Description*****\nCheck Permutation: Given two strings, write a method to determine if one is a permutation of the other.")
else:
	if check_permutation(sys.argv[1], sys.argv[2]):
		print("The strings are permutations.")
	else:
		print("The strings are not permutations")
