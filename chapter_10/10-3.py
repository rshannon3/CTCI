"""
10.3 Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
number of times, write code to find an element in the array. You may assume that the array was
originally sorted in increasing order.
EXAMPLE
lnput:find5in{15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
Output: 8 (the index of 5 in the array)
"""

def rotated_search(a, e):
	if a[0] == e:
		return 0
	elif e > a[0]:
		for i in range(1, len(a)):
			if a[i] == e:
				return i
	else:
		for i in range(len(a)-1, 0, -1):
			if a[i] == e:
				return i


a = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
print(rotated_search(a, 1))
