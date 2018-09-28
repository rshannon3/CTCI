"""
4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.
Hints: #35, #57, #86, #113, #128
"""
import sys
import random

class Node:
	def __init__(self, val=None):
		self.val = val
		self.left = None
		self.right = None


def is_bst(root, min=-99999, max=99999):
	if root == None:
		return True
	else:
		return root.val > min and root.val < max and is_bst(root.left, min, root.val) and is_bst(root.right, root.val, max)

#Helper function for is_balanced
def max_height(root, level=0):
	if root == None:
		return level
	else:
		return max(max_height(root.left, level+1), max_height(root.right, level+1))

#Tree output
def tree_to_string(n, level=0):
	if n != None:
		tree = ""
		tree += tree_to_string(n.right, level+1)
		tree += "\t"*level + str(n.val) + "\n"
		tree += tree_to_string(n.left, level+1)
		return tree
	else:
		return ""

#Used for manual testing
def create_tree_manual():
	root = Node(5)
	root.right = Node(10)
	root.right.left = Node(12)
	root.right.right = Node(20)
	root.right.right.right = Node(21)
	root.right.left.right = Node(13)
	root.right.left.right.right = Node(14)
	root.left = Node(6)
	#root.left.left = Node(7)

	return root

#BST Creation
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

if len(sys.argv) == 1:
	print("Usage: python 4-3.py size")
	print("""*****Problem Description*****\n\n
4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.
Hints: #35, #57, #86, #113, #128 """)
else:
	l = list(range(1, int(sys.argv[1]) + 1))
	t = create_tree(l)
	print(tree_to_string(t))

	print("\n\n\n")
	msg = " a bst." if is_bst(t) else " not a bst."
	print("The tree is " + msg)
