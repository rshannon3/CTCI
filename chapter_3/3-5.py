"""
3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
Hints:# 15, #32, #43
"""

import sys
import random

def sort_stack(s1):
	s2 = []
	tmp = None

	while len(s1) > 0:
		tmp = s1.pop()
		while len(s2) > 0 and tmp > s2[-1]:
			s1.append(s2.pop())
		s2.append(tmp)
	return s2


if len(sys.argv) == 1:
	print("Usage: python 3-5.py size")
	print("""*****Problem Description*****\n
	3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
	an additional temporary stack, but you may not copy the elements into any other data structure
	(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
	Hints:# 15, #32, #43
	""")
else:
	n = int(sys.argv[1])
	nums = []
	for i in range(0, n):
		nums.append(i)
	print("Unsorted: ")
	random.shuffle(nums)
	print(nums)
	print("Sorted: ")
	print(sort_stack(nums))
