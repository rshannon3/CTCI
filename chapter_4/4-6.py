"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
Hints: #79, #91
"""
import sys
import random

class Node:
	def __init__(self, val=None, parent=None):
		self.val = val
		self.left = None
		self.right = None
		self.parent = parent


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
def create_tree(arr, p=None):
	if len(arr) < 3:
		if len(arr) == 2:
			n = Node(arr[1], p)
			n.left = Node(arr[0], n)
		elif len(arr) == 1:
			n = Node(arr[0], p)
		else:
			n = None
	else:
		i = int(len(arr) / 2)
		n = Node(arr[i], p)
		n.left = create_tree(arr[0:i], n)
		n.right = create_tree(arr[i+1:], n)
	return n


visited = []
def next_node(n):
	if n.right == None:
		tmp = n
		while n.parent != None and n.parent.val < n.val:
			n = n.parent
		if n.parent == None:
			return tmp.val
		return n.parent.val
	else:
		 in_order_traversal(n.right)
	return visited[0]

def in_order_traversal(n):
	if n != None:
		in_order_traversal(n.left)
		visit(n)
		in_order_traversal(n.right)

def visit(n):
	visited.append(n.val)

def find(n, target):
	if n != None:
		if n.val == target:
			return n
		else:
			return find(n.left, target) if find(n.right, target) == None else find(n.right, target)
	else:
		return None


if len(sys.argv)  < 3:
	print("Usage: python 4-3.py size target")
	print("""*****Problem Description*****\n\n
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
Hints: #79, #91 """)
else:
	l = list(range(1, int(sys.argv[1]) + 1))
	t = create_tree(l)
	print(tree_to_string(t))

	print("\n\n\n")
	target = find(t, int(sys.argv[2]))
	print("The target is " + str(target.val))
	print("The next node (in order) is " + str(next_node(target)))
