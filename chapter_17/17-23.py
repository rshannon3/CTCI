"""
17 .23 Max Black Square: Imagine you have a square matrix, where each cell (pixel) is either black or white
Design an algorithm to find the maximum subsquare such that all four borders are filled with black
pixels.
Hints: #684, #695, #705, #714, #721, #736
"""
import random

ROW = 0
COL = 1
SIZE = 2

def max_black_square(m):
	subs = enumerate_subsquares(m)
	print(subs)
	max = None
	for sub in subs:
		#top row
		valid = True
		for c in range(sub[COL], sub[COL] + sub[SIZE]):
			if m[sub[ROW]][c] == 'w':
				valid = False
				break
		#bottom row
		if valid:
			for c in range(sub[COL], sub[COL] + sub[SIZE]):
				if m[sub[ROW]+sub[SIZE]][c] == 'w':
					valid = False
					break
		else:
			continue
		#left col
		if valid:
			for r in range(sub[ROW], sub[ROW] + sub[SIZE]):
				if m[r][sub[COL]] == 'w':
					valid = False
					break
		else:
			continue
		#right col
		if valid:
			for r in range(sub[ROW], sub[ROW] + sub[SIZE]):
				if m[r][sub[COL]+sub[SIZE]] == 'w':
					valid = False
					break
		else:
			continue
		if valid:
			if max != None and sub[SIZE] > max[SIZE]:
				 max = sub
	return max

def enumerate_subsquares(m):
	squares = []
	for r in range(0, len(m)):
		for c in range(0, len(m)):
			size = 1
			while r + size < len(m) and c + size < len(m):
				squares.append((r,c,size))
				size += 1
	return squares

def print_m(m):
	for row in m:
		print(row)


size = 10
m = []
for r in range (0, size):
	m.append([])
	for c in range(0,size):
		m[r].append('w' if random.randint(0,1) == 1 else 'b')

print_m(m)
print("Max black squre at: ")
print(max_black_square(m))
