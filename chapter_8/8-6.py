"""
8.6 Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following
constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using Stacks.
"""

def move_disks(n, stack_source, stack_dest, stack_buffer):
	if n == 0:
		print_stacks()
		return

	move_disks(n-1, stack_source, stack_buffer, stack_dest)
	move_top(stack_source, stack_dest)
	move_disks(n-1, stack_buffer, stack_dest, stack_source)

def move_top(stack_source, stack_dest):
	stack_dest.append(stack_source.pop())

def print_stacks():
	print(s1)
	print(s2)
	print(s3)
	print()

s1 = [5,4,3,2,1]
s2 = []
s3 = []

move_disks(len(s1), s1, s3, s2)
