"""
16.19 Pond Sizes: You have an integer matrix representing a plot of land, where the value at that location
represents the height above sea level. A value of zero indicates water. A pond is a region of
water connected vertically, horizontally, or diagonally. The size of the pond is the total number of
connected water cells. Write a method to compute the sizes of all ponds in the matrix.
EXAMPLE
Input:
0 2 1 0
0 1 0 1
1 1 0 1
0 1 0 1
Output: 2, 4, 1 (in any order)
Hints: #674, #687, #706, #723
"""
import random

def find_ponds(m):
	ponds = []
	for r in range(len(m)):
		for c in range(len(m[r])):
			if m[r][c] == 0 and not check_ponds(r,c,m, ponds):
				print("\nFound water at " + str(r) + "," + str(c) + ". Starting pond search.")
				ponds.append( build_pond(r, c, m) )
				print("Pond starting at " + str(r) + ", " + str(c) + " completed. Includes: ")
				print("\t" + str(ponds))
	return ponds

def build_pond(r,c,m, pond=None):
	if pond == None:
		pond = []
	pond.append((r,c))
	print("Pond = " + str(pond))
	adj = valid_adj(r,c,m)
	for a in adj:
		if m[a[0]][a[1]] == 0 and (a[0],a[1]) not in pond:
			print("Found new square [" + str(a[0]) + ", " + str(a[1]) + "] not in pond.")
			print("Searching at [" + str(a[0]) + ", " + str(a[1]) + "] for adjacent water.")
			build_pond(a[0], a[1], m, pond)
	return pond

def valid_adj(r,c,m):
	v = []
	if r+1 >= 0 and r+1 < len(m) and c+1 >= 0 and c+1 < len(m[r]):
		v.append((r+1,c+1))
	if r >= 0 and r < len(m) and c+1 >= 0 and c+1 < len(m[r]):
		v.append((r,c+1))
	if r+1 > 0 and r+1 < len(m) and c >= 0 and c < len(m[r]):
		v.append((r+1,c))
	if r-1 >= 0 and r-1 < len(m) and c-1 >= 0 and c-1 < len(m[r]):
		v.append((r-1,c-1))
	if r-1 >= 0 and r-1 < len(m) and c >= 0 and c < len(m[r]):
		v.append((r-1,c))
	if r >= 0 and r < len(m) and c-1 >= 0 and c-1 < len(m[r]):
		v.append((r,c-1))
	if r+1 >= 0 and r+1 < len(m) and c-1 >= 0 and c-1 < len(m[r]):
		v.append((r+1,c-1))
	if r-1 >= 0 and r-1 < len(m) and c+1 >= 0 and c+1 < len(m[r]):
		v.append((r-1,c+1))
	print("Valid adjacent squares for [" + str(r) + ", " + str(c) + "] found:")
	print("\t" + str(v))
	return v

def check_ponds(r,c,m,ponds):
	for pond in ponds:
		for loc in pond:
			if loc[0] == r and loc[1] == c:
				return True
	return False

def print_m(m):
	for r in range(len(m)):
		if r == 0:
			print(" " + str(list(range(len(m[r])))).replace("[", " ").replace("]", ""))
		print(str(r) + str(m[r]))

def generate_map():
	r = random.randint(5, 5)
	c = random.randint(5, 5)
	m = []
	for ri in range(0, r):
		m.append([])
		for ci in range(0, c):
			m[ri].append( random.randint(0,1) )
	return m

m = generate_map()
print_m(m)
ponds = find_ponds(m)
print("\n")
print_m(m)
print("Found " + str(len(ponds)) + " ponds of size(s) ")
for pond in ponds:
	print("\t" + str(len(pond)) + "\t---> " + str(pond))
