"""
Add Without Plus: Write a function that adds two numbers. You should not use+ or any arithmetic
operators.
Hints: #467, #544, #607, #628, #642, #664, #692, #772, #724
"""
import sys

def add_without_plus(a, b):
	"""
	Using XOR
	1+1 = 0 Carry 1
	1+0 = 1
	0+1 = 1
	0+0 = 0
	"""
	carry = False
	pow = 0
	result = 0
	while 2**pow <= max(a,b):
		mask = 2**pow
		#Grab individual bits at position pow
		a2 = mask & a
		b2 = mask & b
		if carry:
			#1 + 1 + 1 = 1 set carry
			if a2 and b2:
				carry = True
				result |= mask
			#1 + 1 = 0 carry 1
			elif a2^b2:
				carry = True
			#1 + 0 = 0 remove carry flag
			else:
				result |= mask
				carry = False
		else:
			#1 + 1 = 0 set carry
			if a2 and b2:
				carry = True
			#If no carry, just use xor
			else:
				result |= a2^b2
		pow += 1
	#handle leftover carry
	if carry:
		result |= 2**pow
	return result



if len(sys.argv) < 3:
	print("Usage: python a b")
	print("*****Problem Description*****\n\n")
else:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	print(str(a) + " + " + str(b) + " = " + str(add_without_plus(a,b)))
