"""
16.21 Sum Swap: Given two arrays of integers, find a pair of values (one value from each array) that you
can swap to give the two arrays the same sum.
EXAMPLE
Input: {4, 1, 2, 1, 1, 2} and {3, 6, 3, 3}
Output: {1, 3}
Hints: #545, #557, #564, #577, #583, #592, #602, #606, #635
"""

def sum_swap(a1, a2):
	sum1 = sum(a1)
	sum2 = sum(a2)
	sum_diff = sum1 - sum2
	if sum_diff % 2 == 0:
		for v1 in a1:
			for v2 in a2:
				if v1 - v2 == sum_diff / 2:
					return (v1, v2)
	else:
		return None


a1 = [4, 1, 2, 1, 1, 1]
a2 = [3, 6, 3, 3]
print(a1)
print("\tSum = " + str(sum(a1)))
print(a2)
print("\tSum = " + str(sum(a2)))
print(sum_swap(a1, a2))
