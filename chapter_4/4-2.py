"""
4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
Hints: #79, #73, #7 76
"""
import sys

class Node:
	def __init__(self, val=None):
		self.val = val
		self.left = None
		self.right = None


def create_tree(arr):
	if len(arr) < 3:
		if len(arr) == 2:
			n = Node(arr[1])
			n.left = Node(arr[0])
		elif len(arr) == 1:
			n = Node(arr[0])
		else:
			n = None
	else:
		i = int(len(arr) / 2)
		n = Node(arr[i])
		n.left = create_tree( arr[0:i])
		n.right = create_tree(arr[i+1:])
	return n

def tree_to_string(n, level=0):
	if n != None:
		tree = ""
		tree += tree_to_string(n.right, level+1)
		tree += "\t"*level + str(n.val) + "\n"
		tree += tree_to_string(n.left, level+1)
		return tree
	else:
		return ""


if len(sys.argv) == 1:
	print("Usage: python 4-2.py size")
	print("""*****Problem Description*****\n\n
4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
Hints: #79, #73, #7 76""")
else:
	l = list(range(1, int(sys.argv[1]) + 1))
	t = create_tree(l)
	print(tree_to_string(t))
