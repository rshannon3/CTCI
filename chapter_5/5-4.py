"""
5.4 Next Number: Given a positive integer, print the next smallest and the next largest number that
have the same number of 1 bits in their binary representation.
Hints: #747, #7 75, #242, #372, #339, #358, #375, #390
"""
import sys


def count_bits(n):
	count = 0
	while n != 0:
		n &= (n-1)
		count+=1
	return count

def next_number(num):
	count = count_bits(num)
	count_low = 0
	low = num
	while count_low != count:
		low -= 1
		if low < 0:
			low = None
			break
		count_low = count_bits(low)

	count_high = 0
	while count_high != count:
		num += 1
		count_high = count_bits(num)

	print("Next highest: " + str(num))
	if num:
		print(bin(num))
	print("Next lowest: " + str(low))
	if low:
		print(bin(low))

if len(sys.argv) == 1:
	print("Usage: python num")
	print("*****Problem Description*****\n\n")
else:
	print("Value: " + str(sys.argv[1]))
	print(bin(int(sys.argv[1])))
	next_number(int(sys.argv[1]))
