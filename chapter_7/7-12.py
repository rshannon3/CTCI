"""
7.12 Hash Table: Design and implement a hash table which uses chaining (linked lists) to handle collisions.

Hints: #287, #307
"""
import random

class HashTable:
	DEFAULT_SIZE = 100
	def __init__(self):
		self.table = [None] * DEFAULT_SIZE

	def __setitem__(self, key, val):
		i = __index(key)
		if self.table[i] == None:
			self.table[i] = (key,val)
		elif self.table[i] is list:
			self.table[i].append((key,val))
		else:
			self.table[i] = [self.table[i], (key,val)]

	def __getitem__(self, key):
		i = __index(val)
		if self.table[i] == None:
			raise ValueError()
		elif self.table[i] is list:
			for item in self.table[i]:
				if item[0] == key:
					return item[1]
		else:
			return self.table[i][1]

	def __delitem__(self,key):
		i = __index(val)
		if self.table[i] == None:
			raise ValueError()
		elif self.table[i] is list:
			for item in self.table[i]:
				if item[0] == key:
					self.table.remove(item)
		else:
			self.table[i] = None

	def __index(val):
		#Pretend hash function for simulation
		return random.randint(0, DEFAULT_SIZE)
