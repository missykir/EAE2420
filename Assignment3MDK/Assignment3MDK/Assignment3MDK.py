class Node:
	def __init__(self,value):
		self.value = value
		self.next = None
		self.previous = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

# Inserts value into a new node 
# after the given node
	def insertAfter(self, node, value):
		newNode = Node(value)
		node.next.previous = newNode
		newNode.next = node.next
		node.next = newNode
		newNode.previous = node
		if node == self.tail:
			self.tail = newNode
    
# Inserts value into a new node
# before the given node
	def insertBefore(self, node, value):
		newNode = Node(value)
		node.previous.next = newNode
		newNode.previous = node.previous
		node.previous = newNode
		newNode.next = node
		if node == self.head:
			self.head = newNode
    
# Adds the given value as the first
# value in the list
	def addFirst(self, value):
		if(self.head == None):
			self.head = Node(value)
			self.tail = self.head
		else:
			newNode = Node(value)
			newNode.next = self.head
			self.head = newNode
			self.head.next.previous = newNode

#Adds the given value as the last
#value in the list
	def addLast(self, value):		
		if(self.head == None):
			self.head = Node(value)
			self.tail = self.head
		else:
			self.tail.next = Node(value)
			self.tail = self.tail.next

	def first(self):
		return head

	def last(self):
		return tail

	def find(self, value):
		runner = self.head
		while (runner!=None):
			if runner.value == value:
				return runner.value
			else:
				runner = runner.next
		return None
# Removes the given node
# from the list
	def remove(self, node):
		if node == head:
			head = node.next
			node.next.previous = None
			node.next = None
		elif node == tail:
			tail = node.previous
			node.previous.next = None
			node.previous = None
		else:
			node.previous.next = node.next
			node.next.previous = node.previous
			node.next = None
			node.previous = None

		
  
# Returns the number of items in the list
	def count(self):
		count = 0
		runner = self.head
		while (runner!=None):
			runner = runner.next
			count += 1
		return count
			
    
# Allows the user to iterate over
# the values (not the nodes)
	def __iter__(self):
		runner = self.head
		while (runner!=None):
			yield runner.value
			runner = runner.next
		yield None
