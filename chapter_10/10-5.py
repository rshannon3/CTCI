"""
10.5 Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a
method to find the location of a given string.
"""

def sparse_search(a, s):
	mid = find_mid(a)
	if s == a[mid]:
		return mid
	if s < a[mid]:
		return sparse_search(a[0:mid], s)
	else:
		return sparse_search(a[mid+1:], s)

def find_mid(a):
	mid_guess = int(len(a)/2)
	if a[mid_guess] != "":
		return mid_guess
	else:
		for i in range(mid_guess-1, -1, -1):
			if a[i] != "":
				return i
		for i in range(mid_guess+1, len(a)):
			if a[i] != "":
				return i

test = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
test_val = "at"
print(sparse_search(test, test_val))
