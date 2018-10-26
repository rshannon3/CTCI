"""
8.4 Power Set: Write a method to return all subsets of a set.
Hints: #273, #290, #338, #354, #373
"""

import sys


def power_set(s, index=0):
	subs = []
	if len(s) == index:
		subs.append([])
	else:
		subs = power_set(s, index+1)
		val = s[index]
		more = []
		for sub in subs:
			new_subs = []
			new_subs.append(sub)
			new_subs.append(val)
			more.append(new_subs)
		subs.append(more)
	return subs

if len(sys.argv) == 1:
	print("Usage: python ")
	print("""*****Problem Description*****\n\n
8.4 Power Set: Write a method to return all subsets of a set.""")
else:
	s= list(sys.argv[1])
	print(power_set(s))
