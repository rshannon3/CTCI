"""
1.8
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
"""
import sys


def zero_matrix(mat):
	rows = []
	cols = []
	for r in range(0, len(mat)):
		for c in range(0, len(mat[r])):
			if mat[r][c] == 0:
				rows.append(r)
				cols.append(c)
	for r in range(0, len(mat)):
		for c in range(0, len(mat[r])):
			if r in rows or c in cols:
				mat[r][c] = 0
	return mat

def print_matrix(mat):
	for r in range(0, len(mat)):
		print(mat[r])
"""
if len(sys.argv) == 1:
	print("Usage: python 1-8.py")
	print("*****Problem Description*****\nWrite an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.")
"""
mat = [[1,0], [0,1]]
#mat = [[1 , 2, 3, 0, 5], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
print("Matrix before: ")
print_matrix(mat)
print("\nMatrix after: ")
print_matrix(zero_matrix(mat))
