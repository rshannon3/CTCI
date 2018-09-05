"""
16.22 Langton's Ant
An ant is sitting on an infinite grid of white and black squares. Initially, the grid is all white and the ant faces right. At each step, it does the following:
(1) At a white square, flip the color of the square, turn 90 degrees right (clockwise), and move forward one unit.
(2) At a black square, flip the color of the square, turn 90 degrees left (counter-clockwise), and move forward one unit.
Write a program to simulate the first K moves that the ant makes and print the final board as a grid. Note that you are not provided with the data sctructure to represent the grid. his is something that you must design yourself. The only input to your method is K. You should print the final grid and return nothing. The method signature might be something like void printKMoves(int K).
"""
import sys

def printKMoves(k):
	board = [["w"]]
	direction = "right"
	r = 0
	c = 0
	for i in range(0, k):
		#Turn the ant based on the color of the current tile
		if board[r][c] == "w":
			if direction == "right":
				direction = "down"
			elif direction == "down":
				direction = "left"
			elif direction == "left":
				direction = "up"
			elif direction == "up":
				direction = "right"
		elif board[r][c] == "b":
			if direction == "right":
				direction = "up"
			elif direction == "up":
				direction = "left"
			elif direction == "left":
				direction = "down"
			elif direction == "down":
				direction = "right"
		#Flip the color of the current tile
		board[r][c] = "b" if board[r][c] == "w" else "w"
		#Advance one tile in the current direction
		#Adjusts the "infinite" grid if a new row or column needs to be added
		if direction == "right":
			if c == len(board[r]) - 1:
				for row in range(0, len(board)):
					board[row].append("w")
			c += 1
		elif direction == "down":
			if r == len(board) -1:
				tmp = [["w"]]
				for k in range(1, len(board[r])):
					tmp[0].append("w")
				board = board + tmp
			r += 1
		elif direction == "left":
			if c == 0:
				for row in range(0, len(board)):
					board[row] = ['w'] + board[row]
			else:
				c -= 1
		elif direction == "up":
			if r == 0:
				tmp = [["w"]]
				for k in range(1, len(board[r])):
					tmp[0].append("w")
				board = tmp + board
			else:
				r -= 1
	print("Ant has ended on row " + str(r) + ", col " + str(c))
	print_matrix(board)

def print_matrix(mat):
	cols = []
	for col in range(0, len(mat[0])):
		cols.append(str(col))
	print(" " + str(cols))
	for r in range(0, len(mat)):
		print(str(r) + str(mat[r]))


if len(sys.argv) == 1:
	print("Usage: python k")
	print("*****Problem Description*****\n16.22 Langton's Ant\nAn ant is sitting on an infinite grid of white and black squares. Initially, the grid is all white and the ant faces right. At each step, it does the following:\n(1) At a white square, flip the color of the square, turn 90 degrees right (clockwise), and move forward one unit.\n(2) At a black square, flip the color of the square, turn 90 degrees left (counter-clockwise), and move forward one unit.\nWrite a program to simulate the first K moves that the ant makes and print the final board as a grid. Note that you are not provided with the data sctructure to represent the grid. his is something that you must design yourself. The only input to your method is K. You should print the final grid and return nothing. The method signature might be something like void printKMoves(int K).")
else:
	printKMoves(int(sys.argv[1]))
