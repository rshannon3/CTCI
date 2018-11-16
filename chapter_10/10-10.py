"""
10.10
Rank from Stream: Imagine you are reading in a stream of integers. Periodically, you wish to be able
to look up the rank of a numberx (the number of values less than or equal to x). lmplementthe data
structures and algorithms to support these operations. That is, implement the method track ( int
x), which is called when each number is generated, and the method getRankOfNumber(int
x), which returns the number of values less than or equal to x (not including x itself).
EXAMPLE
Stream (in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3
getRankOfNumber(l) 0
getRankOfNumber(3) = 1
getRankOfNumber(4) 3
Hints: #301, #376, #392
"""

import bisect

def track(l, v):
	bisect.insort(l,v)

def getRankOfNumber(l,v):
	index = l.index(v)
	while index < len(l) and l[index] == v:
		index += 1
	return index -1

stream = [5,1,4,4,5,9,7,13,3]
l = []
for item in stream:
	track(l,item)
print(getRankOfNumber(l,1))
print(getRankOfNumber(l,3))
print(getRankOfNumber(l,4))
