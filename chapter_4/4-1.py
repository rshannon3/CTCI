"""
4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
Hints:#127
"""
import sys


graph = { 'A' : ['B', 'C'],
		  'B' : ['D', 'G'],
		  'C' : ['D', 'E'],
		  'D' : [],
		  'E' : ['A', 'B'],
		  'F' : [],
		  'G' : [] }

visited = []

#Simple depth first search
def search(root, target):
	visited.append(root)
	for adj in graph[root]:
		if adj not in visited:
			search(adj, target)



if len(sys.argv) < 3:
	print("Usage: python start end\n")
	print("""*****Problem Description*****\n4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
Hints:#127 """)
else:
	start = str(sys.argv[1])
	target= str(sys.argv[2])
	print(start + " to " + target)
	search(start, target)
	if target in visited:
		print("Path found")
	else:
		print("No path found")
