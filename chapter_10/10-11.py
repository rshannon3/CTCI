"""
10.11 Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal
to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent
integers. For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an
array of integers, sort the array into an alternating sequence of peaks and valleys.
"""

def sorted_valley(a):
	a.sort()
	for i in range(1, len(a), 2):
		v = a[i-1]
		a[i-1] = a[i]
		a[i] = v
	return a

a = [5, 3, 1, 2, 3, 0, 7, 6, 10]

print("List: ")
print(a)
print("Valley Sorted: ")
print(sorted_valley(a))
