"""
4.3 List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
Hints: #107, #123, #135
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

lists = []
def create_linked_lists(root, level = 0):
	if len(lists) <= level and root != None:
		lists.append([])
	if root != None:
		lists[level].append(root.val)
		create_linked_lists(root.left, level+1)
		create_linked_lists(root.right, level+1)



if len(sys.argv) == 1:
	print("Usage: python 4-3.py size")
	print("""*****Problem Description*****\n\n
4.3 List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
Hints: #107, #123, #135""")
else:
	l = list(range(1, int(sys.argv[1]) + 1))
	t = create_tree(l)
	print(tree_to_string(t))

	print("\n\n\n")
	create_linked_lists(t)
	for line in lists:
		print(line)
