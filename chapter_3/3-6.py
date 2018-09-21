class Node:
	def __init__(self,n="", t=""):
		self.name = n
		self.type = t
		self.next_node = None

class LinkedList:
	def __init__(self):
		self.head_node = None
		self.tail_node = None


class AnimalShelter:
	def __init__(self):
		self.animal_list = LinkedList()


	def enqueue(self, animal):
		animal.next_node = self.animal_list.head_node
		self.animal_list.head_node = animal

	#RIP
	def dequeueAny(self):
		look = self.animal_list.head_node.next_node
		current = self.animal_list.head_node
		while look != None:
			current = current.next_node
			look = look.next_node
		tmp = current
		current = None
		return tmp

	def dequeueDog(self):
		current = self.animal_list.head_node
		#If head node is dog, move head and return
		if current.type == "dog":
			self.animal_list.head_node = self.animal_list.head_node.next_node
			return current
		#Otherwise look for first dog
		while current.next_node.type != "dog":
			current = current.next_node
			if current == None:
				return None
		tmp = current.next_node
		#Link to Node behind the node being returned
		current.next_node = current.next_node.next
		return tmp

	def dequeueCat(self):
		current = self.animal_list.head_node
		#If head node is cat, move head and return
		if current.type == "cat":
			self.animal_list.head_node = self.animal_list.head_node.next
			return current
		#Otherwise look for first cat
		while current.next_node.type != "cat":
			current = current.next_node
			if current == None:
				return None
		tmp = current.next_node
		#Link to Node behind the node being returned
		current.next_node = current.next_node.next
		return tmp

	def print_shelter(self):
		current = self.animal_list.head_node
		while current != None:
			print(str(current.type) + " " + str(current.name))
			current = current.next_node
		print()


shel = AnimalShelter()
c = Node()
c.type = "cat"
c.name = "Lucky"
d = Node()
d.type = "dog"
d.name = "Zoom"
shel.enqueue(c)
shel.print_shelter()
shel.enqueue(d)
shel.print_shelter()
shel.dequeueAny()
shel.print_shelter()
