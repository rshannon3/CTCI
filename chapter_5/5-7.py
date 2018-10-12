"""
5.7 Pairwise Swap: Write a program to swap odd and even bits in an integer with as few instructions as
possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
Hints: #745, #248, #328, #355
"""
import sys

def swapped(n):
	even = n & 0b0101010101
	odd = n & 0b1010101010
	return (even << 1) | (odd >> 1)

if len(sys.argv) == 1:
	print("Usage: python num")
	print("""*****Problem Description*****\n\n
5.7 Pairwise Swap: Write a program to swap odd and even bits in an integer with as few instructions as
possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
Hints: #745, #248, #328, #355""")
else:
	n = int(sys.argv[1])
	print("Num:     " + format(n, '08b'))
	print("Swapped: " + format(swapped(n), '08b'))
