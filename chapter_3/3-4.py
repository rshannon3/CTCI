"""
3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
Hints: #98, #7 74
"""

class MyQueue:
	def __init__(self):
		self.s1 = []
		self.s2 = []

	def enqueue(val):
		self.s1.push(val)


	def dequeue():
		if len(self.s2) == 0:
			if len(self.s1) == 0:
				return None
			while len(self.s1) > 0:
				self.s2.append(self.s1.pop())
		else:
			return self.s2.pop()
