"""
16.23 Rand7 from Rands: Implement a method rand7() given rand5( ). That is, given a method that
generates a random number between O and 4 (inclusive), write a method that generates a random
number between O and 6 (inclusive).
Hints:#505, #574, #637, #668, #697, #720
"""
import random

def rand5():
	return random.randint(0,4)
"""
First attempt.
Not even distribution because of adding.
First and last element will be less likely than the middle

def rand7():
	r7 = [0,1,2,3,4,5,6] * 5
	i = 0
	for n in range(0, 7):
		i += rand5()
	return r7[i]
"""

"""
With no adding, each row and col are equally likely to be picked. We cannot find another 0-6 in the remaining 4 elements,
so they trigger a re-roll of the row and col.
"""
def rand7():
	r7 = [[0,1,2,3,4],
		  [5,6,0,1,2],
		  [3,4,5,6,0],
		  [1,2,3,4,5],
		  [6,-1,-1,-1,-1]]

	row = rand5()
	col = rand5()
	while row == 4 and col >= 1:
		row = rand5()
		col = rand5()
	return r7[row][col]

#Check for random distribution
freq = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for i in range(1000000):
	r = rand7()
	freq[r] = freq[r] + 1
for key,value in freq.items():
	print(str(key) + ":" + str(value))
