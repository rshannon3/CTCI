"""
16.9 Operations: Write methods to implement the multiply, subtract, and divide operations for integers.
The results of all of these are integers. Use only the add operator.
Hints: #572, #600, #613, #648
"""

def add(op1, op2):
	return op1 + op2

def subtract(op1, op2):
	return add(op1, multiply(op2, -1))

def multiply(op1, op2):
	iter = -1
	if  op2 < 0:
			iter = 1
			cp = 0
			if op1 <0:
				flip = 1
			else:
				flip = -1
			while op1 != 0:
				cp = add(cp, flip)
				op1 = add(op1, flip)
			op1 = cp
	result = 0
	while op2 != 0:
		result = add(result, op1)
		op2 = add(op2, iter)
	return result


def divide(op1, op2):
	quotient = 0
	if abs(op1) < abs(op2):
		return 0
	if op1 > 0:
		while op1 > 0:
			if op2 > 0:
				op1 = subtract(op1, op2)
				quotient = add(quotient, 1)
			else:
				op1 = add(op1, op2)
				quotient = add(quotient, -1)
	else:
		while op1 < 0:
			if op2 > 0:
				op1 = add(op1, op2)
				quotient = add(quotient, -1)
			else:
				op1 = subtract(op1, op2)
				quotient = add(quotient, 1)
	return quotient


op1 = -5
op2 = 10
print("Adding " + str(op1) + " + " + str(op2) + " = "  + str(add(op1,op2)))
print("Multiplying " + str(op1) + " * " + str(op2) + " = " + str(multiply(op1,op2)))
print("Subtracting " + str(op1) + " - " + str(op2) + " = "  + str(subtract(op1,op2)))
print("Dividing " + str(op1) + " / " + str(op2) + " = "  + str(divide(op1,op2)))
