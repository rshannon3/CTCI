"""
16.4 Tic Tac Win: Design an algorithm to figure out if someone has won a game of tic-tac-toe.
Hints:#710, #732
"""
from itertools import permutations

def winner(p1,p2,board):
	p1_flag = False
	p2_flag = False
	for perm in permutations(p1, 3):
		if sum(perm) == 15:
			p1_flag = True
			break
	for perm in permutations(p2, 3):
		if sum(perm) == 15:
			p2_flag = True
			break
	if p1_flag and p2_flag:
		print("Error, both players have won.")
	elif p1_flag:
		print("Player 1 is the winner!")
	elif p2_flag:
		print("Player 2 is the winner!")
	else:
		print("No player has won.")



magic_square = [[4,9,2],
				[3,5,7],
				[8,1,6]]
p1 = [8,5,4,9,2]
p2 = [1,6,3,7,2]

winner(p1,p2,magic_square)
