"""
5.1 Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and
j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You
can assume that the bits j through i have enough space to fit all of M. That is, if
M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
EXAMPLE
Input: N 10000000000, M
Output: N = 10001001100
Hints: #137, #769, #215
"""
import sys



def insertion(n, m, i, j):
	#Create a mask to zero out the target section
	mask = len(m) * '0'
	mask = mask + "1" * (int(i))
	mask = '1' * (32 - int(j) - int(i)) + mask
	#print(bin(int(mask,2)))
	#print(bin(int(n,2)))

	#Apply mask with AND to zero out the section
	n = int(n,2) & int(mask,2)

	#Creat a mask to add M to the target section
	mask = m
	mask = mask + "0" * (int(i))
	mask = '0' * (32 - int(j) - int(i)) + mask
	#Use OR mask to only affect the target area
	n = n | int(mask,2)
	return n


if len(sys.argv) < 5:
	print("Usage: python n m i j")
	print("""*****Problem Description*****\n\n
	5.1 Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and
	j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You
	can assume that the bits j through i have enough space to fit all of M. That is, if
	M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
	example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
	EXAMPLE
	Input: N 10000000000, M
	Output: N = 10001001100
	Hints: #137, #769, #215 """)
else:
	n = sys.argv[1]
	m = sys.argv[2]
	i = sys.argv[3]
	j = sys.argv[4]

	print(bin(insertion(n, m, i, j)))
