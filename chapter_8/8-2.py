"""
8.2 Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
"""

def find_path(grid):
	if not grid or (len(grid) == 0 or len(grid[0]) == 0):
		return None
	path = []
	if get_path(grid, len(grid) - 1, len(grid[0]) - 1, path):
		return path
	return None



def get_path(grid, row, col, path):
	if col < 0 or row < 0 or not grid[row][col]:
		return False
	atOrigin = (row == 0 and col == 0)

	if atOrigin or get_path(grid, row, col - 1, path) or get_path(grid, row - 1, col, path):
		path.append((row,col))
		return True
	return False

def print_grid(grid):
	for row in grid:
		print(row)


grid = [[1, 1, 1 ,0],
		[1, 0, 1, 1],
		[0, 0, 0, 1],
		[0, 0, 0, 1]]

print_grid(grid)
print(find_path(grid))
