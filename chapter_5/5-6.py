"""
5.6 Conversion: Write a function to determine the number of bits you would need to flip to convert
integer A to integer B.
EXAMPLE
Input: 29 (or: 11101), 15 (or: 01111)
Output: 2
Hints: #336, #369
"""
import sys

def count_bits(n):
	count = 0
	while n != 0:
		n &= (n-1)
		count+=1
	return count


def conversion(a, b):
	return count_bits(a^b)

if len(sys.argv) == 1:
	print("Usage: python a b")
	print("""*****Problem Description*****\n\n
5.6 Conversion: Write a function to determine the number of bits you would need to flip to convert
integer A to integer B.
EXAMPLE
Input: 29 (or: 11101), 15 (or: 01111)
Output: 2
Hints: #336, #369""")
else:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	print("A: " + str(format(a, '08b')))
	print("B: " + str(format(b, '08b')))
	print(str(conversion(a,b)) + " bit flips required.")
