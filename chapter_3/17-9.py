"""
17.9 Kth Multiple:
Design an algorithm to find the kth number such that the only prime factors are 3, 5,
and 7. Note that 3, 5, and 7 do not have to be factors, but it should not have any other prime factors.
For example, the first several multiples would be (in order) 1, 3, 5, 7, 9, 15, 21.
"""

import sys

def kth_multiple(k):
	factors = [1,3,5,7]
	if k <= len(factors):
		return factors[k-1]
	while len(factors) < k:
		potential = []
		index = 1
		while index < len(factors):
			val = factors[index]
			for i in range(1, len(factors)):
				if val * factors[i] not in factors:
					potential.append(val * factors[i])
			index += 1
		factors.append(min(potential))
	print(factors)
	return factors[k-1]

if len(sys.argv) == 1:
	print("Usage: python 17-9.py k")
	print("""*****Problem Description*****\n17.9 Kth Multiple:
	Design an algorithm to find the kth number such that the only prime factors are 3, 5,
	and 7. Note that 3, 5, and 7 do not have to be factors, but it should not have any other prime factors.
	For example, the first several multiples would be (in order) 1, 3, 5, 7, 9, 15, 21.")""")
else:
	print(kth_multiple(int(sys.argv[1])))
