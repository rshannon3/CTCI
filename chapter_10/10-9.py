"""
10.9 Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in
ascending order, write a method to find an element.
"""

def matrix_search(m, e):
	row = len(m)-1
	col = 0
	while row >= 0 and col <= len(m[0]):
		if m[row][col] == e:
			return (row,col)
		elif m[row][col] > e:
			row -= 1
		else:
			col += 1
	return None

m = [[15, 20, 40, 85],
	 [20, 35, 80, 95],
	 [30, 55, 95, 105],
	 [40, 80, 100, 120]]

e = 55

print("Searching for " + str(e) + " in " )
for row in m:
	print(row)

print(matrix_search(m,e))
