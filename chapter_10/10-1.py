"""
10.1 Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.
"""

def sorted_merge(a, b):
	for bc in range(len(b)-1, -1, -1):
		for ac in range(len(a)-1, -1, -1):
			if b[bc] >= a[ac]:
				a.insert(ac+1, b[bc])
				break
		if b[bc] < a[0]:
			a.insert(0, b[bc])
	return a

a = [1,2,3,4,5]
b = [0,6,7]

print(sorted_merge(a,b))
