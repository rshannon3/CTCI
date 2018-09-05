"""
1.3
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the space has sufficient space at the end to hold additional characters, and that you are given the "true" length of the string. (Note: if implementing in Java, please use a character array so that you can perform this operation in place.)
"""
import sys

def urlify(s):
	return s.replace(" ", "%20")

if len(sys.argv) == 1:
	print("Usage: python 1-3.py string")
	print("*****Problem Description*****\nURLify: Write a method to replace all spaces in a string with '%20'. You may assume that the space has sufficient space at the end to hold additional characters, and that you are given the \"true\" length of the string. (Note: if implementing in Java, please use a character array so that you can perform this operation in place.)")
else:
	print(urlify(str(sys.argv[1])))
