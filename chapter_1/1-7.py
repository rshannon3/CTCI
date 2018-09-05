"""
1.7 Rotated Matrix
Given an image represented  by an NxN matrix, where each pixel in the image is represented by 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""
import sys

def rotate_matrix(mat, n):
	for r in range(0, int(n/2)):
		for c in range(r, n-1-r):
			tmp = mat[r][c]
			mat[r][c] = mat[c][n-1-r]
			mat[c][n-1-r] = mat[n-1-r][n-1-c]
			mat[n-1-r][n-1-c] = mat[n-1-c][r]
			mat[n-1-c][r] = tmp
	return mat

def print_matrix(mat):
	for r in range(0, len(mat)):
		print(mat[r])

if len(sys.argv) == 1:
	print("Usage: python 1-7.py matrix_size")
	print("*****Problem Description*****\nGiven an image represented  by an NxN matrix, where each pixel in the image is represented by 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?")
else:
	i = 0
	matrix = []
	for r in range(0, int(sys.argv[1])):
		matrix.append([])
		for c in range(0, int(sys.argv[1])):
			matrix[r].append(i)
			i += 1
	print("The matrix before: ")
	print_matrix(matrix)
	matrix = rotate_matrix(matrix, int(sys.argv[1]))
	print("\nThe matrix is now:")
	print_matrix(matrix)
