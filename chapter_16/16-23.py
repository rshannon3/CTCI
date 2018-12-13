"""
16.23 Rand7 from Rands: Implement a method rand7() given rand5( ). That is, given a method that
generates a random number between O and 4 (inclusive), write a method that generates a random
number between O and 6 (inclusive).
Hints:#505, #574, #637, #668, #697, #720
"""
import random

def rand5():
	return random.randint(0,4)

def rand7():
	r7 = [0,1,2,3,4,5,6]
	i = (rand5() + rand5()) % 7
	return r7[i]

#Check for random distribution
freq = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for i in range(1000000):
	r = rand7()
	freq[r] = freq[r] + 1
for key,value in freq.items():
	print(str(key) + ":" + str(value))
