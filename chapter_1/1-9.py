"""
1.9
String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g. "waterbottle" is a rotation of erbottlewat").
"""
import sys

def is_rotation(s1, s2):
	if len(s1) != len(s2):
		return False
	i = s2.index(s1[0])
	j = 0
	while j < len(s1):
		if s1[j] != s2[i]:
			return False
		i += 1
		i %= len(s2)
		j += 1
	return True


if len(sys.argv) == 1:
	print("Usage: python 1-9.py s1 s2")
	print("*****Problem Description*****\nString Rotation: Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g. \"waterbottle\" is a notation of erbottlewat\").")
else:
	result = " is " if is_rotation(sys.argv[1], sys.argv[2]) else " is not "
	print(str(sys.argv[2]) + result + "a rotation of " + str(sys.argv[1]))
