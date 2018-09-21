"""
3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
Hints:#64, #87
"""


class SetOfStacks:
	def __init__(self):
		self.stacks = []
		self.stack_cap = 5
		self.sub_index = 0


	def push(self, val):
		self.stacks[self.sub_index].append(val)
		if len(self.stacks[self.sub_index]) == self.stack_cap:
			self.sub_index_index += 1
			self.stacks.append([])

	def pop(self):
		if len(self.stacks[self.sub_index]) == 0:
			self.stacks.pop()
			self.sub_index -= 1
		return self.stacks[self.sub_index].pop()

	def popAt(self, index):
		return self.stacks[index].pop()
