"""
10.4 Sorted Search, No Size: You are given an array like data structure Listy which lacks a size
method. It does, however, have an elementAt ( i) method that returns the element at index i in
0( 1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data
structure only supports positive integers.) Given a Li sty which contains sorted, positive integers,
find the index at which an element x occurs. If x occurs multiple times, you may return any index.
Hints: #320, #337, #348
"""


def sorted_search(listy, value):
	val = get(listy, 0)
	if val > value:
		return -1
	size_guess = 2
	while get(listy, size_guess) != -1:
		size_guess *= 2
	while get(listy, size_guess) == -1:
		size_guess -= 1
	print(size_guess)
	index = int(size_guess / 2)
	val = get(listy, index)
	while val != value:
		if value == get(listy, index):
			return index
		elif val > get(listy, index):
			index += int((size_guess - index) / 2)
		else:
			index -= int(index / 2)
	return -1


def get(listy, index):
	return -1 if index >= len(listy) else listy[index]


l = [4,5,6,7,8,9,10,11,12,13,14,16,17,18,20]
v = 4

print("Val = " + str(v))
print("Index = " + str(sorted_search(l,v)))
