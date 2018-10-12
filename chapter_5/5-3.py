"""
5.3 Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
find the length of the longest sequence of ls you could create.
EXAMPLE
Input: 1775
Output: 8
(or: 11011101111)
Hints: #759, #226, #374, #352
"""
import sys

def flip_bit(num):
	seq_max = 0
	pow = 0
	max = [seq_max, pow]

	#Calculate the longest sequence of 1's
	while 2**pow < num:
		if num & (2**pow):
			seq_max += 1
		else:
			if max[0] < seq_max:
				max[0] = seq_max
				max[1] = pow
			seq_max = 0
		pow += 1

	#Flip the bit after longest sequence
	num |= 2**max[1]

	#Recalculate max sequence now that bit has been flipped
	pow = 0
	seq_max = 0
	while 2**pow < num:
		if num & 2**pow :
			seq_max += 1
		else:
			if max[0] < seq_max:
				max[0] = seq_max
				max[1] = pow
			seq_max = 0
		pow += 1

	return max[0]


if len(sys.argv) == 1:
	print("Usage: python num")
	print("""*****Problem Description*****\n\n
	5.3 Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code
	to find the length of the longest sequence of ls you could create.
	EXAMPLE
	Input: 1775
	Output: 8
	(or: 11011101111)
	Hints: #759, #226, #374, #352""")
else:
	print(bin(int(sys.argv[1])))
	print(flip_bit(int(sys.argv[1])))
