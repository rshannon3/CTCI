"""
16.26 Calculator:
Given an arithmetic equation consisting of positive integers, +, -, * and / (no parentheses),
compute the result.
"""

import sys

def calculator(expression):
	#Searchable strings
	digit = "0123456789"
	mul = "*/"
	add = "+-"
	#Buffers for holding operaters while processing the operands
	add_holder = None
	mul_holder = None
	#Handles multi character digits
	digit_holder = ""
	#Convert the expression to postfix notation
	i = 0
	postfix = []
	while i < len(expression):
		if expression[i] in digit:
			digit_holder = digit_holder + expression[i]
		elif digit_holder != "":
			postfix.append(digit_holder)
			if mul_holder != None:
				postfix.append(mul_holder)
				mul_holder = None
			digit_holder = ""
		if expression[i] in add:
			if add_holder != None:
				postfix.append(add_holder)
			add_holder = expression[i]
		elif expression[i] in mul:
			mul_holder = expression[i]
		i+=1
	#Add in any leftovers
	if digit_holder != "":
		postfix.append(digit_holder)
	if mul_holder != None:
		postfix.append(mul_holder)
	if add_holder != None:
		postfix.append(add_holder)

	print(postfix)
	#Flip the stack
	postfix = postfix[::-1]
	print(postfix)

	#Solve postfix
	tmp_stack = []
	while(len(postfix) > 0):
		tmp_stack.append(postfix.pop())
		print(tmp_stack)
		result = 0
		#Peek equivalent. If the top is an operator, pop it and the next two vals to reduce
		if tmp_stack[-1] in mul or tmp_stack[-1] in add:
			operator = tmp_stack.pop()
			operand1 = tmp_stack.pop()
			operand2 = tmp_stack.pop()
			if operator == "+":
				result = float(operand2) + float(operand1)
			elif operator == "-":
				result = float(operand2) - float(operand1)
			elif operator == "*":
				result = float(operand2) * float(operand1)
			elif operator == "/":
				result = float(operand2) / float(operand1)
			tmp_stack.append(result)

	return tmp_stack.pop()

if len(sys.argv) == 1:
	print("Usage: python 16-26.py \"expresion\"")
	print("""*****Problem Description*****\n"
	16.26 Calculator:
	Given an arithmetic equation consisting of positive integers, +, -, * and / (no parentheses),
	compute the result.
	""")
else:
	print(calculator(str(sys.argv[1])))
