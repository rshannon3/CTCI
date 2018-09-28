"""
4.4 Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
Hints:#27, #33, #49, #705, #724
"""
import sys
import random

class Node:
	def __init__(self, val=None):
		self.val = val
		self.left = None
		self.right = None

def is_balanced(root):
	if root == None:
		return True
	elif abs(max_height(root.left) - max_height(root.right)) >= 2:
		return False
	else:
		return is_balanced(root.left) and is_balanced(root.right)

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
def create_tree():
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

if len(sys.argv) == 1:
	print("Usage: python 4-3.py size")
	print("""*****Problem Description*****\n\n
4.4 Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
Hints:#27, #33, #49, #705, #724""")
else:
	t = create_tree()
	print(tree_to_string(t))

	print("\n\n\n")
	msg = " balanced." if is_balanced(t) else " not balanced."
	print("The tree is " + msg)
