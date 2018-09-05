"""
1.6
String Compression: Implement a method to perform basic string compression using repeated characters. For example aaabccdd becomes a3b1c2d2. If the compressed string is longer, you should output the original. You can assume that the string only has uppercase and lowercase letters.
"""
import sys

def string_compression(s):
	out = ""
	i = 0
	while i < len(s):
		j = i
		while j < len(s) - 1 and s[j+1] == s[j]:
			j += 1
		out = out + s[i] + str(j - i + 1)
		i = j + 1
	return out if len(out) < len(s) else s

if len(sys.argv) == 1:
	print("Usage: python 1-6.py string_to_compress")
	print("*****Problem Description*****\nString Compression: Implement a method to perform basic string compression using repeated characters. For example aaabccdd becomes a3b1c2d2. If the compressed string is longer, you should output the original. You can assume that the string only has uppercase and lowercase letters.")
else:
	print(str("Original: " + sys.argv[1]) + "\nCompressed: " + string_compression(sys.argv[1]))
